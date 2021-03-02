public class Die {
    //
    private static int instanceCount = 0;
    private int sideUp;
    

    public static int getDieCnt(){
        return Die.instanceCount;
    }
    private static void incDieCnt(int x){
        Die.instanceCount += x;
    }


    public Die(){
        this(1);
    }

    public Die(int x){
        setUpSide(x);
        Die.incDieCnt(1); 
    }

    public Die(Die x){
        this(x.getUpSide());
    }

    public Die clone(){
        return new Die(this);
    }

    public int getUpSide(){
        return this.sideUp;
    }

    private void setUpSide(int x){
        this.sideUp = x;
    }

    public boolean equals(Die x){
        return this.getUpSide() == x.getUpSide();
    }

}