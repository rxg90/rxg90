#inclusive.py

frase = 'Todos somos programadores'
palabras = frase.split()
frase_t=''

for palabra in palabras:
    if palabra[-1:]=='o':
       palabra=palabra[:-1]+'e'   
    elif palabra[-2:]=='os':
     palabra = palabra [:-2]+'es'
    frase_t = frase_t +' '+palabra
print(frase_t)
#'todes somes programadores'

