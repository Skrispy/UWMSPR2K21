import java.util.ArrayList;

public class BitString{
    // an ordered sequence of bits
    private ArrayList<AbstractBit> bitString;
    private void setAbstractBitList(ArrayList<AbstractBit> bitList){
        this.bitString = bitList;
    }
    protected ArrayList<AbstractBit> getAbstractBitList(){
        return this.bitString;
    }
    // adds a bit to the end of the arrayList of bits
    public void addBit(AbstractBit bit){
        this.bitString.add(0,bit);
    }
    // returns a reference to the bit at location loc in the ArrayList of bits
    public AbstractBit bitAt(int loc){
        if(!isEmpty())
            return this.bitString.get(loc - 1);
        else
            return BinaryBit.zero;

    }
    public BitString(){
        this.bitString = new ArrayList<AbstractBit>;
    }
    protected BitString(ArrayList<AbstractBit> bitList){
        setAbstractBitList(bitList);
    }
    public BitString(BitString guest){
        setAbstractBitList((ArrayList<AbstractBit>)guest.bitString.clone());
    }
    public boolean isEmpty(){
        return bitString.size() == 0;
    }
    public int length(){
        return bitString.size();
    }
    public BitString clone(){
        return new BitString(this);
    }
    public boolean equals(BitString guest){
        if(this.bitString.size() == guest.length()){
            for(int i = 1; i < this.bitString.size();i++){
                return(bitAt(i).equals(guest.bitAt(i)));
            }
            
        }
        return false;
    }
    public String toString(){
        if(this.bitString.isEmpty()){
            return BinaryBit.zero.toString();
        }
        else{
            String hold = "";
            for(AbstractBit x : bitString){
                hold += x;
            }
            return hold;
        }
    }
}