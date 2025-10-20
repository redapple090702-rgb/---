<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>역사·의학 퀴즈</title>
<style>
body{display:flex;align-items:center;justify-content:center;min-height:100vh;background:#f4f6fb;margin:0;font-family:'Noto Sans KR',sans-serif}
.card{width:720px;max-width:95%;background:#fff;padding:24px;border-radius:12px;box-shadow:0 8px 30px rgba(20,30,60,0.08)}
h1{margin:0 0 12px;font-size:22px;text-align:center}
.question{font-size:18px;margin:18px 0}
.choices{display:flex;flex-direction:column;gap:10px}
.choice{padding:12px 14px;border-radius:8px;border:1px solid #d6dce9;background:#fcfdff;cursor:pointer;text-align:left;transition:0.2s}
.choice:hover{background:#eef3ff}
.choice.disabled{opacity:0.6;pointer-events:none}
.choice.correct{border-color:#2e8b57;background:#e8fbf0}
.choice.wrong{border-color:#d9534f;background:#fff0f0}
.feedback{height:28px;margin-top:12px;font-weight:600;text-align:center}
.progress{height:8px;background:#eef3ff;border-radius:999px;overflow:hidden;margin-top:10px}
.progress > i{display:block;height:100%;background:#4b7cff;width:0%}
.footer{display:flex;justify-content:space-between;align-items:center;margin-top:18px;color:#444}
.timer{font-weight:700}
.final{font-size:18px;text-align:center;padding:18px}
</style>
</head>
<body>
<div class="card">
  <h1>역사·의학 퀴즈</h1>
  <div id="quizArea">
    <div class="question" id="questionText">로딩 중...</div>
    <div class="choices" id="choices"></div>
    <div class="feedback" id="feedback"></div>
    <div class="progress"><i id="progressBar"></i></div>
    <div class="footer">
      <div class="timer">남은 시간: <span id="timeLeft">--:--</span></div>
      <div class="small">문제: <span id="qIndex">0</span>/5</div>
    </div>
  </div>
  <div id="resultArea" style="display:none">
    <div class="final" id="finalMsg"></div>
  </div>
</div>

<script>
const questions=[
  {q:'제2차 세계대전 당시, 독일이 병사들의 피로를 줄이고 전투력을 높이기 위해 사용한 각성제의 상표명은 무엇일까?', choices:['히로뽕','페르비틴','아편','메스암페타민','보드카'], answer:1},
  {q:'다음 중 항생제(antibiotic)의 계열에 속하지 않는 성분은 무엇일까?', choices:['페니실린','세팔로스포린','아미노글리코사이드','비스포스포네이트','퀴놀론'], answer:3},
  {q:'20세기 초 전 세계적으로 약 5천만 명 이상의 인명 피해를 남긴 전염병의 이름은 무엇일까?', choices:['페스트','코로나19','메로나','에볼라 바이러스','스페인 독감'], answer:4},
  {q:'나폴레옹의 대륙봉쇄령으로 인해 독일 화학자들이 새로운 합성 의약품을 개발하기 시작했다. 이 시기에 탄생한 대표적인 진통·해열제는?', choices:['모르핀','아스피린','페니실린','퀴닌','스테로이드'], answer:1},
  {q:'제2차 세계대전 당시, 말라리아 피해가 심각해지자 합성 치료제가 개발되었다. 이때 새롭게 만들어진 약은?', choices:['페니실린','모르핀','클로로퀸(Chloroquine)','아스피린','스피락톤'], answer:2}
];

const perQuestionLimit=5*60*1000; // 5분
const nextDelay=3000; // 3초
let current=0,score=0,interval,answered=false;

const eQ=document.getElementById('questionText'),
      eC=document.getElementById('choices'),
      eF=document.getElementById('feedback'),
      eT=document.getElementById('timeLeft'),
      eI=document.getElementById('qIndex'),
      eP=document.getElementById('progressBar'),
      eA=document.getElementById('quizArea'),
      eR=document.getElementById('resultArea'),
      eM=document.getElementById('finalMsg');

function start(){current=0;score=0;showQuestion(current);}
function showQuestion(idx){
  answered=false;
  const q=questions[idx];
  eI.textContent=idx+1;
  eQ.textContent=q.q;
  eF.textContent='';
  eC.innerHTML='';
  q.choices.forEach((choice,i)=>{
    const btn=document.createElement('button');
    btn.className='choice';
    btn.type='button';
    btn.innerHTML=`<strong>${i+1}.</strong> ${choice}`;
    btn.addEventListener('click',()=>selectAnswer(i,q.answer,btn));
    eC.appendChild(btn);
  });
  startTimer();
}
function selectAnswer(sel,answer,btn){
  if(answered) return;
  answered=true;
  clearInterval(interval);
  Array.from(eC.children).forEach(c=>c.classList.add('disabled'));
  if(sel===answer){
    btn.classList.add('correct');
    eF.textContent='정답입니다!';
    score++;
  }else{
    btn.classList.add('wrong');
    eF.textContent='틀렸습니다.';
    eC.children[answer].classList.add('correct');
  }
  setTimeout(()=>nextQuestion(),nextDelay);
}
function nextQuestion(){
  current++;
  if(current>=questions.length) finishQuiz();
  else showQuestion(current);
}
function finishQuiz(){
  eA.style.display='none';
  eR.style.display='block';
  eM.innerHTML=`🎉 수고했습니다!<br>맞힌 문제 수: <strong>${score}</strong> / ${questions.length}`;
}
function startTimer(){
  const start=Date.now();
  const end=start+perQuestionLimit;
  interval=setInterval(()=>{
    const remain=Math.max(0,end-Date.now());
    const sec=Math.ceil(remain/1000);
    const min=Math.floor(sec/60);
    const s=sec%60;
    eT.textContent=`${min<10?'0'+min:min}:${s<10?'0'+s:s}`;
    eP.style.width=`${100-(remain/perQuestionLimit*100)}%`;
    if(remain<=0){
      clearInterval(interval);
      if(!answered){
        answered=true;
        eF.textContent='시간 초과! 틀렸습니다.';
        Array.from(eC.children).forEach(c=>c.classList.add('disabled'));
        setTimeout(nextQuestion,nextDelay);
      }
    }
  },200);
}

start();
</script>
</body>
</html>
# ---
