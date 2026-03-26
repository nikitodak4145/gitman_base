document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
    
    // 1. Кнопка "Очистить взглядом"
    const cleanBtn = document.getElementById('clean-code-btn');
    if (cleanBtn) {
        cleanBtn.onclick = function() {
            const badCode = document.getElementById('bad-code');
            const goodCode = document.getElementById('good-code');
            const resultDiv = document.getElementById('code-result');
            
            if (badCode && goodCode) {
                badCode.style.transition = 'opacity 0.3s';
                badCode.style.opacity = '0';
                
                setTimeout(() => {
                    badCode.style.display = 'none';
                    goodCode.style.display = 'block';
                    goodCode.style.opacity = '0';
                    
                    setTimeout(() => {
                        goodCode.style.transition = 'opacity 0.3s';
                        goodCode.style.opacity = '1';
                        
                        if (resultDiv) {
                            resultDiv.innerHTML = '✅ Код очищен взглядом!';
                            resultDiv.style.color = '#b3ffb3';
                            setTimeout(() => resultDiv.innerHTML = '', 2000);
                        }
                    }, 10);
                }, 300);
            }
        };
    }
    
    // 2. Кнопка "Поток коммитов"
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
                        resultDiv.innerHTML = '✅ Баг смыт! Запись добавлена в лог битв.';
                        resultDiv.style.color = '#b3ffb3';
                    } else {
                        resultDiv.innerHTML = '❌ Ошибка! Попробуй ещё раз.';
                        resultDiv.style.color = '#ff9999';
                    }
                    setTimeout(() => resultDiv.innerHTML = '', 3000);
                }
            });
        };
    }
    
    // 3. Кнопка "Получить совет"
    const wisdomBtn = document.getElementById('wisdom-btn');
    if (wisdomBtn) {
        wisdomBtn.onclick = function() {
            fetch('/get-tip/')
            .then(response => response.json())
            .then(data => {
                const resultDiv = document.getElementById('wisdom-result');
                if (resultDiv && data.tip) {
                    resultDiv.innerHTML = '💡 ' + data.tip;
                    resultDiv.style.color = '#b3ffb3';
                    setTimeout(() => resultDiv.innerHTML = '', 5000);
                }
            });
        };
    }
});