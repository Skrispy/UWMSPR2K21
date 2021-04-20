public class Oct extends Nat implements Mod8{


    //setter
    protected void setN(int n){
        if(n>=0)
            super.setN(n%MODULUS);
        else
            super.setN(0);
    }
    //constructors
    public Oct(){
        this(0);
    }
    public Oct(int n){
        this.setN(n);
    }
    public Oct(Oct guest){
        this(guest.getN());
    }
    //clone
    public Object clone(){
        return new Oct(this);
    }
    //overridden methods
    public boolean equals(Object guest){
        if ((guest == null) || !(guest instanceof Oct))
            return false;
        if (((Oct)guest).getN() != this.getN())
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
        else
            this.setN(7);
    }
    public Nat addition(Nat guest)
    {
      return new Oct(this.getN() + guest.getN());
    }
    //implemented method
    public Nat inverse(){
        return new Oct(MODULUS-this.getN());
        
    }

}
