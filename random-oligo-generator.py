import random

def generate_nucleotide_sequence(sequence_type='DNA', length=10):
    """
    Generate a random nucleotide sequence.
    
    Args:
        sequence_type (str): 'DNA' or 'RNA'. Case insensitive.
        length (int): Length of sequence to generate.
        
    Returns:
        str: Random nucleotide sequence.
    """
    sequence_type = sequence_type.upper()
    if sequence_type == 'D':
        nucleotides = ['A', 'C', 'G', 'T']
    elif sequence_type == 'R':
        nucleotides = ['A', 'C', 'G', 'U']
    else:
        raise ValueError("sequence_type must be 'DNA' or 'RNA'.")
    
    return ''.join(random.choices(nucleotides, k=length))

# Example usage:
if __name__ == "__main__":
    seq_type = input("Enter sequence type ((D) for DNA / (R) for RNA): ")
    length = int(input("Enter sequence length: "))
    print("Generated sequence:\n" + generate_nucleotide_sequence(seq_type, length))
    
    input("Press any key to exit.")
