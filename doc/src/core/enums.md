# Enumerations

Enumerations can be defined and used like so:

```text
enum Bool { True, False }
enum Suit { Spade, Club, Heart, Diamond }
enum Rank { One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King }

let card = Card(
	rank=Rank.Three,
	suit=Suit.Spade
)
```

Optional values for the enum fields can be added like so:

```text
enum BitOptions {
	FOO = 0b0000
	BAR = 0b1000
	BAT = 0b0100
	BAM = 0b0010
}
```