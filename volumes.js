
var formulas = {
    rectangle(w,h){
        return w*h
    },
    cuboid(w,h,d){
        return w*h*d
    },

    circle(r){
        return Math.pi*r*r
    },
    sphere(r){
        return Math.pi*(4/3)*r*r*r
    },

    trapezoid(a,c,h){
        return (a+c)/2*h
    },
    cylinder(r,h){
        return Math.pi*r*r*h
    },

    pyramid(a,b,h){
        return (1/3)*a*b*h
    }
}

