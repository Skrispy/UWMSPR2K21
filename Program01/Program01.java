

public class Program01{

    public static void main(String [] args){
        String [] numberDeck = new String [52];

        static {
        numberDeck = {"1S","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","1D","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","1H","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","1C","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC"}; 
        };

        boolean[] myDeck = new boolean[52];
        final int cardsPerRow = 8;
        int cardsThisRow = 0;
        int myCard;
        initDeck(myDeck);
        System.out.println("\nHere is a shuffled deck ...\n");
        while (!emptyDeck(myDeck)){
            myCard = dealCard(myDeck);
            ++cardsThisRow;
            if (cardsThisRow <= cardsPerRow)
            {
                printCard(myCard);
                System.out.print("  ");
            }else{
                System.out.println("");
                cardsThisRow = 1;
                printCard(myCard);
                System.out.print("  ");
            }}
            System.out .println('\n');
    }

    public static void initDeck(boolean [] deck){
       for(int i = 0; i < deck.length; i++){
           deck[i] = true;
       }
    }
    public static boolean emptyDeck(boolean [] deck){
        for(int i = 0; i < deck.length; i++){
            if(deck[i] == true){
                return false;
            }
        }
        return true;
    }
    public static int dealCard(boolean [] deck){
        int cardNum = (int)Math.floor(Math.random() * 52);
        while(deck[cardNum] != true){ 
            cardNum = (int)Math.floor(Math.random() * 52);

        }
        deck[cardNum] = false;
        return cardNum;
     }
    public static void printCard(int card){
        //why am i initializing this variable every time the method is called?
        System.out.print(numberDeck[card]);
        
    }
}