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

names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]

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
students = [{'name': n, 'score': s} for n, s in zip(names, scores) if s >= 80]

print(students)