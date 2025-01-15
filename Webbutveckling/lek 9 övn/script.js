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

let listan = document.querySelector("ul");

let li_1 = document.createElement("li");
li_1.textContent="Lära javascript syntax";
listan.appendChild(li_1);

let li_2 = document.createElement("li");
li_2.textContent="Lära document objektet";
listan.appendChild(li_2);

listan.classList.add("ul_layout")

let li_array = document.querySelectorAll("li");

for(let i=0; i < li_array.length; i++)
{
    li_array[i].classList.add("fet_text");
}

function växla_tema() {
    document.body.classList.toggle("dark_mode")
}
