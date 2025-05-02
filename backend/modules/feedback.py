import json
import os

FEEDBACK_LOG_FILE = "feedback_log.json"

def process_feedback(feedback: dict):
    """
    Process user feedback to improve the AI agent.
    Stores feedback in a JSON log file for future analysis and learning.
    """
    try:
        if os.path.exists(FEEDBACK_LOG_FILE):
            with open(FEEDBACK_LOG_FILE, "r") as f:
                feedback_list = json.load(f)
        else:
            feedback_list = []
        feedback_list.append(feedback)
        with open(FEEDBACK_LOG_FILE, "w") as f:
            json.dump(feedback_list, f, indent=4)
        print("Feedback processed and saved.")
    except Exception as e:
        print(f"Error processing feedback: {e}")
