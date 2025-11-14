# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [6,7,8,9,10]
# l3 = [11,12,13,14,15]
# d1 = {'a':1, 'b':2, 'c':3,'d':4,'e':5}
# s1 = {1,2,3,4,5}
# print(list(zip(l1, l2, l3)))
# print(list(zip(d1.keys(), d1.values())))
# print(list(d1.items()))
# print(len(d1))
# print(len(s1))

# ll1 = list(zip(l1, l2, l3))
# ll2 = list(zip(l1, l2))
# print(ll1)
# for i, j, k in ll1:
#     print(i, j, k)
# print(dict(zip(l1, l2)))
# print(dict(ll2))

# for i, j in [('a', 1), ('b', 2), ('c', 3)]:
#     print(i, j)

# a, *b, c = d1.items()
# print(a, b, c)

# print(ll1)
# print(list(zip(*ll1)))

# lll1, lll2, lll3 = zip(*ll1)
# print(lll1, lll2, lll3)

# d1 = {'a': 1, 'b': 2, 'c': 3}
# print(list(zip(d1.keys(), d1.values()))) 
# print(list(d1.items()))

# 학생 정보를 리스트로 관리
# names = ['홍길동', '김철수', '이영희']
# scores = [85, 92, 78]

# # 딕셔너리 리스트로 변환
# students = [{'name': n, 'score': s} for n, s in zip(names, scores)]
# print(students)
# # [{'name': '홍길동', 'score': 85}, {'name': '김철수', 'score': 92}, {'name': '이영희', 'score': 78}]

# students2 = dict(zip(names, scores))
# print(students2)
# zipped = zip(names, scores)
# print(list(zipped))
# print(list(zipped))
# zipped_list = list(zip(names, scores))
# print(list(zipped_list))
# print(list(zipped_list))

# 딕셔너리를 함수 인자로 언패킹
# def greet(name, city, age):
#     return f"{name}님은 {age}세, {city}에 거주합니다"

# person = {'name': '홍길동', 'age': 25, 'city': '서울'}
# print(greet(**person))  # 홍길동님은 25세, 서울에 거주합니다

# 여러 연산 조합
# numbers = [1, 2, 3, 4, 5]
# result = [x**2 + 10 for x in numbers]
# print(result)  # [11, 14, 19, 26, 35]

# names = ['홍길동', '김철수', '이영희']
# scores = [85, 92, 78]

# 방법 1: 인덱스 사용
# students = []
# for i in range(len(names)):
#     student = {'name': names[i], 'score': scores[i]}
#     students.append(student)

# 방법 2: enumerate 사용
# students = []
# for i, name in enumerate(names):
#     student = {'name': name, 'score': scores[i]}
#     students.append(student)

# # 방법 3: zip 사용 (가장 깔끔한 전통 방식)
# students = []
# for name, score in zip(names, scores):
#     student = {'name': name, 'score': score}
#     students.append(student)

# # 한 줄로 간결하게 표현
# students = [{'name': n, 'score': s} for n, s in zip(names, scores) if s >= 80]

# print(students)

# print(isinstance(1.5, float))

# print("Welcome to the world of Python", end="\n\n")
# print("Welcome to the world of Python", "abc", "def", sep=", ")
# print("%sABC %s %s" % ("apple", "banana", "cherry"))

# print("%F" % (1.123456789))

# print("aaaa %.8f" % 1.123456789)

# a1 = "cat"
# a2 = "dog"
# a3 = "bird"
# print(f"Animal: {a1}, {a2}, {a3}")
# print("Animal: {1}, {1}, {2}".format(a1, a2, a3))

# i1 = 1
# i2 = 10000000.123456789
# print("{}".format(i1))
# print("{0:10d}".format(i1))
# print(f"{i1:2<10d}")
# print(f"{i2:,.3f}")
# i3 = 0.334
# print(f"{i3:.0%}")
# i4 = 66990000
# print(f"{i4:#x}")
# i5 = f"{i1} + {i2} = {i1 + i2}"
# print(i5)

# a1 = input("Press Enter to continue...\n")
# a2 = input("Press Enter to continue...\n")
# print(a1)
# print(a2)

import json
# f1 = open("./json/test.json", "w")
# d1 = {"name": "John", "age": 30}
# f1.write(json.dumps(d1))
# f1.close()

f1 = open("test.json", "r")
s1 = f1.read()
d1 = json.loads(s1)
print(type(s1))
print(type(d1["name"]))
print(d1["name"])
f1.close()
