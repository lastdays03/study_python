score1 = {'국어': 90, '영어': 78, '수학': 95, '과학': 55}
score2 = {}
if score1['국어'] >= 90:
    score2['국어'] = 'A'
elif 90 > score1['국어'] >= 80:
    score2['국어'] = 'B'
elif 80 > score1['국어'] >= 70:
    score2['국어'] = 'C'
elif 70 > score1['국어'] >= 60:
    score2['국어'] = 'D'
elif 60 > score1['국어'] >= 50:
    score2['국어'] = 'F'

if score1['영어'] >= 90:
    score2['영어'] = 'A'
elif 90 > score1['영어'] >= 80:
    score2['영어'] = 'B'
elif 80 > score1['영어'] >= 70:
    score2['영어'] = 'C'
elif 70 > score1['영어'] >= 60:
    score2['영어'] = 'D'
elif 60 > score1['영어'] >= 50:
    score2['영어'] = 'F'

if score1['수학'] >= 90:
    score2['수학'] = 'A'
elif 90 > score1['수학'] >= 80:
    score2['수학'] = 'B'
elif 80 > score1['수학'] >= 70:
    score2['수학'] = 'C'
elif 70 > score1['수학'] >= 60:
    score2['수학'] = 'D'
elif 60 > score1['수학'] >= 50:
    score2['수학'] = 'F'

if score1['과학'] >= 90:
    score2['과학'] = 'A'
elif 90 > score1['과학'] >= 80:
    score2['과학'] = 'B'
elif 80 > score1['과학'] >= 70:
    score2['과학'] = 'C'
elif 70 > score1['과학'] >= 60:
    score2['과학'] = 'D'
elif 60 > score1['과학'] >= 50:
    score2['과학'] = 'F'

print(score2)
