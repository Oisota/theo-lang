# Core Modules

These are the core modules that will be available:
## Core Data Type Modules
- Function
- Int
- Float
- Bool
- Char
- String
- Collections
	- List
	- Vector
	- Dict
	- Set
- Mut
- Option
- Result

## Other Modules
- math
- io
- regex
- file
- os
- sys
- crypto
- socket
- http
- concurrency

Not sure if excluding all modules by default is a good idea.
Types like `Option`, `Result`, `Mut`, `Bool`, etc are going to be very commonly used and it might get annoying to have something like this in every file:
```
import (
	"std/option" *
	"std/result" *
	"std/mut" *
	"std/bool" *
)
```
Or at the very least include a `common` module that would include/export all the other types.
```
import (
	"std/common" *
)
```

Seems like the usual approach here is to have a 'prelude' module that gets imported automatically into every module.
It would contain all the commonly used types already exported to the top level scope.

I think the `common` module might be a good middle ground in that you still are being explicit with what is imported while still getting all the basic types imported easily.
We should not worry about this at the start.
It's easy enough to add in later if necessary.
