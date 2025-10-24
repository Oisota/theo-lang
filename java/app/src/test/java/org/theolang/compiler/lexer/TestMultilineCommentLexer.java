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

class TestMultilineCommentLexer {
	@ParameterizedTest
	@MethodSource("testCommentProvider")
	void testLexMultilineComment(
		String input,
		int consumed
	) {
		var arr = new ArrayList<Character>();
		for (char c : input.toCharArray()) {
			arr.add(c);
		}
		var ctx = new LexContext(arr);
		var lexer = new MultilineCommentLexer(ctx);
		var result = lexer.call();
		assertEquals(consumed, result.consumedChars);
		assertEquals(null, result.token);
	}

	static Stream<Arguments> testCommentProvider() {
		return Stream.of(
			Arguments.of("/*abcd\nefgh\n*/", 14),
			Arguments.of("/*abcdefgh*/", 12),
			Arguments.of("/abcd\n", 0),
			Arguments.of("/*abcd\n", 0),
			Arguments.of("/*abcd\n*f", 0),
			Arguments.of("/*abcd\n/f", 0),
			Arguments.of("abcd\n", 0)
		);
	}
}
