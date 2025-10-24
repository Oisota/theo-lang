package org.theolang.compiler.lexer;

import java.lang.Character;
import java.lang.RuntimeException;
import java.util.ArrayList;

import org.theolang.compiler.token.TokenizeResult;
import org.theolang.compiler.token.TokenType;
import org.theolang.compiler.token.Token;
import org.theolang.compiler.Keywords;

public class Lexer {

	private LexContext ctx;

	public Lexer(ArrayList<Character> data) {
		this.ctx = new LexContext(data);
	}

	public ArrayList<Token> lex() {
		var tokens = new ArrayList<Token>();
		var tokenizers = getLexCallables();

		// TODO finish impl of this method
		while (ctx.hasNext()) {
			boolean tokenized = false;
			for (LexerCallable tokenizer : tokenizers) {
				if (tokenized) {
					break;
				}

				Token token = null;
				TokenizeResult result = null;
					
				try {
					result = tokenizer.call();
				} catch (Exception e) {
					System.out.println(e);
					break;
				}

				System.out.println(result);

				if (result.consumedChars > 0) {
					tokenized = true;
				}

				token = result.token;
				if (!(token == null)) {
					token.startLine = ctx.getCurrentLine();
					token.startColumn = ctx.getCurrentColumn();
				}
				ctx.consume(result.consumedChars);
				if (!(token == null)) {
					token.endLine = ctx.getCurrentLine();
					token.endColumn = ctx.getCurrentColumn();
					tokens.add(token);
				}
				System.out.println(token);
			}

			if (!tokenized) {
				throw new RuntimeException("Character not recognized: " + ctx.current());
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
