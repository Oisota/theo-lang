package org.theolang.compiler.lexer;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.lang.Character;

class TestLexContext {
	@Test
	void testLexContext() {
		var arr = new ArrayList<Character>();
		arr.add('a');
		arr.add('b');
		arr.add('c');
		var ctx = new LexContext(arr);

		assertEquals(ctx.length(), 3);
		assertEquals(ctx.current(), 'a');
		assertEquals(ctx.atOffset(1), 'b');
		ctx.consume(1);
		assertEquals(ctx.current(), 'b');
	}
}
