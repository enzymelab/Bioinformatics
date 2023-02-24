from bio_structuts import *
import random


class bioSeq:
    """DNA sequence class default value: ATCG, DNA, No label"""

    def __init__(self, seq="ATCG", seqType="DNA", label="No Label"):
        """Sequence initialization and validation"""
        self.seq = seq.upper()
        self.label = label
        self.seqType = seqType
        self.is_valid = self.__validateSeq()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seqType} sequence"
        pass

    def __validateSeq(self):
        """Check the sequence to make sure it is a DNA string and uppercase"""
        return set(Nucleotides).issuperset(self.seq)

    def getSeqBiotype(self):
        return self.seqType

    def showSeqInfo(self):
        """Return sequence information"""
        return f"[Label]: {self.label}\n[sequence]: {self.seq}\n[Biotype]: {self.seqType}\n[Length]: {len(self.seq)}"

    def generateDNASeq(self, length=10, seqType="DNA"):
        seq = ''. join([random.choice(Nucleotides)
                        for nuc in range(length)])
        self.__init__(seq, seqType, "Randomly generated sequence")
