dna = "ATGCGATACGCTTGA"

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

gc_content = (g + c) / len(dna) * 100

print("\nDNA Analysis Result:")
print("-------------------")
print(f"A: {a}")
print(f"T: {t}")
print(f"G: {g}")
print(f"C: {c}")
print(f"GC-content: {gc_content:.2f}%")