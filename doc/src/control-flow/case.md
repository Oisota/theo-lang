# Case Expressions
Case expressions will be used to pattern match over data types and other data structures.
The compiler will check to ensure all cases of a pattern are handled by the expressions.

```text
union Option[a] {
    Some(a),
    None
}

let opt = Option.Some(5)

let result = case opt {
    Option.Some(value) => value,
    Option.None => 0
}

enum Suit { Diamonds, Spade, Club, Heart }
enum Rank { Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King }

struct Card {
	rank: Rank,
	suit: Suit
}

let c1 = Card(rank=Rank.Ace, suit=Suit.Spade)
let c1 = Card(
	rank=Rank.Ace,
	suit=Suit.Spade
)

let mysuit = case mycard {
    (Ace, Diamond) => 'Ace of Diamonds'
    (Ace, Spade) => 'Ace of Spades'
}
//above throws compiler error
```