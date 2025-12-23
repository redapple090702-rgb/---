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

<script>
function measureBP(){
  const sp = Number(document.getElementById("sp").value);
  const dp = Number(document.getElementById("dp").value);

  if(!sp || !dp){
    document.getElementById("bpResult").innerHTML =
      "<p>⚠️ 혈압 값을 정확히 입력하세요.</p>";
    return;
  }

  const pp = sp - dp;
  const map = ((2*dp) + sp) / 3;

  let stage = "";
  let explain = "";
  let action = "";

  if(sp < 120 && dp < 80){
    stage = "정상 혈압";
    explain = "혈관에 무리가 없는 정상 상태입니다.";
    action = "현재 생활습관을 유지하고 정기적으로 혈압을 측정하세요.";
  }
  else if(sp < 140 || dp < 90){
    stage = "고혈압 전단계 / 1기 고혈압";
    explain = "혈압이 상승하기 시작한 단계로 관리가 필요합니다.";
    action = "염분 섭취를 줄이고 규칙적인 운동을 시작하세요.";
  }
  else if(sp < 160 || dp < 100){
    stage = "2기 고혈압";
    explain = "심장과 혈관에 부담이 커진 상태입니다.";
    action = "의료진 상담 및 약물 치료가 필요할 수 있습니다.";
  }
  else{
    stage = "고혈압 위기";
    explain = "즉각적인 의학적 조치가 필요한 응급 상황입니다.";
    action = "즉시 병원을 방문하거나 응급 진료를 받으세요.";
  }

  document.getElementById("bpResult").innerHTML = `
  <hr>
  <p><b>📊 판정:</b> ${stage}</p>
  <p>${explain}</p>

  <p><b>❤️ 맥압(PP):</b> ${pp} mmHg  
  <br>→ 심장이 한 번 뛸 때 혈관에 가해지는 압력</p>

  <p><b>🫀 평균동맥압(MAP):</b> ${map.toFixed(1)} mmHg  
  <br>→ 장기와 조직으로 가는 평균 혈류 압력</p>

  <p><b>📌 권장 행동:</b><br>${action}</p>

  <p>
  🔗 <a href="https://www.kdca.go.kr" target="_blank">
  질병관리청 고혈압 정보 바로가기
  </a>
  </p>
  `;
}
</script>

</body>
</html>
