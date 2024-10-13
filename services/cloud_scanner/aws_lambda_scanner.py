import boto3

def check_lambda_functions():
    lambda_client = boto3.client('lambda')
    functions = lambda_client.list_functions()
    findings = []

    for function in functions['Functions']:
        if function['Runtime'] in ['nodejs4.3', 'python2.7']:
            findings.append(f"Lambda function {function['FunctionName']} uses a deprecated runtime: {function['Runtime']}.")
        
        role_arn = function['Role']
        iam = boto3.client('iam')
        role = iam.get_role(RoleName=role_arn.split('/')[-1])
        if 'AdministratorAccess' in role['RolePolicyList']:
            findings.append(f"Lambda function {function['FunctionName']} uses an overly permissive role.")

    return findings
