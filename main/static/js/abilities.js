document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
    
    const commitBtn = document.getElementById('commit-flow-btn');
    if (commitBtn && csrfToken) {
        commitBtn.onclick = function() {
            fetch('/add-mission/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                const resultDiv = document.getElementById('commit-result');
                if (resultDiv) {
                    if (data.success) {
                        resultDiv.innerHTML = ' Баг смыт! Запись добавлена в лог битв.';
                        resultDiv.style.color = '#b3ffb3';
                    } else {
                        resultDiv.innerHTML = ' Ошибка! Попробуй ещё раз.';
                        resultDiv.style.color = '#ff9999';
                    }
                    setTimeout(() => resultDiv.innerHTML = '', 3000);
                }
            });
        };
    }
});