import csv

def generate_csv_report(findings, filename):
    """Generate a CSV report of findings."""
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Finding'])
        for finding in findings:
            writer.writerow([finding])
