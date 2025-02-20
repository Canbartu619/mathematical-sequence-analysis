import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_mathematical_sequences(n_terms=50):
    """
    Generates different mathematical sequences and their properties
    """
    # Generate sequences
    sequences = {
        'fibonacci': [1, 1],  # Fibonacci sequence
        'square': [],         # Square numbers
        'triangle': [],       # Triangle numbers
        'prime': [],          # Prime numbers
    }
    
    # Generate Fibonacci sequence
    for i in range(2, n_terms):
        sequences['fibonacci'].append(sequences['fibonacci'][i-1] + sequences['fibonacci'][i-2])
    
    # Generate square numbers
    sequences['square'] = [i**2 for i in range(1, n_terms+1)]
    
    # Generate triangle numbers
    sequences['triangle'] = [i*(i+1)//2 for i in range(1, n_terms+1)]
    
    # Generate prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = []
    num = 2
    while len(primes) < n_terms:
        if is_prime(num):
            primes.append(num)
        num += 1
    sequences['prime'] = primes
    
    return sequences

def analyze_sequences(sequences):
    """
    Analyzes mathematical properties of the sequences
    """
    analysis = {}
    
    for name, sequence in sequences.items():
        # Convert to numpy array for calculations
        arr = np.array(sequence)
        
        # Basic statistics
        analysis[name] = {
            'mean': np.mean(arr),
            'median': np.median(arr),
            'std_dev': np.std(arr),
            'growth_rate': arr[-1] / arr[-2],
            'differences': np.diff(arr)
        }
    
    return analysis

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