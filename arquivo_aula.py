# Copiar Lista em python

lista_a = ['lucas','joao','pedro','jessica']
lista_b = lista_a 


lista_b.append("Feijao")
print(lista_a)
print(lista_b)

texto_a = 'Lira'
texto_b = texto_a
texto_b = texto_b.replace("L", "B")
print(texto_a)
print(texto_b)



# 2 formas

lista_c = lista_a[:]
lista_c.append("Arroz")
print(lista_a)
print(lista_c)


# 3 formas 


lista_c = lista_a.copy()
lista_c.append("Arroz")
print(lista_a)
print(lista_c)

# para listas de listas, temos que pensar diferente


produtos = [
    ["Ipad", 5000],
    ["Iphone", 4500],
    
    
]

produtos2 = produtos[:]
produtos2[0][1] = 6000
print(produtos)
print(produtos2)

# solução é um deepcopy
import copy
produtos3 = copy.deepcopy(produtos)
produtos3[0][1] = 1000
print(produtos)
print(produtos3)