import std/cmdline
import std/sequtils
#import std/paths

import "lexer/core"
import "lexer/token"

proc main(): void =
  var
    args = commandLineParams()
    input_file = args[0]
    data = readFile(input_file)

  for t in tokenize(data.toSeq):
    echo $t



main()