import json
import datetime

# File path to store session data
SESSION_DATA_FILE = "session_data.json"

def record_session_start():
    # Get current timestamp
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create session data dictionary
    session_data = {
        "start_time": start_time
    }
    # Write session data to JSON file
    with open(SESSION_DATA_FILE, "w") as file:
        json.dump(session_data, file)

# Call the session start function
record_session_start()