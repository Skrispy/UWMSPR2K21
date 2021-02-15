public class Card {

    private String suit;
    private int rank;

    public Card(){
        this.suit = "Clubs";
        this.rank = 1;
    }

    public Card (int r, String s) {
        s = s.substring(0, 1).toUpperCase() + s.substring(1);
        

        if(s.equals("Club") || s.equals("Diamond") || s.equals("Spade") ||s.equals("Heart")){
             if(r > 0 && r<14){
                 this.suit = s;
                  this.rank = r;
             }
          }
    }

    public String toString(){
        String rank = "";
        if(this.rank == 1){
            rank = "Ace";
        } else if(this.rank == 11){
            rank = "Jack";
        } else if(this.rank == 12){
            rank = "Queen";
        } else if(this.rank == 13){
            rank = "King";
        } else{
            rank = String.valueOf(this.rank);
        }
        String s = this.suit;
        return rank + " of " + s;
    }

    public Card clone(){
        Card card = new Card();
        card.suit = this.suit;
        card.rank = this.rank;
        return card;
    }
    
    public boolean equals(Card guest){
        if(guest.suit.equals(this.suit) && guest.rank == this.rank){
            return true;
        } else{
            return false;
        }
    }

}