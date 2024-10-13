
import subprocess

def scan_kubernetes_cluster():
    """Run Kube-bench to scan a Kubernetes cluster."""
    result = subprocess.run(['kube-bench'], capture_output=True, text=True)
    return result.stdout
