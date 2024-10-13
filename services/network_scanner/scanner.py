# services/network_scanner/scanner.py

import subprocess
from fastapi import FastAPI

app = FastAPI()

def run_nmap_scan(target_ip):
    """Run an Nmap scan and return the results."""
    command = ['nmap', '-sS', '-oX', '-', target_ip]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.post("/scan")
def scan_network(target_ip: str):
    """API endpoint to trigger a network scan."""
    try:
        result = run_nmap_scan(target_ip)
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
