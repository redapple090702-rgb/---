<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리</title>
<style>
body {
  background:#020617;
  color:#fff;
  font-family:sans-serif;
  padding:20px;
}
h1,h2 { text-align:center; }
button {
  padding:14px;
  font-size:18px;
  margin:8px;
  cursor:pointer;
}
.big {
  font-size:26px;
}
.card {
  border:1px solid #475569;
  padding:12px;
  margin:10px 0;
}
</style>
</head>
<body>

<h1>🩺 고혈압 통합 관리 프로그램</h1>

<div id="menu" class="card">
  <button onclick="showBP()">혈압 측정</button>
  <button onclick="showQuiz()">고혈압 퀴즈</button>
  <button onclick="toggleBig()">큰 글씨 모드</button>
</div>

<div id="content"></div>

<script>
let BIG = false;

function toggleBig(){
  BIG = !BIG;
  document.body.className = BIG ? "big" : "";
}

function classify(sp, dp){
  if(sp>=180||dp>=120) return "고혈압 위기";
  if(sp>=160||dp>=100) return "2기 고혈압";
  if(sp>=140||dp>=90) return "1기 고혈압";
  if(sp>=120||dp>=80) return "고혈압 전단계";
  return "정상 혈압";
}

function showBP(){
  document.getElementById("content").innerHTML = `
    <div class="card">
      <h2>혈압 측정</h2>
      수축기 <input id="sp" type="number"><br><br>
      확장기 <input id="dp" type="number"><br><br>
      <button onclick="calc()">측정</button>
      <div id="result"></div>
    </div>`;
}

function calc(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);
  const r = classify(sp,dp);
  document.getElementById("result").innerHTML = `
    <p>판정: <b>${r}</b></p>
    ${r!=="정상 혈압" ? 
      `<a href="https://www.kdca.go.kr" target="_blank">의료 정보 보기</a>` 
      : ""}`;
}

const quiz = [
["혈압약은 임의로 중단하면 안 된다", true],
["혈압은 한 번만 재도 충분하다", false],
["저염식은 혈압 관리에 중요하다", true],
["고혈압은 증상이 없어도 위험하다", true],
["운동은 혈압을 낮출 수 있다", true],
["고혈압은 나이 들면 어쩔 수 없다", false]
];

function showQuiz(){
  let q = quiz.sort(()=>Math.random()-0.5).slice(0,5);
  let html = `<div class="card"><h2>O / X 퀴즈</h2>`;
  q.forEach((e,i)=>{
    html+=`${i+1}. ${e[0]}<br>
    <button onclick="alert(${e[1]})">O</button>
    <button onclick="alert(${!e[1]})">X</button><br><br>`;
  });
  html+="</div>";
  document.getElementById("content").innerHTML = html;
}
</script>

</body>
</html>


