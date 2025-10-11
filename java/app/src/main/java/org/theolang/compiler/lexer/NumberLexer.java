package org.theolang.compiler.lexer;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

import org.theolang.compiler.token.TokenizeResult;
import org.theolang.compiler.token.TokenType;

class NumberLexer extends LexerCallable {

	private Pattern pattern = Pattern.compile("[0-9]|(\.)|(_)");
	private Pattern endPattern = Pattern.compile("x|b|[A-F]|[a-f]|[0-9]|(\.)|(_)");

	public NumberLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
		int consumedChars = 0;
		String value = "";
		char currrent = ctx.getCurrent();
		Matcher matcher = pattern.matcher(String.valueOf(current));
		if (matcher.matches()) {
			Matcher endMatcher = endPatter.matcher(String.valueOf(current));
			while (current && endMatcher.matches()) {
				consumedChars += 1;
				value += current;
				try {
					current = ctx.atOffset(consumedChars);
				} catch (IndexError) {
					break;
				}
			}

			value = value.replace("_", "");
			TokenType tokenType = TokenType.INTEGER;
			if (value.contains(".")) {
				tokenType = TokenType.FLOAT;
			}
			return new TokenizeResult(consumedChars, new Token(tokenType, value));
		}
		return TokenizeResult.empty()
	}
}
