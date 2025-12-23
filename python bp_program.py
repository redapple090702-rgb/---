import random
import webbrowser
from datetime import datetime

# =========================
# 전역 설정
# =========================

BIG_MODE = False
SAVE_FILE = "blood_pressure_result.txt"

def big_print(text):
    if BIG_MODE:
        print("\n" + "=" * 50)
        print(text.upper())
        print("=" * 50 + "\n")
    else:
        print(text)

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

def save_result(sp, dp, pp, map_val, result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(SAVE_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}]\n")
        f.write(f"수축기: {sp} mmHg\n")
        f.write(f"확장기: {dp} mmHg\n")
        f.write(f"맥압: {pp:.1f}\n")
        f.write(f"평균동맥압: {map_val:.1f}\n")
        f.write(f"판정: {result}\n")
        f.write("-" * 30 + "\n")

def blood_pressure_mode():
    try:
        sp = float(input("수축기 혈압(mmHg): "))
        dp = float(input("확장기 혈압(mmHg): "))
    except ValueError:
        big_print("숫자를 정확히 입력해주세요")
        return

    pp = calculate_pp(sp, dp)
    map_val = calculate_map(sp, dp)
    result = classify_blood_pressure(sp, dp)

    big_print("혈압 분석 결과")
    print(f"수축기: {sp} mmHg")
    print(f"확장기: {dp} mmHg")
    print(f"맥압(PP): {pp:.1f}")
    print(f"평균동맥압(MAP): {map_val:.1f}")
    print(f"▶ 판정: {result}")

    save_result(sp, dp, pp, map_val, result)
    big_print("결과가 저장되었습니다")

    if result in ["1기 고혈압", "2기 고혈압", "고혈압 위기"]:
        big_print("질병관리청 사이트로 이동합니다")
        webbrowser.open("https://www.kdca.go.kr")

# =========================
# 퀴즈
# =========================

QUIZ_QUESTIONS = [
    ("혈압약은 의사 지시 없이 중단하면 안 된다.", True),
    ("고혈압이 있으면 저염식이 필요하다.", True),
    ("혈압은 한 번만 재도 충분하다.", False),
    ("고혈압은 뇌졸중 위험을 높인다.", True),
    ("규칙적인 운동은 혈압 조절에 도움 된다.", True),
    ("고혈압은 나이가 들면 자연스러운 현상이다.", False),
    ("스트레스 관리도 혈압 관리의 일부이다.", True),
    ("고혈압은 심장에 부담을 준다.", True),
    ("고혈압은 증상이 없어도 위험할 수 있다.", True),
    ("흡연은 혈압에 영향을 주지 않는다.", False),
    ("체중 감량은 혈압을 낮출 수 있다.", True),
    ("고혈압 위기는 응급상황이다.", True)
]

def quiz_mode():
    score = 0
    questions = random.sample(QUIZ_QUESTIONS, 10)

    for i, (q, ans) in enumerate(questions, 1):
        big_print(f"문제 {i}")
        print(q)
        user = input("O / X : ").strip().upper()

        if (user == "O" and ans) or (user == "X" and not ans):
            print("정답")
            score += 1
        else:
            print("오답")

    big_print(f"퀴즈 종료 - 점수 {score}/10")

# =========================
# 메인 메뉴
# =========================

def main():
    global BIG_MODE

    while True:
        print("\n===== 고혈압 통합 관리 프로그램 =====")
        print("1. 혈압 측정기")
        print("2. 고혈압 퀴즈")
        print("3. 큰 글씨 모드 ON / OFF")
        print("4. 종료")

        choice = input("선택: ")

        if choice == "1":
            blood_pressure_mode()
        elif choice == "2":
            quiz_mode()
        elif choice == "3":
            BIG_MODE = not BIG_MODE
            state = "켜짐" if BIG_MODE else "꺼짐"
            big_print(f"큰 글씨 모드 {state}")
        elif choice == "4":
            big_print("프로그램을 종료합니다")
            break
        else:
            print("잘못된 선택입니다")

if __name__ == "__main__":
    main()

