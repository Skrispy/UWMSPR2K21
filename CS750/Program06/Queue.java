public class Queue extends DynArray{

    public Queue(){
        super();
    }

    public int size(){
        return this.elements();
    }
    public boolean isEmpty(){
        return this.size() == 0;
    }

    public void que(double value){
        this.insert(value);

    }
    public double deQue(){
    	int i = 0;
        return this.removeAt(i);
     
    }
    public void queueDump(){
        for(int i = 0;i<this.size();i++)
        {
            System.out.println(this.at(i)); 
        }
    }


}