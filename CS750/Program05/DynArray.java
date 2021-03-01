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
        double arrHold = new double[sizeDub];
        for(int x = 0; x < arraySize(); x++){
            arrHold[x] = this.array[x];
        }
        this.array = arrHold;
        this.size = sizeDub;
        this.nextIndex = sizeDub-1;
    }

    private void shrink(){
        int sizeHalf = arraySize()/2;
        this.array = new double[sizeHalf];
        this.size = sizeHalf;
        this.nextIndex = sizeHalf-1;
    }

    public void insertAt(int index, double value){
        if(0<=index && index <=nextIndex){
            if(index == nextIndex){
                grow();
            }
            for(int x = index; x < arraySize();x++){
                double hold = at(index);
                this.array[x]=value;
                this.array[x+1]
            }
        }
    }
    
    public void insert(double value){
        this.array[this.nextIndex] = value;
    }
    public double removeAt(int index){

    }





}