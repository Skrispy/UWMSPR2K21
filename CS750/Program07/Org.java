import java.util.ArrayList;

public class Org{
    private String name;
    private Leader leader;
    private ArrayList <Member> members = new ArrayList <Member>();
    public Org(){
        super();
        name = "";
        leader = new Leader();
    }
    public Org(Leader leader, String name){
        this.leader = leader;
        this.name = name;

    }
    public void addMember(Member member){
        members.add(member);
    }
    public String getOrg(){
        return this.name;
    }
    public Leader getLeader(){
        return this.leader;
    }

    public String toString(){
        String orgInfo = "Org name: "+ this.getOrg();
        String leaderInfo = "Leader name: " + leader.getName() +" Leader term: " + Integer.toString(leader.getTerm()) + " Leader id: " + Integer.toString(leader.getId());
        String memberInfo = "Members List: ";
        for(Member member: members){
            String name = member.getName();
            String id = Integer.toString(member.getId());
            memberInfo += "name: " + name + " id: " + id + ", ";
        }

        return orgInfo + leaderInfo + memberInfo;   
    }
}