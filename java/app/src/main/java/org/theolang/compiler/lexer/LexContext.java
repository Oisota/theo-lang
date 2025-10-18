package org.theolang.compiler.lexer;

import java.lang.Character;
import java.util.ArrayList;

/*
 * Context for storing char list and current position.
 * This gets passed to each lexer callable.
 */
class LexContext {
	private ArrayList<Character> data;
	private int index = 0;
	private int currentLine = 1;
	private int currentColumn = 1;

	public LexContext(ArrayList<Character> data) {
		this.data = data;
	}

	public char current() {
		return data.get(index);
	}

	public char atOffset(int offset) {
		return data.get(index + offset);
	}

	public int length() {
		return data.size();
	}

	public int getCurrentLine() {
		return currentLine;
	}

	public int getCurrentColumn() {
		return currentColumn;
	}

	/*
	 * Calculate current line/column position and update index
	 */
	public void consume(int n) {
		// update current line/column 
		for (int i=index; i<(index+n); i++) {
			currentColumn += 1;
			if (data.get(i) == '\n') {
				currentLine += 1;
				currentColumn = 1;
			}
		}
		// bump index indicating the new current position
		index += n;
	}

    /*
     * Check if we can consume the next n chars without
     * going past the data length
     */
    public boolean checkConsume(int n) {
        return (index + n) < data.size();
    }

	/*
	 * Check if there are more tokens to consume
	 */
    public boolean hasNext() {
        return index + 1 < data.size();
    }
}
