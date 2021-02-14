public class CardDriver{
    public static void main(String [] args) {

        Card [] cards = new Card[52];
        int cardsDealt = 0;

        String [] suits = {"Diamond","Spade","Club","Heart"};

        int p = 0;
        for(int i = 0; i<suits.length;i++){
            for(int j = 1; j<14;j++){
                cards[p] = new Card(j,suits[i]);
                p++;
            }
        }

        for(int i = 0; i < cards.length; i++){
           System.out.println(cards[i].toString());
        }
        
        
    }
}