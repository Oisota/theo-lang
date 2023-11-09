# Macros

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
