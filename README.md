<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 O/X 퀴즈 & 정보</title>
<style>
body{
  font-family: Arial, sans-serif;
  background:#f4f6f8;
  margin:0;
  padding:20px;
  font-size:18px; /* 전체 기본 글씨 크게 */
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
button:hover{
  background:#1a5fc2;
}
.correct{ color:green; }
.wrong{ color:red; }
h2{ margin-top:0; }
</style>
</head>

<body>

<div id="content"></div>

<div class="card">
  <button onclick="showQuiz()">퀴즈 시작하기</button>
</div>

<!-- 고혈압 정보 영역 -->
<div class="card">
  <h2>고혈압 종합 정보</h2>

  <h3>1. 고혈압이란?</h3>
  <p>
    고혈압은 혈관 안을 흐르는 혈액이 혈관 벽에 가하는 압력이 정상보다
    지속적으로 높은 상태를 말합니다.
    일반적으로 수축기 혈압이 140mmHg 이상이거나,
    이완기 혈압이 90mmHg 이상일 경우 고혈압으로 진단됩니다.
  </p>

  <h3>2. 고혈압의 주요 증상</h3>
  <p>
    고혈압은 초기에는 특별한 증상이 없는 경우가 많아
    ‘침묵의 살인자’라고 불립니다.
    하지만 혈압이 높게 유지되면 다음과 같은 증상이 나타날 수 있습니다.
  </p>
  <ul>
    <li>두통, 어지러움</li>
    <li>가슴 답답함, 심계항진</li>
    <li>피로감, 집중력 저하</li>
    <li>코피, 시야 흐림</li>
  </ul>

  <h3>3. 고혈압이 위험한 이유</h3>
  <p>
    고혈압은 혈관을 지속적으로 손상시키며,
    장기간 방치할 경우 심각한 합병증을 유발할 수 있습니다.
  </p>
  <ul>
    <li>뇌졸중(뇌출혈, 뇌경색)</li>
    <li>심근경색, 심부전</li>
    <li>신장 기능 저하 및 신부전</li>
    <li>망막 손상으로 인한 시력 저하</li>
  </ul>

  <h3>4. 고혈압의 원인</h3>
  <ul>
    <li>과도한 염분 섭취</li>
    <li>비만 및 운동 부족</li>
    <li>스트레스</li>
    <li>흡연과 음주</li>
    <li>유전적 요인</li>
    <li>수면 부족</li>
  </ul>

  <h3>5. 고혈압 예방법</h3>
  <p>
    고혈압은 완치보다는 꾸준한 관리가 핵심입니다.
    생활습관 개선만으로도 혈압을 효과적으로 낮출 수 있습니다.
  </p>
  <ul>
    <li>하루 염분 섭취 5g 이하 유지</li>
    <li>채소·과일 위주의 식단</li>
    <li>주 3~5회, 30분 이상 걷기 운동</li>
    <li>적정 체중 유지</li>
    <li>금연 및 절주</li>
    <li>충분한 수면</li>
  </ul>

  <h3>6. 고혈압 진단 후 해야 할 것</h3>
  <p>
    고혈압으로 진단받았다면
    단순히 약에만 의존하기보다
    생활 전반을 함께 관리해야 합니다.
  </p>
  <ul>
    <li>혈압을 매일 같은 시간에 측정</li>
    <li>의사의 처방에 따른 약물 복용</li>
    <li>증상이 없어도 치료 중단하지 않기</li>
    <li>정기적인 병원 검진</li>
  </ul>

  <h3>7. 고혈압 관리의 핵심</h3>
  <p>
    고혈압은 평생 관리가 필요한 만성질환이지만,
    올바른 생활습관과 꾸준한 관리만 이루어진다면
    건강한 일상생활을 유지할 수 있습니다.
  </p>
</div>

<script>
const QUIZ = [
["혈압이 높아도 증상이 없을 수 있다",true,"초기 고혈압은 무증상인 경우가 많습니다."],
["고혈압은 심장병 위험을 높인다",true,"혈관 손상으로 심장질환 위험이 증가합니다."],
["짠 음식은 혈압을 낮춘다",false,"나트륨은 혈압을 상승시킵니다."],
["칼륨은 나트륨 배출을 돕는다",true,"나트륨 배출을 돕습니다."],
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
["운동 중 혈압이 높아지면 무조건 중단해야 한다",false,"조절된 운동은 필요합니다."],

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
