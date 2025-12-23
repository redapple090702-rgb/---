<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 관리 프로그램</title>
<style>
:root {
  --font-size: 18px;
}

body {
  font-family: "맑은 고딕", sans-serif;
  font-size: var(--font-size);
  margin: 20px;
}

button {
  font-size: var(--font-size);
  margin: 5px;
  padding: 10px;
}

input {
  font-size: var(--font-size);
  padding: 5px;
}

.hidden {
  display: none;
}

</style>
</head>
<body>

<h1>고혈압 건강 관리 프로그램</h1>

<div id="main">
  <button onclick="show('measure')">혈압 측정기</button>
  <button onclick="startQuiz()">고혈압 퀴즈</button>
  <button onclick="toggleFont()">큰 글씨 모드</button>
</div>

<!-- 측정기 -->
<div id="measure" class="hidden">
  <h2>혈압 측정</h2>
  <p>수축기(mmHg)</p>
  <input id="sys" type="number">
  <p>이완기(mmHg)</p>
  <input id="dia" type="number">
  <br><br>
  <button onclick="checkBP()">결과 확인</button>
  <p id="bpResult"></p>
  <button onclick="goHospital()">병원 정보 보기</button>
  <br><br>
  <button onclick="back()">뒤로가기</button>
</div>

<!-- 퀴즈 -->
<div id="quiz" class="hidden">
  <h2>O / X 퀴즈</h2>
  <form id="quizForm"></form>
  <button onclick="gradeQuiz()">채점하기</button>
  <p id="quizResult"></p>
  <button onclick="back()">뒤로가기</button>
</div>

<script>
let big = false;

function toggleFont() {
  big = !big;
  document.documentElement.style.setProperty(
    "--font-size", big ? "28px" : "18px"
  );
}

function show(id) {
  document.querySelectorAll("div").forEach(d => d.classList.add("hidden"));
  document.getElementById(id).classList.remove("hidden");
}

function back() {
  show("main");
}

function checkBP() {
  const s = Number(sys.value);
  const d = Number(dia.value);
  let result = "";

  if (!s || !d) {
    result = "숫자를 입력하세요.";
  } else if (s >= 140 || d >= 90) {
    result = "⚠ 고혈압입니다. 병원 진료를 권장합니다.";
  } else if (s >= 120 || d >= 80) {
    result = "⚠ 고혈압 전단계입니다.";
  } else {
    result = "✅ 정상 혈압입니다.";
  }

  bpResult.textContent = result;
  localStorage.setItem("bpResult", `${s}/${d} → ${result}`);
}

function goHospital() {
  window.open("https://www.nhis.or.kr", "_blank");
}

/* ===== 퀴즈 ===== */
const QUESTIONS = [
 ["고혈압은 대부분 증상이 없다", true, "침묵의 살인자라 불립니다."],
 ["짠 음식은 혈압을 낮춘다", false, "나트륨은 혈압을 올립니다."],
 ["운동은 혈압 조절에 도움 된다", true, "유산소 운동이 효과적입니다."],
 ["혈압약은 임의로 중단해도 된다", false, "위험합니다."],
 ["고혈압은 뇌졸중 위험을 높인다", true, "주요 원인입니다."],
 ["나이가 들수록 위험이 증가한다", true, "혈관 탄력 감소 때문입니다."],
 ["카페인은 혈압과 무관하다", false, "일시적 상승 가능"]
];

let quizSet = [];

function startQuiz() {
  show("quiz");
  quizForm.innerHTML = "";
  quizSet = QUESTIONS.sort(() => 0.5 - Math.random()).slice(0, 6);

  quizSet.forEach((q, i) => {
    quizForm.innerHTML += `
      <p>${q[0]}</p>
      <label><input type="radio" name="q${i}" value="true"> O</label>
      <label><input type="radio" name="q${i}" value="false"> X</label>
    `;
  });
}

function gradeQuiz() {
  let score = 0;
  let explain = "";

  quizSet.forEach((q, i) => {
    const user = document.querySelector(`input[name="q${i}"]:checked`);
    if (user && (user.value === String(q[1]))) score++;
    explain += `${q[0]}\n정답: ${q[1] ? "O" : "X"}\n설명: ${q[2]}\n\n`;
  });

  quizResult.textContent = `점수: ${score} / 6`;
  alert(explain);
  localStorage.setItem("quizScore", score);
}
</script>

</body>
</html>


