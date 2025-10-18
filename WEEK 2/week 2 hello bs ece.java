public class myfirstcode {
  public static void main(String[] args) {
    System.out.println("BS ECE 1-2 demo");
    for (int i = 10; i > -1; i--) {
      System.out.println(i);
      try {
        Thread.sleep(1000);
      } catch (InterruptedException ex) {}
    }
  }
}


from time import sleep


   