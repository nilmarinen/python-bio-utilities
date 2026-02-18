source = input("Load from (F)ile or (P)aste sequence? ").strip().upper()
if source == "F":
    path = input("Enter file path: ").strip()
    with open(path, "r") as file:
        sequence = file.read()

elif source == "P":
    sequence = input("Paste your sequence here: ")

else:
    print("Unknown option. Choose F or P.")
    exit()
with open("sequence.txt", "r") as file:
    sequence = file.read().strip()

sequence = sequence.upper().replace("\n", "").replace(" ","")

length = len(sequence)
a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

gc_percentage = ((g_count + c_count) / length) * 100
print(f"Here's the stripped sequence: " + sequence)

print("Length:", length)
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
print("GC%:", round(gc_percentage, 2))
input("Press any key to exit")
