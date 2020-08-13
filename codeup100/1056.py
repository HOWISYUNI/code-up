# lambda를 이용해 map()에 사용할 중첩동작 처리하기

# 1. 값을 입력받아서
# 2. int타입으로 바꾸고
# 3. bool타입으로 바꾼다.
a,b = map(lambda x: bool(int(x)),input().split())
print(int(a is not b))