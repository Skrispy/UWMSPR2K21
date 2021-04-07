import javax.swing.plaf.basic.BasicInternalFrameTitlePane.SystemMenuBar;

public class Driver{
    public static void main(String [] args){
        Leader leader1 = new Leader("Sammy",234,1);
        Leader leader2 = new Leader("Ham",134,3);
        Org org1 = new Org(leader1,"Magic the Gathering Party");
        Org org2 = new Org(leader2,"Emo Boy Band");
        System.out.println(org1.toString());
        System.out.println(org2.toString());
    }
    }
}