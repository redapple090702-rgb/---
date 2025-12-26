<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>복지·의료 용어 퀴즈</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    .question {
      margin-bottom: 15px;
    }
    .result {
      margin-top: 10px;
      font-weight: bold;
    }
    button {
      margin-top: 10px;
    }
  </style>
</head>
<body>

<h2>📌 복지·의료 용어 퀴즈</h2>

<div class="question">
  <p>
    1️⃣ 기초생활보장제도에서 국가로부터 생계·의료·주거 지원을 받을 자격이 있는 사람을 무엇이라고 할까요?
  </p>
  <input type="text" id="answer1" placeholder="답을 입력하세요">
  <div id="result1" class="result"></div>
</div>

<div class="question">
  <p>
    2️⃣ 병원에 가서 진료를 받을 때 실제로 본인이 부담하는 비용을 무엇이라고 할까요?
  </p>
  <input type="text" id="answer2" placeholder="답을 입력하세요">
  <div id="result2" class="result"></div>
</div>

<button onclick="checkAnswers()">정답 확인</button>

<script>
function checkAnswers() {
  // 정답 설정
  const correct1 = "수급권자";
  const correct2 = "본인부담금";

  // 사용자 입력
  const user1 = document.getElementById("answer1").value.trim();
  const user2 = document.getElementById("answer2").value.trim();

  // 문제 1 판별
  if (user1 === correct1) {
    document.getElementById("result1").innerText = "⭕ 정답입니다!";
  } else {
    document.getElementById("result1").innerText =
      "❌ 틀렸어요.\n정답: 수급권자\n→ 기초생활보장제도에서 국가의 지원을 받을 수 있는 자격이 있는 사람을 말합니다.";
  }

  // 문제 2 판별
  if (user2 === correct2) {
    document.getElementById("result2").innerText = "⭕ 정답입니다!";
  } else {
    document.getElementById("result2").innerText =
      "❌ 틀렸어요.\n정답: 본인부담금\n→ 의료비 중 건강보험이 아닌, 환자가 직접 내는 비용입니다.";
  }
}
</script>

</body>
</html>
