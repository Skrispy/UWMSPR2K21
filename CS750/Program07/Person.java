public class Person{
    private String name;
    
    public Person(){
        this("");
    }
    public Person(String name){
        this.name = name;
    }

    public String getName(){
        return this.name;
    }
}
