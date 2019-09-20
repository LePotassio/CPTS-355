/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 
 Eric Furukawa
 4/24/19
 CPTS 355
 Some discussion witrh Jimmy Zheng
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.*;

public class BallGame { 

    public static void main(String[] args) {
      Player person = new Player();
    
      ArrayList<BasicBall> ballList = new ArrayList<BasicBall>();
    	// number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
    	
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
    		ballTypes[i] = args[index];
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
    	}
     
    	//TO DO: create a Player object and initialize the player game stats.  
    	
    	
    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);
        int splitSize = 0;
        // create colored balls
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
   		for (int i = 0; i<numBalls; i++) {
            if (ballTypes[i].equals("basic")) {
               BasicBall ball = new BasicBall(ballSizes[i],Color.RED);
               ballList.add(0,ball);
            } else if (ballTypes[i].equals("shrink")) {
               BasicBall ball = new ShrinkBall(ballSizes[i],Color.GREEN);
               ballList.add(0,ball);
            } else if (ballTypes[i].equals("bounce")) {
               BasicBall ball = new BounceBall(ballSizes[i],Color.BLUE);
               ballList.add(0,ball);
            } else if (ballTypes[i].equals("split")) {
               BasicBall ball = new SplitBall(ballSizes[i],Color.ORANGE);
               ballList.add(0,ball);
            } else if (ballTypes[i].equals("magic")) {
               BasicBall ball = new MagicBall(ballSizes[i],Color.BLACK);
               ballList.add(0,ball);
            }
         }
   		//TO DO: initialize the numBallsinGame
   		numBallsinGame = ballList.size();
         //System.out.println(numBallsinGame);
        
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

        	// TODO: move all balls
            for (int i = 0; i<numBallsinGame; i++) {
               ballList.get(i).move();
            }

            //Check if the mouse is clicked
            boolean splitYES = false;
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.
                for (int i = 0; i<numBallsinGame; i++) {
                   if (ballList.get(i).isHit(x,y)) {
                     ballList.get(i).reset();
                     if(ballList.get(i) instanceof ShrinkBall) {
                        person.oneShrink();
                        person.addScore(ballList.get(i).getScore());
                     } else if(ballList.get(i) instanceof BounceBall) {
                        person.oneBounce();
                        person.addScore(ballList.get(i).getScore());
                     } else if(ballList.get(i) instanceof SplitBall) {
                        person.oneSplit();
                        //
                        splitYES = true;
                        splitSize = i;
                        //
                        person.addScore(ballList.get(i).getScore());
                     } else if(ballList.get(i) instanceof MagicBall) {
                        person.oneMagic();
                        person.addScore(ballList.get(i).getScore());
                     } else {
                        person.oneBasic();
                        person.addScore(ballList.get(i).getScore());
                     }
                    	//TO DO: Update player statistics
                   }
                }
                if (splitYES) {
                  BasicBall ball = new SplitBall(ballList.get(splitSize).getRadius(),Color.ORANGE);
                  ballList.add(0,ball);
                  numBallsinGame++;
                  splitYES = false;
                }
            }
                
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game.
            for (int i = 0; i<ballList.size(); i++) {  
               if (ballList.get(i).isOut == false) { 
                  ballList.get(i).draw();
               }
               else {
                  numBallsinGame--;
                  ballList.remove(i);
               }
            }
            
            person.mostHitDecider();
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            //TO DO: print the rest of the player statistics
            StdDraw.text(-0.65, 0.80, "Player Points: "+ String.valueOf(person.getScore()));
            StdDraw.text(-0.65, 0.70, "Most Hit: "+ person.getMostHit());
            StdDraw.text(-0.65, 0.60, "Number of hits: "+ String.valueOf(person.getHits()));

            StdDraw.show();
            StdDraw.pause(20);
        }
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
