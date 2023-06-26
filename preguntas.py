"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def leer():
    lista=[]
    with open('data.csv') as File:
        reader = csv.reader(File, delimiter='\t')
                        
        for row in reader:
            lista.append(row)
    return lista

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    lista = leer()
    count=0
    for i in lista:
        count+= int(i[1])
    return count


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista = leer()
    result=[]
    letras=['A','B','C','D','E']

    for i in letras:
        valor = 0 
        for j in lista:
            if(i==j[0]):
                valor+=1
        result.append((i,valor))
  
    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista = leer()
    result=[]
    letras=['A','B','C','D','E']
    for i in letras:
        valor =0 
        for j in lista:
            if(i==j[0]):
                valor+=int(j[1])
        result.append((i,valor))
 
    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    lista = leer()
    result=[]
    data=['01','02','03','04','05','06','07','08','09','10','11','12']

    for i in data:
        valor=0
        for j in range(len(lista)):
            variable = lista[j][2].split("-")
            fecha = variable[1]
            if(i==fecha):
                valor +=1
        result.append((i,valor))
    
    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    lista = leer()
    result=[]
    data=['A','B','C','D','E']

    for i in data:
        tupla=[]
        for j in lista:
            if(i==j[0]):
                tupla.append(int(j[1]))
        result.append((i,max(tupla),min(tupla)))
   
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista = leer()
    result=[]
    data=['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']
    valores=[]

    for i in lista:
        ultimo = i[4].split(",")
        for k in ultimo:
            valores.append(k)
    
    for d in data:
        tupla=[] 
        for l in valores:
            if(d==l[:3]):
                num = l.split(":")
                tupla.append(int(num[1]))
        result.append((d,min(tupla),max(tupla)))

    
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista = leer()
    result=[]
    numeros=['0','1','2','3','4','5','6','7','8','9']

    for n in numeros:
        contiene =[]
        for a in lista:
            if(a[1]==n):
                contiene.append(a[0])
        result.append((int(n),contiene))

    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista = leer()
    result=[]
    numeros=['0','1','2','3','4','5','6','7','8','9']
    
    for n in numeros:
        contiene =[]
        for a in lista:
            if(a[1]==n and a[0] not in contiene):
                contiene.append(a[0])

        result.append((int(n),sorted(contiene)))
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista = leer()
    result={}
    data=['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']
    valores=[]
    for Lasval in lista:
        ultimo = Lasval[4].split(",")
        for k in ultimo:
            valores.append(k)

    for d in data:
        tupla=[] 
        for l in valores:
            if(d==l[:3]):
                num = l.split(":")
                tupla.append(int(num[1]))
        result.update({d:len(tupla)})

    return result



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista = leer()
    result=[]

    for a in lista:
        val = len(a[3].split(","))
        val2 = len(a[4].split(","))
        result.append((a[0],val,val2))

    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    lista = leer()
    result={}
    letras= ['a','b','c','d','e','f','g']
    newArr=[]
    for a in lista:
        newArr.append((a[1],a[3].split(",")))
    
    for l in letras:
        contar = 0
        for n in newArr:
            if(l in n[1]):
                contar += int(n[0])
        result.update({l:contar})

    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    lista = leer()
    result={}
    letras= ["A","B","C","D","E"]
    for l in letras:
        contar = 0
        for a in lista:
            if(a[0]==l):
                lista2 = a[4].split(",")
                for val in lista2: 
                    s= val.split(":")
                    contar+=int(s[1])
        result.update({l:contar})

    return result
