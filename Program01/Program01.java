

public class Program01{

    public static void main(String [] args){
        
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
    String [] suits = {"D","S","C","H"};
    String [] rank = {"A","1","2","3","4","5","6","7","8","9","10","J","Q","K"};
    String [] numberDeck = new String [60];
    int p = 0;
        for(int i = 0; i<suits.length;i++){
            for(int j = 0; j<rank.length;j++){
                numberDeck[p] = rank[j] + suits[i];
                p++;
            }
        }

        System.out.print(numberDeck[card]);
        
    }
}