// Validation rules: { min, max, label }
const VALIDATION_RULES = {
    battery_power: { min: 500, max: 2000, label: "Battery Power" },
    ram:           { min: 256, max: 4000, label: "RAM" },
    int_memory:    { min: 2,   max: 64,   label: "Internal Memory" },
    clock_speed:   { min: 0.5, max: 3.0,  label: "Clock Speed" },
    mobile_wt:     { min: 80,  max: 200,  label: "Weight" },
    pc:            { min: 0,   max: 20,   label: "Primary Camera" },
    fc:            { min: 0,   max: 19,   label: "Front Camera" },
    px_height:     { min: 0,   max: 1960, label: "Pixel Height" },
    px_width:      { min: 500, max: 1998, label: "Pixel Width" },
    sc_h:          { min: 5,   max: 19,   label: "Screen Height" },
    sc_w:          { min: 0,   max: 18,   label: "Screen Width" }
};

const FEATURES = Object.keys(VALIDATION_RULES);

const RESULT_DESCRIPTIONS = {
    "Low Price": "This device falls in the budget segment — great for basic usage, calls, and light apps.",
    "Medium Price": "A mid-range device offering a solid balance of performance and affordability.",
    "High Price": "A premium device with strong specs suited for gaming, photography, and multitasking.",
    "Very High Price": "A flagship-tier device with top-of-the-line hardware and features."
};

// Clear error when user starts typing
FEATURES.forEach(f => {
    const input = document.getElementById(f);
    input.addEventListener('input', () => {
        clearError(f);
        input.classList.remove('input-error');
    });
});

function clearError(field) {
    const errEl = document.getElementById(`err-${field}`);
    if (errEl) errEl.textContent = '';
}

function showError(field, message) {
    const errEl = document.getElementById(`err-${field}`);
    const input = document.getElementById(field);
    if (errEl) errEl.textContent = message;
    if (input) input.classList.add('input-error');
}

function validateAll() {
    let valid = true;
    let firstInvalid = null;

    FEATURES.forEach(f => {
        const input = document.getElementById(f);
        const value = input.value.trim();
        const rule = VALIDATION_RULES[f];

        clearError(f);
        input.classList.remove('input-error');

        if (value === '') {
            showError(f, `${rule.label} is required.`);
            valid = false;
            if (!firstInvalid) firstInvalid = input;
            return;
        }

        const num = parseFloat(value);
        if (isNaN(num)) {
            showError(f, `Please enter a valid number.`);
            valid = false;
            if (!firstInvalid) firstInvalid = input;
            return;
        }

        if (num < rule.min || num > rule.max) {
            showError(f, `Must be between ${rule.min} and ${rule.max}.`);
            valid = false;
            if (!firstInvalid) firstInvalid = input;
        }
    });

    if (firstInvalid) {
        firstInvalid.focus();
        firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    return valid;
}

document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Validate all fields
    if (!validateAll()) return;

    // Animate button
    const btn = document.getElementById('predict-btn');
    const originalText = btn.innerText;
    btn.innerText = 'Analyzing...';
    btn.style.opacity = '0.7';
    btn.disabled = true;

    // Collect data
    const data = {};
    FEATURES.forEach(f => {
        data[f] = parseFloat(document.getElementById(f).value);
    });

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            // Show server-side validation errors
            if (result.errors) {
                result.errors.forEach(err => {
                    showError(err.field, err.message);
                });
                return;
            }
            throw new Error(result.error || 'Server error');
        }

        // Update UI
        const container = document.getElementById('result-container');
        const tag = document.getElementById('result-tag');
        const desc = document.getElementById('result-desc');

        tag.innerText = result.prediction;
        tag.className = 'result-tag ' + (result.css_class || '');
        desc.innerText = RESULT_DESCRIPTIONS[result.prediction] || '';
        container.classList.remove('hidden');

        container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    } catch (error) {
        alert("An error occurred. Make sure the server is running.");
        console.error(error);
    } finally {
        btn.innerText = originalText;
        btn.style.opacity = '1';
        btn.disabled = false;
    }
});