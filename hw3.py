def get_fixed_price(disprice, dis):
    price=disprice /((100-dis)/100)
    return price

dis=int(input('할인률은? '))
dispriceA = int(input('A 상품의 할인된 가격은? '))
dispriceB = int(input('B 상품의 할인된 가격은? '))

priceA =get_fixed_price(dispriceA, dis)
priceB =get_fixed_price(dispriceB, dis)


print('A 상품의 정가는', priceA, '원')
print('B 상품의 정가는', priceB, '원')
