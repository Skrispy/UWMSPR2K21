public class CountByTwo extends Root implements OtherCount
{
  public CountByTwo()
  {
    super();
  }
  
  public CountByTwo(Root guest)
  {
    super.setData(guest.getData());
  }
 
  public String toString()
  {
    return this.incrementor() + super.toString();
  }

  public void inc()
  {
    super.setData(super.getData() + OtherCount.BY_TWO);
  }
  
  public String incrementor()
  {
    return "By Two : ";
  }
}