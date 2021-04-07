public class Member extends Person{
    private int id;

    public Member(){
        super();
        this.id = (int)Math.floor(Math.random()*100);
    }

    public Member(String name,int id){
        super(name);
        this.id = id;
    }
    public int getId(){
        return this.id;
    }
}