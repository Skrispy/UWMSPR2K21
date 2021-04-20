
public class DriverL8
{
  public static void main(String[] args)
  {
    Nat n1 = new Nat();
    Nat n2 = new Nat(7);
    Nat n3 = new Nat(n2);
    Nat n4 = (Nat)n1.clone();
    Nat n5 = new Nat(-2);
    System.out.println("n1 = " + n1);
    System.out.println("n2 = " + n2);
    System.out.println("n3 = " + n3);
    System.out.println("n4 = " + n4);
    System.out.println("n5 = " + n5);
    
    System.out.println();
    
    Nat no1 = new Oct();
    Nat no2 = new Oct(7);
    Nat no3 = new Oct((Oct)no2);
    Nat no4 = (Oct)no1.clone();
    Nat no5 = new Oct(10);
    System.out.println("no1 = " + no1);
    System.out.println("no2 = " + no2);
    System.out.println("no3 = " + no3);
    System.out.println("no4 = " + no4);
    System.out.println("no5 = " + no5);
    
    System.out.println();
    
    if (!no1.equals(n1))
      System.out.println("Good: Oct can not equal Nat");
    if (no1.equals(no4))
      System.out.println("Good: Oct.clone() works");
    if (no2.equals(no3))
      System.out.println("Good: Oct(Oct o) works");
    
    System.out.println();
    System.out.println("n2 + n3 = " + n2.addition(n3));
    
    System.out.println();

    n1.decrement();
    n2.increment();
    n3.zero();
    System.out.println("n1 = " + n1);
    System.out.println("n2 = " + n2);
    System.out.println("n3 = " + n3);

    System.out.println();
    
    System.out.println("no5 inverse = " + ((Oct)no5).inverse());
    System.out.println("no2 + no5 = " + no2.addition(no5));
    System.out.println("no2 - no5 = " + no2.addition(((Oct)no5).inverse()));
    
    System.out.println();
    
    no1.decrement();
    no2.increment();
    no3.zero();
    System.out.println("no1 = " + no1);
    System.out.println("no2 = " + no2);
    System.out.println("no3 = " + no3);
  }
}
