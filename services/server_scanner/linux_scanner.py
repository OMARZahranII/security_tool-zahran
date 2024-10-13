# services/server_scanner/linux_scanner.py

import subprocess
from fastapi import FastAPI

app = FastAPI()

def run_linux_security_scan():
    """Run Linux security scan."""
    command = ['lynis', 'audit', 'system']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.post("/linux/scan")
def scan_linux():
    """API endpoint to scan Linux servers."""
    try:
        result = run_linux_security_scan()
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
