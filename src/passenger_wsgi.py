import os
import sys
import subprocess
import time

# IMPORTANT: Ensure these paths are ABSOLUTELY correct for your cPanel setup.

# Path to your virtual environment's python executable
# Based on your provided path: /home/czpqmrra/virtualenv/stock-trade/src/3.12/bin/activate
VENV_PYTHON = "/home/czpqmrra/virtualenv/stock-trade/src/3.12/bin/python"

# Path to your Flet main application file (main.py)
FLET_APP_PATH = "/home/czpqmrra/stock-trade/src/main.py"

# The port your Flet app will try to run on internally
FLET_PORT = 8550

# Log file for your Flet app's output
LOG_FILE = "/home/czpqmrra/stock-trade/flet_app.log"

def application(environ, start_response):
    """
    This is the WSGI callable that Passenger (cPanel's Python app manager) expects.
    We're using it to attempt to launch the Flet app as a detached background process.
    """
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    # Basic check to see if the Flet app is already listening on the port
    # This is not a robust check for production, but helps prevent multiple launches
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # 1 second timeout
        result = sock.connect_ex(('127.0.0.1', FLET_PORT))
        sock.close()
        if result == 0:
            return [b"Flet app appears to be already running."]
    except Exception as e:
        # Log any error during the socket check, but don't stop execution
        with open(LOG_FILE, 'a') as f:
            f.write(f"Error during socket check: {e}\n")
        pass

    # Command to run your Flet app as a server in the background using nohup
    # nohup: ensures the process continues after the parent (Passenger) exits
    # > LOG_FILE 2>&1: redirects all output (stdout and stderr) to the log file
    # &: runs the command in the background
    command_parts = [
        "nohup",
        VENV_PYTHON,
        FLET_APP_PATH,
        "--web",
        f"--port={FLET_PORT}",
    ]

    # Ensure the log directory exists
    log_dir = os.path.dirname(LOG_FILE)
    os.makedirs(log_dir, exist_ok=True)

    try:
        # Use subprocess.Popen to execute the command.
        # We open the log file for stdout/stderr redirection.
        # preexec_fn=os.setsid detaches the child process from the parent's session,
        # making it more daemon-like.
        subprocess.Popen(
            command_parts,
            stdout=open(LOG_FILE, 'a'),
            stderr=subprocess.STDOUT,
            preexec_fn=os.setsid
        )
        time.sleep(3) # Give the Flet app a bit more time to start up
        return [f"Attempted to start Flet app on port {FLET_PORT}. Check {LOG_FILE} for status.".encode('utf-8')]
    except Exception as e:
        return [f"Failed to launch Flet app: {e}".encode('utf-8')]

# IMPORTANT: The 'application' callable is what Passenger looks for.
# It's not designed for long-running WebSocket servers.
# This is a workaround to try and launch your Flet app in the background.
