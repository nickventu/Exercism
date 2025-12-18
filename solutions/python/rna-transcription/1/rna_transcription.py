def to_rna(dna_strand):

    dna_to_rna = str.maketrans('GCTA','CGAU')

    rna_strand = dna_strand.translate(dna_to_rna)

    return rna_strand