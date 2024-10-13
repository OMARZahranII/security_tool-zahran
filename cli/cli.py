# cli/cli.py

import click
import requests

@click.group()
def cli():
    """Security Scanner CLI"""
    pass

@cli.command()
@click.option('--target', prompt='Target IP', help='The target IP to scan.')
@click.option('--token', prompt='JWT Token', help='Authentication token')
def network(target, token):
    """Trigger a network scan."""
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post('http://localhost:8001/scan', json={"target_ip": target}, headers=headers)
    click.echo(response.text)
    
@cli.command()
@click.option('--target', prompt='Target IP', help='The target IP to scan.')
def network(target):
    """Trigger a network scan."""
    response = requests.post('http://localhost:8001/scan', json={"target_ip": target})
    click.echo(response.text)

@cli.command()
@click.option('--url', prompt='Target URL', help='The web application to scan.')
def web(url):
    """Trigger a web app vulnerability scan."""
    response = requests.post('http://localhost:8002/scan', json={"target_url": url})
    click.echo(response.text)

@cli.command()
@click.option('--cloud', type=click.Choice(['aws', 'azure', 'gcp']), prompt='Cloud provider')
def cloud(cloud):
    """Trigger cloud security scan."""
    endpoint = f'http://localhost:8003/{cloud}/scan'
    response = requests.post(endpoint)
    click.echo(response.text)

if __name__ == '__main__':
    cli()
