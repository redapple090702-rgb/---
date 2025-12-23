<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>

<style>
body{
  font-family: Arial, sans-serif;
  font-size: 20px;
  background:#f4f6f8;
  padding:20px;
}
h1,h2{text-align:center;}
button{
  font-size:18px;
  padding:10px 16px;
  margin:6px;
  cursor:pointer;
}
input{
  font-size:18px;
  padding:6px;
}
.card{
  background:white;
  padding:20px;
  border-radius:10px;
  margin:20px auto;
  max-width:650px;
  box-shadow:0 2px 8px rgba(0,0,0,0.1);
}
.explain{
  margin-top:6px;
  font-size:16px;
}
.correct{color:green;}
.wrong{color:red;}
.link{
  margin-top:10px;
}
</style>
</head>

<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div class="card" style="text-align:center;">
  <button onclick="showBP()">혈압 측정</button>
  <button onclick="showQuiz()">고혈압 퀴즈</button>
</div>

<div id="content"></div>

<script>
/* =========================
   혈압 판정
========================= */
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
    수축기(mmHg) <input id="sp" type="number"><br><br>
    확장기(mmHg) <input id="dp" type="number"><br><br>
    <button onclick="calc()">측정</button>
    <div id="result"></div>
  </div>`;
}

function calc(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);

  if(isNaN(sp) || isNaN(dp)){
    document.getElementById("result").innerHTML = "값을 정확히 입력하세요.";
    return;
  }

  const r = classify(sp,dp);

  document.getElementById("result").innerHTML = `
    <p>판정 결과: <b>${r}</b></p>
    ${r !== "정상 혈압" ? `
      <div class="link">
        🔗 <a href="https://www.kdca.go.kr" target="_blank">
        질병관리청 고혈압 정보 바로가기
        </a>
      </div>
    ` : ""}
  `;
}

/* =========================
   퀴즈 (30문제 풀 중 10문제 랜덤)
========================= */
const quizPool = [
 ["혈압약은 증상이 없어도 꾸준히 복용해야 한다", true, "고혈압은 무증상이어도 합병증 위험이 큽니다."],
 ["혈압은 하루 중 시간대에 따라 달라질 수 있다", true, "아침에 가장 높은 경우가 많습니다."],
 ["저염식은 혈압 관리에 효과적이다", true, "나트륨 섭취 감소는 혈압을 낮춥니다."],
 ["고혈압은 심장질환과 무관하다", false, "심근경색·심부전 위험을 높입니다."],
 ["규칙적인 운동은 혈압을 낮춘다", true, "유산소 운동이 특히 효과적입니다."],
 ["고혈압은 나이가 들면 자연스러운 현상이다", false, "질병이며 관리 대상입니다."],
 ["흡연은 혈압에 영향을 주지 않는다", false, "혈관 수축을 유발합니다."],
 ["고혈압은 뇌졸중 위험을 높인다", true, "가장 중요한 위험 인자입니다."],
 ["체중]()

