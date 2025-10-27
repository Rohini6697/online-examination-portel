let total_time = 20; // seconds
const quizForm = document.getElementById('quizForm');
const timerDisplay = document.getElementById('time');

function updateTimer() {
    timerDisplay.textContent = total_time.toString().padStart(2, '0');

    if (total_time <= 0) {
        clearInterval(timerInterval);

        // Auto-submit form even if no option selected
        if (quizForm) {
            quizForm.submit();
        }
        return;
    }

    total_time--;
}

let timerInterval = setInterval(updateTimer, 1000);
