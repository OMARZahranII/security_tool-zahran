# services/server_scanner/windows_scanner.py

import subprocess
from fastapi import FastAPI

app = FastAPI()

def run_windows_security_scan():
    """Run Windows security scan."""
    # Command for Windows scan (for example, using PowerShell scripts)
    command = ['powershell', '-Command', 'Get-WindowsDefenderScanStatus']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.post("/windows/scan")
def scan_windows():
    """API endpoint to scan Windows servers."""
    try:
        result = run_windows_security_scan()
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
