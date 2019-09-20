import java.awt.Color;

public class BounceBall extends BasicBall {
   private double bounces = 0;
   
   public BounceBall(double r, Color c) {
      super(r,c);
   }
   
   public int getScore() {
      return 15;
   }
   
   public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius)) {
			return true;
      }
		else return false;
   }
   
    public void move() {
      rx = rx + vx;
      ry = ry + vy;
      if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0))
         bounces++;
         if(bounces == 4) { 
            isOut = true;
         }
         else {
            if(Math.abs(rx) > 1.0) {
               vx = -vx;
            }
            if(Math.abs(ry) > 1.0) {
               vy = -vy;
            }
         }
    }
   
   public void draw() { 
    	if ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0)) {
    		StdDraw.setPenColor(color);
    		StdDraw.filledCircle(rx, ry, radius);
      }
   }
}