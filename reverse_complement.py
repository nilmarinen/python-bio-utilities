def load_sequence():
    choice = input("Paste (p) or file (f)? ").strip().lower()

    if choice == "p":
        print("Paste your DNA sequence below. Finish with an empty line:")
        lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            if not line.startswith(">"):  # ignore FASTA headers
                lines.append(line)
        return "".join(lines).upper()

    elif choice == "f":
        path = input("Enter the file path: ").strip()
        seq = []
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line.startswith(">"):
                    seq.append(line)
        return "".join(seq).upper()

    else:
        print("Invalid choice.")
        return load_sequence()


def reverse_complement(seq):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
        "N": "N"
    }
    return "".join(complement.get(base, "N") for base in reversed(seq))


# --- Main program ---
sequence = load_sequence()
revcomp = reverse_complement(sequence)

print("\nReverse complement:")
print(revcomp)
input("\nPress Enter to exit...")

