import java.awt.Color;

public class MagicBall extends BasicBall {//Bonus "FUN" Ball for making the game a little bit more than required
   int cycle;
   public MagicBall(double r, Color c) {
      super(r,c);
      cycle = 0;
   }
   
   public void move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
        	isOut = true;
    }
   
   public int reset() {
        rx = 0.0;
        ry = 0.0;  	
        // TO DO: assign a random speed
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        cycle++;
        if(cycle == 1) {
           changeColor(Color.BLUE);
        } else if(cycle == 2) {
           changeColor(Color.RED);
        } else if (cycle == 3) {
            changeColor(color.GREEN);
            cycle = 0;
        }
        return 1;
    }
   
   public int getScore() {
      return -100;
   }
}