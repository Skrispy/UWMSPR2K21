
public class Nat
{
  private int n;
  
  protected void setN(int n)
  {
    if (n >= 0)
      this.n = n;
    else
      this.n = 0;
  }

  public int getN()
  {
    return this.n;
  }
  
  public Nat()
  {
    this(0);
  }
  
  public Nat(int n)
  {
    super();
    this.setN(n);
  }
  
  public Nat(Nat guest)
  {
    this(guest.getN());
  }
  
  public Object clone()
  {
    return new Nat(this);
  }
  
  public boolean equals(Object guest)
  {
    if ((guest == null) || !(guest instanceof Nat))
      return false;
    if (((Nat)guest).getN() != this.getN())
      return false;
    
    return true;
  }
  
  public String toString()
  {
    return "" + this.getN();
  }
  
  public void zero()
  {
    this.setN(0);
  }
  
  public void increment()
  {
    this.setN(this.getN() + 1);
  }
  
  void decrement()
  {
    if (this.getN() != 0)
      this.setN(this.getN() - 1);
  }
  
  public Nat addition(Nat guest)
  {
    return new Nat(this.getN() + guest.getN());
  }
}
