<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 관리 프로그램</title>

<style>
/* 🔹 기본 글씨 크기 크게 고정 */
body {
  font-family: "맑은 고딕", sans-serif;
  font-size: 26px;
  margin: 20px;
}

button {
  font-size: 26px;
  padding: 12px 20px;
  margin: 8px 0;
}

input {
  font-size: 26px;
  padding: 8px;
  width: 200px;
}

.hidden {
  display: none;
}
</style>
</head>

<body>

<h1>고혈압 건강 관리 프로그램</h1>

<div id="main">
  <button onclick="show('measure')">혈압 측정기</button><br>
  <button onclick="startQuiz()">고혈압 퀴즈</button>
</div>

<!-- ================= 혈압 측정기 ================= -->
<div id="measure" class="hidden">
  <h2>혈압 측정</h2>

  <p>수축기 혈압 (mmHg)</p>
  <input id="sys" type="number">

  <p>이완기 혈압 (mmHg)</p>
  <input id="dia" type="number">

  <br><br>
  <button onclick="checkBP()">결과 확인</button>

  <p id="bpResult"></p>

  <button onclick="goHospital()">병원 정보 보기</button>
  <br><br>
  <button onclick="back()">뒤로가기</button>
</div>

<!-- ================= 퀴즈 ================= -->
<div id="quiz" class="hidden">
  <h2>O / X 퀴즈</h2>
  <form id="quizForm"></form>

  <button onclick="gradeQuiz()">채점하기</button>
  <p id="quizResult"></p>

  <button onclick="back()">뒤로가기</button>
</div>

<script>
/* 화면 전환 */
function show(id) {
  document.querySelectorAll("div").forEach(d => d.classList.add("hidden"));
  document.getElementById(id).classList.remove("hidden");
}

function back() {
  show("main");
}

/* ================= 혈압 측정 ================= */
function checkBP() {
  const s = Number(document.getElementById("sys").value);
  const d = Number(document.getElementById("dia").value);
  let result = "";

  if (!s || !d) {
    result = "⚠ 숫자를 정확히 입력하세요.";
  } else if (s >= 140 || d >= 90) {
    result = "⚠ 고혈압입니다. 병원 진료를 권장합니다.";
  } else if (s >= 120 || d >= 80) {
    result = "⚠ 고혈압 전단계입니다.";
  } else {
    result = "✅ 정상 혈압입니다.";
  }

  document.getElementById("bpResult").textContent = result;

  /* 결과 저장 */
  localStorage.setItem("bloodPressure",
    `수축기 ${s}, 이완기 ${d} → ${result}`);
}

function goHospital() {
  window.open("https://www.nhis.or.kr", "_blank");
}

/* ================= 퀴즈 ================= */
const QUESTIONS = [
  ["고혈압은 대부분 증상이 없다", true, "침묵의 살인자라고 불립니다."],
  ["짠 음식은 혈압을 낮춘다", false, "나트륨은 혈압을 상승시킵니다."],
  ["운동은 혈압 조절에 도움 된다", true, "유산소 운동이 효과적입니다."],
  ["혈압약은 임의로 중단해도 된다", false, "위험한 행동입니다."],
  ["고혈압은 뇌졸중 위험을 높인다", true, "주요 위험 요인입니다."],
  ["나이가 들수록 고혈압 위험이 증가한다", true, "혈관 탄력이 감소합니다."],
  ["카페인은 혈압과 무관하다", false, "일시적 상승을 유발할 수 있습니다."],
  ["체중 감량은 혈압을 낮출 수 있다", true, "체중 감소는 효과적입니다."]
];

let quizSet = [];

function startQuiz() {
  show("quiz");
  quizForm.innerHTML = "";
  quizResult.textContent = "";

  quizSet = [...QUESTIONS]
    .sort(() => Math.random() - 0.5)
    .slice(0, 6);

  quizSet.forEach((q, i) => {
    quizForm.innerHTML += `
      <p>${i + 1}. ${q[0]}</p>
      <label><input type="radio" name="q${i}" value="true"> O</label>
      <label><input type="radio" name="q${i}" value="false"> X</label>
    `;
  });
}

function gradeQuiz() {
  let score = 0;
  let explanation = "";

  quizSet.forEach((q, i) => {
    const user = document.querySelector(`input[name="q${i}"]:checked`);
    const correct = q[1];

    if (user && user.value === String(correct)) score++;

    explanation += `
${i + 1}. ${q[0]}
정답: ${correct ? "O" : "X"}
설명: ${q[2]}

`;
  });

  quizResult.textContent = `점수: ${score} / ${quizSet.length}`;
  alert(explanation);

  localStorage.setItem("quizScore", score);
}
</script>

</body>
</html>



