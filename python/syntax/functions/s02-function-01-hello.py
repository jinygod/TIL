# 함수
# 함수는 호출하기 전에 정의가 되어 있어야 한다.
"""
def 함수명(파라미터):
    명령문
    retun 값
"""


# 함수정의: hello
# 입력값: 없음
# 출력값: 리턴값이 없음
# 처리: "hello" 를 화면에 보여줌
def hello():
    print("hello")

# 함수호출: hello()
# 리턴값이 없다.
# 값이 없다 : None
y = None
x = hello()
print(x)
print(y)