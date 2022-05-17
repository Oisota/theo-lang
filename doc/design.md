Language Design
===============
Overview
--------
### Small
The language must be extremely small and easy to understand.
The entire language and its inner workings must be able to be kept in one's head (For ex. 'C').
It should have slightly more syntax than lisp.
The language should be completely separate from its standard library.
Nothing is baked in from the start.
Extra functionality is added as needed.

### Extensible
The language must be able to be easily extended, ideally using its own features, but new features and libs should be able to be written in any language.
The language should easily communicate with other languages.
If a feature isn't present, implementing it yourself should be straightforward.

### Specification
The grammar for the language will be formally specified using E.B.N.F.
This should be no more than 1-2 pages in length.
A skilled programmer should be able to reimplement the language at will, without much effort.
This will allow the language to be easily ported to other platforms.

### Problem Domains
The language will most likely be best suited towards scripting and applications programming.
Systems programming would be fairly difficult, although, an extension library may alleviate this.
The language should be fairly general purpose. 
Extensions and Libraries should be able to be added to the language in order to tackle most problem domains.

### Programming Paradigms
The language will be an expression based language.
It will support mainly a mix of functional and procedural/imperative programming, favoring the functional approach.
This should be considered when building the standard library and how built-in data structures should operate.

Design
------
### Types
The language will be statically typed and have the following built-in primitive types:
- Function (**fn**)
- Integer (**int**)
- Float (**float**)
- Char (**char**)
- Tuple (**tuple**)

**TODO:** figure which types will be primitives and which will be collections

The types of expressions will be inferred and will rarely need to be stated explicitly.
Type annotations may be used if the user feels they make the code clearer or if the compiler can't infer the type.
Programs won't compile unless they type check.

See [Types](types.markdown) and [Core Modules](core_modules.markdown) for more detail.

### Enumerations
Algebraic datatypes will be able to be defined as so:
```text
enum List<A> {
    Cons (A, List<A>),
    Nil
}

enum Bool { True, False }

enum Suit { Spade, Club, Heart, Diamond }
enum Rank { One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King }

//used like so
let mylist = List.Cons (5, List.Cons (6, List.Cons (7, List.Nil)))

let card = (Rank.Three, Suit.Spade)
```


### Type Synonyms/Named Tuples
```
type Point = (int, int)
type Name = string
type MoneyAmount = (int, int)

let p = Point (5, 6)
let n:name = 'Derek'
let d = MoneyAmount (5, 75)
```

### If Else Expressions
Conditional branching will be expression based.
Each `if` expression will evaluate to a value.
Every `if` must have a corresponding `else`.

```text
let x = 5, y = 8

if x == 10 { 'Foo' }
else if y == 9 { 'Bar' }
else { 'Bat' }
```

### Variables
The `let` keyword will be used to bind a name to a value.
The bindings will be not be able to be changed once assigned and primitive values will be immutable.
Although the name binding may be immutable, changes to a mutable data structure will still be possible.

Variable declaration will look like:
```text
let x:string = 'Hello, World' //with type annotation
let a = 5
```


### Case Expressions
Case expressions will be used to pattern match over data types and other data structures.
The compiler will check to ensure all cases of a pattern are handled by the expressions.

```text
enum Option<a> {
    Some a,
    None
}

let opt = Option.Some 5

let result = case opt {
    Option.Some value => value,
    Option.None => 0
}

enum Suit { Diamonds, Spade, Club, Heart }
enum Rank { Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King }

struct Card {
	rank: Rank,
	suit: Suit
}

let mycard = (Rank.Ace, Suit.Spade)
let c1 = Card { rank: Rank.Ace, suit: Suit.Spade }
let c1 = Card {
	rank = Rank.Ace,
	suit = Suit.Spade
}

let mysuit = case mycard {
    (Ace, Diamond) => 'Ace of Diamonds'
    (Ace, Spade) => 'Ace of Spades'
}
//above throws compiler error
```

### Module System
The module system will be file and directory based similar to how Python and Node.js do things.
A single file will be considered a "module" and a directory with a special index file (name for this file TBD) will be considered a package.
Under the hood, modules and packages will be transformed into structs with the top-level file contents being the members of the struct.

### Comments
'C' style inline and block comments will be supported.
```text
/*
    This is a comment
*/

//This is an inline comment
```

### Macros
Should the language have macros?
I'm debating on whether there should even be literal notation for dicts/lists/etc.
It might be easier from a grammar definition standpoint to have macros that would expand to create lists.
For example:
```text
let l1 = @list[1,2,3,4,5]
```
Would expand to:
```text
let l1 = list()
l1.add(1)
l1.add(2)
l1.add(4)
l1.add(4)
l1.add(5)
```