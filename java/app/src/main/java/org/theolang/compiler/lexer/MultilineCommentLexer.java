package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class MultilineCommentLexer extends LexerCallable {

	public MultilineCommentLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
		int consumed = 2;
		String value = "";
		if (ctx.current() == '/' && ctx.atOffset(1) == '*') {
			char current = ctx.atOffset(consumed);
			char nextChar = ctx.atOffset(consumed + 1);
			while (!(current == '*' && nextChar == '/')) {
				value += current;
				current = ctx.atOffset(consumed);
				nextChar = ctx.atOffset(consumed + 1);
			}
			consumed += 2;
			return new TokenizeResult(consumed, null);
		}
		return TokenizeResult.empty();
	}
}
