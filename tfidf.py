import math, collections

def preprocess(corpus:list[str])->list:
    new_corpus = []
    for sentence in corpus:
        new_corpus = sentence.lower().split()
    return new_corpus

# tf = (term frequency) how frequent is this word in the document?
def tf(doc:list)->dict:
    """
    input: preprocessed document
    output: term freuency data from collections.Counter
    """
    return collections.Counter(doc)

# idf = (inverse document frequency) 
# ... prioritizes words with low frequency
# ... tries to emphasize words that are too frequent in the corpus
def idf_corp(corpus):
    """
    calculate idf for corpus
    """
    pass

A = ["The car is driven on the road"]
B = ["The Truck is Driven on the highway"]
A = preprocess(A)
B = preprocess(B)
print(A,B)
print(tf(A))
print(tf(B))
