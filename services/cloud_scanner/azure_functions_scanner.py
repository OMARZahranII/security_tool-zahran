from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient

def check_azure_functions():
    credential = DefaultAzureCredential()
    client = WebSiteManagementClient(credential, '<subscription_id>')
    findings = []

    functions = client.web_apps.list()
    for function in functions:
        if not function.https_only:
            findings.append(f"Azure Function {function.name} does not enforce HTTPS.")
    return findings
