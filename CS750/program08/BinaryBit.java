public class BinaryBit extends AbstractBit{

    public static final BinaryBit zero = new BinaryBit(false);
    public static final BinaryBit one = new BinaryBit(true);
    
    public BinaryBit(){
        super();
    }
    public BinaryBit(boolean bit){// allows construction with a boolean - false->0, true->1
        super(bit);
    }
    public BinaryBit(int bit){// allows construction with an int - should be 0 or 1
        super(bit == 1);
    }
    public BinaryBit(BinaryBit guest){
        super(guest);
    }
    public BinaryBit clone(){
        return new BinaryBit(this);
    }
    public boolean equals(BinaryBit guest){
        return super.equals(guest);
    }
    public String toString(){
        return super.toString();
    }    
    // returns the low order bit of adding the host bit to the guest bit
    public AbstractBit addBits(AbstractBit guest)
    {
        if(this.equals(one) && guest.equals(zero))
            return one;
        else
            return zero;
    }
    // returns the low order bit of adding the host bit, the guest1 bit, and the guest2 bit
    public AbstractBit addBits(AbstractBit guest1, AbstractBit guest2){
        AbstractBit add = guest1.addBits(guest2);
        return addBits(add);
    }
    // returns the high order bit of adding the host bit to the guest bit
    public AbstractBit carryBit(AbstractBit guest){
        if(this.equals(one) && guest.equals(one))
            return one;
        else
            return zero;
    }
    // returns the high order bit of adding the host bit to the guest bit
    public AbstractBit carryBit(AbstractBit guest1, AbstractBit guest2){
        int hold = 0;
        if(this.equals(BinaryBit.one))
            hold++;
        if(guest1.equals(BinaryBit.one))
            hold++;
        if(guest2.equals(BinaryBit.one))
            hold++;
        if(hold >= 2)
            return BinaryBit.one;
        else
            return BinaryBit.zero;
    }

}