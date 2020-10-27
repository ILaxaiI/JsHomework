
let buttons = {"button1":document.getElementById("a"),"button2":document.getElementById("b")}
let current = 0
let img = document.getElementById("img1")
let img2 = document.getElementById("img2")
let block = false

letinput = document.getElementById("input");
input.innerHTML = images[current].html

for(let inp of input.getElementsByClassName("input")){
    console.log(inp)
    console.log("adding event to",inp)
    inp.addEventListener("click",clearSelf)
}

function finish(){
    block = false
    img.classList.remove("ROut");
    img.classList.remove("LOut");
    img.style.display = "none"; 
    img.removeEventListener("animationend",finish)
    img2.classList.remove("RIn");
    img2.classList.remove("LIn");
    let tmp = img; img = img2;img2 = tmp;

}

function clearSelf(eve){
    console.log(eve)
}

function swipeRight(){
    if (block) return; block = true;
    current = (current-1)%images.length;
    current = current < 0 ? images.length-1 : current;
  
    img.classList.add("ROut")
    img.addEventListener("animationend",finish)    
    img2.setAttribute("src","images/"+images[(current)%images.length].name)
    
    for(let inp of  input.getElementsByClassName("input")){
        inp.removeEventListener("click",clearSelf)
    }
    
    input.innerHTML = images[current].html || ""
    
    for(let inp of  input.getElementsByClassName("input")){
        inp.addEventListener("click",clearSelf)
    }
    
    img2.style.display = "block";
    img2.classList.add("RIn")
}
function swipeLeft(){
    if (block) return;
    block = true
  
    current = (current+1)%images.length
    current = current < 0 ? images.lenhth+1 : current;
  
    for(let inp of  input.getElementsByClassName("input")){
        inp.removeEventListener("click",clearSelf)
    }
    
    input.innerHTML = images[current].html || ""
    
    for(let inp of  input.getElementsByClassName("input")){
        inp.addEventListener("click",clearSelf)
    }
    
    img.classList.add("LOut")
    img.addEventListener("animationend",finish)
    img2.setAttribute("src","images/"+images[(current)%images.length].name)
    img2.style.display = "block";
    img2.classList.add("LIn")            
}