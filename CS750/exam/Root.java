public abstract class Root
{
  private int data;
  
  public abstract void inc();
  
  public Root()
  {
    this.setData(0);
  }
  
  protected void setData(int data)
  {
    this.data = data;
  }

  public int getData()
  {
    return this.data;
  }
  
  public boolean equals(Object guest)
  {
    if (guest == null || !(guest instanceof Root))
      return false;
    else
      return this.getData() == ((Root)guest).getData();
  }
  
  public String toString()
  {
    return "" + this.getData();
  }
}