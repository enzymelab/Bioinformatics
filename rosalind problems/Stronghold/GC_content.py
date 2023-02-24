
def readFile(filePath):
    """read a file and return a list of lines"""
    with open (filePath, 'r') as f:
        return[l.strip() for l in f.readlines()]

def gcContent(seq):
    """GC Content in aDNA/RNA string"""
    return round((seq.count('C')+seq.count('G'))/len(seq) * 100, 6)

# Read data from the file(FASTA formatted file)
# storing file contents in a list
FASTAFile = readFile("test_data/gc_content.txt")
# dictionary for Labels + data
FASTADict = {}
# String for hilding the current label
FASTALabel = ""
# Clean/prepare the data (format for ease of you with our GC-content finction)

# # coverting FASTA/List data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] =""
    else:
        FASTADict[FASTALabel] += line


# format the data (store the data in a convient way)
# Run needed operation on the data (pass the data to our gc-content function)
# using dictionary comprehension to generate a new dictionary
ResultDict = {key: gcContent(value) for (key, value) in FASTADict.items()}
print (ResultDict)
# looking for the max value in values() for our new dictionary
MaxGCKey = max(ResultDict, key = ResultDict.get)
# Collect results (Rosalind Subminssion in our case)
print (f'{MaxGCKey[1:]}\n{ResultDict[MaxGCKey]}')