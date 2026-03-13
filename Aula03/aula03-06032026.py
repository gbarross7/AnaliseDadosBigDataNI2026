#Anotações da Aula 03
# '><' - 
# '>=' -
# '<=' -  
# '==' -
# '!=' - 

#Ex1:
a=10
b=5

#f abaixo significa formatar 
print(f'Soma:{a + b}/n')   
print("Subtração:",a - b)
print("Multiplicação:",a*b)
print("Divisão:", a/b)

# Ex2:tem como somar variáveis (definidas pelo'=') mesmo que sejam textos
primeiro_nome="Maria"
segundo_nome="Silva"
nome_completo= primeiro_nome + segundo_nome
print(nome_completo)
print(f"O tipo armazenado na variável 'primeiro_nome' é {type(primeiro_nome)}")

#fórmula para fazer quebra de linha (começar com aspas dupla)
print("O tipo armazenado \n"
      f"na variável 'primeiro_nome' é{type(primeiro_nome)}")

#Ex 3:
x=21
y=30
print("x é maior que y?", x > y)
print("x é igual a y?", x == y)


#Nas comparações de variáveis utiliza-se: 'and' (E), 'or' (ou), 'not' (não)
#Ex4:
tem_carteira= True
idade= 18
tem_carro=False
pode_dirigir= idade >= 18 and tem_carteira
print("pode dirigir?", pode_dirigir)


#Ex5: 
#tipos de comando print,ower,replace, upper
#no caso de ower e upper precisa do parentesis vazio
frase= "Python é divertido!"
print(frase.upper())
nova_frase= frase.replace("divertido", "poderoso")
print(nova_frase)

#Ex6 - formas de atualizar uma mesma lista 
contador = 0
contador += 5 #outra forma de escrever isso: contador=contador+5 - nome disso Incremento 
contador -= 2 # outra forma de escrever isso: contador=contador-2 - nome disso Decremento 
contador *= 3 #outra forma de escrever isso: contador=contador*3 - 
contador /=3 #outra forma de escrever isso: contador=contador/3
print("valor final contador:",contador)  # dentro do parantesis tem que colocar a variável fora das aspas

c1= 'arroz,'
c1+= 'feijão'
print("valor final contador1", c1)


#Ex7 
f = 10
l = 20
u = 30

média = (f+l+u)/3
print (média)

i = int(input("Digite uma nota"))
j = 40
k = 50

escreva = (i+j+k)/3
print("escreva", escreva)


