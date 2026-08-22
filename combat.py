import random

hp = 10
mana = 6
fuga = False
turnos = 0

monstros = ["orc", "goblin", "ladrão", "lobo", "demonio", "esqueleto", "slime", "espirito", "monstro", "zumbi"]

while True: 
    hp_monstro = random.randint(5, 15)
    monstro = random.choice(monstros)
    print(f"Ah não, um {monstro} apareceu no caminho, o que voce vai fazer?\n")
    while hp_monstro > 0:
        acao = input("1 - Atacar ele\n2 - Se defender\n3 - Correr\n4 - Usar magia\n5 - Rezar\nDiga a opção: ")
        if acao == "1":
            x = random.randint(1,2)
            if x == 1:
                print(f"O {monstro} esquivou e contra atacou.\n")
                turnos += 1
                hp -= 1
                print(f"Seu HP: {hp} // HP do {monstro}: {hp_monstro} // Mana: {mana}")
                print("-"*50,"\n")
            elif x == 2:
                print(f"Voce conseguiu bater no {monstro}, mas ele ainda esta de pé.\n")
                turnos += 1
                y = random.randint(1, 10)
                if y != 10:
                    hp_monstro -= 1
                elif y == 10:
                    print("Parabens, voce deu um dano critico!\n")
                    hp_monstro -= 2
                print(f"Seu HP: {hp} // HP do {monstro}: {hp_monstro} // Mana: {mana}")
                print("-"*50,"\n")

        elif acao == "2":
             x = random.randint(1,2)
             if x == 1:
                  print(f"O {monstro} percebeu e não atacou.\n")
                  turnos += 1
                  print("-"*50,"\n")
             elif x == 2:
                print(f"O {monstro} atacou e voce se defendeu.\n")
                turnos += 1
                print("-"*50,"\n")

        elif acao == "3":
             x = random.randint(1, 3)
             if x == 1:
                  print(f"O {monstro} te alcançou e te deu uma voadora.")
                  turnos += 1
                  hp -= 5
                  print(f"Seu HP: {hp} // HP do {monstro}: {hp_monstro} // Mana: {mana}")
                  print("-"*50,"\n")
             elif x == 2:
                print("Voce conseguiu fugir da briga, sem honra mas com vida.\n")
                turnos += 1
                fuga = True
                break
             elif x == 3:
                print(f"O {monstro} percebeu a sua covardia e te deu um golpe fatal na cabeca.\n")
                turnos += 1
                hp -= 11
                fuga = True
                break
             
        elif acao == "4":
             x = random.randint(1,2)
             if x == 1:
                  print("Voce errou o alvo, e usou mana atoa.\n")
                  mana -= 2
                  turnos += 1
                  print(f"Seu HP: {hp} // HP do {monstro}: {hp_monstro} // Mana: {mana}")
                  print("-"*50,"\n")
             elif x == 2:
                  if mana > 0:
                    print(f"Voce acertou o {monstro}, mas ele ainda esta de pé.\n")
                    turnos += 1
                    mana -= 2
                    hp_monstro -= 2
                    print(f"Seu HP: {hp} // HP do {monstro}: {hp_monstro} // Mana: {mana}")
                    print("-"*50,"\n")
                  elif mana <= 0:
                       print("Voce não tem mana o suficiente.\n")
                       turnos += 1
             
        elif acao == "5":
             if monstro == "demonio" or monstro == "espirito":
                  print(f"A sua reza foi boa e o {monstro} morreu.\n")
                  turnos += 1
                  hp_monstro -= 15
                  break
             elif monstro != "demonio":
                  print("Rezar nao adianta e voce tomou um murro.")
                  turnos += 1
                  hp -= 2
                  print(f"Seu HP: {hp} // HP do {monstro}: {hp_monstro} // Mana: {mana}")
                  print("-"*50,"\n")

        else:
             print("Opcao invalida\n")



    if hp_monstro <= 0:
        print(f"Parabens, voce derrotou o {monstro}!")
        print(f"Voce o derrotou em {turnos} turnos\n")
        break
    elif hp <= 0:
        print("Voce morreu.")
        print(f"Voce durou {turnos} turnos.\n")
        break

    if hp_monstro <= 0:
            break
    
    elif hp <= 0:
             break
    
    elif fuga == True:
        break
