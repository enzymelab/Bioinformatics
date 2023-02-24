# import this

# Variables and Some Arithmetic
a = 871
b = 987
result = a**2 + b**2
print (f'{a}^2 + {b}^2 = {result}')

# Strings and Lists
word1Start = 27
word1End = 32

word2Start = 85
word2End = 98
textContent = "hqxQwkAlOWWbstQOrINjvs9XtcfTurdusX6UHusZbBpORuNQcPnA5wnLvsODuLyIfELhmWmEO0R1V1vuW9tNhflavomaculatus1SBsndgH7spCoG90yzsP4WYCvBU3yb0AsrAdJiVhbMvTpXGmMJMseW5eQzM3AMFho4fkYOTbGukR8mese3lIxsoi4cYx2l."
print(
    f'{textContent[word1Start:word1End + 1]} {textContent[word2Start:word2End+1]}'
)
print(
    f'{textContent[27:33]} {textContent[85:99]}'
)

#Conditions and Loops
result = 0
startN = 4844 
endN = 9298
for x in range(startN,endN +1):
    if x %2 != 0:
        result += x
print(result)

# Working with Files

num = 0
f = open("test.txt", "r")
for line in f.readlines():
    if num %2 == 1:
        print (line)
    num += 1
#another method
outputFile = []
with open('test.txt','r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines() )if pos %2 !=0
    ]
print(outputFile)
with open ('out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))

# Dictionaries
from collections import Counter
text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
# first way
# countWord = {}
# for word in text.split(' '):
#     if word in countWord:
#         countWord[word] += 1
#     else:
#         countWord[word] = 1

#Counter way
countWord = Counter(text.split(' '))
for key, value in countWord.items():
    print(key,value)