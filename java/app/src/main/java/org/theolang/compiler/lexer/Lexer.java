package org.theolang.compiler.lexer;

import java.lang.Character;
import java.util.ArrayList;

import org.theolang.compiler.token.TokenizeResult;
import org.theolang.compiler.token.TokenType;
import org.theolang.compiler.token.Token;

import org.theolang.compiler.lexer.CharLexer;
import org.theolang.compiler.lexer.IdentifierLexer;
import org.theolang.compiler.lexer.KeywordLexer;
import org.theolang.compiler.lexer.LineCommentLexer;
import org.theolang.compiler.lexer.MultilineCommentLexer;
import org.theolang.compiler.lexer.NumberLexer;
import org.theolang.compiler.lexer.StringLexer;
import org.theolang.compiler.lexer.WhitespaceLexer;

class Lexer {

	private LexContext ctx;

	public Lexer(ArrayList<Character> data) {
		this.ctx = new LexContext(data);
	}

	public ArrayList<Token> lex() {
		var tokens = new ArrayList<Token>();
		var tokenizers = getLexCallables();

		int dataLength = data.length();
		int currentLine = 1;
		int currentColumn = 1;

		// TODO finish impl of this method
		while (index < dataLength) {
			boolean tokenized = false;
			for (LexerCallable tokenizer : tokenizers) {
				TokenizeResult result = tokenizer.call();
			}
		}

		return tokens;
	}

	private ArrayList<LexerCallable> getLexCallables() {
		var callables = new ArrayList<LexerCallable>();
		callables.add(new WhitespaceLexer(ctx));
		callables.add(new LineCommentLexer(ctx));
		callables.add(new MultilineCommentLexer(ctx));
		callables.add(new CharLexer(ctx, TokenType.PAREN_OPEN, '('));
		callables.add(new CharLexer(ctx, TokenType.PAREN_CLOSE, ')'));
		callables.add(new CharLexer(ctx, TokenType.CURLY_OPEN, '{'));
		callables.add(new CharLexer(ctx, TokenType.CURLY_CLOSE, '}'));
		callables.add(new CharLexer(ctx, TokenType.SQUARE_OPEN, '['));
		callables.add(new CharLexer(ctx, TokenType.SQUARE_CLOSE, ']'));
		callables.add(new CharLexer(ctx, TokenType.COLON, ':'));
		callables.add(new CharLexer(ctx, TokenType.COMMA, ','));
		for (String keyword : Keywords.KEYWORDS) {
			callables.add(new KeywordLexer(ctx, TokenType.KEYWORD, keyword));
		}
		for (String reserved : Keywords.RESERVED) {
			callables.add(new KeywordLexer(ctx, TokenType.RESERVED, reserved));
		}
		for (String operator : Keywords.OPERATORS) {
			callables.add(new KeywordLexer(ctx, TokenType.OPERATOR, operator));
		}
		callables.add(new IdentifierLexer(ctx));
		callables.add(new NumberLexer(ctx));
		callables.add(new StringLexer(ctx));
		return callables;
	}
}
