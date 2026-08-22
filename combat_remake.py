#assets

import random

hp = 10
mana = 10
turno = 0
focus_uses = 0
heal_uses = 0
fuga = False

enemyies = ["ladrao", "goblin", "demonio", "lobo", "zumbi", "monstro"]
enemy = random.choice(enemyies)
hp_enemy = random.randint(15, 20)
print("\033[H\033[J", end="")
print(f"\nHá um {enemy} na sua frente, o que voce irá fazer?\n")

#--------------------------------------------------------------------------#

while True:


    print(f"Seu HP: {hp} | Sua mana: {mana} | HP do {enemy}: {hp_enemy}\n\n")

    act = input("1 - Atacar\n2 - Ataque mágico\n3 - Curar\n4 - Usar 'Focus'\n5 - Fugir\n\nO que vai fazer? ")



#Ataque Padrao

    if act == "1":
        x = random.randint(1, 3)
        if x == 1:
            print("\033[H\033[J", end="")
            print("\nVoce conseguiu atingir o monstro!\n")
            hp_enemy -= 2
            turno += 1

        elif x == 2:
            print("\033[H\033[J", end="")
            print("\nVoce conseguiu um acerto critico!\n")
            hp_enemy -= 3
            turno += 1

        elif x == 3:
            print("\033[H\033[J", end="")
            x = random.randint(1, 2)
            if hp_enemy >= 7:
               if x == 1:
                    print("\nVoce recebeu um contra-ataque...\n")
                    hp -= 2
                    turno += 1
               elif x == 2:
                    print("\nVoce recebeu um contra-ataque critico...\n")
                    hp -= 3
                    turno += 1

            elif hp_enemy <= 6:
                print("\nVoce recebeu um contra-ataque critico...\n")
                hp -= 3
                turno += 1
                

                
#Ataque Magico

    elif act == "2":
        x = random.randint(1, 2)
        if mana >= 2:
          if x == 1:
               print("\033[H\033[J", end="")
               print("\nVoce acertou o ataque mágico!\n")
               hp_enemy -= 3
               mana -= 2
               turno += 1

          elif x == 2:
               print("\033[H\033[J", end="")
               print("\nVoce errou o ataque...\n")
               mana -= 2
               turno += 1

        elif mana <= 1:
            print("\033[H\033[J", end="")
            print("\nVoce não tem mana o suficiente...\n")



#Cura

    elif act == "3":

        if heal_uses > 2:
             print("\033[H\033[J", end="")
             print(f"\nO {enemy} percebeu sua tatica e revidou. Melhor não tentar de novo...\n")
             turno += 1
             hp -= 2

        else:
            if mana >= 3:
                print("\033[H\033[J", end="")
                print("\nVoce usou mana para se curar!\n")
                hp += 2
                mana -= 3
                turno += 1
                heal_uses += 1
            
            elif mana <= 2:
                print("\033[H\033[J", end="")
                print("\nVoce não tem mana o suficiente...\n")
                turno += 1
            


#Focus

    elif act == "4":

        if focus_uses > 2:
            print("\033[H\033[J", end="")
            print(f"\nO {enemy} percebeu sua tatica e revidou. Melhor não tentar de novo...\n")
            turno += 1
            hp -= 2

        else:
            x = random.randint(1, 3)
            
            if x == 1:
                print("\033[H\033[J", end="")
                print("\nVoce usou o 'Focus' e recuperou um pouco de mana!\n")
                mana += 2
                turno += 1
                focus_uses += 1
            
            elif x == 2:
                print("\033[H\033[J", end="")
                print("\nVoce usou o 'Focus' e conseguiu curar mana e hp!!\n")
                mana += 2
                hp += 1
                turno += 1
                focus_uses += 1
            
            elif x == 3:
                print("\033[H\033[J", end="")
                print("\nVoce não conseguiu executar o 'Focus' corretamente...\n")
                turno += 1
                focus_uses += 1



#Fuga

    elif act == "5":
        x = random.randint(1, 2)

        if x == 1:
            print("\033[H\033[J", end="")
            print(f"\nSem honra e sem coragem, voce foge com o rabo entre as pernas, lembrando pelo resto de sua vida do quao covarde voce é...\n")
            turno += 1
            fuga = True

        elif x == 2:
            print("\033[H\033[J", end="")
            print(f"\nEm uma tentativa desesperada de fugir, voce é apunhalado pelas costas em um golpe fatal.\nVoce morre de uma forma tao estupida quanto a sua coragem, por alguem tao fraco como a sua honra.\n")
            turno += 1
            fuga = True



#Quit Game

    elif act == "6":
        print("\033[H\033[J", end="")
        print("\nJogo encerrado...\n\n")
        break



#Input Vazio

    elif act == "":
        print("\033[H\033[J", end="")
        print("\n")
        pass



#Input Maior que 1

    elif len(act) > 1:
        print("\033[H\033[J", end="")
        print("\n")
        pass


    if hp_enemy <= 0:
        print(f"\nFim de jogo! Voce ganhou em {turno} turnos.\n")
        break

    if hp <= 0:
        print(f"\nFim de jogo. Voce durou {turno} turnos...\n")
        break

    if fuga == True:
        print(f"\nFim de jogo. Sua covardia durou até o turno {turno}.\n")
        break



#Versão 2.0 do codigo de combate feito por mim antes
#Feito por Vittz._

