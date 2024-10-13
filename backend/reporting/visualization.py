import matplotlib.pyplot as plt
import seaborn as sns

def generate_vulnerability_charts(findings):
    fig, ax = plt.subplots()
    sns.countplot(y=[finding['type'] for finding in findings], ax=ax)
    ax.set_title("Vulnerabilities by Type")
    plt.savefig('vulnerability_chart.png')
