def get_integer():
    money = 0
    money = int(input("동전으로 교환하고자 하는 금액은? "))
    return money
    
def exchange():
    money = get_integer()

    c500 = money // 500
    money %= 500

    c100 = money // 100
    money %= 100

    c50 = money // 50
    money %= 50

    c10 = money // 10
    money %= 10

    print('500원 동전의 개수: %d' %c500)
    print('100원 동전의 개수: %d' %c100)
    print('50원 동전의 개수: %d' %c50)
    print('10원 동전의 개수: %d' %c10)

    

exchange()

