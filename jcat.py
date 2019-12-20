
def jcat(jcat_out):

    aa_input = ['F','L','I','M','V','S','P','T','A','Y','H','Q','N','K','D','E','C','W','R','G']

    with open(jcat_out,"r") as jfile:
        nt_seq = jfile.readline()
        codons = [nt_seq[i:i+3] for i in range(0, len(nt_seq), 3)]

    codon_conv = {k: v for k, v in zip(aa_input, codons)}

    print(codon_conv)
