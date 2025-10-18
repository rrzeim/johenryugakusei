using System;
using System.Threading;

class Program {
  static void Main() {
    Console.WriteLine("BS ECE 1-2 DEMO");
    for (int i = 10; i > -1; i--) {
      Console.WriteLine(i);
      Thread.Sleep(1000);

    }
  }
}