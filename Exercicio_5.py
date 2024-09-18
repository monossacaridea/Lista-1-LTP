# Exercício 5: Escreva um programa que jogue "pedra, papel ou tesoura" contra o usuário. O jogo deve continuar até o usuário escolher parar, e retornar o número de vitórias do usuário, da máquina, e empates.

import random

def escolha_maquina():
    return random.choice(['pedra', 'papel', 'tesoura'])

def determinar_vencedor(escolha_usuario, escolha_maquina):
    if escolha_usuario == escolha_maquina:
        return 'empate'
    elif (escolha_usuario == 'pedra' and escolha_maquina == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_maquina == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_maquina == 'papel'):
        return 'usuario'
    else:
        return 'maquina'

def main():
    vitoria_usuario = 0
    vitoria_maquina = 0
    empates = 0

    while True:
        escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'parar' para encerrar): ").strip().lower()

        if escolha_usuario == 'parar':
            break

        if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida. Tente novamente.")
            continue

        escolha_maq = escolha_maquina() # Changed variable name to avoid conflict with function name
        resultado = determinar_vencedor(escolha_usuario, escolha_maq)

        print(f"Você escolheu: {escolha_usuario}")
        print(f"A máquina escolheu: {escolha_maq}")

        if resultado == 'empate':
            print("Empate!")
            empates += 1
        elif resultado == 'usuario':
            print("Você ganhou!")
            vitoria_usuario += 1
        else:
            print("A máquina ganhou!")
            vitoria_maquina += 1

    print("\nResultados finais:")
    print(f"Vitórias do usuário: {vitoria_usuario}")
    print(f"Vitórias da máquina: {vitoria_maquina}")
    print(f"Empates: {empates}")

if __name__ == "__main__":
    main()
