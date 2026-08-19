from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
p=PorterStemmer()
text="it is very important to be pythonly while you are pythoing with python. while other pythoners have poorly pythoned atlest once"
for w in word_tokenize(text):
    print(" ",p.stem(w),end='')
