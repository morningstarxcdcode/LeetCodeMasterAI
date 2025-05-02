import requests

def test_solve():
    url = "http://localhost:8000/solve"
    problem_description = """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    response = requests.post(url, json={"problem_description": problem_description})
    if response.status_code == 200:
        data = response.json()
        print("Solution Code:\\n", data.get("solution_code"))
        print("Explanation:\\n", data.get("explanation"))
        print("Confidence:", data.get("confidence"))
    else:
        print("Failed to get response:", response.status_code, response.text)

if __name__ == "__main__":
    test_solve()
