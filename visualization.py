import matplotlib.pyplot as plt
import seaborn as sns

def visualize_sequences(sequences, analysis):
    """
    Creates visualizations for the sequences
    """
    plt.figure(figsize=(15, 10))
    
    # Plot sequences
    plt.subplot(2, 2, 1)
    for name, sequence in sequences.items():
        plt.plot(sequence, label=name)
    plt.title('Growth of Different Sequences')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.yscale('log')
    
    # Plot growth rates
    plt.subplot(2, 2, 2)
    names = list(sequences.keys())
    growth_rates = [analysis[name]['growth_rate'] for name in names]
    plt.bar(names, growth_rates)
    plt.title('Growth Rates')
    plt.xticks(rotation=45)
    
    # Plot differences distribution
    plt.subplot(2, 2, 3)
    for name in sequences.keys():
        differences = analysis[name]['differences']
        
        if len(differences) > 1:  # KDE için en az 2 farklı değer olmalı
            sns.kdeplot(differences, label=name)
        else:
            print(f"{name} dizisi için KDE hesaplanamadı, yeterli veri yok.")
            
    plt.title('Distribution of Differences')
    plt.legend()
    
    plt.tight_layout()
    
    return plt.gcf()