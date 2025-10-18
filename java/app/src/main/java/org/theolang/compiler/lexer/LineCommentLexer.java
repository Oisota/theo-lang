package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class LineCommentLexer extends LexerCallable {

	public LineCommentLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
		int consumed = 2;
		String value = "";
		if (ctx.current() == '/' && ctx.atOffset(1) == '/') {
			char current = ctx.atOffset(consumed);
			while (!(current == '\n')) {
				value += current;
				consumed += 1;
				current = ctx.atOffset(consumed);
			}
			return new TokenizeResult(consumed, null);
		}
		return TokenizeResult.empty();
	}
}
