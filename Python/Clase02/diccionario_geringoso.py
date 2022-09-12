

def diccionario_geringoso(lista):
    nueva_lista=[]
    capadepenapa=''
    diccionario={}
    vocales='a,e,i,o,u'
    for palabra in lista:
        for c in palabra:
            if c in vocales:
                capadepenapa += c + 'p' + c
            else:
                capadepenapa += c
        nueva_lista.append(capadepenapa)
        capadepenapa=''
    diccionario = dict(zip(lista, nueva_lista))
    print(diccionario)

lista1 = ['banana', 'manzana', 'mandarina']

diccionario_geringoso(lista1)


#Output:
#diccionario{'banana':bapanapanapa,
#           'manzana':manpazapanapa,
#            'mandarina':manpadaparipinapa
#            }