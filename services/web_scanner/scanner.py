# services/web_scanner/scanner.py

import subprocess
from fastapi import FastAPI

app = FastAPI()

def run_owasp_zap(target_url):
    """Run OWASP ZAP scan."""
    command = ['zap-cli', 'quick-scan', '-r', target_url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.post("/scan")
def scan_web_app(target_url: str):
    """API endpoint to trigger web application scan."""
    try:
        result = run_owasp_zap(target_url)
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
