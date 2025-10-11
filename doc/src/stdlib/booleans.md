# Booleans

Might make sense to not implement booleans in the language as primitives since they can just created as enums:

```text
// file: std/bool.theo

enum Bool { True, False }

// can even have more common choices in std/bool
enum Toggle { On, Off }
enum Answer { Yes, No }
enum UpDown { Up, Down }
enum LeftRight { Left, Right }
enum PosNeg { Positive, Negative }
enum Voltage { Hi, Lo }
```

I am thinking it might be nice to facilitate using booleans other than true/false depending on the context.
Might make for more readable code.
For example feature flags might make more sense as either `On` or `Off` instead of `True` and `False`.

Need to think about how this would work the comparison operators.
I think each numeric type would need to define comparison methods for each operators (dunder methods) and these can return bools.