var formulas = [
    
    function circle(r){
        return Math.pi*r*r
    },
    function sphere(r){
        return Math.pi*(4/3)*r*r*r
    },
    function cylinder(r,h){
        return Math.pi*r*r*h
    },  
    function rectangle(w,h){
        return w*h
    },
    function cuboid(w,h,d){
        return w*h*d
    },

    
    function trapezoid(a,c,h){
        return (a+c)/2*h
    },


    function pyramid(a,b,h){
        return (1/3)*a*b*h
    }
];

