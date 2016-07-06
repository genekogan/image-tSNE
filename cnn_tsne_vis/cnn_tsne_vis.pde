ArrayList<PImage> images;
ArrayList<PVector> positions;

void setup() {
  size(displayWidth,displayHeight);
  
  images = new ArrayList<PImage>();
  positions = new ArrayList<PVector>();
  
  String[] lines = loadStrings("tsne_points.txt");
  for (int i=0; i<lines.length; i++) {
    if (i % 20 == 0) {
      println("opening image "+i+" of "+lines.length);
    }
    String l = lines[i];
    String[] l2 = split(l,",");
    PImage img = loadImage(l2[0]);
    img.resize(100, 100);
    images.add(img);
    positions.add(new PVector(float(l2[1]), float(l2[2])));
  }
}

void draw() {
  background(0);
  pushMatrix();
  translate(map(mouseX, 0, width, 0, -3*width), map(mouseY, 0, height, 0, -3*height));
  
  for (int i=0; i<positions.size(); i++) {
    float x = positions.get(i).x * 4*width;
    float y = positions.get(i).y * 4*height;
    image(images.get(i), x, y);
  }
  popMatrix();
}
