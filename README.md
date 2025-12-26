<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 종합 페이지</title>
<style>
body{
  font-family: Arial, sans-serif;
  background:#f4f6f8;
  margin:0;
  padding:20px;
  font-size:18px;
}
.card{
  background:white;
  padding:20px;
  border-radius:10px;
  margin-bottom:25px;
  box-shadow:0 2px 8px rgba(0,0,0,0.1);
}
button{
  padding:10px 18px;
  font-size:18px;
  border:none;
  border-radius:6px;
  background:#2c7be5;
  color:white;
  cursor:pointer;
}
button:hover{ background:#1a5fc2; }
input{
  font-size:18px;
  padding:6px;
  width:100px;
}
.correct{ color:green; }
.wrong{ color:red; }
</style>
</head>

<body>

<!-- 혈압 측정기 -->
<div class="card">
  <h2>혈압 측정기</h2>
  <p>수축기 혈압과 이완기 혈압을 입력하세요.</p>

  <p>
    수축기(mmHg):
    <input type="number" id="sys">
  </p>
  <p>
    이완기(mmHg):
    <input type="number" id="dia">
  </p>

  <button onclick="checkBP()">결과 확인</button>

  <h3 id="bpResult"></h3>
</div>

<!-- 퀴즈 영역 -->
<div id="content"></div>

<div class="card">
  <button onclick="showQuiz()">고혈압 O / X 퀴즈 시작</button>
</div>

<!-- 고혈압 정보 -->
<div class="card">
  <h2>고혈압 종합 정보</h2>

  <h3>고혈압이란?</h3>
  <p>
    고혈압은 혈관 속 혈액이 혈관 벽에 가하는 압력이
    정상 범위를 넘어 지속적으로 높은 상태를 말합니다.
    일반적으로 수축기 혈압 140mmHg 이상 또는
    이완기 혈압 90mmHg 이상이면 고혈압으로 분류됩니다.
  </p>

  <h3>주요 증상</h3>
  <ul>
    <li>두통, 어지러움</li>
    <li>가슴 답답함</li>
    <li>피로감, 시야 흐림</li>
    <li>심하면 코피</li>
  </ul>

  <h3>위험성</h3>
  <p>
    고혈압은 증상이 없더라도 혈관을 지속적으로 손상시키며,
    방치 시 뇌졸중, 심근경색, 신장 질환 등
    심각한 합병증으로 이어질 수 있습니다.
  </p>

  <h3>예방 및 관리</h3>
  <ul>
    <li>염분 섭취 줄이기</li>
    <li>규칙적인 걷기 운동</li>
    <li>체중 관리</li>
    <li>금연 및 절주</li>
    <li>스트레스 관리</li>
  </ul>

  <h3>진단 후 해야 할 것</h3>
  <p>
    고혈압은 완치보다는 관리가 중요한 질환입니다.
    의사의 처방에 따라 약을 복용하고,
    정기적으로 혈압을 측정하며
    생활습관 개선을 병행해야 합니다.
  </p>
</div>

<script>
/* 혈압 판정 */
function checkBP(){
  const s = Number(document.getElementById("sys").value);
  const d = Number(document.getElementById("dia").value);
  let result = "";

  if(!s || !d){
    result = "혈압 값을 모두 입력하세요.";
  }else if(s < 120 && d < 80){
    result = "정상 혈압입니다 👍";
  }else if(s < 130 && d < 80){
    result = "주의 혈압(고혈압 전단계)입니다.";
  }else if(s < 140 || d < 90){
    result = "고혈압 1단계입니다.";
  }else{
    result = "고혈압 2단계입니다. 관리가 필요합니다.";
  }

  document.getElementById("bpResult").innerText = result;
}

/* 퀴즈 */
const QUIZ = [
["혈압이 높아도 증상이 없을 수 있다",true,"초기 고혈압은 무증상인 경우가 많습니다."],
["고혈압은 심장병 위험을 높인다",true,"혈관 손상으로 심장질환 위험이 증가합니다."],
["짠 음식은 혈압을 낮춘다",false,"나트륨은 혈압을 상승시킵니다."],
["칼륨은 나트륨 배출을 돕는다",true,"나트륨 배출을 돕습니다."],
["고혈압은 생활습관 관리가 핵심이다",true,"식습관·운동·약물 관리가 중요합니다."],
["고혈압은 노인만 발생한다",false,"젊은 층에서도 증가하고 있습니다."],
["수면 부족은 혈압 상승 요인이다",true,"만성 수면 부족은 위험 요인입니다."],
["혈압은 한 번만 재도 충분하다",false,"여러 번 측정해야 정확합니다."],
["체중 감량은 혈압을 낮춘다",true,"체중 감소 효과가 큽니다."],
["스트레스 관리는 혈압 치료의 일부이다",true,"정신적 요인도 중요합니다."]
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

  html += `<br><br><button onclick="grade()">채점하기</button></div>`;
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
