<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>DNA 특성 선택 게임</title>
<style>
body {
  background:#020617;
  color:#fff;
  font-family:sans-serif;
  padding:20px;
}
h1,h2 { text-align:center; }
.section {
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:12px;
  margin-top:20px;
}
.card {
  border:1px solid #475569;
  padding:12px;
  cursor:pointer;
  background:#020617;
}
.card.selected {
  background:#22c55e;
  color:#000;
}
button {
  margin-top:20px;
  padding:10px 20px;
  font-size:16px;
  cursor:pointer;
}
#result {
  white-space:pre-line;
  font-size:18px;
  margin-top:30px;
  text-align:center;
}
</style>
</head>
<body>

<h1>🧬 DNA 특성 조합 게임</h1>
<h2 id="stepTitle"></h2>

<div id="cards" class="section"></div>

<div style="text-align:center;">
<button onclick="nextStep()">다음</button>
</div>

<div id="result"></div>

<script>
const dna = {
head: [
{animal:"치타", gene:"PAX6", desc:"시각 기능 강화"},
{animal:"치타", gene:"MITF", desc:"눈 주변 색 대비"},
{animal:"치타", gene:"FOXA2", desc:"호흡기 발달"},
{animal:"기린", gene:"PAX3", desc:"감각 구조 형성"},
{animal:"기린", gene:"ALX4", desc:"두개골 형태"},
{animal:"기린", gene:"OTX2", desc:"시각계 발달"},
{animal:"펭귄", gene:"BMP4", desc:"부리 형태"},
{animal:"펭귄", gene:"SHH", desc:"안면 구조 패턴"},
{animal:"펭귄", gene:"PAX6", desc:"수중 시야"},
{animal:"문어", gene:"PAX6", desc:"눈 형성"},
{animal:"문어", gene:"PCDH", desc:"신경 연결 다양화"},
{animal:"문어", gene:"ELAVL", desc:"신경 안정성"}
],
body: [
{animal:"치타", gene:"MSTN", desc:"근육 경량화"},
{animal:"치타", gene:"COL1A1", desc:"결합조직 탄성"},
{animal:"치타", gene:"TTN", desc:"근섬유 탄성"},
{animal:"기린", gene:"HOXA5", desc:"척추 길이 증가"},
{animal:"기린", gene:"FGFRL1", desc:"혈관 발달"},
{animal:"기린", gene:"VEGFA", desc:"혈류 효율"},
{animal:"펭귄", gene:"UCP1", desc:"체온 유지"},
{animal:"펭귄", gene:"MYH7", desc:"지구력 근육"},
{animal:"펭귄", gene:"PPARG", desc:"지방 대사"},
{animal:"문어", gene:"ADAR", desc:"RNA 편집"},
{animal:"문어", gene:"SLC6A", desc:"신경 전달"},
{animal:"문어", gene:"MYH", desc:"근육 수축"}
],
leg: [
{animal:"치타", gene:"ACTN3", desc:"속근 기능"},
{animal:"치타", gene:"COL5A1", desc:"힘줄 강도"},
{animal:"치타", gene:"MYH2", desc:"빠른 근수축"},
{animal:"기린", gene:"RUNX2", desc:"골형성"},
{animal:"기린", gene:"COL1A2", desc:"뼈 강도"},
{animal:"기린", gene:"IGF1", desc:"성장 조절"},
{animal:"펭귄", gene:"TBX5", desc:"수영 추진"},
{animal:"펭귄", gene:"HOXD11", desc:"사지 길이"},
{animal:"펭귄", gene:"ACTA1", desc:"근수축"},
{animal:"문어", gene:"Reflectin", desc:"위장 능력"},
{animal:"문어", gene:"NEUROD", desc:"신경 분화"},
{animal:"문어", gene:"ACTB", desc:"세포골격"}
]
};

const order = ["head","body","leg"];
const labels = ["머리","몸통","다리"];
let step = 0;
let selected = [];
const result = {};

function shuffle(arr) {
  return arr.sort(()=>Math.random()-0.5);
}

function render() {
  document.getElementById("stepTitle").innerText =
    `${labels[step]} DNA 선택 (5개)`;

  selected = [];
  const area = document.getElementById("cards");
  area.innerHTML = "";

  shuffle([...dna[order[step]]]).forEach(d=>{
    const card = document.createElement("div");
    card.className="card";
    card.innerText = `${d.gene}\n${d.desc}`;
    card.onclick = ()=>{
      if (card.classList.contains("selected")) {
        card.classList.remove("selected");
        selected = selected.filter(x=>x!==d);
      } else {
        if (selected.length>=5) return;
        card.classList.add("selected");
        selected.push(d);
      }
    };
    area.appendChild(card);
  });
}

function decide(arr) {
  const count = {};
  arr.forEach(d=>count[d.animal]=(count[d.animal]||0)+1);
  const max = Math.max(...Object.values(count));
  const top = Object.keys(count).filter(k=>count[k]===max);
  return top[Math.floor(Math.random()*top.length)];
}

function nextStep() {
  if (selected.length!==5) {
    alert("5개를 선택하세요");
    return;
  }
  result[order[step]] = decide(selected);
  step++;
  if (step<3) render();
  else showResult();
}

function showResult() {
  document.getElementById("cards").innerHTML="";
  document.getElementById("stepTitle").innerText="🎉 최종 결과";
  document.getElementById("result").innerText =
`🧠 머리: ${result.head}
🫀 몸통: ${result.body}
🦵 다리: ${result.leg}`;
}

render();
</script>

</body>
</html>
