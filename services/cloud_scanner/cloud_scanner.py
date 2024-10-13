
def check_ecs_clusters():
    ecs_client = boto3.client('ecs')
    clusters = ecs_client.list_clusters()
    findings = []

    for cluster_arn in clusters['clusterArns']:
        cluster = ecs_client.describe_clusters(clusters=[cluster_arn])
        if cluster['clusters'][0]['status'] != 'ACTIVE':
            findings.append(f"ECS Cluster {cluster_arn} is inactive.")
    return findings

def check_gcp_iam():
    client = google.cloud.iam.IAMPolicyClient()
    policies = client.list_policies(parent=f"projects/{project_id}")
    findings = []
    for policy in policies:
        if '*' in policy.bindings:
            findings.append(f"IAM policy {policy.name} has overly broad permissions.")
    return findings

def check_azure_storage():
    credential = DefaultAzureCredential()
    storage_client = StorageManagementClient(credential, '<subscription_id>')
    findings = []
    for account in storage_client.storage_accounts.list():
        if account.allow_blob_public_access:
            findings.append(f"Azure Storage Account {account.name} is publicly accessible.")
    return findings
