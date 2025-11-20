score_list = [
    {'이름': '홍길동', '국어': 90, '영어': 78, '수학': 95, '과학': 55},
    {'이름': '김철수', '국어': 85, '영어': 88, '수학': 75, '과학': 93},
    {'이름': '이영희', '국어': 72, '영어': 67, '수학': 80, '과학': 74},
    {'이름': '박민수', '국어': 59, '영어': 95, '수학': 65, '과학': 70},
    {'이름': '최수정', '국어': 100, '영어': 45, '수학': 82, '과학': 60},
]

grade_list = []

for score in score_list:
    grade = {'이름': score['이름']}
    for key, value in score.items():
        if key != '이름':
            if value >= 90:
                grade[key] = 'A'
            elif 90 > value >= 80:
                grade[key] = 'B'
            elif 80 > value >= 70:
                grade[key] = 'C'
            elif 70 > value >= 60:
                grade[key] = 'D'
            else:
                grade[key] = 'F'
    grade_list.append(grade)

print(grade_list)
