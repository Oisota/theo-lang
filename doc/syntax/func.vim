" Vim syntax file
" Language:	Func
" Maintainer: Derek Morey

if exists("b:current_syntax") && b:current_syntax == "func"
  finish
endif

syn keyword javaScriptCommentTodo      TODO FIXME XXX TBD contained
syn match   javaScriptLineComment      "\/\/.*" contains=@Spell,javaScriptCommentTodo
syn match   javaScriptCommentSkip      "^[ \t]*\*\($\|[ \t]\+\)"
syn region  javaScriptComment	       start="/\*"  end="\*/" contains=@Spell,javaScriptCommentTodo
syn match   javaScriptSpecial	       "\\\d\d\d\|\\."
syn region  javaScriptStringD	       start=+"+  skip=+\\\\\|\\"+  end=+"\|$+	contains=javaScriptSpecial,@htmlPreproc
syn region  javaScriptStringS	       start=+'+  skip=+\\\\\|\\'+  end=+'\|$+	contains=javaScriptSpecial,@htmlPreproc

syn match    Label  "(\s*)"
syn match    Label  "\[\s*\]"
syn match    Label  "#\[\s*\]"
syn match    Label  "\u\(\w\|'\)*\>"

syn match   javaScriptSpecialCharacter "'\\.'"
syn match   javaScriptNumber	       "-\=\<\d\+L\=\>\|0[xX][0-9a-fA-F]\+\>"
syn match	javaScriptBraces	   "[{}\[\]<>#]"
syn match	javaScriptParens	   "[()]"

syn keyword javaScriptType	float int string char bool list vector set dict unit
syn keyword javaScriptConditional	if else and or xor not
syn keyword javaScriptOperator		exception raise case use 
syn keyword javaScriptStatement		interface namespace
syn keyword javaScriptBoolean		true false
syn keyword javaScriptNull		nil _
syn keyword javaScriptIdentifier	let type ref struct enum
syn keyword javaScriptFunction	fun fn import

highlight link javaScriptComment		Comment
highlight link javaScriptLineComment		Comment
highlight link javaScriptCommentTodo		Todo
highlight link javaScriptSpecial		Special
highlight link javaScriptStringS		String
highlight link javaScriptStringD		String
highlight link javaScriptCharacter		Character
highlight link javaScriptSpecialCharacter	javaScriptSpecial
highlight link javaScriptNumber		Number
highlight link javaScriptConditional		Conditional
highlight link javaScriptRepeat		Repeat
highlight link javaScriptBranch		Conditional
highlight link javaScriptOperator		Operator
highlight link javaScriptType			Type
highlight link javaScriptStatement		Statement
highlight link javaScriptFunction		Function
highlight link javaScriptBraces		Function
highlight link javaScriptError		Error
highlight link javaScrParenError		javaScriptError
highlight link javaScriptNull			Keyword
highlight link javaScriptBoolean		Boolean
highlight link javaScriptRegexpString		String
highlight link javaScriptIdentifier		Identifier
highlight link javaScriptLabel		Label
highlight link javaScriptException		Exception
highlight link javaScriptMessage		Keyword
highlight link javaScriptGlobal		Keyword
highlight link javaScriptMember		Keyword
highlight link javaScriptDeprecated		Exception 
highlight link javaScriptReserved		Keyword
highlight link javaScriptDebug		Debug
highlight link javaScriptConstant		Label
