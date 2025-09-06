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

#Regla 1
if(objeto['A'] != '' and objeto['B'] != ''):
    if(objeto['A'] == 'v' and objeto['B'] == 'v'):
        objeto['C'] = 'v'
    else:
        objeto['C'] = 'f'
#Regla 2
if(objeto['D'] != '' and objeto['E'] != '' and objeto['F'] != ''):
    if(objeto['D'] == 'v' and objeto['E'] == 'v' and objeto['F']):
        objeto['G'] = 'v'
    else:
        objeto['G'] = 'f'
#Regla 3
if(objeto['H'] != '' and objeto['I'] != ''):
    if(objeto['H'] == 'v' and objeto['I'] == 'v'):
        objeto['J'] = 'v'
    else:
        objeto['J'] = 'f'
#Regla 4
if(objeto['C'] != '' and objeto['G'] != ''):
    if(objeto['C'] == 'v' and objeto['G'] == 'v'):
        objeto['K'] = 'v'
    else:
        objeto['K'] = 'f'
#Regla 5
if(objeto['G'] != '' and objeto['J'] != ''):
    if(objeto['G'] == 'v' and objeto['J'] == 'v'):
        objeto['L'] = 'v'
    else:
        objeto['L'] = 'f'
#Regla 6
if(objeto['K'] != '' and objeto['L'] != ''):
    if(objeto['K'] == 'v' and objeto['L'] == 'v'):
        objeto['M'] = 'v'
    else:
        objeto['M'] = 'f'

for i in objeto:
    print(f'El objeto {i} es: {objeto[i]}')

if(objeto['M'] == ''):
    print("No se ha podido completar la conclusion del nodo objetivo...")
else:
    print(f"El valor del nodo objetivo 'M' es '{'verdadero' if objeto['M'] == 'v' else 'falso'}'")