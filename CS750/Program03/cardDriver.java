public class CardDriver{
    public static void main(String [] args) {
        //declare array
        Card [] cards = new Card[52];

        //test invalid card
        Card test = new Card(999,"pig");
        System.out.println(test.toString());
        
        //deck instantiation
        String [] suits = {"Diamond","Spade","Club","Heart"};
        int p = 0;
        for(int i = 0; i<suits.length;i++){
            for(int j = 1; j<14;j++){
                cards[p] = new Card(j,suits[i]);
                p++;
            }
        }
        //index swapper
        for(int i = 0; i < 100; i++){
            int rand1 = (int)Math.floor(Math.random()*52);
            int rand2 = (int)Math.floor(Math.random()*52);
            Card cardHold = cards[rand1].clone();
            cards[rand1] = cards[rand2].clone();
            cards[rand2] = cardHold.clone();

        }

        //print deck + find queen
        int queenIndex = 0;
        Card queen = new Card(12,"club");
        System.out.println("Here is a Shuffled Deck\n***********************\n");
        
        for(int i = 0; i < cards.length; i++){
            if(cards[i].equals(queen)){
                queenIndex = i;
            }
           System.out.println(cards[i].toString());
        }
        //print queen
        System.out.println("\n***********************\n");
        System.out.println("The " + cards[queenIndex].toString() + "s is at index " + queenIndex);
        
        
    }
}