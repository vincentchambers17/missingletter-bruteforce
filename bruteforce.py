import itertools
import string

# The word to be bruteforced
word = "t-a-19-/"

letters = [l for l in string.ascii_lowercase] #['a','b','c'.....]

for c1,c2,c3 in itertools.product(letters, repeat=3):
    print(word.replace('-','%s')%(c1,c2,c3))