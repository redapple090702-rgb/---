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
}
body.big {
  font-size:28px;
}
h1,h2 { text-align:center; }
button {
  padding:14px;
  font-size:1em;
  margin:6px;
  cursor:pointer;
}
.card {
  border:1px solid #475569;
  padding:16px;
  margin:12px 0;
}
input {
  font-size:1em;
  padding:6px;
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
let BIG = false;
function toggleBig(){
  BIG = !BIG;
  document.body.classList.toggle("big", BIG);
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
    수축기 <input id="sp" type="number"><br><br>
    확장기 <input id="dp" type="number"><br><br>
    <button onclick="calcBP()">측정</button>
    <div id="bpResult"></div>
  </div>`;
}

function calcBP(){
  const sp = +spInput.value;
  const dp = +dpInput.value;
  const r = classify(sp,dp);
  const record = {date:new Date().toLocaleString(), sp, dp, r};
  const data = JSON.parse(localStorage.getItem("bp")||"[]");
  data.push(record);
  localStorage.setItem("bp", JSON.stringify(data));

  document.getElementById("bpResult").innerHTML = `
    <p><b>판정:</b> ${r}</p>
    ${r!=="정상 혈압"?
      `<a href="https://www.kdca.go.kr" target="_blank">의료 정보 보기</a>`:""}
    <p>기록 저장 완료</p>`;
}

/* ================= 퀴즈 ================= */

const QUIZ = [
["혈압약은 의사 지시 없이 중단하면 안 된다",true,"갑작스러운 중단은 혈압 급상승을 유발할 수 있습니다."],
["고혈압은 증상이 없어도 위험하다",true,"무증상이어도 심장·뇌 손상을 일으킬 수 있습니다."],
["저염식은 혈압 조절에 도움이 된다",true,"나트륨 섭취 감소는 혈압을 낮춥니다."],
["혈압은 한 번만 재면 충분하다",false,"여러 번 측정해 평균을 봐야 정확합니다."],
["규칙적인 유산소 운동은 혈압을 낮춘다",true,"걷기·수영 등은 혈압 조절에 효과적입니다."],
["고혈압은 나이가 들면 당연하다",false,"관리하면 충분히 예방·조절 가능합니다."],
["흡연은 혈압에 영향을 주지 않는다",false,"니코틴은 혈압과 심박수를 증가시킵니다."],
["스트레스 관리도 혈압 관리의 일부다",true,"스트레스는 혈압 상승 요인입니다."],
["체중 감량은 혈압을 낮출 수 있다",true,"비만은 고혈압 위험을 높입니다."],
["고혈압은 심부전 위험을 높인다",true,"심장이 과도한 부담을 받습니다."]
];

let currentQuiz = [];

function showQuiz(){
  currentQuiz = QUIZ.sort(()=>Math.random()-0.5).slice(0,8);
  let html = `<div class="card"><h2>O / X 퀴즈</h2>`;
  currentQuiz.forEach((q,i)=>{
    html += `
    <p>${i+1}. ${q[0]}</p>
    <label><input type="radio" name="q${i}" value="true"> O</label>
    <label><input type="radio" name="q${i}" value="false"> X</label>
    `;
  });
  html += `<br><button onclick="grade()">채점하기</button></div>`;
  document.getElementById("content").innerHTML = html;
}

function grade(){
  let score = 0;
  let html = `<div class="card"><h2>결과</h2>`;
  currentQuiz.forEach((q,i)=>{
    const sel = document.querySelector(`input[name="q${i}"]:checked`);
    const correct = sel && (sel.value==="true")===q[1];
    if(correct) score++;
    html += `
    <p class="${correct?'correct':'wrong'}">
      ${i+1}. ${correct?'정답':'오답'}
      <button onclick="alert('${q[2]}')">설명</button>
    </p>`;
  });
  html += `<h3>점수: ${score} / ${currentQuiz.length}</h3></div>`;
  document.getElementById("content").innerHTML = html;
}
</script>

</body>
</html>
