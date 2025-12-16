<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>동물 DNA 조합 게임</title>
<style>
body {
  background:#0f172a;
  color:#fff;
  font-family:sans-serif;
  padding:20px;
}
h1,h2 { text-align:center; }
.section {
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:10px;
  margin-top:20px;
}
.card {
  border:1px solid #475569;
  padding:10px;
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

<h1>🧬 동물 DNA 조합 게임</h1>
<h2 id="stepTitle"></h2>

<div id="cards" class="section"></div>

<div style="text-align:center;">
<button onclick="next()">다음</button>
</div>

<div id="result"></div>

<script>
const dna = {
head: [
{a:"치타",g:"PAX6",d:"시각 발달"},
{a:"치타",g:"MITF",d:"눈가 줄무늬"},
{a:"치타",g:"FOXA2",d:"호흡 발달"},
{a:"기린",g:"PAX3",d:"감각 구조"},
{a:"기린",g:"ALX4",d:"두개골 형태"},
{a:"기린",g:"OTX2",d:"시각계"},
{a:"펭귄",g:"BMP4",d:"부리 형태"},
{a:"펭귄",g:"SHH",d:"안면 패턴"},
{a:"펭귄",g:"PAX6",d:"수중 시야"},
{a:"문어",g:"PAX6",d:"눈 형성"},
{a:"문어",g:"PCDH",d:"신경 연결"},
{a:"문어",g:"ELAVL",d:"신경 안정"}
],
body: [
{a:"치타",g:"MSTN",d:"근육 경량화"},
{a:"치타",g:"COL1A1",d:"결합조직 탄성"},
{a:"치타",g:"TTN",d:"근섬유 탄성"},
{a:"기린",g:"HOXA5",d:"척추 길이"},
{a:"기린",g:"FGFRL1",d:"혈관 발달"},
{a:"기린",g:"VEGFA",d:"혈류 증가"},
{a:"펭귄",g:"UCP1",d:"체온 유지"},
{a:"펭귄",g:"MYH7",d:"지구력"},
{a:"펭귄",g:"PPARG",d:"지방 대사"},
{a:"문어",g:"ADAR",d:"RNA 편집"},
{a:"문어",g:"SLC6A",d:"신경 전달"},
{a:"문어",g:"MYH",d:"근육 수축"}
],
leg: [
{a:"치타",g:"ACTN3",d:"속근"},
{a:"치타",g:"COL5A1",d:"힘줄"},
{a:"치타",g:"MYH2",d:"빠른 수축"},
{a:"기린",g:"RUNX2",d:"골형성"},
{a:"기린",g:"COL1A2",d:"뼈 강도"},
{a:"기린",g:"IGF1",d:"성장"},
{a:"펭귄",g:"TBX5",d:"수영 추진"},
{a:"펭귄",g:"HOXD11",d:"사지 길이"},
{a:"펭귄",g:"ACTA1",d:"근수축"},
{a:"문어",g:"Reflectin",d:"위장"},
{a:"문어",g:"NEUROD",d:"신경 분화"},
{a:"문어",g:"ACTB",d:"세포골격"}
]
};

let step = 0;
const order = ["head","body","leg"];
const chosen = {};
let selected = [];

function render() {
  document.getElementById("stepTitle").innerText =
    `${["머리","몸통","다리"][step]} DNA 선택 (5개)`;
  const area = document.getElementById("cards");
  area.innerHTML = "";
  selected = [];

  dna[order[step]].forEach(d=>{
    const c = document.createElement("div");
    c.className="card";
    c.innerText = `${d.a}\n${d.g}\n(${d.d})`;
    c.onclick = ()=>{
      if (c.classList.contains("selected")) {
        c.classList.remove("selected");
        selected = selected.filter(x=>x!==d);
      } else {
        if (selected.length>=5) return;
        c.classList.add("selected");
        selected.push(d);
      }
    };
    area.appendChild(c);
  });
}

function decide(arr) {
  const cnt = {};
  arr.forEach(d=>cnt[d.a]=(cnt[d.a]||0)+1);
  const max = Math.max(...Object.values(cnt));
  const top = Object.keys(cnt).filter(k=>cnt[k]===max);
  return top[Math.floor(Math.random()*top.length)];
}

function next() {
  if (selected.length!==5) {
    alert("5개를 선택하세요");
    return;
  }
  chosen[order[step]] = decide(selected);
  step++;
  if (step<3) render();
  else showResult();
}

function showResult() {
  document.getElementById("cards").innerHTML="";
  document.getElementById("stepTitle").innerText="🎉 최종 결과";
  document.getElementById("result").innerText =
`🧠 머리: ${chosen.head}
🫀 몸통: ${chosen.body}
🦵 다리: ${chosen.leg}

완성된 혼합 생물 탄생!`;
}

render();
</script>

</body>
</html>
