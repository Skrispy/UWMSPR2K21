public class Deck{
        
        private Card [] cards = new Card[52];
        private int cardsDealt;

        public Deck(){
            String [] suits = {"Diamond","Spade","Club","Heart"};
            int p = 0;
            for(int i = 0; i<suits.length;i++){
                for(int j = 1; j<14;j++){
                    cards[p] = new Card(j,suits[i]);
                    p++;
                }
            }
            collectCards();
        }

        public int getCardsDealt(){
            return this.cardsDealt;
        }

        private void setCardsDealt(int j){
            this.cardsDealt = j;
        }

        public boolean isEmptyDeck(){
            return getCardsDealt() == 52;
        }

        public void collectCards(){
            setCardsDealt(0);
        }        

        public Card dealCard(){
            if(!isEmptyDeck()){
                int cardLoc = getCardsDealt();
                setCardsDealt(cardLoc + 1);
                return cards[cardLoc];
            } else {
                return null;
            }
        }
        public void shuffleDeck(){
            shuffleDeck(100);
        }

        public void shuffleDeck(int cuts){
            for(int i = 0; i < cuts; i++){
                int rand1 = (int)Math.floor(Math.random()*52);
                int rand2 = (int)Math.floor(Math.random()*52);
                Card cardHold = cards[rand1].clone();
                cards[rand1] = cards[rand2].clone();
                cards[rand2] = cardHold.clone();
            }
        }
        
}
