import numpy as np

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
            'growth_rate': arr[-1] / arr[-2] if arr[-2] != 0 else 0,
            'differences': np.diff(arr)
        }
    
    return analysis