import java.awt.Color;

public class ShrinkBall extends BasicBall {
   public final double firstRad;

   public ShrinkBall(double r, Color c) {
      super(r,c);
      firstRad = r;
   }
   
   public int getScore() {
      return 20;
   }
   
   public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius)) {
         //System.out.println(radius);
         radius = radius * (2.0/3.0);
         if (radius <= firstRad * (1.0/4.0)) {
            radius = firstRad;
         }
			return true;
      }
		else return false;
   }
}