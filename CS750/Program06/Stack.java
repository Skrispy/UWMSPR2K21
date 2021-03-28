package CS750.Program06;

public class Stack extends DynArray{

    public Stack(){
        super();
    }
    public int size(){
        return this.arraySize();
    }
    public boolean isEmpty(){
        return this.arraySize() == 0;
    }

    public void push(double value){
        this.insert(value);
    }
    public double pop(){
        if(!isEmpty()){
            return this.remove();
        }
        return Double.NaN;
    }
    public void stackDump(){
        for(int i = this.size();i>=0;i--){
            System.out.println(this.at(i)); 
        }
    }


}