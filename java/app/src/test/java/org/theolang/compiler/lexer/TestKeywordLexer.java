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

class TestKeywordLexer {
	@ParameterizedTest
	@MethodSource("testKeywordProvider")
	void testLexKeyword(String input, String output, int consumed) {
		var arr = new ArrayList<Character>();
		for (char c : input.toCharArray()) {
			arr.add(c);
		}
		var ctx = new LexContext(arr);
		var lexer = new KeywordLexer(ctx, TokenType.KEYWORD, "fun");
		var result = lexer.call();
		assertEquals(result.consumedChars, consumed);
		if (output == null) {
			assertEquals(result.token, null);
		} else {
			assertEquals(result.token.type, TokenType.KEYWORD);
			assertEquals(result.token.value, output);
		}
	}

	static Stream<Arguments> testKeywordProvider() {
		return Stream.of(
			Arguments.of("fun", "fun", 3),
			Arguments.of("fu", null, 0),
			Arguments.of("_abc", null, 0)
		);
	}
}
