import os
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import sys

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vector_db.faiss_db import VectorDB

def generate_synthetic_pairs(metadata):
    """Generate (Query, Context) pairs based on chunks."""
    examples = []
    
    for key, chunk in metadata.items():
        text = chunk["text"]
        section = chunk.get("section_number", "")
        law = chunk.get("law_type", "")
        
        if len(text.split()) < 10: 
            continue
            
        # Example 1: Section definition query
        q1 = f"What does {section} of {law} state?"
        examples.append(InputExample(texts=[q1, text]))
        
        # Example 2: General query (e.g. keywords)
        words = text.split()
        if len(words) > 10:
            first_sentence = text.split('.')[0]
            # Limit length
            q2 = f"Tell me about {first_sentence[:50].strip()} under {law}"
            examples.append(InputExample(texts=[q2, text]))
            
    return examples

def fine_tune_model(base_model_name="all-MiniLM-L6-v2", epochs=1):
    db = VectorDB()
    if not db.metadata:
        print("No data in Vector DB. Cannot fine-tune. Run python ingest.py first.")
        return
        
    print("Generating synthetic training pairs...")
    train_examples = generate_synthetic_pairs(db.metadata)
    
    if len(train_examples) < 10:
        print("Not enough examples to fine-tune")
        return
        
    print(f"Generated {len(train_examples)} pairs. Loading base model {base_model_name}...")
    model = SentenceTransformer(base_model_name)
    
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=4)
    
    # We use MultipleNegativesRankingLoss because it works very well with only positive pairs (x,y)
    train_loss = losses.MultipleNegativesRankingLoss(model=model)
    
    print("Starting lightweight training...")
    model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=epochs, warmup_steps=10)
    
    save_path = "data/fine_tuned_model"
    model.save(save_path)
    print(f"Model saved to {save_path}")

if __name__ == "__main__":
    fine_tune_model()
