public class Card{

    private String suit;
    private int rank;

    public Card(){
        this.suit = "Clubs"
        this.rank = 0;
    }

    public Card (int r, String s){
        s = s.substring(0, 1).toUpperCase() + s.substring(1);

        if(s == "Club" || s == "Diamond" || s == "Spade" ||s == "Heart"){
             if(r < 0 && r>14){
                 this.suit = s;
                  this.rank = r;
             }
          }
    }

    public String toString(){
        String rank;
        if(this.rank == 1){
            rank = "Ace";
        } else if(this.rank == 11){
            rank = "Jack";
        } else if(this.rank == 12){
            rank = "Queen";
        } else if(this.rank == 13){
            rank = "King";
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
        if(guest.suit == this.suit && guest.rank == this.rank){
            return true;
        } else{
            return false;
        }
    }

}