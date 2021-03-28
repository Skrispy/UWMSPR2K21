package CS750.Program06;

public class Queue extends DynArray{

    public Queue(){
        super();
    }

    public int size(){
        return this.arraySize();
    }
    public boolean isEmpty(){
        return this.arraySize() == 0;
    }

    public void que(double value){
        this.insertAt(0,value);
    }
    public double deQue(){
        if(!isEmpty()){
            return this.remove();
        }
        return Double.NaN;
    }
    public void queueDump(){
        for(int i = 0;i<this.size();i++)
        {
            System.out.println(this.at(i)); 
        }
    }


}