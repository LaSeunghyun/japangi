drink_list = {"물": 1, "코카콜라": 2, '환타': 0}

def checkDrink():
    for key, value in list(drink_list.items()):
        if value == 0:
            drink_list[key] = '품절'

    return drink_list

def sellDrink(drink):
    print(drink)
    if drink_list[drink] == '품절':
        order = int(input('준비된 음료가 모두 소진되었어요. 비용을 반환할까요?\n 1. 다른 음료 주문, 2. 잔돈 반환\n'))
        if order == 1:
            return 1
        elif order == 2:
            return 2
        else:
            print('다시 입력하세요.')
            return True
    else :
        drink_list[drink] += -1
        print(f'{drink}의 수량이 {drink_list[drink]}개 남았습니다.')
        return 0