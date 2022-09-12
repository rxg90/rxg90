cadena = 'Geringoso'
capadenenapa=''
vocales='a,e,i,o,u'

for c in cadena:
    if c in vocales:
        c=c.replace('a','apa')
        c=c.replace('e','epe')
        c=c.replace('i','ipi')
        c=c.replace('o','opo')
        c=c.replace('u','upu')
    capadenenapa=capadenenapa+c    
print(capadenenapa)  
#Output: Geperipingoposopo



    




