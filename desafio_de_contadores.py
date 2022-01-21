lista = []

for contador_regressivo in range(10, 1, -1):
    lista.append(contador_regressivo)

for indice, valor in enumerate(lista):
    print(indice, valor)

#Solução pelo professor
print('--------------------')
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
