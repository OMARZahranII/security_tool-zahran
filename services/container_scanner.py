
import subprocess

def scan_docker_image(image_name):
    """Run Trivy to scan a Docker image for vulnerabilities."""
    result = subprocess.run(['trivy', 'image', image_name], capture_output=True, text=True)
    return result.stdout
