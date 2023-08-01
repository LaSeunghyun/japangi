from checkDrink import *
from checkMoney import *

def drinkMachine():
    insertCoin = 0
    drink_price = {"물" : 600, "코카콜라" : 1200, '환타' : 1000}

    while True:
        print(f'현재 투입금액 {insertCoin}원')
        insertCoin += int(input('투입하실 금액을 입력하세요\n'))
        print('구매를 원하시는 음료의 번호를 입력하세요')
        # enumerate는 for문에서 index, element 쌍으로 순회할때 사용하는 함수
        for i, (key, value) in enumerate(checkDrink().items()):
            if value == '품절':
                print(f'{i+1} : {key}({value})')
                continue
            print(f'{i+1} : {key}')
        drink_num = int(input())
        if drink_num <= len(drink_price) and drink_num > 0:
            # checkDrink의 값을 확인한다
            sell_drink = list(checkDrink().items())
            # 비용이 모자랄 경우 금액을 더 넣을 것인지 확인한다.
            if insertCoin < drink_price[sell_drink[drink_num-1][0]]:
                result = int(input('비용이 모자랍니다\n 추가 비용을 투입하시겠어요?\n 1. 추가비용 투입, 2. 잔돈 반환\n'))
                if result == 1:
                    continue
                elif result == 2:
                    insertCoin = returnMoney(insertCoin)
                    continue
                else:
                    print('다시 입력하세요.')
                    continue
            # 비용이 같거나 넘을 경우 구매 여부를 확인한 후 금액, 재고를 차감, 음료를 제공하고 추가 구매여부를 물어본다.
            else:
                result = sellDrink(sell_drink[drink_num-1][0])
                if result == 0:
                    insertCoin -= drink_price[sell_drink[drink_num-1][0]]
                    print(f'{insertCoin}원이 남았습니다.')
                    order = int(input('추가 주문 하시겠어요?\n 1. 추가주문 진행, 2. 잔돈 반환\n'))
                    if order == 1:
                        continue
                    elif order == 2:
                        insertCoin = returnMoney(insertCoin)
                        continue
                    else:
                        print('다시 입력하세요.')
                        continue
                elif result == 1:
                    continue
                elif result == 2:
                    insertCoin = returnMoney(insertCoin)
                    continue
                else:
                    continue
        else:
            print('다시 입력하세요.')
            continue

drinkMachine()