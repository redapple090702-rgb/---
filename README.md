<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>

<style>
body{
  background:#020617;
  color:#ffffff;
  font-family: Arial, sans-serif;
  padding:20px;
  font-size:22px;
  line-height:1.7;
}
h1,h2,h3{ text-align:center; }
.card{
  border:1px solid #475569;
  border-radius:12px;
  padding:25px;
  margin-bottom:30px;
}
button{
  padding:12px 24px;
  font-size:22px;
  margin:8px 4px;
  cursor:pointer;
}
input{
  font-size:22px;
  padding:6px;
}
a{ color:#38bdf8; }
.correct{ color:#22c55e; }
.wrong{ color:#ef4444; }
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div class="card" style="text-align:center">
  <button onclick="showBP()">혈압 측정기</button>
  <button onclick="showQuiz()">고혈압 퀴즈</button>
  <button onclick="showInfo()">고혈압 정보</button>
</div>

<div id="content"></div>

<script>
/* =======================
   혈압 측정기
======================= */
function showBP(){
document.getElementById("content").innerHTML = `
<div class="card">
<h2>혈압 측정기</h2>

수축기 혈압(mmHg): <input id="sp" type="number"><br><br>
이완기 혈압(mmHg): <input id="dp" type="number"><br><br>

<button onclick="measure()">측정하기</button>
<div id="bpResult"></div>
</div>`;
}

function measure(){
const sp = Number(document.getElementById("sp").value);
const dp = Number(document.getElementById("dp").value);

if(!sp || !dp){
  document.getElementById("bpResult").innerHTML =
  "<p>⚠️ 혈압 값을 정확히 입력하세요.</p>";
  return;
}

const pp = sp - dp;
const map = ((2*dp)+sp)/3;

let stage="", explain="", action="";

if(sp<120 && dp<80){
  stage="정상 혈압";
  explain="혈관과 심장에 무리가 없는 상태입니다.";
  action="현재 생활습관을 유지하며 정기적으로 혈압을 측정하세요.";
}
else if(sp<140 || dp<90){
  stage="고혈압 전단계 / 1기";
  explain="혈압이 서서히 상승하기 시작한 단계입니다.";
  action="염분 섭취 감소, 규칙적 운동을 시작하세요.";
}
else if(sp<160 || dp<100){
  stage="2기 고혈압";
  explain="심장·뇌·신장 합병증 위험이 증가합니다.";
  action="의료진 상담 및 약물 치료를 고려해야 합니다.";
}
else{
  stage="고혈압 위기";
  explain="즉각적인 의학적 처치가 필요한 응급 상태입니다.";
  action="지체하지 말고 병원을 방문하세요.";
}

document.getElementById("bpResult").innerHTML = `
<hr>
<p><b>📊 판정:</b> ${stage}</p>
<p>${explain}</p>

<p><b>❤️ 맥압(PP):</b> ${pp} mmHg<br>
→ 심장이 수축할 때 혈관에 가해지는 압력</p>

<p><b>🫀 평균동맥압(MAP):</b> ${map.toFixed(1)} mmHg<br>
→ 장기로 전달되는 평균 혈류 압력</p>

<p><b>📌 이후 행동:</b><br>${action}</p>

<p>🔗 <a href="https://www.kdca.go.kr" target="_blank">
질병관리청 고혈압 정보 바로가기</a></p>`;
}

/* =======================
   퀴즈
======================= */
const QUIZ = [
["혈압약은 임의로 중단하면 안 된다",true,"중단 시 뇌졸중 위험이 증가합니다."],
["저염식은 혈압 관리의 핵심이다",true,"나트륨 섭취 감소가 중요합니다."],
["혈압은 한 번만 재도 충분하다",false,"여러 번 측정해야 정확합니다."],
["고혈압은 증상이 없어도 위험하다",true,"침묵의 살인자로 불립니다."],
["운동은 혈압을 낮춘다",true,"유산소 운동이 효과적입니다."],
["고혈압은 노인만 생긴다",false,"젊은 층에서도 증가 중입니다."],
["비만은 고혈압 위험 요인이다",true,"체중 감량이 혈압을 낮춥니다."],
["스트레스 관리는 혈압 치료의 일부이다",true,"자율신경계와 관련됩니다."],
["고혈압은 신장 손상을 일으킬 수 있다",true,"만성 신부전 위험이 있습니다."],
["카페인은 혈압에 영향이 없다",false,"일시적 혈압 상승을 유발합니다."],
["걷기 운동은 혈압에 효과적이다",true,"가장 안전한 운동입니다."],
["흡연은 혈압과 무관하다",false,"혈관 수축을 유발합니다."],
["혈압약은 평생 복용할 수 있다",true,"상태에 따라 장기 복용합니다."],
["고혈압은 완치보다 관리가 중요하다",true,"조절이 핵심입니다."],
["염분 섭취 권장량은 하루 5g 이하",true,"WHO 권고 기준입니다."],
["수면 부족은 혈압을 올린다",true,"만성 수면 부족은 위험합니다."],
["술은 혈압을 낮춘다",false,"알코올은 혈압을 올립니다."],
["고혈압은 실명 위험도 높인다",true,"망막 혈관 손상 때문입니다."],
["가공식품은 고혈압에 불리하다",true,"나트륨 함량이 높습니다."],
["규칙적 측정은 필수이다",true,"변화 조기 발견 가능"]
];

let CURRENT = [];

function showQuiz(){
CURRENT = QUIZ.sort(()=>Math.random()-0.5).slice(0,10);
let html = `<div class="card"><h2>고혈압 O / X 퀴즈</h2>`;

CURRENT.forEach((q,i)=>{
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
let score=0;
let html=`<div class="card"><h2>퀴즈 결과</h2>`;

CURRENT.forEach((q,i)=>{
const sel=document.querySelector(\`input[name="q${i}"]:checked\`);
const ok=sel && (sel.value==="true")===q[1];
if(ok) score++;

html+=`
<p class="${ok?'correct':'wrong'}">
${i+1}. ${ok?'정답':'오답'}
<button onclick="alert('${q[2]}')">해설</button>
</p>`;
});

html+=`<h3>점수: ${score}/10</h3></div>`;
document.getElementById("content").innerHTML=html;
}

/* =======================
   정보 페이지
======================= */
function showInfo(){
document.getElementById("content").innerHTML=`
<div class="card">
<h2>고혈압이란?</h2>
<p>고혈압은 혈관 내 압력이 정상 범위를 지속적으로 초과한 상태로,
심장·뇌·신장에 심각한 합병증을 유발할 수 있습니다.</p>

<h3>주요 증상</h3>
<p>대부분 증상이 없으며, 두통·어지럼·시야 흐림이 나타날 수 있습니다.</p>

<h3>원인</h3>
<p>염분 과다 섭취, 비만, 스트레스, 운동 부족, 유전 요인</p>

<h3>예방 방법</h3>
<p>저염식, 규칙적 운동, 금연, 절주, 체중 관리</p>

<h3>진단 이후 해야 할 일</h3>
<p>정기 측정, 약물 복용 준수, 생활습관 개선</p>

<p>🔗 <a href="https://www.kdca.go.kr" target="_blank">
질병관리청 고혈압 정보</a></p>
</div>`;
}
</script>

</body>
</html>
