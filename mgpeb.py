# ==============================
# MGPEB - Aurora Siger
# Sistema de Gerenciamento de Pouso
# ==============================

# Estruturas de dados
fila_pouso = []   # fila de módulos
pousados = []     # módulos que pousaram
historico = []    # histórico (pilha)

# ==============================
# CADASTRAR MÓDULO
# ==============================
def cadastrar_modulo(nome, prioridade, combustivel):
    modulo = {
        "nome": nome,
        "prioridade": prioridade,
        "combustivel": combustivel
    }
    fila_pouso.append(modulo)


# ==============================
# MOSTRAR FILA
# ==============================
def mostrar_fila():
    print("\n--- FILA DE POUSO ---")
    for m in fila_pouso:
        print(f"{m['nome']} | Prioridade: {m['prioridade']} | Combustível: {m['combustivel']}%")


# ==============================
# ORDENAR POR PRIORIDADE (simples)
# ==============================
def ordenar_por_prioridade():
    for i in range(len(fila_pouso)):
        for j in range(i + 1, len(fila_pouso)):
            if fila_pouso[j]["prioridade"] > fila_pouso[i]["prioridade"]:
                temp = fila_pouso[i]
                fila_pouso[i] = fila_pouso[j]
                fila_pouso[j] = temp


# ==============================
# VERIFICAR SE PODE POUSAR
# ==============================
def pode_pousar(modulo):
    area_livre = True
    clima_ok = True

    if modulo["combustivel"] > 30 and area_livre and clima_ok:
        return True
    else:
        return False


# ==============================
# SIMULAR POUSOS
# ==============================
def simular_pousos():
    ordenar_por_prioridade()

    print("\n--- SIMULAÇÃO ---")

    while len(fila_pouso) > 0:
        modulo = fila_pouso.pop(0)

        if pode_pousar(modulo):
            print(f"✅ Pouso autorizado: {modulo['nome']}")
            pousados.append(modulo)
            historico.append(f"{modulo['nome']} pousou")
        else:
            print(f"❌ Pouso negado: {modulo['nome']}")
            historico.append(f"{modulo['nome']} negado")


# ==============================
# MOSTRAR RESULTADOS
# ==============================
def mostrar_resultados():
    print("\n--- POUSADOS ---")
    for m in pousados:
        print(m["nome"])

    print("\n--- HISTÓRICO ---")
    for h in historico:
        print(h)


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

cadastrar_modulo("Habitação", 5, 50)
cadastrar_modulo("Energia", 4, 20)
cadastrar_modulo("Laboratório", 3, 60)

mostrar_fila()

simular_pousos()

mostrar_resultados()