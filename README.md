# RAT_Project

## Project Description

This project is a Remote Access Trojan (RAT) designed for educational purposes. The RAT allows a remote user to control a target machine, execute commands, capture screenshots, and log keystrokes. It consists of a server that listens for incoming connections and a client that connects to the server and executes commands sent by the server.

## Setup Instructions

### Server Setup

1. Clone the repository to your local machine.
2. Navigate to the `server` directory.
3. Run the server script:
   ```bash
   python server.py
   ```

### Client Setup

1. Clone the repository to the target machine.
2. Navigate to the `client` directory.
3. Run the client script:
   ```bash
   python client.py
   ```

## Usage Instructions

### Available Commands

- `screenshot`: Capture a screenshot of the target machine.
- `keylogger`: Start a keylogger on the target machine.
- `download <filepath>`: Download a file from the target machine.
- `exit`: Terminate the connection with the target machine.
- Any other command will be executed on the target machine's shell.
