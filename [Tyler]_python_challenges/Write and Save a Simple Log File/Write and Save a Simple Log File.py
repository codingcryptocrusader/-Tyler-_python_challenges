from datetime import datetime

def log_user_input():
    # Prompt the user for a message or activity
    user_input = input("Enter a message or activity to log: ")

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the log entry
    log_entry = f"[{timestamp}] {user_input}\n"

    # Write the log entry to a file
    with open("activity_log.txt", "a") as log_file:
        log_file.write(log_entry)

    print("Your input has been logged.")

if __name__ == "__main__":
    log_user_input()

