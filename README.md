<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>

<style>
body{
  font-family: Arial, sans-serif;
  font-size: 26px;   /* 전체 기본 폰트 크게 */
  background:#f4f6f8;
  padding:20px;
}

h1{text-align:center;}

button{
  font-size:24px;
  padding:12px 20px;
  margin:8px;
  cursor:pointer;
}

input{
  font-size:24px;
  padding:8px;
  width:150px;
}

.card{
  background:white;
  padding:25px;
  border-radius:12px;
  margin:20px auto;
  max-width:700px;
  box-shadow:0 2px 8px rgba(0,0,0,0.1);
}

.explain{
  margin-top:8px;
  font-size:22px;
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
    <div id="result" style="margin-top:15px;"></div>
  </div>`;
}

function calc(){
  const spVal = document.getElementById("sp").value;
  const dpVal = document.getElementById("dp").value;

  if(spVal === "" || dpVal === ""){
    document.getElementById("result").innerHTML =
      "<b>⚠ 숫자를 모두 입력하세요.</b>";
    return;
  }

  const sp = Number(spVal);
  const dp = Number(dpVal);
  const r = classify(sp,dp);

  let link = "";
  if(r !== "정상 혈압"){
    link = `
    <p style="margin-top:10px;">
      🔗 <a href="https://www.kdca.go.kr" target="_blank">
      질병관리청 고혈압 정보 보기
      </a>
    </p>`;
  }

  document.getElementById("result").innerHTML = `
    <p>판정 결과: <b>${r}</b></p>
    ${link}
  `;
}

/* 퀴즈 풀은 이전과 동일 */
const quizPool = [
 ["혈압약은 증상이 없어도 계속 복용해야 한다", true, "무증상 고혈압도 합병증 위험이 큽니다."],
 ["고혈압은 뇌졸중 위험을 높인다", true, "가장 큰 위험 요인 중 하나입니다."],
 ["저염식은 혈압 관리에 효과가 있다", true, "나트륨 섭취 감소는 혈압을 낮춥니다."],
 ["운동은 혈압을 일시적으로만 낮춘다", false, "꾸준한 운동은 장기적 효과가 있습니다."],
 ["고혈압은 유전과 무관하다", false, "가족력도 중요한 요인입니다."],
 ["수면 부족은 혈압에 영향을 준다", true, "교감신경 활성과 관련됩니다."],
 ["흡연은 혈압에 영향을 주지 않는다", false, "혈관을 수축시킵니다."],
 ["칼륨 섭취는 혈압 조절에 도움된다", true, "나트륨 배출을 돕습니다."],
 ["고혈압 전단계는 치료가 필요 없다", false, "생활습관 관리가 필요합니다."],
 ["혈압 측정 전 휴식이 필요하다", true, "정확도를 높입니다."]
];

function showQuiz(){
  const picked = quizPool.sort(()=>Math.random()-0.5).slice(0,10);
  let html = `<div class="card"><h2>O / X 퀴즈</h2>`;

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
