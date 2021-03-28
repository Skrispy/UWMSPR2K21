package CS750.Program06;
public class DynArray{
    private double [] array;
    private int size;
    private int nextIndex;

    public DynArray(){
        this.array = new double[1];
        this.size = 1;
        this.nextIndex = 0;

    }
    public int arraySize(){
        return this.size;
    }
    public int elements(){
        return this.nextIndex;
    }
    public double at(int index){
        if(0<=index && index<nextIndex){
            return array[index];
        }else{
            return Double.NaN;
        }
    }
    private void grow(){
        int sizeDub = arraySize()*2;
        double [] arrHold = new double[sizeDub];
        for(int x = 0; x < elements(); x++){
            arrHold[x] = this.array[x];
        }
        this.array = arrHold;
        this.size = sizeDub;
    }

    private void shrink(){
        int sizeHalf = arraySize()/2;
        double [] arrHold = new double[sizeHalf];
        for(int x = 0; x < elements(); x++){
            arrHold[x] = this.array[x];
        }
        this.array = arrHold;
        this.size = sizeHalf;
    }

    public void insertAt(int index, double value){
        if(0<=index && index <=elements()){
            if(elements() == arraySize()){
                grow();
            }
            double hold = at(index);
            this.array[index] = value;
            this.nextIndex++;
            for(int x = index+1; x < elements();x++){
                this.array[x] = hold;
                hold = at(x);
            }
            
        }
    }
    public void insert(double value){
        insertAt(elements(),value);
    }
    public double removeAt(int index){
        if(0<=index && index <=elements()){
            double hold = at(index);
            for(int x = index + 1; x < elements();x++){
                this.array[x] = at(x);
                hold = at(x);
            }
            this.nextIndex--;
            if(arraySize()/2 > elements()){
                shrink();
            }
            return hold;
        }
        return Double.NaN;
    }
    public double remove(){
        return removeAt(elements()-1);
    }

    public void printArray(){
        for(int x = 0; x<elements();x++){
            System.out.println(at(x));
        }
            
    }








}