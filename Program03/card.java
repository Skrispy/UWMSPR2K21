public class Card {

    private String suit;
    private int rank;

    public Card(){
        this(1,"Club");
    }

    public Card (int r, String s) {
        this.setRank(r);
        this.setSuit(s);
    }

    public int getRank(){
        return this.rank;
    }
    public String getSuit(){
        return this.suit;
    }

    private void setRank(int r){
        if(r > 0 && r<14){
            this.rank = r;
        } 
    }

    
    private void setSuit(String s){
        s = s.substring(0, 1).toUpperCase() + s.substring(1);
        if(s.equals("Club") || s.equals("Diamond") || s.equals("Spade") ||s.equals("Heart")){
            this.suit = s;
        }
    }

    public String toString(){
        String rankStr = "";
        int rank = this.getRank();
        if(rank > 0 && rank<14 && this.getSuit() != null){
         
            if(rank == 1){
               rankStr = "Ace";
            } else if(rank == 11){
                rankStr = "Jack";
            } else if(rank == 12){
                rankStr = "Queen";
            } else if(rank == 13){
                rankStr = "King";
            } else {
                rankStr = String.valueOf(rank);
            }
            
            return rankStr + " of " + this.getSuit();
         }
         return rankStr;
    }

    public Card clone(){
        Card card = new Card();
        card.suit = this.getSuit();
        card.rank = this.getRank();
        return card;
    }
    
    public boolean equals(Card guest){
        if(guest.suit.equals(this.getSuit()) && guest.rank == this.getRank()){
            return true;
        } else{
            return false;
        }
    }

}