public class Binary extends BitString{
    private BitString bits;
    public Binary(){
        this.bits = new BitString();
        bits.addBit(BinaryBit.zero);
    }
    // encode a non-negative (base 10) number val such into
    // the host’s bitstring - used in the 
    
    Binary(long val){
        this.bits = new BitString();
        encode(val);
    }
    private void encode(long val){
        while(val>0){
            int x = (int)val%2;
            val = val/2;
            this.bits.addBit(new BinaryBit(x));
        }
    }
    
    public Binary(BitString guest){
        this.bits = guest.clone();
    }
    public Binary(Binary guest){
        this(guest.bits);
    }
    public Binary clone(){
        return new Binary(this);
    }
    // return a new Binary number that is the result of adding the
    // host bitstring to the guest bitstring under then assumption
    // that both are representing (base 2) numbers
    public Binary addition(Binary guest){
        int l1 = bits.length();
        int l2 = guest.length();
        AbstractBit hold = BinaryBit.zero;
        AbstractBit sum;
        BitString res = new BitString();
        AbstractBit b1,b2;
        
        while(l1>0 || l2>0){
            if(l1 == 0){
                b1 = BinaryBit.zero;
            }else{
                b1 = bitAt(l1--);
            }
            if(l2 == 0){
                b2 = BinaryBit.zero;
            }
            else{
                b2 = guest.bitAt(l2--);
                sum = b1.addBits(hold,b2);
            }
            hold = b1.carryBit(hold, b2);

            res.addBit(sum);

        }
        if(hold.equals(BinaryBit.one)){
            res.addBit(hold);
        }
        return new Binary(res);

    }
}