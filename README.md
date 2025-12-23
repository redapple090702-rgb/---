<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>

<style>
body{
  background:#020617;
  color:#ffffff;
  font-family:Arial, sans-serif;
  font-size:18px;
  padding:20px;
}
h1,h2{text-align:center;}
button{
  padding:10px 16px;
  margin:6px;
  font-size:18px;
  cursor:pointer;
}
input{
  font-size:18px;
  padding:5px;
}
.card{
  border:1px solid #475569;
  padding:16px;
  margin:16px auto;
  max-width:700px;
}
pre{
  background:#020617;
  color:#ffffff;
  padding:12px;
  border:1px solid #475569;
  white-space:pre-wrap;
}
.correct{color:#22c55e;}
.wrong{color:#ef4444;}
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div class="card" style="text-align:center">
  <button onclick="showBP()">혈압 측정</button>
  <button onclick="showQuiz()">고혈압 O/X 퀴즈</button>
</div>

<div id="content"></div>

<script>
/* ================= 혈압 ================= */
function classify(sp, dp){
  if(sp>=180||dp>=120) return "고혈압 위기";
  if(sp>=160||dp>=100) return "2기 고혈압";
  if(sp>=140||dp>=90)  return "1기 고혈압";
  if(sp>=120||dp>=80)  return "고혈압 전단계";
  return "정상 혈압";
}

function showBP(){
  document.getElementById("content").innerHTML = `
  <div class="card">
    <h2>혈압 측정</h2>
    수축기(mmHg) <input id="sp" type="number"><br><br>
    확장기(mmHg) <input id="dp" type="number"><br><br>
    <button onclick="calcBP()">측정하기</button>
    <div id="bpResult"></div>
  </div>`;
}

function calcBP(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);
  if(!sp || !dp){
    alert("혈압 값을 입력하세요");
    return;
  }

  const pp = sp - dp;
  const map_val = dp + pp/3;
  const classification = classify(sp,dp);

  document.getElementById("bpResult").innerHTML = `
<pre>
======== 혈압 분석 결과 =========
* 수축기 혈압(SP): ${sp.toFixed(1)} mmHg
* 확장기 혈압(DP): ${dp.toFixed(1)} mmHg
* 맥압(PP): ${pp.toFixed(1)} mmHg
* 평균 동맥압(MAP): ${map_val.toFixed(1)} mmHg
▶ 혈압 상태 분류: ${classification}
</pre>
<a href="https://www.kdca.go.kr" target="_blank">
질병관리청 고혈압 정보 바로가기
</a>`;
}

/* ================= 퀴즈 ================= */
const QUIZ_POOL = [
["혈압약은 의사 지시 없이 중단하면 안 된다",true,"갑작스러운 중단은 혈압 급상승 위험이 있습니다."],
["고혈압은 증상이 없어도 위험하다",true,"합병증은 조용히 진행됩니다."],
["저염식은 혈압을 낮춘다",true,"나트륨 섭취 감소가 핵심입니다."],
["혈압은 한 번만 재면 충분하다",false,"여러 번 측정해야 정확합니다."],
["운동은 혈압 관리에 도움이 된다",true,"유산소 운동이 효과적입니다."],
["흡연은 혈압에 영향이 없다",false,"혈관 수축을 유발합니다."],
["스트레스는 혈압을 높인다",true,"교감신경이 활성화됩니다."],
["고혈압은 뇌졸중 위험을 높인다",true,"주요 위험 인자입니다."],
["체중 감소는 혈압을 낮출 수 있다",true,"체중 1kg 감소 효과가 있습니다."],
["고혈압은 노인에게만 생긴다",false,"젊은 층에서도 발생합니다."],

["카페인은 혈압을 올릴 수 있다",true,"일시적 상승을 유발합니다."],
["수면 부족은 혈압과 무관하다",false,"만성 수면 부족은 혈압을 올립니다."],
["고혈압은 신장 기능에 영향을 준다",true,"신장 손상 원인입니다."],
["술은 소량이라도 혈압에 영향이 없다",false,"알코올은 혈압을 올립니다."],
["고혈압 전단계도 관리가 필요하다",true,"조기 관리가 중요합니다."],

["운동 직후 혈압을 재도 정확하다",false,"안정 후 측정해야 합니다."],
["복부 비만은 혈압과 관련 있다",true,"내장지방이 위험합니다."],
["칼륨 섭취는 혈압 조절에 도움 된다",true,"나트륨 배출을 돕습니다."],
["혈압은 기온 변화와 무관하다",false,"추울수록 혈압이 상승합니다."],
["고혈압은 실명 위험을 높일 수 있다",true,"망막 손상이 발생할 수 있습니다."],

["식이섬유는 혈압 관리에 도움 된다",true,"혈관 건강에 좋습니다."],
["심박수와 혈압은 항상 비례한다",false,"항상 일치하지 않습니다."],
["혈압 측정 전 5분 휴식이 필요하다",true,"정확도를 높입니다."],
["고혈압은 생활습관병이다",true,"식습관·운동과 관련됩니다."],
["고혈압은 완치가 불가능하다",false,"관리로 정상 유지 가능합니다."],

["국·찌개 위주 식사는 혈압을 높인다",true,"나트륨 함량이 높습니다."],
["근력운동은 고혈압에 해롭다",false,"적절하면 도움이 됩니다."],
["고혈압은 심장에 부담을 준다",true,"심부전 위험 증가"],
["혈압은 양쪽 팔이 다를 수 있다",true,"초기엔 양쪽 측정이 필요합니다."],
["고혈압 위기는 응급상황이다",true,"즉시 병원 진료가 필요합니다."]
];

let currentQuiz = [];

function showQuiz(){
  currentQuiz = QUIZ_POOL.sort(()=>Math.random()-0.5).slice(0,10);
  let html = `<div class="card"><h2>O / X 퀴즈 (10문제)</h2>`;
  currentQuiz.forEach((q,i)=>{
    html += `
    <p><b>${i+1}. ${q[0]}</b></p>
    <label><input type="radio" name="q${i}" value="true"> O</label>
    <label><input type="radio" name="q${i}" value="false"> X</label>
    `;
  });
  html += `<br><button onclick="grade()">채점</button></div>`;
  document.getElementById("content").innerHTML = html;
}

function grade(){
  let score = 0;
  let html = `<div class="card"><h2>퀴즈 결과</h2>`;
  currentQuiz.forEach((q,i)=>{
    const sel = document.querySelector(\`input[name="q${i}"]:checked\`);
    const ok = sel && (sel.value==="true")===q[1];
    if(ok) score++;
    html += `
    <p class="${ok?'correct':'wrong'}">
      ${i+1}. ${ok?'정답':'오답'} — ${q[2]}
    </p>`;
  });
  html += `<h3>점수: ${score}/10</h3></div>`;
  document.getElementById("content").innerHTML = html;
}
</script>

</body>
</html>
