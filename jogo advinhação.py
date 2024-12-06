import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)  # Número aleatório entre 1 e 100
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        diferenca = abs(numero_secreto - palpite)
        
        # Dicas de proximidade
        if diferenca == 0:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
        elif diferenca <= 3:
            print("Quase lá! Você está muito perto!")
        elif diferenca <= 10:
            print("Você está um pouco longe.")
        else:
            print("Você está muito longe.")
        
        # Dicas de direção
        if palpite < numero_secreto:
            print("Dica: O número é maior.")
        elif palpite > numero_secreto:
            print("Dica: O número é menor.")

# Iniciar o jogo
jogo_adivinhacao()
