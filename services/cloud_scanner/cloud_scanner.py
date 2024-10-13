from aws_scanner import check_s3_buckets, check_iam_policies
from azure_scanner import check_blob_storage
from gcp_scanner import check_storage_buckets

def run_cloud_scan():
    """Run all cloud security scans."""
    findings = []
    findings.extend(check_s3_buckets())
    findings.extend(check_iam_policies())
    findings.extend(check_blob_storage())
    findings.extend(check_storage_buckets())
    return findings
