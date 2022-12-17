import random
count = 0
for player in range(10):
    if count == 3:
       print("Победа!") 
       break
    player = int(input("Сделайте ход: 1 Камень, 2 ножницы, 3 бумага: "))		
    if player == 1:
        print("Вы выбрали камень")
    if player == 2:
        print("Вы выбрали ножницы")
    if player == 3:
        print("Вы выбрали бумагу")
    comp = random.randint(1,3)

    if comp == 1:
        print("Ход оппонента - камень")
    if comp == 2:
        print("Ход оппонента - ножницы")
    if comp == 3:
        print("Ход оппонента - бумага")

    if comp == 1 and player == 1 or comp == 2 and player == 2 or comp == 3 and player == 3:
        print("Ничья!")
        print("Твой счет: " + str(count))
    if comp == 1 and player == 2 or comp == 1 and player == 3 or comp == 2 and player == 3:
        print("Вы проиграли!")
        print("Твой счет: " + str(count))
    if comp == 2 and player == 1 or comp == 3 and player == 1 or comp == 3 and player == 2:
        print("Вы выйграли!")
        count += 1
        print("Твой счет: " + str(count))