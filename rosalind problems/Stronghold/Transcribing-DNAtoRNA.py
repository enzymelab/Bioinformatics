import collections


def transcription(seq):
    """transcript DNA to RNA sequence, replace T with U"""
    return seq.replace("T", "U")
testDNA = "CCGACCCGGTCCACTATCAAGGAACAGACGTGGACTTTACCGGAACAATAAGGTGATGTTTGATGCTTATGTCTTACAAATTACCACTTCGGATAGAGGGAGATAAAAGTGACGACCACTAACCCCGGTCAAACATAAGGGACCCCACGATCTTGGTGAATCACGACGTTATCCTCCCCGGCGCTGTACCAGCATGTCCCCAAATGGACGGCTACAGAGTCAGTGAATCATATGCTATCCAAATGGTAGCCAATCGCGCTTCGGTCAGAGGGCTTGACACTTGTGTATCGCTCCCATCTTTGCAAATTAGTAGCCCAGACCGGTGTCTGGCCGATGATCTCAGCGAGGTATGGTTATGACCACCCAGAAGACACTACAGCACAACATAAACCCCCTTATTAATCTGATTCCCGAAGTGCCCGCCCCTCGAGCCAATGCGTGACTGGAGGGACACAATAACGAGGCGCAGTCTTGGTTTCATATTTCAGAGACCCTTGGCCCAGCTGCATTAGAGCTTAATCCTGTTGTCTATACAACGGTAGCCGCCGACCAGCTCAATAATGAACCTTGTAGGTCGATTCCCCGAGATAAAATATGCTACGGTGCCCGATTGGCGTCGCTGCATCGTGAGGAACGCTTTAGTGACTTGTAACTCGACAAAGCGCCGTCTTGACAGGAGGATGTTTCTCCTACCAAACAGCGTAAGGTCAGGATCTCTATTGAGCCGTTGAGCGTGCTATCCAGGATTCTGCCTAGTGTGTGTAATGAGATTCGCAAAGCGTTTATTGCATGGCATAGAGCAACGCTGAGCACCTGCGTATGGCGAGAAGTCATACACGGAGCGTATTACGTTGCGTTTTGTGAATCTAATTTGACTCCCGTTG"

print(f'RNA transcription: {transcription(testDNA)}\n')