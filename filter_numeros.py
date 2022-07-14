# 1- retornar uma lista com números negativos

lista = [-1, 4, 66, -11, -3, 7, 50, 34, -42, -1000]

negativos = list(filter(lambda x : x < 0, lista))

print(f'Lista de números negativos\n{negativos}')


# 2- retornar uma lista com os números entre 1 e 100

intervalo = list(filter(lambda x : x >= 0 and x <= 100, lista))

print(f'Lista de números de 1 a 100\n{intervalo}')

# 3- retornar uma lista com números pares

pares = list(filter(lambda x : x % 2 == 0, lista))

print(f'Os números pares são:\n{pares}')