Might make sense to not implement booleans in the language as primitives since they can just created as enums:

```text
// file: std/bool.theo

enum Bool { true, false }

// can even have more common choices in std/bool
enum OnOff { On, Off }
enum YesNo { Yes, No }
enum UpDown { Up, Down }
```