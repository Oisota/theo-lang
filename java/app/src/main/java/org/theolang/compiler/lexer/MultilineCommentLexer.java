package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class MultilineCommentLexer extends LexerCallable {

	public MultilineCommentLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
		int consumed = 2;
		String value = "";
		boolean endFound = false;
		if (ctx.current() == '/' && ctx.atOffset(1) == '*') {
			char current = ctx.atOffset(consumed);
			char nextChar = ctx.atOffset(consumed + 1);
			while (
				ctx.checkConsume(consumed + 2) &&
				!(current == '*' && nextChar == '/')
			) {
				value += current;
				consumed += 1;
				current = ctx.atOffset(consumed);
				nextChar = ctx.atOffset(consumed + 1);
				if (current == '*' && nextChar == '/') {
					endFound = true;
				}
			}
			if (endFound) {
				consumed += 2;
				return new TokenizeResult(consumed, null);
			}
		}
		return TokenizeResult.empty();
	}
}
