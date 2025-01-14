let rubrik = document.querySelector("h1");

console.log("rubriken text är  "+rubrik.textContent);

rubrik.textContent="Javascript it is ";

let p = document.querySelector("p");

p.textContent="Text has changed due to javascript";

let text = document.querySelector(".text");

text.style.border="4px solid black";

text.style.marginLeft="10vw";
text.style.marginRight="10vw";

rubrik.classList.add("xtra");

document.body.classList.add("yellow_background");

let listan= document.querySelector("ul");