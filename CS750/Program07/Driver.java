import javax.swing.plaf.basic.BasicInternalFrameTitlePane.SystemMenuBar;

public class Driver{
    public static void main(String [] args){
        Member mem1 = new Member("GUy1",12314);
        Member mem2 = new Member("GUy2",22314);
        Member mem3 = new Member("GUy3",42314);
        Member mem4 = new Member("GUy4",12514);
        Member mem5 = new Member("GUy5",22644);
        Leader leader1 = new Leader("Sammy",234,1);
        Leader leader2 = new Leader("Ham",134,3);
        Org org1 = new Org(leader1,"Magic the Gathering Party");
        Org org2 = new Org(leader2,"Emo Boy Band");
        org1.addMember(mem1);
        org2.addMember(mem1);
        org1.addMember(mem2);
        org2.addMember(mem4);
        org2.addMember(mem5);
        org1.addMember(mem4);
        org1.addMember(mem3);
        System.out.println(org1.toString());
        System.out.println(org2.toString());
    }
}