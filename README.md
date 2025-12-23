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
  font-size:18px;
  transition:0.2s;
}

/* ✅ 큰 글씨 모드 */
body.big {
  font-size:30px;
}

h1,h2 { text-align:center; }

button {
  padding:14px;
  margin:8px;
  font-size:1.2em;
  cursor:pointer;
}

input {
  font-size:1.2em;
  padding:6px;
  margin:6px;
}

.card {
  border:1px solid #475569;
  padding:16px;
  margin-top:16px;
}
.correct { color:#22c55e; }
.wrong { color:#ef4444; }
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div class="card" style="text-align:center">
  <button onclick="showBP()">혈압 측정</button>
  <button onclick="showQuiz()">고혈압 퀴즈</button>
  <button onclick="toggleBig()">큰 글씨 모드</button>
</div>

<div id="content"></div>

<script>
/* ================= 공통 ================= */
function toggleBig(){
  document.body.classList.toggle("big");
}

/* ================= 혈압 ================= */
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
    수축기(mmHg) <input id="sp" type="number"><br>
    확장기(mmHg) <input id="dp" type="number"><br><br>
    <button onclick="calcBP()">측정하기</button>
    <div id="bpResult"></div>
  </div>`;
}

function calcBP(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);

  if(!sp || !dp){
    alert("숫자를 입력하세요");
    return;
  }

  const r = classify(sp,dp);

  /* 결과 저장 */
  const log = JSON.parse(localStorage.getItem("bpLog") || "[]");
  log.push({date:new Date().toLocaleString(), sp, dp, r});
  localStorage.setItem("bpLog", JSON.stringify(log));

  document.getElementById("bpResult").innerHTML = `
    <p><b>판정:</b> ${r}</p>
    <p>결과가 저장되었습니다.</p>
    ${r!=="정상 혈압"
      ? `<a href="https://www.kdca.go.kr" target="_blank">의료 정보 보기</a>`
      : ""}`;
}

/* ================= 퀴즈 ================= */
const QUIZ = [
["혈압약은 의사 지시 없이 중단하면 안 된다",true,"갑작스러운 중단은 위험합니다."],
["고혈압은 증상이 없어도 위험하다",true,"장기 손상이 진행될 수 있습니다."],
["저염식은 혈압 관리에 도움 된다",true,"나트륨 섭취를 줄이세요."],
["혈압은 한 번만 재면 충분하다",false,"여러 번 재야 정확합니다."],
["운동은 혈압을 낮출 수 있다",true,"걷기 같은 유산소 운동이 좋습니다."],
["흡연은 혈압에 영향이 없다",false,"혈관을 수축시킵니다."],
["스트레스 관리도 중요하다",true,"혈압 상승 요인입니다."]
];

let currentQuiz = [];

function showQuiz(){
  currentQuiz = QUIZ.sort(()=>Math.random()-0.5).slice(0,6);
  let html = `<div class="card"><h2>O / X 퀴즈</h2>`;
  currentQuiz.forEach((q,i)=>{
    html += `
    <p>${i+1}. ${q[0]}</p>
    <label><input type="radio" name="q${i}" value="true"> O</label>
    <label><input type="radio" name="q${i}" value="false"> X</label>`;
  });
  html += `<br><br><button onclick="grade()">채점</button></div>`;
  document.getElementById("content").innerHTML = html;
}

function grade(){
  let score = 0;
  let html = `<div class="card"><h2>퀴즈 결과</h2>`;
  currentQuiz.forEach((q,i)=>{
    const sel = document.querySelector(`input[name="q${i}"]:checked`);
    const ok = sel && (sel.value==="true")===q[1];
    if(ok) score++;
    html += `
    <p class="${ok?'correct':'wrong'}">
      ${i+1}. ${ok?'정답':'오답'}
      <button onclick="alert('${q[2]}')">설명</button>
    </p>`;
  });
  html += `<h3>점수: ${score}/${currentQuiz.length}</h3></div>`;
  document.getElementById("content").innerHTML = html;
}
</script>

</body>
</html>

