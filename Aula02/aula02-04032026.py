#AULA DE VARIÁVEIS 
#boas práticas

print('olá mundo!') #comando pra imprimir uma resposta no terminal
idade=30
nome='maria'
preco=19.99
print(nome)
'''print('olámundo!)'''
print(type(nome))
print(type (idade))
print(type(preco))
vazio=None

print(type(vazio))

decisao1=True
decisao2=False
print(type(decisao1))
print(type(decisao2))

nota1=7.0
nota2=8.0
nota3=((nota1+nota2)/2)


print(nota3)

valor1=5
valor2=4

valor3=(valor1+valor2),(valor1-valor2),(valor1*valor2),(valor1/valor2)
print(valor3)

#pra calcular módulo %

#Condições 

#if (sempre o primeiro elemento), elif (todos elementos, menos o primeiro e último), else (último elemento) - entre 

#Ex1:
placar_time1=None
placar_time2=None
resultado=None

if placar_time1 > placar_time2:
    resultado= 'Time 1 ganhou!'
elif placar_time1 < placar_time2:
    resultado='Time 2 ganhou!'
else: 
    resultado='Empate!'


