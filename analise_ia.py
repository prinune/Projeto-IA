import os
import time

def calcular_risco_ia(salario, score, historico_negativo):
    """
    Simula um modelo de Machine Learning Supervisionado (Regressão Logística Básica).
    O modelo calcula uma probabilidade de risco de 0% a 100%.
    """
    # Pesos fictícios que o 'modelo treinado' usa para analisar as variáveis (features)
    peso_salario = -0.0005  # Quanto maior o salário, menor o risco
    peso_score = -0.008     # Quanto maior o score, menor o risco
    peso_historico = 2.5    # Se tiver histórico negativo, o risco sobe muito
    
    # Linha de base (intercepto do modelo)
    intercepto = 5.0
    
    # Cálculo da pontuação do cliente (Equação linear)
    pontuacao = intercepto + (salario * peso_salario) + (score * peso_score) + (historico_negativo * peso_historico)
    
    # Função de ativação para transformar a pontuação em uma porcentagem de 0 a 100 (Função Sigmoide)
    # Usando aproximação simples para evitar import de bibliotecas matemáticas
    if pontuacao > 4:
        probabilidade = 95.0
    elif pontuacao < -4:
        probabilidade = 5.0
    else:
        probabilidade = round((1 / (1 + (2.718 ** -pontuacao))) * 100, 1)
        
    return probabilidade

def iniciar_sistema():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 75)
    print("   SISTEMA DE INTELIGÊNCIA ARTIFICIAL — ANÁLISE PREDICTIVA DE CRÉDITO")
    print("=" * 75)
    print("[SISTEMA]: Carregando pesos do modelo matemático supervisionado...")
    time.sleep(0.8)
    print("[SISTEMA]: Modelo pronto para análise de score corporativo.")
    print("-" * 75)

    while True:
        print("\n--- INSERIR DADOS DO PROPONENTE ---")
        try:
            salario = float(input("Digite o Salário Mensal (R$): "))
            score = int(input("Digite o Score de Crédito (0 a 1000): "))
            
            historico = input("Possui histórico de restrição? (s/n): ").strip().lower()
            historico_val = 1 if historico == 's' else 0
        except ValueError:
            print("\n[ERRO]: Digite valores numéricos válidos!")
            continue

        print("\n[IA]: Executando inferência e analisando variáveis preditivas...")
        time.sleep(1.5)  # Pausa dramática para o vídeo parecer que está processando

        risco = calcular_risco_ia(salario, score, historico_val)

        print("\n" + "="*45)
        print("          RESULTADO DA ANÁLISE IA          ")
        print("="*45)
        print(f"Probabilidade de Inadimplência: {risco}%")
        
        if risco < 30:
            print("Classificação Final: [PERFIL DE BAIXO RISCO - APROVADO]")
        elif risco < 70:
            print("Classificação Final: [PERFIL DE MÉDIO RISCO - REQUER AVAL] ")
        else:
            print("Classificação Final: [PERFIL DE ALTO RISCO - RECUSADO]")
        print("="*45)

        print("\n" + "-" * 75)
        continuar = input("Deseja analisar outro cliente? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nSistema encerrado. Logs de predição salvos.")
            break

if __name__ == "__main__":
    iniciar_sistema()