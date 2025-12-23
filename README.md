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
  padding:10px 18px;
  font-size:18px;
  margin:6px;
  cursor:pointer;
}
input{
  font-size:18px;
  padding:6px;
}
.card{
  border:1px solid #475569;
  padding:20px;
  margin:20px auto;
  max-width:700px;
}
.correct{color:#22c55e;}
.wrong{color:#ef4444;}
a{color:#38bdf8;}
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
    수축기 혈압(mmHg) <input id="sp" type="number"><br><br>
    확장기 혈압(mmHg) <input id="dp" type="number"><br><br>
    <button onclick="calcBP()">분석하기</button>
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
  const classification = classify(sp, dp);

  document.getElementById("bpResult").innerHTML = `
  <hr>
  <h3>혈압 분석 결과</h3>
  <p>* 수축기 혈압(SP): ${sp.toFixed(1)} mmHg</p>
  <p>* 확장기 혈압(DP): ${dp.toFixed(1)} mmHg</p>
  <p>* 맥압(PP): ${pp.toFixed(1)} mmHg</p>
  <p>* 평균 동맥압(MAP): ${map_val.toFixed(1)} mmHg</p>
  <p><b>▶ 혈압 상태 분류: ${classification}</b></p>
  <a href="https://www.kdca.go.kr" target="_blank">
    질병관리청 고혈압 정보 바로가기
  </a>`;
}

/* ================= 퀴즈 ================= */
const QUIZ_POOL = [
["고혈압은 증상이 없어도 위험하다",true,"장기 손상이 진행될 수 있습니다."],
["혈압약은 임의로 중단해도 된다",false,"중단 시 합병증 위험이 큽니다."],
["저염식은 혈압을 낮추는 데 도움 된다",true,"나트륨 제한은 기본 관리법입니다."],
["운동은 혈압에 영향을 주지 않는다",false,"규칙적 운동은 혈압을 낮춥니다."],
["고혈압은 뇌졸중 위험을 높인다",true,"주요 위험 인자입니다."],
["흡연은 혈압과 무관하다",false,"혈관 수축을 유발합니다."],
["스트레스는 혈압 상승 요인이다",true,"교감신경을 활성화합니다."],
["혈압은 하루 중 변하지 않는다",false,"아침에 높아집니다."],
["비만은 고혈압 위험을 높인다",true,"체중 감량이 중요합니다."],
["고혈압은 노인에게만 생긴다",false,"청소년도 발생할 수 있습니다."],

["카페인은 혈압을 일시적으로 올릴 수 있다",true,"민감한 사람에게 영향 큼"],
["혈압 측정 전 휴식은 필요 없다",false,"5분 이상 안정 필요"],
["알코올은 혈압을 낮춘다",false,"과음 시 상승"],
["칼륨 섭취는 혈압에 도움된다",true,"나트륨 배출 도움"],
["수면 부족은 혈압에 영향 없다",false,"만성 부족 시 상승"],
["고혈압은 심장병 위험 인자다",true,"심근경색 위험 증가"],
["운동 후 바로 혈압 측정해도 된다",false,"안정 후 측정"],
["고혈압 전단계는 관리 필요 없다",false,"조기 관리 중요"],
["고혈압은 신장 질환과 관련 없다",false,"신장 손상 원인"],
["식이섬유는 혈압과 무관하다",false,"혈관 건강 개선"],

["짠 음식은 혈압을 높인다",true,"나트륨 영향"],
["고혈압은 생활습관병이다",true,"식습관·]()

