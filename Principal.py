'''
Created on 7 nov. 2017

@author: tecuapan
'''

import itertools
from prompt_toolkit.key_binding.bindings.vi import TextObject
from blaze.expr.reductions import nelements
import gensim
import os, string, re, nltk, glob, codecs,sys
from collections import Counter
from sets import Set 
from time import time
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.preprocessing import normalize
import numpy as np
from WordNgrams import getWordNgrams
from distributed.bokeh.status.main import doc
from openpyxl.styles.builtins import total
#from quitanexos import conjunciones
LabeledSentence = gensim.models.doc2vec.LabeledSentence
global x
x=0
################################################################################################
'''Esta funcion tiene como objetivo limpiar txt y crea pre'''
def cleaning_text(file_content):
    file_content=file_content.replace('\xa3','')
    file_content=file_content.replace('\xad','')
    file_content=file_content.replace('\x96','')
    file_content=file_content.replace('\xb7','')
    file_content=file_content.replace('\x95','')
    file_content=file_content.replace('\x85','')
    file_content=file_content.replace('\x0d','')
    file_content=file_content.replace('\x0a','')
    file_content=file_content.replace('\x1a','')
    file_content=file_content.replace('...','')
    file_content=file_content.replace('<br>','')
    file_content=file_content.replace('</br>','')
    file_content=file_content.replace('"','')
    file_content=file_content.replace('-','')
    file_content=file_content.replace('(','')
    file_content=file_content.replace(')','')
    file_content=file_content.replace('.',' ')
    file_content=file_content.replace(',',' ')
    file_content=file_content.replace('?',' ')
    file_content=file_content.replace('!',' ')
    file_content=file_content.replace(':',' ')
    file_content=file_content.replace(';',' ')
    file_content=file_content.replace('{',' ')
    file_content=file_content.replace('}',' ')
    file_content=file_content.replace('[',' ')
    file_content=file_content.replace('$',' ')
    file_content=file_content.replace(']',' ')
    file_content=file_content.replace('<br />',' ')
    file_content=file_content.replace(' and ',' ')
    file_content=file_content.replace(' but ',' ')
    file_content=file_content.replace(' or ',' ')
    file_content=file_content.replace(' so ',' ')
    file_content=file_content.replace(' after ',' ')
    file_content=file_content.replace(' as ',' ')
    file_content=file_content.replace(' because ',' ')
    file_content=file_content.replace(' before ',' ')
    file_content=file_content.replace(' since ',' ')
    file_content=file_content.replace(' until ',' ')
    file_content=file_content.replace(' when ',' ')
    file_content=file_content.replace(' while ',' ')
    file_content=file_content.replace(' until ',' ')
    file_content=file_content.replace(' till ',' ')
    file_content=file_content.replace(' over ',' ')
    file_content=file_content.replace(' from ',' ')
    file_content=file_content.replace(' for ',' ')
    file_content=file_content.replace(' during ',' ')
    file_content=file_content.replace(' down ',' ')
    file_content=file_content.replace(' by ',' ')
    file_content=file_content.replace(' between ',' ')
    file_content=file_content.replace(' besides ',' ')
    file_content=file_content.replace('out of','')
    file_content=file_content.replace(' on ',' ')
    file_content=file_content.replace(' off ',' ')
    file_content=file_content.replace(' of ',' ')
    file_content=file_content.replace('next to',' ')
    file_content=file_content.replace(' near ',' ')
    file_content=file_content.replace(' below ',' ')
    file_content=file_content.replace(' behind ',' ')
    file_content=file_content.replace(' before ',' ')
    file_content=file_content.replace(' at ',' ')
    file_content=file_content.replace(' after ',' ')
    file_content=file_content.replace(' about ',' ')
    file_content=file_content.replace(' an ',' ')
    file_content=file_content.replace(' a ',' ')
    file_content=file_content.replace(' under',' ')
    file_content=file_content.replace(' of ',' ')
    file_content=file_content.replace(' by ',' ')
    file_content=file_content.replace(' to ',' ')
    file_content=file_content.replace(' at ',' ')
    file_content=file_content.replace('opposite to','')
    file_content=file_content.replace('in order to','')
    file_content=file_content.replace('in spite of','')
    file_content=file_content.replace('close to','')
    file_content=file_content.replace('as far ass','')
    file_content=file_content.replace(' without ',' ')
    file_content=file_content.replace(' with ',' ')
    file_content=file_content.replace(' up ',' ')
    file_content=file_content.replace(' under ',' ')
    return file_content
    
#################################################################################################
'''Jala todos los archivos de directorio'''
def conseguir_todos_los_archivos(ruta):
    clasificacion=[]
    archivos=[]
    tem=glob.glob(ruta+"/*")
    tamano=len(tem)
    for item in tem:
        nelements=glob.glob(item+"/*")
        archivos.extend(nelements)
        for a in range(len(nelements)):
            clasificacion.append(re.sub(ruta,"",item))
    return archivos,clasificacion
#################################################################################################
def barra(progreso):
    tme=0
    
    a=int(progreso/10)
    print 
    if tme!=a:
        tme=a
        gato="#"
        for x in range(a):
            print gato*x
        os.system("cls")
#################################################################################################
'''Genera un pre de la carpeta que quieres'''
def Generacion_texto_limpiado_pre(ruta_entrada,ruta_salida):
    a,b=conseguir_todos_los_archivos(ruta_entrada)
    try:
        ayuda=None
        os.mkdir(ruta_salida)
        for tem in b:
            if ayuda!=tem:
                ayuda=tem
                os.mkdir(ruta_salida+ayuda)
        return complemento(a,b,ruta_salida)
    except WindowsError:
        print "Directorio creado"
        try:
            ayuda=None
            for tem in b:
                if ayuda!=tem:
                    ayuda=tem
                    os.mkdir(ruta_salida+ayuda)
            return complemento(a,b,ruta_salida)
        except WindowsError:
            return complemento(a,b,ruta_salida)
def complemento(a,b,ruta_salida):          
    global x
    tamano=len(a)
    if x<tamano:
        outf = codecs.open(filename=ruta_salida+b[x]+".pre" ,encoding='utf-8',mode='w',errors='replace') 
        doc = open(a[x],'r')
        temporal = doc.read()
        file_content = cleaning_text(temporal)
        outf = open(ruta_salida+b[x]+"/"+str(x)+".pre", "w")
        outf.write(file_content)
        if True:
            sucio=temporal
            limpio=file_content
        outf.flush()
        doc.close()
        outf.close()    
        x=x+1
        muestra=x
        total=tamano
        logico=True
        if x==tamano:
            logico=False
            x=0
        print "Archivo convertido a .pre "+str(1+x)+" de "+str(tamano) 
    return sucio,limpio,muestra,total,logico
#################################################################################################
'''Se encarga de
 leer los pre y hacer listas'''
def read_corpus(train_files,test_files):
    traindata   = []
    testdata    = []    
    for item in train_files:
        doc = ""
        infile = codecs.open(item, 'r', encoding='utf-8', errors='replace') 
        for line in infile.readlines():
            line =line.rstrip()
            doc+=line
        traindata.append(doc)
        infile.close()
    for item in test_files:
        doc = ""
        infile = codecs.open(item, 'r', encoding='utf-8', errors='replace') 
        for line in infile.readlines():
            line =line.rstrip()
            doc+=line
        testdata.append(doc)
        infile.close()
    return traindata,testdata
#################################################################################################
def cleanText(corpus):
    '''
    Funcion que preprocesa el texto para usar el modelo de bolsa de palabras
    '''
    punctuation = """.,?!:;(){}[]"""
    corpus = [z.lower().replace('\n','') for z in corpus]
    corpus = [z.replace('<br />', ' ') for z in corpus]
    #treat punctuation as individual words
    for c in punctuation:
        corpus = [z.replace(c, ' %s '%c) for z in corpus]
    corpus = [z.split() for z in corpus]
    return corpus
#################################################################################################
def parse_corpus(train_docs,test_docs,train_target,test_target):
    '''
    Metodo que aplica el modelo de bolsa de palabras al corpus 
    '''
    traindata = []
    testdata  = []
    for item in train_docs:
        #print item
        ngramCounter = Counter(item)          
        traindata.append(dict(ngramCounter))
    for item in test_docs:
        #print item
        ngramCounter = Counter(item)          
        testdata.append(dict(ngramCounter))
        
    vectorizer = DictVectorizer()    
    X = vectorizer.fit_transform(traindata)
    Y = vectorizer.transform(testdata)
    train_tar = np.array(train_target)
    test_tar = np.array(test_target)    
    features = vectorizer.get_feature_names()
    return (X,train_tar,Y,test_tar,features)        
######################################################


def machineLearning_scikit(train,train_tar,test,test_tar):
    liblinear = LinearSVC()
    clf = SVC(kernel='linear')
    train = normalize(train,norm='l2')
    test = normalize(test,norm='l2')                                                                                            
    liblinear.fit(train, train_tar)
    clf.fit(train, train_tar)
    score = liblinear.score(test, test_tar)
    score2 = clf.score(test, test_tar)
    print "Liblinear: "+str(score)
    print(liblinear.predict(test))
    print "SVC: "+str(score2)
    print(clf.predict(test))
#################################################################################################
#train_files,target = conseguir_todos_los_archivos("C:/TECUAPAN2")
#test_files,target2 = conseguir_todos_los_archivos("C:/TECUAPAN2")
#train_data,test_data = read_corpus(train_files,test_files)
#print train_data
#print "Dimension de vector "+str(len(train_data))
#print "Dimension de vector2 "+str(len(train_data))

'''
print "Inicio"
Generacion_texto_limpiado_pre("C:/tecuapan", "C:/TECUAPAN2")
print "termino"
'''
'''   
if __name__ == '__main__':
    print "Inicio"
    a,b=Generacion_texto_limpiado_pre("C:/tecuapan", "C:/Users/tecuapan/Pictures/Tesis")
    print "Listo"
    print "Texto sucio "+str(a)
    print "Texto limpio "+str(b)
'''    
'''
    trainpath = "C:\TECUAPAN2"
    testpath = "C:\TECUAPAN2"
    
    #limpia_corpus(trainpath)
    #limpia_corpus(testpath)
    train_files,target = conseguir_todos_los_archivos(trainpath)
    test_files,target2 = conseguir_todos_los_archivos(testpath)

    train_data,test_data = read_corpus(train_files,test_files)
    #print train_data
    #train_data=conjunciones(train_data)
    #test_data=conjunciones(test_data)
    #print type(train_data)
    train_data = getWordNgrams(train_data, 1)
    test_data = getWordNgrams(test_data, 1)
    #train_data = cleanText(train_data)
    #test_data = cleanText(test_data)
       
    train,train_tar,test,test_tar,features = parse_corpus(train_data,test_data,target,target2)
    machineLearning_scikit(train,train_tar,test,test_tar)

    print "Programa terminado"
'''