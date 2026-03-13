# # Operadores: AND (E), OR(OU), NOT (INVERTE O SENTIDO)

carro = True
combustivel = True

# #Qual a condição para este carro rodar? 

if carro==True and combustivel==True:
    print ("Meu fusquinha está rodando.")
else:
    print("Não sobrou nada pro fusquinha")

# #não precisa do "== e a definição" se ela estiver definida anteriormente 
# if carro and combustivel:
#     print("Meu fusquinha está rodando.")



#IF/ ELIF/ ELSE
    #else sempre o último e acompanhado de ":", nunca escrever nada com ele

semana = int(input("Informe o dia da semana"))

if semana == 1:
    print("Domingo")
elif semana == 2:
    print("Segunda-feira")
elif semana ==3:
    print("Terça-feira")
elif semana ==4:
    print("Quarta-feira")
elif semana==5:
    print("Quinta-feira")
elif semana==6:
    print("Sexta-feira")
elif semana ==7:
    print("Sábado")
else: #SEMPRE VAZIO
    print ("Dia Iválido")


#MATCH CASE (sem tratamento de exceção):
    
mes = int(input("Informe mes"))

match mes:
    case 1:
        print("Janeiro")
    case 2: 
        print("Fevereiro")
    case 3: 
        print ("Março")
    case 4:
        print ("Abril")
    case 5 :
        print ("Maio")
    case 6: 
        print("Junho")
    case 7: 
        print("Julho")
    case 8:
        print ("Agosto")
    case 9:
        print ("Setembro")
    case 10:
        print ("Outubro")
    case 11: 
        print ("Novembro")
    case 12: 
        print ("Dezembro")
    case _: 
        print("Mês inválido")
        
#MATCH CASE (com tratamento de exceção): 
           


try:

    mes = int(input("Informe mês"))
    match mes:
        case 1:
            print("Janeiro")
        case 2: 
            print("Fevereiro")
        case 3: 
            print ("Março")
        case 4:
            print ("Abril")
        case 5 :
            print ("Maio")
        case 6: 
            print("Junho")
        case 7: 
            print("Julho")
        case 8:
            print ("Agosto")
        case 9:
            print ("Setembro")
        case 10:
            print ("Outubro")
        case 11: 
            print ("Novembro")
        case 12: 
            print ("Dezembro")
        case _: 
            print("mês inválido")
except ValueError:
    print ("Entrada inválida. Por favor, digite um número inteiro.")
except:
    print ("Erro desconhecido.")
    