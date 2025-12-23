<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리</title>

<style>
body {
  background:#020617;
  color:#fff;
  font-family:sans-serif;
  padding:20px;
  font-size:20px;
}
h1,h2 { text-align:center; }

button {
  padding:14px;
  font-size:20px;
  margin:8px;
  cursor:pointer;
}

input {
  font-size:20px;
  padding:6px;
}

.big * {
  font-size:28px !important;
}

.card {
  border:1px solid #475569;
  padding:15px;
  margin:15px 0;
  border-radius:10px;
}
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div id="menu" class="card">
  <button onclick="showBP()">혈압 측정</button>
  <button onclick="showQuiz()">고혈압 퀴즈</button>
  <button onclick="toggleBig()">큰 글씨 모드</button>
</div>

<div id="content"></div>

<script>
let BIG = false;

function toggleBig(){
  BIG = !BIG;
  document.body.className = BIG ? "big" : "";
}

// ================= 혈압 =================
function classify(sp, dp){
  if(sp>=180||dp>=120) return "고혈압 위기";
  if(sp>=160||dp>=100) return "2기 고혈압";
  if(sp>=140||dp>=90) return "1기 고혈압";
  if(sp>=120||dp>=80) return "고혈압 전단계";
  return "정상 혈압";
}

function showBP(){
  document.getElementById("content").innerHTML = `
  <div class="card">
    <h2>혈압 측정</h2>
    수축기(mmHg) <input id="sp" type="number"><br><br>
    확장기(mmHg) <input id="dp" type="number"><br><br>
    <button onclick="calc()">측정</button>
    <div id="result"></div>
  </div>`;
}

function calc(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);

  if(!sp || !dp){
    document.getElementById("result").innerText = "숫자를 정확히 입력하세요.";
    return;
  }

  const r = classify(sp,dp);
  const pp = sp - dp;
  const map = ((2*dp)+sp)/3;

  document.getElementById("result").innerHTML = `
  <p><b>판정:</b> ${r}</p>
  <p>맥압(PP): ${pp.toFixed(1)}</p>
  <p>평균동맥압(MAP): ${map.toFixed(1)}</p>
  ${r!=="정상 혈압" ?
    `<a href="https://www.kdca.go.kr" target="_blank">관련 의료 정보 보기</a>`
    : ""}`;
}

// ================= 퀴즈 =================
const quiz = [
["혈압약은 임의로 중단하면 안 된다", true, "약 중단은 급격한 혈압 상승을 유발합니다."],
["혈압은 한 번만 재도 충분하다", false, "여러 번 재 평균을 봐야 합니다."],
["저염식은 혈압 관리에 중요하다", true, "나트륨 섭취는 혈압 상승 요인입니다."],
["고혈압은 증상이 없어도 위험하다", true, "무증상이라도 장기 손상이 진행됩니다."],
["운동은 혈압을 낮출 수 있다", true, "규칙적 운동은 혈관 탄성을 개선합니다."],
["고혈압은 나이 들면 어쩔 수 없다", false, "생활습관 관리로 충분히 조절 가능합니다."]
];

let quizSet = [];
let answers = [];

function showQuiz(){
  quizSet = quiz.sort(()=>Math.random()-0.5).slice(0,5);
  answers = [];

  let html = `<div class="card"><h2>O / X 퀴즈</h2>`;

  quizSet.forEach((q,i)=>{
    html += `
    <div class="card">
      ${i+1}. ${q[0]}<br><br>
      <button onclick="answers[${i}]=true">O</button>
      <button onclick="answers[${i}]=false">X</button>
    </div>`;
  });

  html += `<button onclick="grade()">채점하기</button></div>`;
  document.getElementById("content").innerHTML = html;
}

function grade(){
  let score = 0;
  let text = "";

  quizSet.forEach((q,i)=>{
    if(answers[i] === q[1]) score++;
    text += `${i+1}. ${q[1]?"O":"X"}\n설명: ${q[2]}\n\n`;
  });

  document.getElementById("content").innerHTML +=
  `<div class="card"><h2>결과</h2>
  점수: ${score} / ${quizSet.length}<br><br>
  <pre>${text}</pre></div>`;
}
</script>

</body>
</html>
