<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>

<style>
body{
  background:#020617;
  color:#ffffff;
  font-family:sans-serif;
  padding:20px;
  font-size:18px;
}

h1,h2{text-align:center;}

button{
  padding:12px 18px;
  margin:8px;
  font-size:1em;
  cursor:pointer;
}

input{
  padding:6px;
  font-size:1em;
  margin:6px;
}

.card{
  border:1px solid #475569;
  padding:16px;
  margin-top:16px;
}

.correct{color:#22c55e;}
.wrong{color:#ef4444;}
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div class="card" style="text-align:center">
  <button onclick="showBP()">혈압 측정</button>
  <button onclick="showQuiz()">고혈압 퀴즈</button>
</div>

<div id="content"></div>

<script>
/* ================= 혈압 측정 ================= */
function classify(sp, dp){
  if(sp>=180 || dp>=120) return "고혈압 위기";
  if(sp>=160 || dp>=100) return "2기 고혈압";
  if(sp>=140 || dp>=90)  return "1기 고혈압";
  if(sp>=120 || dp>=80)  return "고혈압 전단계";
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

  const result = classify(sp,dp);

  document.getElementById("bpResult").innerHTML = `
    <p><b>판정:</b> ${result}</p>
    ${result!=="정상 혈압"
      ? `<a href="https://www.kdca.go.kr" target="_blank">질병관리청 의료 정보 보기</a>`
      : ""}
  `;
}

/* ================= 퀴즈 (30문제) ================= */
const QUIZ = [
["고혈압은 증상이 없어도 위험하다",true,"자각 증상이 없어도 장기 손상이 진행됩니다."],
["혈압약은 증상이 없으면 중단해도 된다",false,"의사 지시 없이 중단하면 위험합니다."],
["짠 음식은 혈압을 상승시킨다",true,"나트륨은 혈압 상승의 주요 원인입니다."],
["운동은 고혈압 치료에 도움이 된다",true,"유산소 운동이 혈압을 낮춥니다."],
["흡연은 혈압과 무관하다",false,"흡연은 혈관을 수축시킵니다."],
["스트레스는 혈압에 영향을 준다",true,"스트레스 호르몬이 혈압을 올립니다."],
["혈압은 아침과 저녁에 차이가 없다",false,"시간대에 따라 혈압은 달라집니다."],
["고혈압은 뇌졸중 위험을 높인다",true,"혈관 손상으로 뇌졸중 위험이 증가합니다."],
["비만은 고혈압의 위험 요인이다",true,"체중 증가가 혈압을 올립니다."],
["커피는 혈압에 아무 영향이 없다",false,"카페인은 일시적으로 혈압을 올릴 수 있습니다."],

["고혈압은 심장병 위험을 높인다",true,"심장에 부담을 줍니다."],
["염분 섭취는 하루 10g 이상이 권장된다",false,"WHO 권고는 5g 이하입니다."],
["걷기 운동은 혈압 관리에 도움이 된다",true,"가장 안전한 유산소 운동입니다."],
["고혈압은 노인만 걸린다",false,"젊은 층도 증가하고 있습니다."],
["술은 혈압을 낮춘다",false,"과음은 혈압을 상승시킵니다."],
["고혈압은 신장 질환을 유발할 수 있다",true,"신장 혈관이 손상됩니다."],
["혈압은 한 번만 재도 정확하다",false,"여러 번 측정해야 정확합니다."],
["규칙적인 수면은 혈압에 도움 된다",true,"수면 부족은 혈압 상승 요인입니다."],
["고혈압은 완치가 불가능하다",true,"관리로 조절하는 질환입니다."],
["채소 섭취는 혈압 관리에 도움 된다",true,"칼륨 섭취가 중요합니다."],

["소금 대신 허브 사용은 혈압에 좋다",true,"나트륨 섭취를 줄입니다."],
["고혈압은 유전과 무관하다",false,"가족력이 영향을 줍니다."],
["혈압약은 평생 먹을 수도 있다",true,"상태에 따라 장기 복용이 필요합니다."],
["체중 감량은 혈압을 낮춘다",true,"체중 감소 효과가 큽니다."],
["탄산음료는 혈압에 영향 없다",false,"당분과 나트륨이 문제됩니다."],
["고혈압은 실명 위험도 높인다",true,"망막 혈관 손상이 발생합니다."],
["혈압이 높아도 운동하면 안 된다",false,"의사 상담 후 운동이 권장됩니다."],
["가공식품은 고혈압에 불리하다",true,"나트륨 함량이 높습니다."],
["칼륨은 혈압을 낮추는 역할을 한다",true,"나트륨 배출을 돕습니다."],
["고혈압은 생활습관 개선이 중요하다",true,"약물과 함께 필수입니다."]
];

let currentQuiz = [];

function showQuiz(){
  currentQuiz = QUIZ.sort(()=>Math.random()-0.5).slice(0,10);
  let html = `<div class="card"><h2>고혈압 O / X 퀴즈</h2>`;

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
    const ok = sel && (sel.value==="true")===q[1];
    if(ok) score++;

    html += `
    <p class="${ok?'correct':'wrong'}">
      ${i+1}. ${ok?'정답':'오답'}
      <button onclick="alert('${q[2]}')">해설</button>
    </p>`;
  });

  html += `<h3>점수: ${score}/10</h3></div>`;
  document.getElementById("content").innerHTML = html;
}
</script>

</body>
</html>
