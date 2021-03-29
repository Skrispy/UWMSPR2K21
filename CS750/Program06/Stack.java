public class Stack extends DynArray{

    public Stack(){
        super();
    }
    public int size(){
        return this.elements();
    }
    public boolean isEmpty(){
        return this.size() == 0;
    }

    public void push(double value){
        this.insert(value);
    }
    public double pop(){
        return this.remove();
    }
    public void stackDump(){
        for(int i = this.size()-1;i>=0;i--){
            System.out.println(this.at(i)); 
        }
    }


}