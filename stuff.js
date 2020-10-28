
let buttons = {"button1":document.getElementById("a"),"button2":document.getElementById("b")}
let current = 0
let img = document.getElementById("img1")
let img2 = document.getElementById("img2")
let block = false

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
    if(eve.target.value === eve.target.initialValue){
      eve.target.value =""
    }
}

function oc(eve){
    if(eve.target.value === ""){
        eve.target.value = eve.target.initialValue
    }
}

let resspace = document.getElementById("result")
function displayResult(){
    let args = []
    for (ele of images[current].html.getElementsByTagName("input")){
        let val = parseFloat(ele.value)
        if (!isNaN(val)){
        args.push(val)
       } else return;
    }
    let result = images[current].formula(args[0],args[1],args[2])
    resspace.innerHTML = "Result: "+result;
}

for(o of images){
    for (ele of o.html.getElementsByTagName("input")){
        obj.initialValue = obj.value
        obj.addEventListener("click",clearSelf)
        obj.addEventListener("blur",oc)
    }
}



function swipeRight(){
    if (block) return; block = true;
    images[current].html.style.display = "none"

    current = (current-1)%images.length;
    current = current < 0 ? images.length-1 : current;
    
    images[current].html.style.display = ""
    img.classList.add("ROut")
    img.addEventListener("animationend",finish)    
    img2.setAttribute("src","images/"+images[(current)%images.length].name)
    img2.style.display = "block";
    img2.classList.add("RIn")
}

function swipeLeft(){
    if (block) return;
    block = true
  
    images[current].html.style.display = "none"
    current = (current+1)%images.length
    current = current < 0 ? images.lenhth+1 : current;
  
    images[current].html.style.display = ""
    
    img.classList.add("LOut")
    img.addEventListener("animationend",finish)
    img2.setAttribute("src","images/"+images[(current)%images.length].name)
    img2.style.display = "block";
    img2.classList.add("LIn")            
}