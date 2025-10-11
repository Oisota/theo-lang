package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class KeywordLexer extends LexerCallable {

	private TokenType type;
	private String keyword;

	public KeywordLexer(LexContext ctx, TokenType type, String keyword) {
		super(ctx);
		this.type = type;
		this.keyword = keyword;
	}

	public TokenizeResult call() {
		int consumedChars = 0;
		while (
			(ctx.index + consumedChars < ctx.length()) &&
			(consumedChars < keyword.length()) &&
			(keyword.codePointAt(consumedChars) == ctx.atOffset(consumedChars))
		) {
			consumedChars += 1;
		}

		if (keyword.length() == consumedChars) {
			return new TokenizeResult(
				consumedChars,
				new Token(type, keyword)
			);
		}
		return TokenizeResult.empty();
	}
}
