#Iniciamos o restaurante com 10 mesas todas disponíveis (True)
mesas_restaurante = {f"Mesa {i}": True for i in range(1, 10)}

def atualizar_mesa(numero_mesa, status_novo):
    """Atualiza a disponibilidade de uma mesa específica. status_novo: True para 'Disponível', False para 'Ocupada'"""
    identificador = f"Mesa {numero_mesa}"
    
    if identificador in mesas_restaurante:
        mesas_restaurante[identificador] = status_novo
        estado = "LIBERADA" if status_novo else "OCUPADA"
        print(f"Status da {identificador} atualizado para: {estado}.")
    else:
        print("Erro: Mesa não encontrada no sistema.")
        def conferir_disponibilidade():
    """Exibe para o garçom a lista de todas as mesas e seus status."""
print("\n--- MAPA DE RESERVAS ---")
    for mesa, disponivel in mesas_restaurante.items():
        status = "Disponível" if disponivel else "Ocupada"
        print(f"{mesa}: {status}")
    print("------------------------\n")

# --- TESTANDO O SISTEMA ---

# O garçom confere o mapa inicial
conferir_disponibilidade()

# Um cliente chega e ocupa a mesa 3
atualizar_mesa(3, False)

# Um cliente sai e libera a mesa 5 (caso já estivesse ocupada)
atualizar_mesa(5, True)

# Conferindo o status atualizado
conferir_disponibilidade()