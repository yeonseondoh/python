class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getWidth(self):
        return (x2 - x1)

    def getHeight(self):
        return (y2 - y1)

    def getPerimeter(self):
        return 2 * ((x2 - x1) + (y2 - y1))

    def getArea(self):
        return (x2 - x1) * (y2 - y1)

    def show(self):
        print('좌측 상단 꼭짓점이', (x1, y1),'이고 우측 하단 꼭짓점이', (x2, y2), '인 사각형입니다.' )

# 두 꼭짓점의 좌표 입력받기
x1, y1 = map(int, input("첫 번째 꼭짓점의 좌표를 입력하세요 (x1 y1): ").split())
x2, y2 = map(int, input("두 번째 꼭짓점의 좌표를 입력하세요 (x2 y2): ").split())

# 직사각형 객체 생성
r1 = Rectangle(x1, y1, x2, y2)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"넓이는 {a}, 둘레는 {p}")
