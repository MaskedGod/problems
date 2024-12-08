def to_rna(dna_strand):
    """
    replacing each nucleotide with its complement:
    G -> C
    C -> G
    T -> A
    A -> U
    """
    rna_table = str.maketrans({"G": "C", "C": "G", "T": "A", "A": "U"})
    transcripted = dna_strand.translate(rna_table)
    return transcripted


print(to_rna(""))  # , ""
print(to_rna("C"))  # , "G"
print(to_rna("G"))  # , "C"
print(to_rna("T"))  # , "A"
print(to_rna("A"))  # , "U"
print(to_rna("ACGTGGTCTTAA"))  # , "UGCACCAGAAUU"
