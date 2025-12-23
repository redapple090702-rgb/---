<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>혈압 분석 & 건강 퀴즈</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f5f7fa;
      padding: 20px;
      color: #000;
    }

    h1, h2 {
      color: #222;
    }

    .box {
      background: #ffffff;
      padding: 20px;
      border-radius: 10px;
      margin-bottom: 30px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    input, button {
      padding: 8px;
      margin: 5px 0;
      font-size: 16px;
    }

    button {
      cursor: pointer;
    }

    .result {
      margin-top: 15px;
      white-space: pre-line;
      font-size: 16px;
      color: #000;
    }

    .quiz {
      margin-top: 10px;
    }

    .hidden {
      display: none;
    }
  </style>
</head>
<body>

<h1>🩺 혈압 분석 & 건강 퀴즈</h1>

<!-- 혈압 분석기 -->
<div class="box">
  <h2>혈압 분석기</h2>

  <label>수축기 혈압 (SP):</label><br>
  <input type="number" id="sp"><br>

  <label>확장기 혈압 (DP):</label><br>
  <input type="number" id="dp"><br>

  <button onclick="analyzeBP()">분석하기</button>

  <div id="bpResult" class="result"></div>
</div>

<!-- 퀴즈 -->
<div class="box">
  <h2>건강 OX 퀴즈 (10문제 랜덤)</h2>
  <div id="quizArea"></div>
  <button onclick="submitQuiz()">채점하기</button>
  <div id="quizResult" class="result"></div>
</div>

<script>
/* ================= 혈압 분석 ================= */
function analyzeBP() {
  const sp = parseFloat(document.getElementById("sp").value);
  const dp = parseFloat(document.getElementById("dp").value);

  if (isNaN(sp) || isNaN(dp)) {
    alert("혈압 값을 모두 입력하세요.");
    return;
  }

  const pp = sp - dp;
  const map_val = dp + (pp / 3);

  let classification = "";
  if (sp < 120 && dp < 80) {
    classification = "정상 혈압";
  } else if (sp < 130 && dp < 80) {
    classification = "고혈압 전단계";
  } else if (sp < 140 || dp < 90) {
    classification = "고혈압 1기";
  } else {
    classification = "고혈압 2기";
  }

  document.getElementById("bpResult").innerText =
`======== 혈압 분석 결과 ========
* 수축기 혈압(SP): ${sp.toFixed(1)} mmH*
