import socket
import threading

clients = {}

def broadcast(command, target=None):
    """Send a command to all connected clients or a specific target."""
    if target:
        target.send(command.encode())
    else:
        for client in clients.values():
            client.send(command.encode())

def handle_client(client_socket, addr):
    """Handle individual client connections."""
    print(f"[+] New connection: {addr}")
    clients[addr] = client_socket

    while True:
        try:
            response = client_socket.recv(4096).decode()
            if response:
                print(f"Response from {addr}: {response}")
        except ConnectionResetError:
            print(f"[-] Connection lost: {addr}")
            del clients[addr]
            break

def start_server(host="0.0.0.0", port=9001):
    """Start the server and listen for connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[+] Listening on {host}:{port}...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
