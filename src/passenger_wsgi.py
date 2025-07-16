import os
import sys
import subprocess
import time
import socket

# --- IMPORTANT CONFIGURATION ---
# These paths MUST be absolutely correct for your cPanel setup.
# You can verify these paths in your cPanel's "Setup Python App" section
# or by navigating your file manager.
# from main import app as application
# Path to your virtual environment's Python executable
# Example: /home/czpqmrra/virtualenv/stock-trade/src/3.12/bin/python
VENV_PYTHON = "/home/czpqmrra/virtualenv/stock-trade/src/3.12/bin/python"

# Path to your Flet main application file (e.g., main.py)
# Example: /home/czpqmrra/stock-trade/src/main.py
FLET_APP_PATH = "/home/czpqmrra/stock-trade/src/main.py"

# The internal port your Flet app will listen on.
# This port must be accessible internally by Apache/Nginx on your server.
FLET_PORT = 8550

# Log file for your Flet app's output (stdout/stderr)
# This will help you debug if the Flet app fails to start or encounters errors.
LOG_FILE = "/home/czpqmrra/stock-trade/flet_app.log"

# --- DO NOT MODIFY BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING ---

def is_flet_app_listening(host, port):
    """
    Checks if a process is currently listening on the given host and port.
    This is a basic check and may not be entirely foolproof.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5) # Shorter timeout to avoid blocking too long
        try:
            sock.connect((host, port))
            return True # Connection successful, something is listening
        except (socket.error, socket.timeout):
            return False # Connection failed or timed out, nothing listening

def application(environ, start_response):
    """
    This is the WSGI callable that Phusion Passenger expects.
    It attempts to launch the Flet app as a detached background process
    if it's not already running.
    """
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    # Ensure the log directory exists
    log_dir = os.path.dirname(LOG_FILE)
    os.makedirs(log_dir, exist_ok=True)

    # Check if the Flet app is already running on the specified internal port
    if is_flet_app_listening('127.0.0.1', FLET_PORT):
        message = (
            f"Flet app appears to be already running on port {FLET_PORT}.<br>"
            f"Access it via your domain after Apache reverse proxy setup. "
            f"Remember that WebSocket proxying is crucial for Flet's full functionality."
        )
        return [message.encode('utf-8')]

    # If not running, attempt to launch the Flet app in the background
    # using subprocess.Popen to execute the command directly.
    # preexec_fn=os.setsid detaches the child process from the parent's session,
    # making it behave like a daemon and continue running after this script exits.
    command_parts = [
        VENV_PYTHON,
        FLET_APP_PATH,
        "--web",
        f"--port={FLET_PORT}",
    ]

    try:
        # Open the log file for writing stdout and stderr of the Flet process
        # Using 'with' ensures the file handle is properly closed.
        with open(LOG_FILE, 'a') as log_f:
            subprocess.Popen(
                command_parts,
                stdout=log_f,        # Redirect standard output to the log file
                stderr=subprocess.STDOUT, # Redirect standard error to standard output
                preexec_fn=os.setsid  # Detach the process from the parent session
            )
        
        # Give the Flet app a short moment to initialize.
        # This is not a guarantee, but provides a buffer.
        time.sleep(2) 
        
        message = (
            f"Attempted to start Flet app on port {FLET_PORT}.<br>"
            f"Please check <code style='font-family: monospace;'>{LOG_FILE}</code> for its status and any errors.<br>"
            f"<b style='color: red;'>WARNING:</b> For full Flet functionality, you still need Apache reverse proxy "
            f"configuration for WebSockets on your domain (<code style='font-family: monospace;'>test.piidus.in</code>)."
        )
        return [message.encode('utf-8')]
    except Exception as e:
        # Log any errors that occur during the launch attempt itself
        with open(LOG_FILE, 'a') as f:
            f.write(f"ERROR: Failed to launch Flet app via passenger_wsgi.py: {e}\n")
        
        message = (
            f"Failed to launch Flet app: {e}.<br>"
            f"Check <code style='font-family: monospace;'>{LOG_FILE}</code> for detailed error information."
        )
        return [message.encode('utf-8')]
