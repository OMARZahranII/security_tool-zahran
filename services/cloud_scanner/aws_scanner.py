# services/cloud_scanner/aws_scanner.py

import boto3
from fastapi import FastAPI
from botocore.exceptions import NoCredentialsError

app = FastAPI()

def check_s3_buckets():
    """Check for S3 bucket misconfigurations."""
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    findings = []
    
    for bucket in buckets['Buckets']:
        acl = s3.get_bucket_acl(Bucket=bucket['Name'])
        # Check if any of the grants allow public access
        for grant in acl['Grants']:
            if grant['Grantee']['Type'] == 'Group' and 'AllUsers' in grant['Grantee']['URI']:
                findings.append(f"Bucket {bucket['Name']} is publicly accessible.")
    return findings

def check_iam_policies():
    """Check for overly permissive IAM policies."""
    iam = boto3.client('iam')
    policies = iam.list_policies(Scope='Local')
    findings = []
    
    for policy in policies['Policies']:
        # Check if the policy grants '*' permissions
        document = iam.get_policy_version(PolicyArn=policy['Arn'], VersionId=policy['DefaultVersionId'])
        if '*' in str(document['PolicyVersion']['Document']):
            findings.append(f"IAM Policy {policy['PolicyName']} allows too much access.")
    return findings

@app.post("/aws/scan")
def scan_aws_s3():
    """API endpoint to check for public S3 buckets."""
    try:
        result = check_s3_buckets()
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
