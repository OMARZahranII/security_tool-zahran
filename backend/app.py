from flask import Flask, request, jsonify
from ml.threat_detection import train_advanced_model
from reporting.pdf_report import generate_pdf_report
from services.cloud_scanner.aws_lambda_scanner import check_lambda_functions
from services.cloud_scanner.azure_functions_scanner import check_azure_functions
from services.cloud_scanner.gke_scanner import check_gke_clusters

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def run_scan():
    # Logic for running the security scan
    findings = []
    
    findings.extend(check_lambda_functions())
    findings.extend(check_azure_functions())
    findings.extend(check_gke_clusters())
    
    if findings:
        generate_pdf_report(findings, "security_report.pdf")
        return jsonify({"message": "Scan completed", "findings": findings}), 200
    else:
        return jsonify({"message": "No vulnerabilities found"}), 200

if __name__ == '__main__':
    app.run(debug=True)
