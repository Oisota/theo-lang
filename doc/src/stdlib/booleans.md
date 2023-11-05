# Booleans

Might make sense to not implement booleans in the language as primitives since they can just created as enums:

```text
// file: std/bool.theo

enum Bool { true, false }

// can even have more common choices in std/bool
enum Toggle { On, Off }
enum Answer { Yes, No }
enum UpDown { Up, Down }
enum PosNeg { Positive, Negative }
enum Voltage { Hi, Lo }
```

I am thinking it might be nice to facilitate using booleans other than true/false depending on the context.
Might make for more readable code.
For example feature flags might make more sense as either `On` or `Off` instead of `True` and `False`.
Will need to decide how this interacts with `if`/`else` expressions.
Maybe if expressions can work with any enum that has only 2 choices and assumes the first choice is the "truthy" value.
Need to think on this, could be abused.
Maybe limit if expressions to only work with values defined in `std/bool`.

If/Else can just be syntax sugar of case expressions.