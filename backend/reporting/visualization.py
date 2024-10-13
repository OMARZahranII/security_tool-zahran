
import matplotlib.pyplot as plt

def generate_vulnerability_trend_chart(findings):
    data = [5, 7, 4, 9, 6, 10]
    plt.plot(data)
    plt.title("Vulnerability Trends Over Time")
    plt.xlabel("Scans")
    plt.ylabel("Vulnerabilities")
    plt.savefig('vulnerability_trend_chart.png')

def generate_scan_comparison_chart(scan_results):
    scan_names = ['Scan 1', 'Scan 2', 'Scan 3']
    values = [10, 12, 8]
    plt.bar(scan_names, values)
    plt.title("Vulnerability Comparison Between Scans")
    plt.savefig('scan_comparison_chart.png')
