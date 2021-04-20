package exam02;
public class Multiplicative extends Thing implements Invertable{

    //setter
    public Multiplicative(){
        super(0);
    }
    public Multiplicative(double n){
        super(n);
    }
    public Multiplicative(Multiplicative guest){
        super(guest.getValue());
    }
   //clone
   public Thing clone(){
       return new Multiplicative(this);
   }
   //overridden methods
   public boolean equals(Object guest){
       if ((guest == null) || !(guest instanceof Multiplicative))
           return false;
       if (((Multiplicative)guest).getValue() != this.getValue())
           return false;
     
       return true;
   }
   public String toString()
   {
     return MULTIPLICATIVE + " Inverse " + this.getInverse();
   }

   public double getInverse(){
       return (1 / this.getValue());
   }
}