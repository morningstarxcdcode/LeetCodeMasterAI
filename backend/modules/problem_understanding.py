import re

def understand_problem(problem_description: str) -> dict:
    """
    Analyze and understand the LeetCode problem description.
    Returns a structured representation of the problem.
    """
    # Improved parsing implementation
    lines = problem_description.split('\n')
    constraints = [line.strip() for line in lines if re.search(r'constraint', line, re.I)]
    inputs = [line.strip() for line in lines if re.search(r'input', line, re.I)]
    outputs = [line.strip() for line in lines if re.search(r'output', line, re.I)]
    examples = []
    example_pattern = re.compile(r'example', re.I)
    current_example = []
    in_example = False
    for line in lines:
        if example_pattern.search(line):
            if current_example:
                examples.append('\n'.join(current_example).strip())
                current_example = []
            in_example = True
            current_example.append(line.strip())
        elif in_example and line.strip() == '':
            if current_example:
                examples.append('\n'.join(current_example).strip())
                current_example = []
            in_example = False
        elif in_example:
            current_example.append(line.strip())
    if current_example:
        examples.append('\n'.join(current_example).strip())
    return {
        "description": problem_description,
        "constraints": constraints,
        "inputs": inputs,
        "outputs": outputs,
        "examples": examples,
        "lines": lines
    }
