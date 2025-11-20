# 모듈 임포트
import json

# 과목명 리스트
score_names = ["국어", "영어", "수학", "과학"]
# 전체 학생 성적 데이터를 저장할 딕셔너리 (메모리)
scores_data = {}

def write_scores_file():
    """성적 데이터를 JSON 파일에 저장하는 함수"""
    with open("scores.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(scores_data))

def read_scores_file():
    """JSON 파일에서 성적 데이터를 읽어오는 함수"""
    with open("scores.json", "r", encoding="utf-8") as f:
        s1 = f.read()
        # 빈 파일인 경우 빈 딕셔너리 반환
        if s1 == "":
            return {}
        return json.loads(s1)

def input_scores(i, scores={}):
    """
    사용자로부터 각 과목의 점수를 입력받는 재귀 함수
    
    Args:
        i: 현재 입력할 과목의 인덱스
        scores: 입력받은 점수를 저장할 딕셔너리
    
    Returns:
        모든 과목 점수와 평균이 포함된 딕셔너리
    """
    if i < len(score_names):
        # 현재 과목의 점수 입력 요청
        score = input(f"{score_names[i]} 점수를 입력하세요.\n")
        if score.isdigit():
            # 점수가 0~100 범위인지 확인
            if 0 <= int(score) <= 100:
                scores[score_names[i]] = int(score)
                # 다음 과목 입력으로 재귀 호출
                input_scores(i+1, scores)
            else:
                print("0~100 사이의 숫자를 입력하세요.")
                # 같은 과목 다시 입력
                input_scores(i, scores)
        else:
            print("숫자를 입력하세요.")
            # 같은 과목 다시 입력
            input_scores(i, scores)
    else:
        # 모든 과목 입력 완료 시 평균 계산
        scores.update({"평균" : sum(scores.values()) / len(scores.values())})
    return scores

def print_scores():
    """모든 학생의 전체 성적을 표 형식으로 출력하는 함수"""
    print("이름\t국어\t영어\t수학\t과학\t평균")
    for name, scores in scores_data.items():
        print(name, end="\t")
        # 각 과목 점수 출력
        for score_name in score_names:
            print(scores[score_name], end="\t")
        # 평균 점수 출력
        print(scores["평균"])

def print_average_scores():
    """모든 학생의 평균 점수만 출력하는 함수"""
    print("이름\t평균")
    for name, scores in scores_data.items():
        print(name, end="\t")
        print(scores["평균"])

def print_max_min_scores():
    """
    각 과목별 최대 점수와 최소 점수를 출력하는 함수
    리스트 컴프리헨션을 사용하여 각 과목의 점수 리스트를 생성한 후 max/min 함수 적용
    """
    print("과목\t최대\t최소")
    scores = scores_data.values()
    for score_name in score_names:
        print(score_name, end="\t")
        # 리스트 컴프리헨션: 각 학생의 해당 과목 점수를 리스트로 추출
        score_list = [score[score_name] for score in scores]
        # 최대 점수 출력
        print(max(score_list), end="\t")
        # 최소 점수 출력
        print(min(score_list))
        # 람다 함수를 사용한 방법 (주석 처리됨)
        # print(max(scores, key=lambda x: x[score_name])[score_name], end="\t")
        # print(min(scores, key=lambda x: x[score_name])[score_name])

def delete_scores():
    """성적 삭제 함수"""
    name = input("삭제할 이름을 입력하세요.\n")
    if scores_data.get(name):
        del scores_data[name]
        write_scores_file()
        print("성적이 삭제되었습니다.")
    else:
        print("해당 이름의 성적이 없습니다.")

# 프로그램 시작 시 파일에서 성적 데이터 로드
scores_data = read_scores_file()

# 메인 프로그램 루프
while True:
    i1 = input("서비스를 선택하세요. 1. 성적 입력 2. 성적 조회 3. 학생별 평균 4. 과목별 최대/최소 점수 5. 성적 삭제 0. 종료\n")
    if i1 == "1":
        # 성적 입력 기능
        name = input("이름을 입력하세요.\n")
        scores = input_scores(0, {})
        # 학생 이름을 키로 하여 성적 데이터 추가
        scores_data.update({name: scores})
        # 파일에 저장
        write_scores_file()
        print("성적이 입력되었습니다.")
    elif i1 == "2":
        # 전체 성적 조회
        print_scores()
    elif i1 == "3":
        # 학생별 평균 조회
        print_average_scores()
    elif i1 == "4":
        # 과목별 최대/최소 점수 조회
        print_max_min_scores()
    elif i1 == "5":
        # 성적 삭제
        delete_scores()
    elif i1 == "0":
        # 프로그램 종료
        print("종료")
        break
    else:
        # 잘못된 입력 처리
        print("잘못된 입력")
