/* Slideshow 1 - Director Visit */
let firstImgs = [
  "../imgs/history/director visit/1.jpg",
  "../imgs/history/director visit/2.jpg",
  "../imgs/history/director visit/3.jpg",
  "../imgs/history/director visit/4.jpg",
];

let x = 0;
function slideShow1() {
  if (x === 4) {
    x = 0;
  }
  document.getElementById("slideFirst").src = firstImgs[x];
  x++;
}

setInterval(slideShow1, 5000);

/* Slideshow 2 - ISEF */
let img2 = [
  "../imgs/history/isef/1.jpg",
  "../imgs/history/isef/2.jpg",
  "../imgs/history/isef/3.jpg",
  "../imgs/history/isef/4.jpg",
];

let y = 0;
function slideShow2() {
  if (y === 4) {
    y = 0;
  }
  document.getElementById("slide2").src = img2[y];
  y++;
}

setInterval(slideShow2, 5000);

/* Slideshow 3 - EJUST Tour */
let img3 = [
  "../imgs/history/ejust tour/1.jpg",
  "../imgs/history/ejust tour/2.jpg",
  "../imgs/history/ejust tour/3.jpg",
  "../imgs/history/ejust tour/4.jpg",
];

let z = 0;
function slideShow3() {
  if (z === 4) {
    z = 0;
  }
  document.getElementById("slide3").src = img3[z];
  z++;
}

setInterval(slideShow3, 5000);

/* Slideshow 4 - Morning Line */
let img4 = [
  "../imgs/history/morning line/1.jpg",
  "../imgs/history/morning line/2.jpg",
  "../imgs/history/morning line/3.jpg",
  "../imgs/history/morning line/4.jpg",
];

let a = 0;
function slideShow4() {
  if (a === 4) {
    a = 0;
  }
  document.getElementById("slide4").src = img4[a];
  a++;
}

setInterval(slideShow4, 5000);

/* Slideshow 5 - Capstone */
let img5 = [
  "../imgs/history/capstone/1.jpg",
  "../imgs/history/capstone/2.jpg",
  "../imgs/history/capstone/3.jpg",
  "../imgs/history/capstone/4.jpg",
];

let b = 0;
function slideShow5() {
  if (b === 4) {
    b = 0;
  }
  document.getElementById("slide5").src = img5[b];
  b++;
}

setInterval(slideShow5, 5000);

/* Slideshow 6 - Teba Visit */
let img6 = [
  "../imgs/history/teba visit/1.jpg",
  "../imgs/history/teba visit/2.jpg",
  "../imgs/history/teba visit/3.jpg",
  "../imgs/history/teba visit/4.jpg",
];

let c = 0;
function slideShow6() {
  if (c === 4) {
    c = 0;
  }
  document.getElementById("slide6").src = img6[c];
  c++;
}

setInterval(slideShow6, 5000);

/* Slideshow 7 - Oman Visit */
let img7 = [
  "../imgs/history/oman visit/1.jpg",
  "../imgs/history/oman visit/2.jpg",
  "../imgs/history/oman visit/3.jpg",
  "../imgs/history/oman visit/4.jpg",
];

let d = 0;
function slideShow7() {
  if (d === 4) {
    d = 0;
  }
  document.getElementById("slide7").src = img7[d];
  d++;
}

setInterval(slideShow7, 5000);

/* Slideshow 8 - German Day */
let img8 = [
  "../imgs/history/german day/1.jpg",
  "../imgs/history/german day/2.jpg",
  "../imgs/history/german day/3.jpg",
  "../imgs/history/german day/4.jpg",
];

let e = 0;
function slideShow8() {
  if (e === 4) {
    e = 0;
  }
  document.getElementById("slide8").src = img8[e];
  e++;
}

setInterval(slideShow8, 5000);

/* Slideshow 9 - Dr. Zewail Visit */
let img9 = [
  "../imgs/history/dr. zewil/1.jpg",
  "../imgs/history/dr. zewil/2.jpg",
  "../imgs/history/dr. zewil/3.jpg",
  "../imgs/history/dr. zewil/4.jpg",
];

let f = 0;
function slideShow9() {
  if (f === 4) {
    f = 0;
  }
  document.getElementById("slide9").src = img9[f];
  f++;
}

setInterval(slideShow9, 5000);
