# Language Design
## Overview
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

### Problem Domains
The language will most likely be best suited towards scripting and applications programming.
Systems programming would be fairly difficult, although, an extension library may alleviate this.
The language should be fairly general purpose. 
Extensions and Libraries should be able to be added to the language in order to tackle most problem domains.

### Programming Paradigms
The language will be an expression based language.
It will support mainly a mix of functional and procedural/imperative programming, favoring the functional approach.
This should be considered when building the standard library and how built-in data structures should operate.

### Implementation
I'm thinking that it will be easiest to have the language compile to C source code similar to how Nim works.
This will make it easy to generate a standalone executable and will allow the language to run anywhere that has a C compiler.
Can also piggy-back off C libraries easily.

## Design
### Types
The language will be statically typed and have the following built-in primitive types:
- Function (**fn**)
- Integer (**int**)
- Float (**float**)
- Char (**char**)
- Tuple (**tuple**)

**TODO:**
- figure which types will be primitives and which will be collections
- figure out how unsigned ints will be added and if different sizes should be supported like `i32`, `u8`, etc.

The types of expressions will be inferred and will rarely need to be stated explicitly.
Type annotations may be used if the user feels they make the code clearer or if the compiler can't infer the type.
Function signatures must always be specified.
Programs won't compile unless they type check.

See [Types](types.markdown) and [Core Modules](core_modules.markdown) for more detail.

Should there be a distinction between primitives and other types? (structs/funcs/collections/etc).
Need to think about how high level the language should be.
Could be like python where everything is an object, in this case a struct.
This might make low level stuff harder to implement.
Need to think on this...

### Type Synonyms
```text
type Point = Coord[int, int] // instantiate a generic type with concrete types
type Name = string
type MoneyAmount = (int, int)

let p = Point(5, 6)
let n:name = "Derek"
let d = MoneyAmount(5, 75)
```

### Variables
The `let` keyword will be used to bind a name to a value.
The bindings will be not be able to be changed once assigned and primitive values will be immutable.
Although the name binding may be immutable, changes to a mutable data structure will still be possible.

Variable declaration will look like:
```text
let x: string = 'Hello, World' //with type annotation
let a = 5 // with type inference
```

### If Else Expressions
Conditional branching will be expression based.
Each `if` expression will evaluate to a value.
Every `if` must have a corresponding `else`.

```text
let x = 5
let y = 8

if x == 10 { 'Foo' }
else if y == 9 { 'Bar' }
else { 'Bat' }
```

*Idea:* This may be best implemented as syntax sugar over case expressions.
This would simplify things since every if else can just be translated to its corresponding case expressions.
The above example would be translated to a nested case expression:

```text
case x == 10 {
	True => 'Foo',
	False => case y == 9 {
		True => 'Bar',
		False => 'Bat
	}
}
```

This would make sense since booleans wouldn't necessarily need to be built into the language.
They could just be a simple enum.

### Case Expressions
Case expressions will be used to pattern match over data types and other data structures.
The compiler will check to ensure all cases of a pattern are handled by the expressions.

```text
enum Option<a> {
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

let mycard = (Rank.Ace, Suit.Spade)
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
Having literal notation for data structures complicates the grammar needing special cases for various data
structures.
It also adds mental tax having to remember what each symbol means.
Would also need to overload the curly brackets to mean several different things: (blocks, dicts, sets).
Probably best to leave them out to make things more regular.

The only argument against removal of literals would be sequence access with square brackets being so ubiquitous it would hinder adoption since people are so used to it.
This could be alleviated somewhat with helper methods on sequences like `.first()`, `.second()`, `.last()`, etc methods for common use cases.
Removal of bracket notation could help incentivise using map/filter/reduce and using a different structure if non sequential access is needed.
Could also just provide a simple `.get(n: int)` or `.at(n: int)` method for indexed access.

Could also make all sequences callable such that you can just use parens where brackets are normally used.
I like this idea.


This could most likely be added later and we shouldn't worry about this for the initial implementation.

### Generics
Should generics use angle brackets like Java/C++/C# or square brackets?
```text
enum Option[A] {
	Some(A)
	None
}

enum Option<A> {
	Some(A)
	None
}
```
Leaning heavily towards square brackets.