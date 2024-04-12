def read_single_digit(user):
  if user == 1:
    return '일'
  if user == 2:
    return '이'
  if user == 3:
    return '삼'
  if user == 4:
    return '사'
  if user == 5:
    return '오'
  if user == 6:
    return '육'
  if user == 7:
    return '칠'
  if user == 8:
    return '팔'
  if user == 9:
    return '구'
  if user == 0:
    return '영'

    

def read_number(user):
    if user >= 100 and user < 1000:
        print(read_single_digit(user // 100), read_single_digit((user % 100) // 10), read_single_digit(user % 10))
        
    elif user >= 10 and user < 100:
        print(read_single_digit(user // 10), read_single_digit(user % 10))
        
    elif user >= 0 and user < 10:
        print(read_single_digit(user))


user = int(input("세 자리 정수 입력:"))
read_number(user)
