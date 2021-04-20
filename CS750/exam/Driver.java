import java.util.ArrayList;

public class Driver
{
  public static void main(String[] args)
  {
    ArrayList<Root> myList = new ArrayList<>();
    CountByTwo c2 = new CountByTwo();
    CountByThree c3 = new CountByThree();
    System.out.println(c2.equals(c3));

    for (int i = 0; i < 4; ++i)
    {
      if (i % 2 == 0)
      {  
        myList.add(new CountByTwo());
        System.out.println("New ByTwo created");
      }
      else
      {
        myList.add(new CountByThree());
        System.out.println("New ByThree created");
      }
      
      for (Root listItem : myList)
      {
        System.out.println(listItem.toString());
        listItem.inc();
      }

      System.out.println();
    }
  }
}