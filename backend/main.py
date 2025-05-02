from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modules.problem_understanding import understand_problem
from modules.solution_generation import generate_solution
from modules.explanation import generate_explanation
from modules.confidence import estimate_confidence
from modules.feedback import process_feedback

import uvicorn

app = FastAPI(title="Advanced LeetCode AI Agent")

class ProblemRequest(BaseModel):
    problem_description: str

class SolutionResponse(BaseModel):
    solution_code: str
    explanation: str
    confidence: float

@app.post("/solve", response_model=SolutionResponse)
async def solve_problem(request: ProblemRequest):
    try:
        problem = request.problem_description
        understanding = understand_problem(problem)
        solution = generate_solution(understanding)
        explanation = generate_explanation(solution, understanding)
        confidence = estimate_confidence(solution)
        return SolutionResponse(
            solution_code=solution,
            explanation=explanation,
            confidence=confidence
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/feedback")
async def feedback(feedback: dict):
    try:
        process_feedback(feedback)
        return {"message": "Feedback processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
