#Euler16-------------------------------------------------------------------------

def sommepuissance(n):
    c = str(2**n)
    s = 0
    for i in range(len(c)):
        s = s + int(c[i])
    return s

assert sommepuissance(15) == 26
print(sommepuissance(1000))

#Euler22-------------------------------------------------------------------------

def names():
    import os
    l = open("p022_names.txt", "r")
            
    L= sorted(l)
    print(L)
    L = L[0].split(",")
    L.sort()
    
    for i in range(len(L)):
        L[i] = L[i].replace('"','')
    
     
    somme = 0
    for i in range(len(L)):
        nom = L[i]
        s = 0
        for k in range(len(nom)):
            s += ord(nom[k])-64
            #j'avais fait ce TD avant le cours de vendredi, je ne connaissais alors pas les dictionnaires
        somme += (i+1)*s
    l.close()
    return somme

print(names())

#Euler55--------------------------------------------------------------------------

def palindrom(k):
    n=str(k)
    N=n[::-1]
    return (int(N))

print (palindrom (1062))
print (palindrom (5335))



def boucle(a):
    s=0
    b=a
    for i in range (50):
        b=palindrom(a)+a
        if s==0:
            if b==palindrom(b):
                s=1
        a=b
        if s!=0:
            i=49
    return(s)

    
def lychrel(T):
    lychrel=0
    for a in range (10,T):
        if boucle(a)==0:
            lychrel +=1
    return (lychrel)

print (lychrel(10000))





