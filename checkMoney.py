
# 반환금액 6600원: 5000원:1 1000원:1 500원:1 100원 :1
def returnMoney(insertCoin):
    change = insertCoin
    changeCoin = {'오천원' : 0, '천원' : 0, '오백원' : 0, '백원' : 0}

    changeCoin['오천원'] = change // 5000
    changeCoin['천원'] = (change % 5000) // 1000
    changeCoin['오백원'] = (change % 1000) // 500
    changeCoin['백원'] = (change % 500) // 100

    print('잔돈을 반환합니다.')
    for key, value in changeCoin.items():
        print(f'{key} : {value}개', sep=', ', end='\n')

    change = 0

    return change