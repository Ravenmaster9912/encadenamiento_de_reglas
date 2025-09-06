objeto = {
    'A': '',
    'B': '',
    'C': '',
    'D': '',
    'E': '',
    'F': '',
    'G': '',
    'H': '',
    'J': '',
    'K': '',
    'L': '',
    'M': ''
}

objeto['H'] = 'v'
objeto['I'] = 'v'
objeto['K'] = 'v'
objeto['M'] = 'f'

#Regla 6
if(objeto['M'] != ''):
    if(objeto['M'] == 'v'):
        objeto['K'] = 'v'
        objeto['L'] = 'v'
#Regla 5
if(objeto['L'] != ''):
    if(objeto['L'] == 'v'):
        objeto['G'] = 'v'
        objeto['J'] = 'v'
#Regla 4
if(objeto['K'] != ''):
    if(objeto['K'] == 'v'):
        objeto['C'] = 'v'
        objeto['G'] = 'v'
#Regla 3
if(objeto['J'] != ''):
    if(objeto['J'] == 'v'):
        objeto['H'] = 'v'
        objeto['I'] = 'v'
#Regla 2
if(objeto['G'] != ''):
    if(objeto['G'] == 'v'):
        objeto['D'] = 'v'
        objeto['E'] = 'v'
        objeto['F'] = 'v'
#Regla 1
if(objeto['C'] != ''):
    if(objeto['C'] == 'v'):
        objeto['A'] = 'v'
        objeto['B'] = 'v'

for i in objeto:
    print(f'El objeto {i} es: {objeto[i]}')

if(objeto['A'] == ''):
    print("No se ha podido completar la conclusion del nodo objetivo...")
else:
    print(f"El valor del nodo objetivo 'A' es '{'verdadero' if objeto['A'] == 'v' else 'falso'}'")