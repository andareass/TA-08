#import gensim.models as gs
#from os import listdir
#from os.path import isfile, join
# from gensim.models.doc2vec import TaggedDocument
#from collections import OrderedDict
# import nltk
# from nltk import tokenize
# import unidecode
# from nltk.tokenize import sent_tokenize
# import re
# from collections import Counter
# from docx import Document

#path to the input corpus files
def main(file_1,file_2):
    file_dir = 'project/Similarity/Data/test/'
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns
    import math
    import re
    import unidecode
    import nltk
    from os import listdir
    from os.path import isfile, join
    from nltk import tokenize
    from nltk.tokenize import sent_tokenize
    from collections import Counter

    def twoCharGram(dataset):
        with open(dataset, 'r') as data:
            textFile = data.read().replace('\n', ' ')
            kGrams = set()
            # 2-Char gram
            for i in range(len(textFile)-1):
                if textFile[i] + textFile[i+1] not in kGrams:
                    kGrams.add(textFile[i] + textFile[i+1])
        return kGrams

    def jaccard(D1, D2):
        jaccard_calculation = 100.* len(D1.intersection(D2))/ len(D1.union(D2))
        return jaccard_calculation

    filename1=file_dir+file_1
    filename2=file_dir+file_2
    D1set = twoCharGram(filename1)
    D2set = twoCharGram(filename2)
    return (jaccard(D1set,D2set))