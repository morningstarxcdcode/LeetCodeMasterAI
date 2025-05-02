const solveBtn = document.getElementById('solveBtn');
const problemInput = document.getElementById('problemInput');
const solutionCode = document.getElementById('solutionCode');
const explanationText = document.getElementById('explanationText');
const confidenceText = document.getElementById('confidenceText');
const agentFace = document.getElementById('agentFace');
const leftEye = agentFace.querySelector('.eye.left');
const rightEye = agentFace.querySelector('.eye.right');
const mouth = agentFace.querySelector('.mouth');

function setFaceExpression(confidence) {
    // Adjust eyes and mouth based on confidence level (0 to 1)
    const eyeScale = 0.5 + confidence * 0.5;
    leftEye.style.transform = `scale(${eyeScale}) rotate(${Math.sin(Date.now() / 200) * 10}deg)`;
    rightEye.style.transform = `scale(${eyeScale}) rotate(${Math.cos(Date.now() / 200) * 10}deg)`;

    if (confidence > 0.75) {
        mouth.style.borderBottomColor = '#00ff00'; // happy green
        mouth.style.borderBottomWidth = '7px';
        mouth.style.borderRadius = '0 0 40px 40px';
        mouth.style.transform = `translateY(${Math.sin(Date.now() / 300) * 3}px)`;
    } else if (confidence > 0.4) {
        mouth.style.borderBottomColor = '#ffff00'; // neutral yellow
        mouth.style.borderBottomWidth = '5px';
        mouth.style.borderRadius = '0 0 20px 20px';
        mouth.style.transform = `translateY(${Math.sin(Date.now() / 500) * 1.5}px)`;
    } else {
        mouth.style.borderBottomColor = '#ff0000'; // sad red
        mouth.style.borderBottomWidth = '3px';
        mouth.style.borderRadius = '0 0 10px 10px';
        mouth.style.transform = `translateY(${Math.sin(Date.now() / 700) * 1}px)`;
    }
}

async function solveProblem() {
    const problem = problemInput.value.trim();
    if (!problem) {
        alert('Please enter a LeetCode problem description.');
        return;
    }

    // Show loading state
    solveBtn.disabled = true;
    solveBtn.textContent = 'Solving...';
    solutionCode.textContent = '';
    explanationText.textContent = '';
    confidenceText.textContent = '';
    setFaceExpression(0.5);

    try {
        const response = await fetch('http://localhost:8000/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ problem_description: problem })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        const data = await response.json();
        solutionCode.textContent = data.solution_code;
        explanationText.textContent = data.explanation;
        confidenceText.textContent = (data.confidence * 100).toFixed(1) + '%';
        setFaceExpression(data.confidence);
    } catch (error) {
        alert('Error: ' + error.message);
        setFaceExpression(0.2);
    } finally {
        solveBtn.disabled = false;
        solveBtn.textContent = 'Solve Problem';
    }
}

solveBtn.addEventListener('click', solveProblem);
