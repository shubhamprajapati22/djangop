var img;

function preload(){
    img = loadImage("../static/images/clockimg.png");
}

function setup() {
  createCanvas(65, 65);
    angleMode(DEGREES);
    
}


function draw() {
    background(img);
    h = hour();
    m = minute();
    s = second();
    fill(255);
    h = h % 12;
    if(h == 0)
        h = 12;
    
    
    text(h + ':' + m + ':' + s,240 ,290);
    translate(height/2, width/2)
   
      push();
    
    rotate(map(h, 0, 12, 0, 360));
    strokeWeight(2.5);
    stroke("black");
    line(0, 5, 0, -height * 6 / 30);//hour
    
    pop();
    
    push();
    
    rotate(map(m, 0, 60, 0, 360));
    strokeWeight(1.5);
    stroke("green");
    line(0, 8, 0, -height * 17 / 60);//minute
    
    pop();
    
   
    
      push();
    
    rotate(map(s, 0, 60, 0, 360));
    strokeWeight(0.8);
    stroke("red");
    line(0, 8, 0, -height/3.5);//second
    pop();
    
    
    
   
     noStroke();
    fill(204, 0, 102);
    ellipse(0, 0, 5);
}