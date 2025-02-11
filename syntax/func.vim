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

syn keyword javaScriptReserved	class as private public pub export module mod namespace const while do in prop
syn keyword javaScriptType	float int string char void uint byte ubyte int8 int16 int32 int64 uint8 uint16 uint32 uint64
syn keyword javaScriptConditional	case if else loop break continue for
syn keyword javaScriptOperator		and or xor not
syn keyword javaScriptStatement		type struct enum union interface impl
"syn keyword javaScriptBoolean		true false
"syn keyword javaScriptNull		nil _
syn keyword javaScriptIdentifier	let scope distinct
syn keyword javaScriptFunction	fun fn done recur import

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
