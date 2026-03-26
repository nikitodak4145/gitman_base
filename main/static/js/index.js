// index.js — скрипты для главной страницы

document.addEventListener('DOMContentLoaded', function() {
    const cleanBtn = document.getElementById('clean-code-btn');
    if (cleanBtn) {
        cleanBtn.onclick = function() {
            fetch('/increase-seed/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCsrfToken(),
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const seedValue = document.getElementById('seed-value');
                    const seedFill = document.getElementById('seed-fill');
                    
                    if (seedValue) seedValue.innerText = data.new_value;
                    if (seedFill) seedFill.style.width = data.new_value + '%';
                    
                    const msg = document.getElementById('seed-message');
                    if (msg) {
                        msg.innerHTML = '✅ Сила увеличилась! +10';
                        msg.style.color = '#b3ffb3';
                        setTimeout(() => msg.innerHTML = '', 2000);
                    }
                }
            });
        };
    }
    
    function getCsrfToken() {
        const token = document.querySelector('[name=csrfmiddlewaretoken]');
        return token ? token.value : '';
    }
});