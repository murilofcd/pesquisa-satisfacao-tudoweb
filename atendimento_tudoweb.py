# =========================================================
# EMPRESA: TudoWeb
# OBJETIVO: Pesquisa de Satisfação do Cliente
# LINGUAGEM: Python 3
# =========================================================

# Quantidade final de entrevistados conforme o enunciado
TOTAL_ENTREVISTADOS = 50

# Inicialização dos contadores
excelente = 0
bom = 0
ruim = 0

print("=" * 50)
print("      PESQUISA DE SATISFAÇÃO - TUDOWEB      ")
print("=" * 50)
print(f"Total de entrevistas a realizar: {TOTAL_ENTREVISTADOS}\n")

# Estrutura de repetição para coletar os dados dos entrevistados
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    
    # Coleta do nome
    nome = input("Digite o seu nome: ").strip()
    
    # Coleta e validação da idade
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
            if idade > 0:
                break
            else:
                print("Por favor, digite uma idade válida (maior que 0).")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros para a idade.")

    # Apresentação do menu de opções
    print("\nQual a sua opinião sobre o atendimento prestado?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    # Coleta e validação da opção de opinião
    while True:
        try:
            opiniao = int(input("Digite o número correspondente à sua opção (1, 2 ou 3): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Opção inválida! Escolha apenas 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite apenas os números 1, 2 ou 3.")

    # Estrutura de decisão para contabilizar a opinião
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1

    print("-" * 40)

# Exibição do relatório final das respostas
print("\n" + "=" * 50)
print("             RELATÓRIO FINAL DA PESQUISA            ")
print("=" * 50)
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'RUIM'     : {ruim}")
print(f"   Quantidade de respostas 'BOM'      : {bom}")
print("-" * 50)
print(f"Total de pesquisas concluídas: {excelente + bom + ruim}")
print("=" * 50)
