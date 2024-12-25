from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])  # Allow POST method
def run_script():
    try:
        # Replace with the actual script path
        subprocess.run(["python3", "/home/dane/server/playsound.py"], check=True)
        return "Script executed successfully.", 200
    except Exception as e:
        return f"Error running script: {e}", 500

if __name__ == '__main__':
    app.run(host='192.168.0.40', port=5000)

