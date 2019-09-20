//Number Hits
//Player score
//Most hit
//Bounce Ball


public class Player {
   int basicHit;
   int shrinkHit;
   int bounceHit;
   int splitHit;
   int magicHit;
   int playerPoints;
   String mostHit;
   
   public Player() {
      basicHit = 0;
      shrinkHit = 0;
      bounceHit = 0;
      splitHit = 0;
      magicHit = 0;
      playerPoints = 0;
      mostHit = "";
   }
   
   
   public int getBasic() {
      return basicHit;
   }
   
   public int getShrink() {
      return shrinkHit;
   }
    
   public int getBounce() {
      return bounceHit;
   }
   
   public int getSplit() {
      return splitHit;
   }
   
   public int getmagic() {
      return magicHit;
   }
   
   public int getPoints() {
      return playerPoints;
   }
   
   public String getMostHit() {
      return mostHit;
   }
   
   public void oneBasic() {
      basicHit++;
   }
   
   public void oneShrink() {
      shrinkHit++;
   }
   
   public void oneBounce() {
      bounceHit++;
   }
   
   public void oneSplit() {
      splitHit++;
   }
   
   public void oneMagic() {
      magicHit++;
   }
   
   public int getHits() {
      return basicHit + shrinkHit + bounceHit + splitHit + magicHit;
   }
   
   public void addScore(int p) {
      playerPoints += p;
   }
   
   public int getScore() {
      return playerPoints;
   }
   
  public void mostHitDecider() {
      if((basicHit > shrinkHit) && (basicHit > bounceHit) && (basicHit > splitHit)) {
         mostHit = "basic";
      } else if((shrinkHit > bounceHit) && (shrinkHit > splitHit) && (shrinkHit > basicHit) && (shrinkHit > magicHit)) {
         mostHit = "shrink";
      } else if ((bounceHit > splitHit) && (bounceHit > basicHit) && (bounceHit > shrinkHit) && (bounceHit > magicHit)) {
         mostHit = "bounce";
      } else if ((splitHit > basicHit) && (splitHit > shrinkHit) && (splitHit > bounceHit) && (splitHit > magicHit)) {
         mostHit = "split";
      } else if ((magicHit > basicHit) && (magicHit > shrinkHit) && (magicHit > bounceHit) && (magicHit > splitHit)) {
         mostHit = "magic";
      } else {
         mostHit = "tie";
      }
   }
}