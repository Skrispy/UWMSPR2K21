public class DeckDriver{
    public static void main(String [] args){
        
        Deck deck = new Deck();
        deck.shuffleDeck();

        System.out.println("\nHere is a Shuffled Deck\n***********************\n");
        
        while(!deck.isEmptyDeck()){
            Card hold = deck.dealCard();
            System.out.println(hold.toString());
        }
        System.out.println("\n***********************\n");
    }
}