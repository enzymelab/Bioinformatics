from DNAToolKit import *
from utilities import colored
import random

randDNAStr = ''. join([random.choice(Nucleotides)
                       for nuc in range(50)])

print(validateSeq(randDNAStr))
print(countNucFrequency(randDNAStr).values())
for valus in countNucFrequency(randDNAStr).values():
    print(valus)

print(f'\nSequence:{randDNAStr}\n')
print(f'RNA transcription: {transcription(randDNAStr)}\n')
print(f'\nSequence: {colored(randDNAStr)}\n')
print(f'[1] = Sequence Length: {len(randDNAStr)}\n')
print(
    colored(f'[2] = Nuclaotide Frenquency: {countNucFrequency(randDNAStr)}\n'))
print(colored(f'[3] = Reverse complement: {reverseComplement(randDNAStr)}\n'))

print(f"[4] = DNA string + Reversecomplement: \n5' {colored(randDNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(randDNAStr))])}")
print(colored(f"3' {reverseComplement(randDNAStr)[::-1]} 5' [complement]"))
print(colored(f"5' {reverseComplement(randDNAStr)} 3'[reversecomplement]\n"))
print(f'[5] = GC Percentage: {gcContent(randDNAStr)}%')
print(
    f'[6] = GC percentage in Subsection k=5: {gcContentSubsec(randDNAStr, k=5)}\n')
print(f'[7] = AminoAcids Sequence from DNA: {translateSeq(randDNAStr, 0)}\n')
print(f'[8] = Codon Frequency (L): {codonUsage(randDNAStr, "L")}\n')
print('[9] = Reading Frames: ')
for frame in genReadingFrames(randDNAStr):
    print(frame)
testrfframe = ['S', 'D', 'M', 'D', 'I', 'Y', 'L',
               'E', 'F', 'I', 'F', 'M', 'G', 'L',  'S', 'M', '_', 'D', 'T']
print(proteinsFromRf(testrfframe))

print('\n[10] = Allproteins in 6 open reading frames:')
for prot in allProteinsFromorfs(NM_000207_3, 0, 0, True):
    print(f'{prot}')
