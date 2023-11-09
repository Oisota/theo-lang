# Key

The key type will be like a constant string that is replaced at compile time.
It will take the place of using strings as keys.
Still deciding on a notation. (#foo :foo $foo @foo)
Leaning towards `#foo` as the symbol is already called `hash` and the symbols will likely turn into hashes at compile time anyway.

```text
x.at(#foo) = 5
```