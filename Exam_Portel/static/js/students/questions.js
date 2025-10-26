let total_time = 10 * 60; // 10 minutes in seconds
let currentQuestion = 0;
let totalQuestions = 0;
let score = 0;

const timerDisplay = document.getElementById('time');
const questionBox = document.getElementById('question-box');
const nextBtn = document.getElementById('next-btn');

// ----------------- Timer -----------------
function updateTimer() {
    let minutes = Math.floor(total_time / 60);
    let seconds = total_time % 60;

    timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

    if (total_time === 60) {
        alert('Time is about to end!');
    }

    if (total_time < 0) {
        clearInterval(timerInterval);
        alert('Time is up!');
        window.location.href = '/question_home/'; // redirect to home or results
    }

    total_time--;
}

let timerInterval = setInterval(updateTimer, 1000); // run once on page load

// ----------------- CSRF helper -----------------
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ----------------- Load Question -----------------
function loadQuestion() {
    fetch(`${quizUrl}?q=${currentQuestion}`)
        .then(response => response.json())
        .then(data => {
            if (data.finished) {
                window.location.href = '/results/';
                return;
            }

            totalQuestions = data.total_questions;

            let html = `<p class="question-counter">Question ${currentQuestion + 1} of ${totalQuestions}</p>`;
            html += `<h3 class="question-text">${data.question_text}</h3>`;
            html += `<div class="options">`;
            data.options.forEach((opt, idx) => {
                html += `<label>
                            <input type="radio" name="answer" value="option${idx + 1}" required> ${opt}
                         </label>`;
            });
            html += `</div>`;
            questionBox.innerHTML = html;
        });
}

// ----------------- Submit Answer -----------------
nextBtn.addEventListener('click', () => {
    const selected = document.querySelector('input[name="answer"]:checked');
    if (!selected) {
        alert('Please select an answer!');
        return;
    }

    fetch(`${quizUrl}?q=${currentQuestion}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ answer: selected.value })
    })
        .then(response => response.json())
        .then(data => {
            score = data.score;
            currentQuestion++;
            loadQuestion(); // only updates the question, timer continues
        });
});

// ----------------- Initialize -----------------
loadQuestion();
