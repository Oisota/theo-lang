package org.theolang.compiler.lexer;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.Arguments;
import static org.junit.jupiter.api.Assertions.*;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Character;

import org.theolang.compiler.token.TokenType;

class TestIdentifierLexer {
	@ParameterizedTest
	@MethodSource("testIdentifierProvider")
	void testLexIdentifier(String input, String output, int consumed) {
		var arr = new ArrayList<Character>();
		for (char c : input.toCharArray()) {
			arr.add(c);
		}
		var ctx = new LexContext(arr);
		var lexer = new IdentifierLexer(ctx);
		var result = lexer.call();
		assertEquals(result.consumedChars, consumed);
		if (output == null) {
			assertEquals(result.token, null);
		} else {
			assertEquals(result.token.type, TokenType.IDENTIFIER);
			assertEquals(result.token.value, output);
		}
	}

	static Stream<Arguments> testIdentifierProvider() {
		return Stream.of(
			Arguments.of("abc", "abc", 3),
			Arguments.of("_abc", "_abc", 4),
			Arguments.of("foo_123", "foo_123", 7),
			Arguments.of("1234", null, 0), // invalid var name
			Arguments.of("a", "a", 1),
			Arguments.of("1", null, 0)
		);
	}
}
