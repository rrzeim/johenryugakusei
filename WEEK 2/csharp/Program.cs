using System;
using System.Threading;

class Program {
  static void Main() {
    Console.WriteLine("BS ECE 1-4 DEMO");
    for (int x = 10; x > -1; x--) {
      Console.WriteLine(x);
      Thread.Sleep(1000);

    }
  }
}
 