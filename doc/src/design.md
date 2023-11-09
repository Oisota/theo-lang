# Language Design

*Note: A lot of these docs are incomplete and contain my thoughts (ramblings) on how things could or should work.*
*There's a range of some things being set in stone and some things being still decided upon.*
*Just wanted to emphasize the rough draft status of the docs.*

## Small
The language must be extremely small and easy to understand.
The entire language and its inner workings must be able to be kept in one's head (For ex. 'C').
It should have slightly more syntax than lisp.
The language should be completely separate from its standard library.
Nothing is baked in from the start.
Extra functionality is added as needed.

## Extensible
The language must be able to be easily extended, ideally using its own features, but new features and libs should be able to be written in any language.
The language should easily communicate with other languages.
If a feature isn't present, implementing it yourself should be straightforward.

## Specification
The grammar for the language will be formally specified using E.B.N.F.
This should be no more than 1-2 pages in length.

## Problem Domains
The language will most likely be best suited towards scripting and applications programming.
Systems programming would be fairly difficult, although, an extension library may alleviate this.
The language should be fairly general purpose. 
Extensions and Libraries should be able to be added to the language in order to tackle most problem domains.

## Programming Paradigms
The language will be an expression based language.
It will support mainly a mix of functional and procedural/imperative programming, favoring the functional approach.
This should be considered when building the standard library and how built-in data structures should operate.

## Implementation
I'm thinking that it will be easiest to have the language compile to C source code similar to how Nim works.
This will make it easy to generate a standalone executable and will allow the language to run anywhere that has a C compiler.
Can also piggy-back off C libraries easily.

The types of expressions will be inferred and will rarely need to be stated explicitly.
Type annotations may be used if the user feels they make the code clearer or if the compiler can't infer the type.
Function signatures must always be specified.
Programs won't compile unless they type check.

Should there be a distinction between primitives and other types? (structs/funcs/collections/etc).
Need to think about how high level the language should be.
Could be like python where everything is an object, in this case a struct.
This might make low level stuff harder to implement.
Need to think on this...
Currently leaning towards have a some primitive types that all of literal syntax and everything else being a higher level data structure.