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
/* ================= 혈압 분석 ================= */
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
    수축기 혈압(SP) <input id="sp" type="number"> mmHg<br>
    확장기 혈압(DP) <input id="dp" type="number"> mmHg<br><br>
    <button onclick="calcBP()">분석하기</button>
    <div id="bpResult"></div>
  </div>`;
}

function calcBP(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);

  if(!sp || !dp){
    alert("혈압 값을 모두 입력하세요.");
    return;
  }

  const pp = sp - dp;
  const mapVal = dp + pp / 3;
  const classification = classify(sp, dp);

  document.getElementById("bpResult").innerHTML = `
<pre>
======== 혈압 분석 결과 ========
* 수축기 혈압(SP): ${sp.toFixed(1)} mmHg
* 확장기 혈압(DP): ${dp.toFixed(1)} mmHg
* 맥압(PP): ${pp.toFixed(1)} mmHg
* 평균 동맥압(MAP): ${mapVal.toFixed(1)} mmHg
▶ 혈압 상태 분류: ${classification}
</pre>
${classification !== "정상 혈압"
  ? `<a href="https://www.kdca.go.kr" target="_blank">질병관리청 고혈압 정보 보기</a>`
  : ""}
`;
}

/* ================= 퀴즈 ================= */
const QUIZ = [
["고혈압은 증상이 없어도 위험하다",true,"무증상 상태에서도 장기 손상이 진행됩니다."],
["혈압약은 증상이 없으면 중단해도 된다",false,"의사 지시 없이 중단하면 위험합니다."],
["짠 음식은 혈압을 상승시킨다",true,"나트륨 섭취는 혈압 상승의 주요 원인입니다."],
["운동은 고혈압 관리에 도움이 된다",true,"유산소 운동은 혈압을 낮춥니다."],
["흡연은 혈압과 무관하다",false,"흡연은 혈관을 수축시켜 혈압을 올립니다."],
["스트레스는 혈압에 영향을 준다",true,"스트레스 호르몬은 혈압을 상승시킵니다."],
["고혈압은 뇌졸중 위험을 높인다",true,"혈관 손상으로 뇌졸중 위험이 증가합니다."],
["비만은 고혈압의 위험 요인이다",true,"체중 증가는 혈압을 상승시킵니다."],
["칼륨 섭취는 혈압 조절에 도움 된다",true,"나트륨 배출을 돕습니다."],
["고혈압은 생활습관 관리가 핵심이다",true,"식습관·운동·약물 관리가 중요합니다."],

["고혈압은 노인만 발생한다",false,"젊은 층에서도 증가하고 있습니다."],
["술은 혈압을 낮춘다",false,"알코올은 혈압을 상승시킵니다."],
["수면 부족은 혈압 상승 요인이다",true,"만성 수면 부족은 고혈압 위험을 높입니다."],
["고혈압은 신장 질환을 유발할 수 있다",true,"신장 혈관 손상이 발생합니다."],
["혈압은 한 번만 재도 충분하다",false,"여러 번 측정해야 정확합니다."],

["가공식품은 고혈압에 불리하다",true,"나트륨 함량이 높습니다."],
["체중 감량은 혈압을 낮춘다",true,"체중 감소 효과가 큽니다."],
["커피는 혈압에 영향이 없다",false,"카페인은 일시적으로 혈압을 올릴 수 있습니다."],
["고혈압은 실명 위험도 높인다",true,"망막 혈관 손상이 발생할 수 있습니다."],
["운동 중 혈압이 높아지면 무조건 중단해야 한다",false,"의사 상담 후 조절된 운동은 필요합니다."],

["혈압약은 평생 복용할 수도 있다",true,"상태에 따라 장기 복용이 필요합니다."],
["염분 섭취는 하루 5g 이하가 권장된다",true,"WHO 권고 기준입니다."],
["걷기 운동은 혈압 관리에 효과적이다",true,"가장 안전한 유산소 운동입니다."],
["고혈압은 유전과 무관하다",false,"가족력이 영향을 줍니다."],
["채소 섭취는 혈압 관리에 도움 된다",true,"칼륨과 식이섬유가 풍부합니다."],

["혈압은 기온 변화와 무관하다",false,"추운 날 혈압이 상승합니다."],
["스트레스 관리는 혈압 치료의 일부이다",true,"정신적 요인도 중요합니다."],
["탄산음료는 혈압에 영향 없다",false,"당분과 나트륨이 문제됩니다."],
["고혈압은 완치보다 관리가 중요하다",true,"조절이 핵심입니다."],
["규칙적인 측정은 혈압 관리에 필수이다",true,"변화를 조기에 파악할 수 있습니다."]
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
  let html = `<div class="card"><h2>퀴즈 결과</h2>`;

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
