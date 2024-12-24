def log_activity(activity):
    """Log server-side activity."""
    with open("server_logs.txt", "a") as log_file:
        log_file.write(activity + "\n")
