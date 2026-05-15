async function submitQuery() {
    const input = document.getElementById('queryInput');
    const query = input.value.trim();
    if (!query) return;

    const btn = document.getElementById('askBtn');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const answerText = document.getElementById('answerText');
    const sourceList = document.getElementById('sourceList');

    btn.disabled = true;
    loading.classList.remove('hidden');
    results.classList.add('hidden');
    answerText.innerHTML = '';
    sourceList.innerHTML = '';

    try {
        const response = await fetch('/api/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        if (!response.ok) throw new Error('Network response was not ok');

        const data = await response.json();
        
        // Use marked.js to parse LLM markdown into beautiful HTML
        answerText.innerHTML = marked.parse(data.answer);

        // Render sources
        if (data.sources && data.sources.length > 0) {
            const uniqueSources = [...new Set(data.sources)];
            uniqueSources.forEach(src => {
                const li = document.createElement('li');
                li.textContent = src;
                sourceList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = "No specific references found in the database.";
            sourceList.appendChild(li);
        }

        results.classList.remove('hidden');
    } catch (error) {
        answerText.innerHTML = `<span style="color:#ff6b6b">Error retrieving response: ${error.message}.<br><br>Please make sure you have started your local Ollama instance with 'ollama run mistral' and that PDFs have been ingested.</span>`;
        results.classList.remove('hidden');
    } finally {
        btn.disabled = false;
        loading.classList.add('hidden');
    }
}
