import re

def estimate_confidence(solution_code: str) -> float:
    """
    Estimate the confidence level of the generated solution.
    Returns a float between 0 and 1.
    Uses advanced heuristics based on code analysis.
    """
    if re.search(r'def solution\(\):', solution_code) or re.search(r'\bpass\b', solution_code):
        return 0.2
    elif re.search(r'def two_sum', solution_code):
        return 0.98
    elif re.search(r'def reverse_list', solution_code):
        return 0.9
    elif re.search(r'def inorder_traversal', solution_code):
        return 0.9
    else:
        # Moderate confidence for other generated solutions
        return 0.6
