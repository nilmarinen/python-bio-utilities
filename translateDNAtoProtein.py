# 3-frame protein translation tool

# Standard codon table
codon_table = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
}

def translate(seq):
    seq = seq.upper().replace(" ", "")
    protein = ""
    # translate in steps of 3, ignoring leftover bases (<3)
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, "X")   # X = unknown/invalid codon
    return protein


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("Paste your DNA sequence below (multi-line allowed).")
print("Finish with an empty line:\n")

lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

dna = "".join(lines)  # join all lines without newline characters

# Generate all three reading frames
frame1 = translate(dna[0:])
frame2 = translate(dna[1:])
frame3 = translate(dna[2:])

print("\n--- Translation Results ---")
print("Frame 1:", frame1)
print("Frame 2:", frame2)
print("Frame 3:", frame3)

input("\nPress Enter to exit...")
