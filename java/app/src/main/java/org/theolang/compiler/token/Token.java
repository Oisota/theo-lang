package org.theolang.compiler.token;

public class Token {
	public final TokenType type;
	public final String value;
	public final int start_line;
	public final int end_line;
	public final int start_column;
	public final int end_column;

	public Token(
		TokenType type,
		String value
	) {
		this.type = type;
		this.value = value;
		this.start_line = 0;
		this.end_line = 0;
		this.start_column = 0;
		this.end_column = 0;
	}

	public Token(
		TokenType type,
		String value,
		int start_line,
		int end_line,
		int start_column,
		int end_column
	) {
		this.type = type;
		this.value = value;
		this.start_line = start_line;
		this.end_line = end_line;
		this.start_column = start_column;
		this.end_column = end_column;
	}

	public String toString() {
		return "Token({}, '{}', line: {}-{}, column: {}-{})".formatted(
			type.name(),
			value,
			start_line,
			end_line,
			start_column,
			end_column
		);
	}
}
