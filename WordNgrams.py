import itertools

def cleanText(corpus):
    punctuation = """.,?!:;(){}[]"""
    corpus = [z.lower().replace('\n','') for z in corpus]
    corpus = [z.replace('<br />', ' ') for z in corpus]
    #treat punctuation as individual words
    for c in punctuation:
        corpus = [z.replace(c, ' %s '%c) for z in corpus]
    corpus = [z.split() for z in corpus]
    return corpus 
##########################################################
##########################################################


def getWordNgrams(corpus, n):
    bi = []   
    corpus = cleanText(corpus)
    if n == 1:
        return corpus
    elif n > 1:      
        for doc in corpus:
            bidoc=[]
            bigrams = ngrams(doc, None, n)
            for itx in bigrams: 
                gg = ""                                      
                for item in itx:
                    gg += item+"_"
                gg = gg.rstrip("_")
                #ngram = str(list(bigrams[itx]))#Conversion de los ngramas                        
                #ngram.replace("[","{")
                bidoc.append(gg)
            bi.append(list(bidoc))
        return(bi)
##########################################################
    

def ngrams(xs, f = None, n=2):
    ts = itertools.tee(xs, n)
    for i, t in enumerate(ts[1:]):
        for _ in xrange(i + 1):
            next(t, None)
    return map(f, itertools.izip(*ts))
#########################################