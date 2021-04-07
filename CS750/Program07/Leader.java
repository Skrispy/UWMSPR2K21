public class Leader extends Member{
    private int term;
    public Leader(){
        super();
        this.term = 1;  
        
    }
    public Leader(String name, int id, int term){
        super(name,id);
        if(term>=1){
            this.term=term;
        }
    }
    public int getTerm(){
        return this.term;
    }
}