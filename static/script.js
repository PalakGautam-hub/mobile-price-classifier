document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Animate button
    const btn = document.getElementById('predict-btn');
    const originalText = btn.innerText;
    btn.innerText = 'Analyzing...';
    btn.style.opacity = '0.7';

    // Collect data
    const features = [
        "battery_power", "ram", "px_height", "px_width", "mobile_wt",
        "int_memory", "pc", "fc", "clock_speed", "sc_h", "sc_w"
    ];

    const data = {};
    features.forEach(f => {
        data[f] = document.getElementById(f).value;
    });

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Network error');
        }

        const result = await response.json();

        // Update UI
        const container = document.getElementById('result-container');
        const tag = document.getElementById('result-tag');
        
        tag.innerText = result.prediction;
        container.classList.remove('hidden');

        // Scroll to result smoothly
        container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    } catch (error) {
        alert("An error occurred. Make sure the server is running.");
        console.error(error);
    } finally {
        btn.innerText = originalText;
        btn.style.opacity = '1';
    }
});