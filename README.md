import random
import webbrowser

# =========================
# 혈압 계산 & 분류
# =========================

def classify_blood_pressure(sp, dp):
    if sp >= 180 or dp >= 120:
        return "고혈압 위기"
    elif sp >= 160 or dp >= 100:
        return "2기 고혈압"
    elif sp >= 140 or dp >= 90:
        return "1기 고혈압"
    elif 120 <= sp <= 139 or 80 <= dp <= 89:
        return "고혈압 전단계"
    elif sp < 120 and dp < 80:
        return "정상 혈압"
    else:
        return "측정 오류"

def calculate_pp(sp, dp):
    return sp - dp

def calculate_map(sp, dp):
    return ((2 * dp) + sp) / 3

def blood_pressure_mode():
    try:
        sp = float(input("수축기 혈압(mmHg): "))
        dp = float(input("확장기 혈압(mmHg): "))
    except ValueError:
        print("숫자로 입력하세요.")
        return

    pp = calculate_pp(sp, dp)
    map_val = calculate_map(sp, dp)
    result = classify_blood_pressure(sp, dp)

    print("\n===== 혈압 분석 결과 =====")
    print(f"수축기: {sp} mmHg")
    print(f"확장기: {dp} mmHg")
    print(f"맥압(PP): {pp:.1f}")
    print(f"평균동맥압(MAP): {map_val:.1f}")
    print(f"▶ 판정: {result}")

    if result in ["1기 고혈압", "2기 고혈압", "고혈압 위기"]:
        print("\n의료 정보 사이트로 이동합니다...")
        webbrowser.open("https://www.kdca.go.kr") # 질병관리청
    print()

# =========================
# 고혈압 퀴즈
# =========================

QUIZ_QUESTIONS = [
    # 낮은 난이도 (행동 중심)
    ("혈압 측정 후 고혈압이면 바로 병원 상담이 필요하다.", True),
    ("고혈압 환자는 짠 음식을 피하는 것이 좋다.", True),
    ("혈압약은 증상이 없으면 끊어도 된다.", False),
    ("규칙적인 걷기 운동은 혈압 관리에 도움이 된다.", True),
    ("고혈압이 있어도 특별한 관리가 필요 없다.", False),

    # 중간 난이도
    ("수축기 혈압이 140 이상이면 고혈압이다.", True),
    ("스트레스는 혈압 상승과 관련이 있다.", True),
    ("고혈압은 젊은 사람에게는 생기지 않는다.", False),
    ("카페인은 혈압을 일시적으로 올릴 수 있다.", True),
    ("고혈압은 심장병과 무관하다.", False),

    # 약간 깊이 있는 문제
    ("고혈압은 뇌졸중 위험을 증가시킨다.", True),
    ("체중 감량은 혈압을 낮출 수 있다.", True),
    ("고혈압 위기는 응급 상황이다.", True),
    ("혈압은 하루 중 항상 같다.", False),
    ("고혈압은 신장 기능에도 영향을 준다.", True)
]

def quiz_mode():
    score = 0
    questions = random.sample(QUIZ_QUESTIONS, 10)

    for i, (q, ans) in enumerate(questions, 1):
        print(f"\n문제 {i}. {q}")
        user = input("O / X : ").strip().upper()

        if (user == "O" and ans) or (user == "X" and not ans):
            print("정답!")
            score += 1
        else:
            print("오답!")

    print(f"\n퀴즈 종료! 점수: {score}/10\n")

# =========================
# 메인 메뉴
# =========================

def main():
    while True:
        print("===== 고혈압 통합 프로그램 =====")
        print("1. 혈압 측정기")
        print("2. 고혈압 퀴즈")
        print("3. 종료")

        choice = input("선택: ")

        if choice == "1":
            blood_pressure_mode()
        elif choice == "2":
            quiz_mode()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.\n")

main()

