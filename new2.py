score1 = {'국어': 90, '영어': 78, '수학': 95, '과학': 55}
score2 = {}

for key, value in score1.items():
    if value >= 90:
        score2[key] = 'A'
    elif 90 > value >= 80:
        score2[key] = 'B'
    elif 80 > value >= 70:
        score2[key] = 'C'
    elif 70 > value >= 60:
        score2[key] = 'D'
    else:
        score2[key] = 'F'
print(score2)
    