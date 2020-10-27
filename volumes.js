const images = [ 
    {   
        name:"circle.png", 
        formula:function (r){return Math.pi*r*r;},
        html:`
            <input class = 'input' id='rad' type = 'text' value = 'Radius'></input>`
    },
    {
        name:"sphere.png",
        formula:function(r){return Math.pi*(4/3)*r*r*r;}, 
        html:`
            <input class = 'input' id ='rad' type = 'text' value = 'Radius'></input>`
        },
    {
        name:"cylinder.png", 
        formula:function(r,h){return Math.pi*r*r*h},
        html:`
                <input class = 'input' type = 'text' id = 'rad' value = 'Radius' style = 'margin-right:50px;'></input>
                <input class = 'input' id = 'hei' type = 'text' value = 'Height'></input>   `
    },
    {
        name:"rectangle.png", 
        formula:function(w,h){return w*h},
        html:`
            <input class = 'input' type = 'text' id = 'rad' value = 'Width' style = 'margin-right:50px;'></input>
            <input class = 'input' id = 'hei' type = 'text' value = 'Height'></input>`
    },
    {
        name:"cuboid.png", 
        formula:function(w,h,d){return w*h*d},
        html:`
        <input class = 'input' type = 'text' id = 'rad' value = 'Width' style = 'margin-right:50px;'></input>
        <input class = 'input' type = 'text' id = 'rad' value = 'Height' style = 'margin-right:50px;'></input>
        <input class = 'input' id = 'hei' type = 'text' value = 'Debth'></input>        `
    }, 
   {    
        name:"trapezoid.png", 
        formula:function(a,c,h){return (a+c)/2*h},
        html:`
        <input class = 'input' type = 'text' id = 'rad' value = 'Base 1' style = 'margin-right:50px;'></input>
        <input class = 'input' type = 'text' id = 'rad' value = 'Base 2' style = 'margin-right:50px;'></input>
        <input class = 'input' id = 'hei' type = 'text' value = 'Height'></input>`
    },
    {
        name:"pyramid.png", 
        formula:function(a,b,h){return (1/3)*a*b*h},
        html:`
        <input class = 'input' type = 'text' id = 'rad' value = 'Width' style = 'margin-right:50px;'></input>
        <input class = 'input' type = 'text' id = 'rad' value = 'Height' style = 'margin-right:50px;'></input>
        <input class = 'input' id = 'hei' type = 'text' value = 'Debth'></input>
          `
        }
];

