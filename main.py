import matplotlib.pyplot as plt
from sequences import generate_mathematical_sequences
from visualization import visualize_sequences
from analysis import analyze_sequences

def main():
    # Generate sequences
    sequences = generate_mathematical_sequences(50)
    
    # Analyze sequences
    analysis = analyze_sequences(sequences)
    
    # Create visualizations
    fig = visualize_sequences(sequences, analysis)
    
    # Create a summary report
    report = "Mathematical Sequence Analysis\n"
    report += "=" * 30 + "\n\n"
    
    for name in sequences.keys():
        report += f"\n{name.capitalize()} Sequence:\n"
        report += f"Mean: {analysis[name]['mean']:.2f}\n"
        report += f"Median: {analysis[name]['median']:.2f}\n"
        report += f"Standard Deviation: {analysis[name]['std_dev']:.2f}\n"
        report += f"Growth Rate: {analysis[name]['growth_rate']:.2f}\n"
        report += "-" * 30 + "\n"
    
    return sequences, analysis, fig, report

if __name__ == "__main__":
    sequences, analysis, fig, report = main()
    print(report)
    plt.show()