<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>고혈압 통합 관리 프로그램</title>

<style>
body{
  font-family: Arial, sans-serif;
  background:#f4f6f8;
  padding:20px;
}

h1{text-align:center;}

button{
  padding:10px 16px;
  margin:6px;
  cursor:pointer;
}

input{
  padding:6px;
  width:140px;
}

.card{
  background:white;
  padding:20px;
  border-radius:10px;
  margin:20px auto;
  max-width:700px;
  box-shadow:0 2px 8px rgba(0,0,0,0.1);
}

.explain{
  margin-top:6px;
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
// ================= 혈압 측정 =================
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
    <div id="result" style="margin-top:10px;"></div>
  </div>`;
}

function calc(){
  const sp = document.getElementById("sp").value;
  const dp = document.getElementById("dp").value;

  if(sp==="" || dp===""){
    document.getElementById("result").innerHTML =
      "<b>숫자를 모두 입력하세요.</b>";
    return;
  }

  const result = classify(Number(sp), Number(dp));
  let link = "";

  if(result !== "정상 혈압"){
    link = `
    <p>
      🔗 <a href="https://www.kdca.go.kr" target="_blank">
      질병관리청 고혈압 정보
      </a>
    </p>`;
  }

  document.getElementById("result").innerHTML = `
    <p>판정 결과: <b>${result}</b></p>
    ${link}
  `;
}

// ================= 퀴즈 =================
const quizPool = [
 ["혈압약은 증상이 없어도 복용해야 한다", true, "무증상 고혈압도 합병증 위험이 큽니다."],
 ["고혈압은 뇌졸중 위험을 높인다", true, "주요 위험 인자입니다."],
 ["저염식은 혈압 관리에 중요하다", true, "나트륨 섭취 감소 효과"],
 ["운동은 혈압에 장기적 효과가 없다", false, "꾸준한 운동은 지속 효과"],
 ["고혈압은 유전과 무관하다", false, "가족력 영향 있음"],
 ["수면 부족은 혈압을 올릴 수 있다", true, "교감신경 활성"],
 ["흡연은 혈압과 무관하다", false, "혈관 수축 유발"],
 ["칼륨 섭취는 혈압에 도움된다", true, "나트륨 배출 도움"],
 ["고혈압 전단계는 관리가 필요 없다", false, "생활습관 개선 필요"],
 ["혈압은 안정 후 측정해야 정확하다", true, "오차 감소"],
 ["스트레스는 혈압을 높일 수 있다", true, "호르몬 영향"],
 ["체중 감량은 혈압을 낮출 수 있다", true, "말초 저항 감소"],
 ["고혈압은 심장에 부담을 준다", true, "심부전 위험"],
 ["고혈압 위기는 응급상황이다", true, "즉각적 치료 필요"],
 ["카페인은 혈압에 영향이 없다", false, "일시적 상승"],
 ["염분 섭취량과 혈압은 관련 있다", true, "상관관계 명확"],
 ["혈압은 하루 중 변하지 않는다", false, "변동성 큼"],
 ["운동 직후 혈압은 항상 낮다", false, "일시적 상승 가능"],
 ["고혈압은 신장 기능에 영향을 준다", true, "신장 손상 위험"],
 ["과도한 음주는 혈압을 높인다", true, "혈관 조절 장애"],
 ["고혈압은 동맥경화 위험을 높인다", true, "혈관 손상"],
 ["야채 섭취는 혈압 관리에 도움된다", true, "미네랄 풍부"],
 ["혈압약은 평생 먹어야만 한다", false, "상태에 따라 조절"],
 ["고혈압은 시력에도 영향을 준다", true, "망막 손상 가능"],
 ["운동은 심박수만 높인다", false, "혈관 기능 개선"],
 ["혈압은 양팔에서 같아야 한다", false, "차이 발생 가능"],
 ["고혈압은 치매 위험을 높인다", true, "혈관성 치매"],
 ["소금은 전혀 섭취하면 안 된다", false, "적정량 필요"],
 ["혈압은 집에서도 측정 가능하다", true, "가정 혈압 중요"],
 ["고혈압은 관리하면 합병증 줄일 수 있다", true, "조절 가능"]
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
