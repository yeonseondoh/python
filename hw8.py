shopping_bag = {}

print('[구입]')

def buy(shopping_bag):
    while True:
    
        item = input('상품명? ')

        if item == '':
            break
        num = int(input('수량은? '))
        print("장바구니에", item, num, "개가 담겼습니다.")
        shopping_bag[item] = num

def show(shopping_bag):
        print('장바구니 보기:', shopping_bag)
    
def find(shopping_bag):
    print('[검색]')
    search = input('장바구니에서 확인하고자 하는 상품은? ')
    
    if search in shopping_bag:
        print(search,'은(는)', shopping_bag[search],'개 담겨 있습니다.')
        print('[검색]')
    
    else:
        print("장바구니에", search, '은(는) 없습니다.')
    

buy(shopping_bag)
show(shopping_bag) 
find(shopping_bag)
    
