import copy

a = [1, 2, 3]
b = a
print(id(a), '주소만 복사')
b[0] = 6
print(id(b), b, a) 
# 하지만 바로 b 값을 변경하면 주소가 변경됨
#numpy.copy(b,a) , b.copy(a), b=copy.deepcopy(a) 의 방법이 존재
b = [1, 2]
print(id(b))
#그래서 copy 메소드가 필요
b = copy.deepcopy(a)
print(id(a), '다른 메모리 주소에 데이터를 복사')
b[0] = 7
print(id(b), b, a)
