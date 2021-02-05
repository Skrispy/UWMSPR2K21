
public class DeckDriver{
    public static void main(String [] args){

        final int cardsPerRow = 8;
        int cardsThisRow = 0;
        Deck myDeck = new Deck();
        SmartDeck smartDeck = new SmartDeck();
        

        smartDeck.initDeck();
        myDeck.initDeck();
        
        System.out.println("A run with Deck\n----------");
        
        System.out.println("\nHere is a shuffled deck ...\n");
        
        
        while (myDeck.emptyDeck() == false){
        	int card = myDeck.dealCard();

            ++cardsThisRow;
            if (cardsThisRow <= cardsPerRow)
            {
                System.out.print(Deck.cardToString(card));
                System.out.print("  ");
            }else{
                System.out.println("");
                cardsThisRow = 1;
                System.out.print(Deck.cardToString(card));
                System.out.print("  ");
            }}
            System.out .println('\n');
            
        System.out.println("A run with SmartDeck\n----------");
        System.out.println("\nHere is a shuffled deck ...\n");
        cardsThisRow = 0;
        while (smartDeck.emptyDeck() == false){
        	int card = smartDeck.dealCard();

            ++cardsThisRow;
            if (cardsThisRow <= cardsPerRow)
            {
                System.out.print(SmartDeck.cardToString(card));
                System.out.print("  ");
            }else{
                System.out.println("");
                cardsThisRow = 1;
                System.out.print(SmartDeck.cardToString(card));
                System.out.print("  ");
            }}
            System.out .println('\n');
        
       }

    
 }
