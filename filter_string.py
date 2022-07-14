# quantidade de espaços em uma string

string = 'O rato roeu a roupa do rei de roma.'

def espaco(x):
    return x == ' '

espacos = filter(espaco, string)

lista = list(espacos)

print(f'A string tem {len(lista)} espaços.')

def espaco2(x):
    return len(list(filter(lambda s: s == ' ', x)))
print(f"{espaco2('O espaço aqui é diferente.')}")

# 2 - Verificar se a letra 'c' está na string

def c_presente(s):
    return filter(lambda x: x =='c', s)

cp = list(c_presente(string))
if len(cp) == 0:
    print('A letra c não está presente na frase.')
else:
    print(f'A letra c está presente {len(cp)} vezes na frase.')

string = 'Comprei um cavalo de cor caramelo'

cp = list(c_presente(string))
if len(cp) == 0:
    print('A letra c não está presente na frase.')
else:
    print(f'A letra c está presente {len(cp)} vezes na segunda frase.')