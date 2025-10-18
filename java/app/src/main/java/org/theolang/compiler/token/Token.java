package org.theolang.compiler.token;

public class Token {
	public final TokenType type;
	public final String value;
	public int startLine;
	public int endLine;
	public int startColumn;
	public int endColumn;

	public Token(
		TokenType type,
		String value
	) {
		this.type = type;
		this.value = value;
		this.startLine = 0;
		this.endLine = 0;
		this.startColumn = 0;
		this.endColumn = 0;
	}

	public Token(
		TokenType type,
		String value,
		int startLine,
		int endLine,
		int startColumn,
		int endcolumn
	) {
		this.type = type;
		this.value = value;
		this.startLine = startLine;
		this.endLine = endLine;
		this.startColumn = startColumn;
		this.endColumn = endColumn;
	}

	public String toString() {
		return "Token({}, '{}', line: {}-{}, column: {}-{})".formatted(
			type.name(),
			value,
			startLine,
			endLine,
			startColumn,
			endColumn
		);
	}
}
