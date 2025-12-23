<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>

<style>
body {
  background:#020617;
  color:#ffffff;
  font-family: Arial, sans-serif;
  padding:20px;
  font-size:20px; /* 기본 글씨 크게 */
}

h1, h2 {
  text-align:center;
}

.section {
  max-width:700px;
  margin:30px auto;
  border:1px solid #475569;
  padding:20px;
  border-radius:10px;
}

button {
  padding:10px 20px;
  font-size:18px;
  cursor:pointer;
  margin-top:15px;
}

input {
  font-size:18px;
  padding:5px;
  width:120px;
}

.question {
  margin-top:20px;
  padding:15px;
  border:1px solid #475569;
  border-radius:8px;
}

.result {
  margin-top:20px;
  white-space:pre-line;
}
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div class="section">
  <h2>📊 혈압 측정기</h2>
  <p>
    수축기(mmHg):
    <input id="sp" type="number">
  </p>
  <p>
    확장기(mmHg):
    <input id="dp" type="number">
  </p>
  <button onclick="analyzeBP()">분석하기</button>
  <div id="bpResult" class="result"></div>
</div>

<div class="section">
  <h2>🧠 고혈압 퀴즈 (랜덤 10문제)</h2>
  <div id="quiz"></div>
  <button onclick="gradeQuiz()">채점하기</button>
  <div id="quizResult" class="result"></div>
</div>

<script>
// ================= 혈압 측정 =================
function analyzeBP() {
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);

  if (!sp || !dp) {
    document.getElementById("bpResult").innerText = "숫자를 정확히 입력하세요.";
    return;
  }

  let result = "";
  if (sp >= 180 || dp >= 120) result = "고혈압 위기";
  else if (sp >= 160 || dp >= 100) result = "2기 고혈압";
  else if (sp >= 140 || dp >= 90) result = "1기 고혈압";
  else if (sp >= 120 || dp >= 80) result = "고혈압 전단계";
  else result = "정상 혈압";

  const pp = sp - dp;
  const map = ((2 * dp) + sp) / 3;

  document.getElementById("bpResult").innerText =
`수축기: ${sp} mmHg
확장기: ${dp} mmHg
맥압(PP): ${pp.toFixed(1)}
평균동맥압(MAP): ${map.toFixed(1)}
▶ 판정: ${result}`;
}

// ================= 퀴즈 문제 =================
const QUESTIONS = [
  ["고혈압은 대부분 증상이 없다", true, "고혈압은 증상이 없어도 장기 손상을 일으킵니다."],
  ["수축기 혈압은 심장이 이완할 때의 압력이다", false, "수축기 혈압은 심장이 수축할 때입니다."],
  ["이완기 혈압 상승도 위험하다", true, "이완기 혈압도 심혈관 위험을 높입니다."],
  ["나트륨 섭취는 혈압을 낮춘다", false, "나트륨은 혈압을 상승시킵니다."],
  ["고혈압은 뇌졸중 위험을 높인다", true, "혈관 손상으로 뇌졸중 위험이 증가합니다."],
  ["운동은 혈압과 무관하다", false, "규칙적인 운동은 혈압을 낮춥니다."],
  ["혈압은 하루 중 변할 수 있다", true, "활동·스트레스·시간에 따라 변합니다."],
  ["비만은 고혈압 위험 요인이다", true, "체중 증가로 혈관 부담이 커집니다."],
  ["고혈압은 유전과 무관하다", false, "가족력은 중요한 요인입니다."],
  ["혈압약은 임의 중단해도 된다", false, "임의 중단은 위험합니다."],

  ["혈관 탄력 감소는 혈압 상승 원인이다", true, "노화로 혈관이 딱딱해집니다."],
  ["스트레스는 혈압에 영향 없다", false, "스트레스는 교감신경을 자극합니다."],
  ["흡연은 혈압을 올릴 수 있다", true, "니코틴은 혈관을 수축시킵니다."],
  ["고혈압은 심부전 위험을 높인다", true, "심장이 지속적으로 과부하됩니다."],
  ["수면 부족은 혈압과 무관하다", false, "수면 부족은 혈압을 높입니다."],
  ["고혈압 전단계는 관리 필요 없다", false, "이 단계에서 관리가 중요합니다."],
  ["염분 제한은 혈압을 낮춘다", true, "나트륨 감소는 효과적입니다."],
  ["고혈압은 노인만 걸린다", false, "젊은 층도 발생합니다."],
  ["혈압 측정 시 팔은 심장 높이", true, "심장 높이가 가장 정확합니다."],
  ["집에서 잰 혈압도 중요하다", true, "백의 고혈압 구분에 도움 됩니다."],

  ["고혈압은 신장 기능과 관련 있다", true, "신장 혈관 손상이 발생합니다."],
  ["이완기 혈압만 높아도 치료 대상", true, "특히 젊은 층에서 중요합니다."],
  ["술은 혈압을 낮춘다", false, "과음은 혈압을 올립니다."],
  ["고혈압 위기는 응급상황이다", true, "즉시 치료가 필요합니다."],
  ["고혈압은 심근경색 위험 증가", true, "관상동맥 손상 위험이 큽니다."],
  ["혈압은 바로 재야 정확하다", false, "안정 후 측정해야 합니다."],
  ["채소·과일은 혈압에 도움", true, "칼륨 섭취가 도움 됩니다."],
  ["생활습관 개선으로 예방 가능", true, "운동·식습관이 핵심입니다."],
  ["고혈압은 완치 불가능하다", false, "관리로 충분히 조절 가능합니다."],
  ["규칙적 운동은 약만큼 중요하다", true, "비약물 치료의 핵심입니다."]
];

let quizSet = [];
const quizDiv = document.getElementById("quiz");

// 랜덤 10문제 생성
function loadQuiz() {
  quizSet = [...QUESTIONS].sort(() => Math.random() - 0.5).slice(0, 10);
  quizDiv.innerHTML = "";

  quizSet.forEach((q, i) => {
    quizDiv.innerHTML += `
      <div class="question">
        <b>문제 ${i+1}</b><br>${q[0]}<br><br>
        <label><input type="radio" name="q${i}" value="true"> O</label>
        <label><input type="radio" name="q${i}" value="false"> X</label>
      </div>
    `;
  });
}

// 채점
function gradeQuiz() {
  let score = 0;
  let text = "";

  quizSet.forEach((q, i) => {
    const checked = document.querySelector(`input[name="q${i}"]:checked`);
    const correct = q[1];

    if (checked && checked.value === String(correct)) score++;

    text += `문제 ${i+1}: ${correct ? "O" : "X"}\n설명: ${q[2]}\n\n`;
  });

  document.getElementById("quizResult").innerText =
`점수: ${score} / 10\n\n${text}`;
}

loadQuiz();
</script>

</body>
</html>



