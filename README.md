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
  font-size:20px;
  line-height:1.7;
}
h1,h2{
  text-align:center;
}
.card{
  border:1px solid #475569;
  border-radius:10px;
  padding:20px;
  margin-bottom:30px;
  background:#020617;
}
button{
  padding:12px 20px;
  font-size:20px;
  margin-top:10px;
  cursor:pointer;
}
input{
  font-size:20px;
  padding:6px;
}
.correct{ color:#22c55e; }
.wrong{ color:#ef4444; }
a{ color:#38bdf8; }
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<!-- ================= 혈압 측정기 ================= -->
<div class="card">
<h2>혈압 측정기</h2>

수축기 혈압(mmHg): <input type="number" id="sp"><br><br>
이완기 혈압(mmHg): <input type="number" id="dp"><br><br>

<button onclick="measureBP()">측정하기</button>

<div id="bpResult"></div>
</div>

<!-- ================= 고혈압 퀴즈 ================= -->
<div class="card">
<h2>고혈압 O / X 퀴즈</h2>
<button onclick="showQuiz()">퀴즈 시작</button>
<div id="quizArea"></div>
</div>

<!-- ================= 고혈압 정보 ================= -->
<div class="card">
<h2>고혈압 정보</h2>
<p>
고혈압은 혈관 내 압력이 정상 범위를 초과하여 지속적으로 유지되는 상태를 의미한다.
대표적으로 수축기 혈압 140mmHg 이상 또는 이완기 혈압 90mmHg 이상일 경우 고혈압으로 분류된다.
고혈압은 특별한 증상이 없는 경우가 많아 ‘침묵의 살인자’라고도 불린다.
</p>

<p>
주요 증상으로는 두통, 어지럼증, 가슴 답답함, 심한 피로감 등이 나타날 수 있으며,
장기간 방치할 경우 뇌졸중, 심근경색, 신장 질환, 시력 손상 등의 심각한 합병증으로 이어질 수 있다.
</p>

<p>
고혈압의 원인에는 과도한 염분 섭취, 비만, 운동 부족, 스트레스, 흡연, 음주, 유전적 요인이 포함된다.
특히 가공식품과 외식 위주의 식습관은 고혈압 위험을 크게 증가시킨다.
</p>

<p>
예방을 위해서는 저염식 식단 유지, 규칙적인 유산소 운동, 체중 관리,
충분한 수면과 스트레스 조절이 중요하다.
혈압약은 반드시 의사의 처방에 따라 복용해야 하며 임의로 중단해서는 안 된다.
</p>

<p>
고혈압 진단을 받은 이후에는 정기적인 혈압 측정과 함께
생활습관 개선과 약물 치료를 병행해야 한다.
필요 시 의료진과 상담하여 개인에게 맞는 관리 계획을 세우는 것이 중요하다.
</p>
</div>

<script>
/* ===== 혈압 측정 ===== */
function measureBP(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);
  let result = "";

  if(!sp || !dp){
    result = "혈압 값을 정확히 입력하세요.";
  }else if(sp < 120 && dp < 80){
    result = "정상 혈압입니다 👍";
  }else if(sp < 140 || dp < 90){
    result = "고혈압 전단계 또는 1기 고혈압입니다.<br>" + kdca();
  }else{
    result = "고혈압 2기입니다. 적극적인 관리가 필요합니다.<br>" + kdca();
  }

  document.getElementById("bpResult").innerHTML = `<p>${result}</p>`;
}

function kdca(){
  return `<a href="https://www.kdca.go.kr" target="_blank">
  질병관리청 고혈압 정보 바로가기
  </a>`;
}

/* ===== 퀴즈 ===== */
const QUIZ = [
["고혈압은 증상이 없어도 위험하다",true,"증상이 없어도 합병증 위험이 큽니다."],
["염분 섭취는 혈압 상승 원인이다",true,"나트륨은 혈압을 올립니다."],
["고혈압은 노인만 발생한다",false,"젊은 층에서도 증가하고 있습니다."],
["체중 감량은 혈압을 낮춘다",true,"비만은 주요 위험 요인입니다."],
["혈압은 한 번만 재도 충분하다",false,"여러 번 측정해야 정확합니다."],
["운동은 혈압 관리에 효과적이다",true,"유산소 운동이 특히 중요합니다."],
["스트레스는 혈압과 무관하다",false,"스트레스는 혈압 상승 요인입니다."],
["고혈압은 신장 질환을 유발할 수 있다",true,"신장 혈관 손상이 발생합니다."],
["술은 혈압을 낮춘다",false,"알코올은 혈압을 상승시킵니다."],
["걷기 운동은 혈압 관리에 도움 된다",true,"가장 안전한 운동입니다."],

["혈압약은 임의로 중단해도 된다",false,"의사 지시 없이 중단하면 위험합니다."],
["고혈압은 실명 위험을 높인다",true,"망막 손상이 발생할 수 있습니다."],
["커피는 혈압에 영향이 없다",false,"카페인은 일시적 상승을 유발합니다."],
["규칙적인 측정은 혈압 관리에 필수이다",true,"조기 이상 발견이 가능합니다."],
["고혈압은 관리가 핵심이다",true,"완치보다 조절이 중요합니다."]
];

let currentQuiz = [];

function showQuiz(){
  currentQuiz = QUIZ.sort(()=>Math.random()-0.5).slice(0,10);
  let html = "";

  currentQuiz.forEach((q,i)=>{
    html += `
    <p>${i+1}. ${q[0]}</p>
    <label><input type="radio" name="q${i}" value="true"> O</label>
    <label><input type="radio" name="q${i}" value="false"> X</label>
    `;
  });

  html += `<br><button onclick="grade()">채점하기</button>`;
  document.getElementById("quizArea").innerHTML = html;
}

function grade(){
  let score = 0;
  let html = "";

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

  html += `<h3>점수: ${score} / 10</h3>`;
  document.getElementById("quizArea").innerHTML = html;
}
</script>

</body>
</html>
