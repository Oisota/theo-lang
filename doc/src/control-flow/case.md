# Case Expressions
Case expressions will be used to pattern match over data types and other data structures.
The compiler will check to ensure all cases of a pattern are handled by the expressions.
All logical branching will be done with case expressions since the language will not have tradition if/else expressions.
This decision was inspired by [Gleam](https://gleam.run/book/tour/case-expressions.html) which only has case expressions as well.

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

Fibonacci function example:
```
fun fib(n int) int {

	case n {
		0 => 0,
		1 => 1,
		n => recur(n - 1) + recur(n - 2)
	}

	// alternate way of writing it, slightly shorter
	case n == 0 or n == 1 {
		True => n,
		False => recur(n - 1) + recur(n - 2)
	}
}
```