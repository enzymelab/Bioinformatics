# DNA toolkit file
import collections
from structure import *

# Check th sequence to make sure it is a DNA string and uppercase


def validateSeq(dnaSeq):
    tmpseq = dnaSeq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    # tmpFreqDict = {"A":0, "T":0, "C": 0, "G": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] +=1
    # return tmpFreqDict
    return dict(collections.Counter(seq))

# transcript DNA to RNA sequence


def transcription(seq):
    """transcript DNA to RNA sequence, replace T with U"""
    return seq.replace("T", "U")

# reverse complement


def reverseComplement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string"""
   # return ''.join([DNAReverseComplement[nuc] for nuc in seq])[::-1]

    # Pythpnic approach. A little bit faster
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]


def gcContent(seq):
    """GC Content in aDNA/RNA string"""
    return round((seq.count('C')+seq.count('G'))/len(seq) * 100)


def gcContentSubsec(seq, k=20):
    """GC content in a DNA/RNA sub-sequence length k, k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gcContent(subseq))
    return res


def translateSeq(seq, initPos=0):
    """Translates DNA sequence into protein sequence"""
    return [DNACodons[seq[pos:pos + 3]] for pos in range(initPos, len(seq) - 2, 3)]


def codonUsage(seq, aminoacid):
    """provide the frequency of each codon in the sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNACodons[seq[i:i+3]] == aminoacid:
            tmpList.append(seq[i:i+3])
    freqDict = dict(collections.Counter(tmpList))

    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict


def genReadingFrames(seq):
    frames = []
    frames.append(translateSeq(seq, 0))
    frames.append(translateSeq(seq, 1))
    frames.append(translateSeq(seq, 2))
    frames.append(translateSeq(reverseComplement(seq), 0))
    frames.append(translateSeq(reverseComplement(seq), 1))
    frames.append(translateSeq(reverseComplement(seq), 2))
    return frames


def proteinsFromRf(aaSeq):
    """Compute all possible proteins in an aminoacid seq and return a list of possible proteins"""
    currentProt = []
    proteins = []
    for aa in aaSeq:
        if aa == "_":
            # stop accumulating amino acid if _ stop was found
            if currentProt:
                for p in currentProt:
                    proteins.append(p)
                currentProt = []
        else:
            # Start accumulating amino acidd if M is found
            if aa == "M":
                currentProt.append("")
            for i in range(len(currentProt)):
                currentProt[i] += aa
    return proteins


def allProteinsFromorfs(seq, startReadPos=0, endReadPos=0, ordered=False):
    if endReadPos > startReadPos:
        rfs = genReadingFrames(seq[startReadPos: endReadPos])
    else:
        rfs = genReadingFrames(seq)
    res = []
    for rf in rfs:
        prots = proteinsFromRf(rf)
        for p in prots:
            res.append(p)
    if ordered:
        return sorted(res, key=len, reverse=True)
    return res
