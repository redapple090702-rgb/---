<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>
<style>
body{
  font-family: Arial, sans-serif;
  font-size: 20px;   /* 기본 글씨 크게 */
  background:#f4f6f8;
  padding:20px;
}
h1{text-align:center;}
button{
  font-size:18px;
  padding:10px 16px;
  margin:5px;
  cursor:pointer;
}
input{
  font-size:18px;
  padding:5px;
}
.card{
  background:white;
  padding:20px;
  border-radius:10px;
  margin:15px auto;
  max-width:600px;
  box-shadow:0 2px 8px rgba(0,0,0,0.1);
}
.explain{
  color:#333;
  margin-top:5px;
  font-size:16px;
}
.correct{color:green;}
.wrong{color:red;}
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div id="menu" class="card">
  <button onclick="showBP()">혈압 측정</button>
  <button onclick="showQuiz()">고혈압 퀴즈</button>
</div>

<div id="content"></div>

<script>
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
    <button onclick="calc()">측정</button>
    <div id="result"></div>
  </div>`;
}

function calc(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);
  if(!sp || !dp){
    document.getElementById("result").innerHTML="값을 입력하세요.";
    return;
  }
  const r = classify(sp,dp);
  document.getElementById("result").innerHTML = `
    <p>판정: <b>${r}</b></p>
    ${r!=="정상 혈압"
      ? `<a href="https://www.kdca.go.kr" target="_blank">질병관리청 정보 보기</a>`
      : ""}`;
}

/* 총 30문제 */
const quizPool = [
 ["혈압약은 증상이 없어도 계속 복용해야 한다", true, "고혈압은 무증상이어도 합병증 위험이 큽니다."],
 ["혈압은 하루 중 시간에 따라 변할 수 있다", true, "아침에 가장 높아지는 경향이 있습니다."],
 ["저염식은 혈압 관리에 효과가 있다", true, "나트륨 섭취 감소는 혈압을 낮춥니다."],
 ["고혈압은 심장병과 무관하다", false, "심근경색·심부전 위험을 높입니다."],
 ["운동은 혈압을 일시적으로만 낮춘다", false, "꾸준한 운동은 장기적으로 혈압을 낮춥니다."],
 ["스트레스는 혈압 상승 요인이다", true, "교감신경 활성으로 혈압이 오릅니다."],
 ["흡연은 혈압에 영향을 주지 않는다", false, "혈관 수축을 유발합니다."],
 ["고혈압은 뇌졸중 위험을 높인다", true, "가장 큰 위험 인자 중 하나입니다."],
 ["체중 감소는 혈압을 낮출 수 있다", true, "체중 1kg 감소 시 혈압도 감소합니다."],
 ["혈압은 한쪽 팔만 재면 충분하다", false, "양쪽 팔 측정이 권장됩니다."],

 ["카페인은 혈압을 일시적으로 올릴 수 있다", true, "특히 카페인 민감자에게 영향이 큽니다."],
 ["고혈압 환자는 근력운동을 하면 안 된다", false, "적절한 근력운동은 도움이 됩니다."],
 ["짠 국물 위주 식사는 혈압을 높인다", true, "국·찌개는 나트륨 함량이 높습니다."],
 ["고혈압은 유전과 무관하다", false, "가족력이 중요한 요인입니다."],
 ["수면 부족은 혈압에 영향을 준다", true, "만성 수면 부족은 혈압 상승과 연관됩니다."],
 ["혈압약은 평생 복용해야만 한다", false, "생활습관 개선으로 줄일 수 있는 경우도 있습니다."],
 ["혈압은 앉은 자세에서 재야 정확하다", true, "안정된 자세가 중요합니다."],
 ["고혈압은 신장 기능에 영향을 준다", true, "신장 손상의 주요 원인입니다."],
 ["술은 소량이라도 혈압에 영향이 없다", false, "알코올은 혈압을 상승시킵니다."],
 ["고혈압 전단계도 관리가 필요하다", true, "조기 관리가 중요합니다."],

 ["운동 후 바로 혈압을 재도 된다", false, "안정 후 측정해야 합니다."],
 ["복부 비만은 혈압 상승과 연관된다", true, "내장지방은 고혈압 위험 요인입니다."],
 ["칼륨 섭취는 혈압 조절에 도움된다", true, "나트륨 배출을 돕습니다."],
 ["혈압은 기온 변화와 무관하다", false, "추운 날 혈압이 상승합니다."],
 ["고혈압은 노인에게만 생긴다", false, "청소년·청년도 발생할 수 있습니다."],
 ["심박수와 혈압은 항상 비례한다", false, "항상 일치하지는 않습니다."],
 ["고혈압은 실명 위험을 높일 수 있다", true, "망막 혈관 손상을 유발합니다."],
 ["식이섬유 섭취는 혈압에 도움이 된다", true, "혈관 건강을 개선합니다."],
 ["고혈압은 생활습관병이다", true, "식습관·운동과 밀접합니다."],
 ["혈압 측정 전 5분 휴식이 필요하다", true, "안정 상태가 정확도를 높입니다."]
];

function showQuiz(){
  const picked = quizPool.sort(()=>Math.random()-0.5).slice(0,10);
  let html = `<div class="card"><h2>O / X 퀴즈 (10문제)</h2>`;
  picked.forEach((q,i)=>{
    html += `
    <p><b>${i+1}. ${q[0]}</b></p>
    <button onclick="answer(this,true,${q[1]},'${q[2]}')">O</button>
    <button onclick="answer(this,false,${q[1]},'${q[2]}')">X</button>
    <div class="explain"></div>
    `;
  });
  html += `</div>`;
  document.getElementById("content").innerHTML = html;
}

function answer(btn, user, correct, exp){
  const box = btn.parentElement.querySelector(".explain");
  if(user===correct){
    box.innerHTML = `✔ 정답! ${exp}`;
    box.className="explain correct";
  }else{
    box.innerHTML = `✘ 오답! ${exp}`;
    box.className="explain wrong";
  }
}
</script>

</body>
</html>
