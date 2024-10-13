# services/cloud_scanner/gke_scanner.py

from fastapi import FastAPI
from google.cloud import storage
from google.auth import exceptions

app = FastAPI()

def check_storage_buckets():
    """Check for Google Cloud Storage misconfigurations."""
    client = storage.Client()
    findings = []

    try:
        buckets = client.list_buckets()
        for bucket in buckets:
            policy = bucket.get_iam_policy()
            if 'allUsers' in policy.bindings:
                findings.append(f"Bucket {bucket.name} is publicly accessible.")
    except exceptions.GoogleAuthError as e:
        findings.append(f"Authentication error: {str(e)}")
    except Exception as e:
        findings.append(f"Error accessing storage buckets: {str(e)}")
    
    return findings

@app.post("/gcp/scan")
def scan_gcp_infrastructure():
    """API endpoint to scan GCP for misconfigurations."""
    findings = check_storage_buckets()
    if findings:
        return {"status": "error", "data": findings}
    return {"status": "success", "data": "No misconfigurations found."}
