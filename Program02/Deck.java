public class Deck {
    
    private boolean[] deck = new boolean[52];

 
    public void initDeck(){

       for(int i = 0; i < this.deck.length; i++){
           this.deck[i] = true;
       }    

    }
    public boolean emptyDeck(){
        for(int i = 0; i < deck.length; i++){
            if(this.deck[i] == true){
                return false;
            }
        }
        return true;
    }

    public int dealCard(){
        int cardNum = (int)Math.floor(Math.random() * 52);
        while(this.deck[cardNum] != true){ 
            cardNum = (int)Math.floor(Math.random() * 52);
        }
        this.deck[cardNum] = false;
        return cardNum;
     }
    public static String cardToString(int card){
        String [] deckValue = new String [60];
        String [] suits = {"D","S","C","H"};
        String [] rank = {"A","1","2","3","4","5","6","7","8","9","10","J","Q","K"};
        int p = 0;
        for(int i = 0; i<suits.length;i++){
            for(int j = 0; j<rank.length;j++){
                deckValue[p] = rank[j] + suits[i];
                p++;
            }
        }
    	return deckValue[card];
        
    }

}