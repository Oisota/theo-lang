package org.theolang.compiler.lexer;

import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.lang.IndexOutOfBoundsException;

import org.theolang.compiler.token.TokenizeResult;

class WhitespaceLexer extends LexerCallable {
	private Pattern pattern = Pattern.compile("\\p{Space}");

	public WhitespaceLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
		int consumed = 0;
		char current = ctx.atOffset(consumed);

		Matcher matcher = pattern.matcher(String.valueOf(current));
		while (matcher.matches()) {
			consumed += 1;
			if (!ctx.checkConsume(consumed)) {
				break;
			}
			current = ctx.atOffset(consumed);
			matcher = pattern.matcher(String.valueOf(current));
		}
		return new TokenizeResult(consumed);
	}
}
