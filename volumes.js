Math.pi = 3.14159265359
const images = [ 
    {   
        name:"circle.png", 
        formula:function (r){return Math.pi*r*r;},
        html:document.getElementById("circle")
    },
    {
        name:"sphere.png",
        formula:function(r){return Math.pi*(4/3)*r*r*r;}, 
        html:document.getElementById("sphere")
        },
    {
        name:"cylinder.png", 
        formula:function(r,h){return Math.pi*r*r*h},
        html:document.getElementById("cylinder")
    },
    {
        name:"rectangle.png", 
        formula:function(w,h){return w*h},
        html:document.getElementById("rectangle")

          
    },
    {
        name:"cuboid.png", 
        formula:function(w,h,d){return w*h*d},
        html:document.getElementById("cuboid")
    }, 
   {    
        name:"trapezoid.png", 
        formula:function(a,c,h){return (a+c)/2*h},
        html:document.getElementById("trapezoid")
        
    },
    {
        name:"pyramid.png", 
        formula:function(a,b,h){return (1/3)*a*b*h},
        html:document.getElementById("pyramid")
        }
];

