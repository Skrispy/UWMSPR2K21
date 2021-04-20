public class CountByThree extends Root implements OtherCount
{
  public CountByThree()
  {
    super();
  }
  
  public CountByThree(Root guest)
  {
    super.setData(guest.getData());
  }
 
  public String toString()
  {
    return this.incrementor() + super.toString();
  }

  public void inc()
  {
    super.setData(super.getData() + OtherCount.BY_THREE);
  }
  
  public String incrementor()
  {
    return "By Three : ";
  }
}