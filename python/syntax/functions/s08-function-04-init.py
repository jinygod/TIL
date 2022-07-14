# 함수
# 매개변수 초깃값(기본값, default value)

# 초깃값으로 파라미터 y, z
# 초깃값은 파라미터의 가장 오른쪽부터 왼쪽으로 연속해 지정을 해야 한다.

# 중간에 초깃값을 지정하지 않고 왼쪽으로 건너 뛸 수 없다.
# def move(x=1, y, z=3):

# 가장 오른쪽에 초깃값을 지정하지 않고 왼쪽에 초깃값을 지정할 수 없다.
# def move(x=1, y=2, z):

def move(x, y=2, z=3):
    print('x축: ', x)
    print('y축: ', y)
    print('z축: ', z)
    
move(10)