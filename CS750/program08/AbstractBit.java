public abstract class AbstractBit{

private boolean bit;

public abstract AbstractBit clone();
public abstract AbstractBit addBits(AbstractBit guest);
public abstract AbstractBit addBits(AbstractBit guest1, AbstractBit guest2);
public abstract AbstractBit carryBit(AbstractBit guest);
public abstract AbstractBit carryBit(AbstractBit guest1, AbstractBit guest2);
protected void setBit(boolean value){
    this.bit = value;
}
public boolean getBit(){
    return this.bit;
}
public AbstractBit(){
    this();
}
public AbstractBit(boolean value){
    super();
    this.setBit(value);
}
public AbstractBit(AbstractBit guest){
    this(guest.getBit());
}
public boolean equals(AbstractBit guest){

    if ( guest == null )
    return false;
  if ( guest == this )
    return true;
  if ( !(guest instanceof AbstractBit)) 
    return false; 
  
  AbstractBit tg = (AbstractBit)guest;
  return this.getBit() == tg.getBit();
}
public String toString(){
    return ""+this.getBit();
}
}