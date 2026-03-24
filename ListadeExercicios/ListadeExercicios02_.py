#Exercícios Aula 06

# Criando a lista vazia para armazenar o histórico
resultados = []

for i in range(1, 6):
    print(f"--- Dados do Aluno {i} ---")
    
    # Leitura das notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Cálculo da média
    media = (nota1 + nota2) / 2
    
    # Decisão baseada na média
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    # Criando a string formatada e adicionando à lista
    item = f"Aluno {i} - {situacao} (Média: {media:.1f})"
    resultados.append(item)
    print("Resultado registrado!\n")

# Exibindo o relatório final
print("="*30)
print("RELATÓRIO FINAL")
for res in resultados:
    print(res)


#############################

# Lista para armazenar apenas os candidatos que passarem no filtro
candidatos_validos = []

for i in range(1, 6):
    print(f"--- Cadastro do Candidato {i} ---")
    nome = input("Nome: ")
    email = input("Email: ")
    idade = int(input("Idade: "))
    
    # Verificação de idade
    if idade < 18:
        print(f"Candidato {nome} rejeitado: menor de idade.\n")
    else:
        # Criando o dicionário com os dados do candidato válido
        candidato = {
            'nome': nome,
            'email': email,
            'idade': idade
        }
        
        # Adicionando o dicionário à lista principal
        candidatos_validos.append(candidato)
        print(f"Candidato {nome} cadastrado com sucesso!\n")

# Exibindo os resultados finais
print("="*30)
print(f"Total de candidatos válidos: {len(candidatos_validos)}")
for c in candidatos_validos:
    print(f"Nome: {c['nome']} | Contato: {c['email']}")

#############

#Exercícios Aula 08

def calcular_multa(peso_total):
    """
    Recebe o peso total e retorna o valor da multa.
    Limite: 100kg | Multa: R$ 4,00 por quilo excedente.
    """
    limite = 100
    valor_por_quilo = 4.00
    
    if peso_total > limite:
        excesso = peso_total - limite
        return excesso * valor_por_quilo
    else:
        return 0.0

# --- Programa Principal ---
total_multas_acumulado = 0.0

print("=== Sistema de Controle de Pesca ===")
print("(Digite '0' para encerrar e ver o total acumulado)")

while True:
    peso = float(input("\nInforme o peso da pescaria (em kg): "))
    
    # Condição de parada do loop
    if peso == 0:
        break
    
    # Chamada da função para calcular a multa
    multa_atual = calcular_multa(peso)
    
    if multa_atual > 0:
        print(f"Alerta: Peso excedido! Multa desta pescaria: R$ {multa_atual:.2f}")
        total_multas_acumulado += multa_atual
    else:
        print("✅ Peso dentro do limite. Nenhuma multa a pagar.")

# Exibição do resumo final
print("\n" + "="*40)
print(f"RESUMO DO DIA")
print(f"Total de multas a pagar: R$ {total_multas_acumulado:.2f}")
print("="*40)

################
# Função 1: Apenas calcula o valor numérico do IMC
def calcular_imc(peso, altura):
    return peso / (altura * altura)

# Função 2: Recebe o IMC e retorna a categoria em texto
def obter_classificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# --- Programa Principal ---

# Pergunta ao usuário quantas pessoas serão avaliadas (N)
n = int(input("Quantas pessoas deseja avaliar? "))

for i in range(1, n + 1):
    print(f"\n--- Dados da Pessoa {i} ---")
    
    # Entrada de dados
    p = float(input("Digite o peso (kg): "))
    a = float(input("Digite a altura (ex: 1.75): "))
    
    # Chamada da Função 1
    valor_imc = calcular_imc(p, a)
    
    # Chamada da Função 2 (passando o resultado da Função 1)
    classificacao = obter_classificacao(valor_imc)
    
    # Exibição do resultado formatado
    print(f"Resultado: IMC {valor_imc:.2f} -> {classificacao}")

print("\n--- Processamento finalizado ---")

###############################

Aqui está o programa de conversão de temperaturas estruturado com as duas funções solicitadas e um menu de navegação no programa principal.Para as conversões, utilizamos as seguintes fórmulas matemáticas:$$F = \left(C \cdot \frac{9}{5}\right) + 32$$$$C = (F - 32) \cdot \frac{5}{9}$$Python# Função 1: Converte Celsius para Fahrenheit
def celsius_para_fahrenheit(temp_c):
    return (temp_c * 9/5) + 32

# Função 2: Converte Fahrenheit para Celsius
def fahrenheit_para_celsius(temp_f):
    return (temp_f - 32) * 5/9

# --- Programa Principal ---

print("=== Conversor de Temperaturas ===")
print("Escolha a opção desejada:")
print("1 - Converter Celsius para Fahrenheit (C -> F)")
print("2 - Converter Fahrenheit para Celsius (F -> C)")

opcao = input("\nDigite sua opção (1 ou 2): ")

if opcao == '1':
    c = float(input("Digite a temperatura em Celsius: "))
    resultado_f = celsius_para_fahrenheit(c)
    print(f"Resultado: {c}°C equivale a {resultado_f:.2f}°F")

elif opcao == '2':
    f = float(input("Digite a temperatura em Fahrenheit: "))
    resultado_c = fahrenheit_para_celsius(f)
    print(f"Resultado: {f}°F equivale a {resultado_c:.2f}°C")

else:
    print("Opção inválida! Por favor, reinicie e escolha 1 ou 2.")

print("\n--- Conversão finalizada ---")
