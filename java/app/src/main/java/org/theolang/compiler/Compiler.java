package org.theolang.compiler;

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.lang.Character;
import java.nio.charset.Charset;
import java.util.ArrayList;

import org.theolang.compiler.lexer.Lexer;
import org.theolang.compiler.token.Token;

public class Compiler {
	public static void main(String[] args) {
		// TODO want to be able to say:
		for (String fileName : args) {
			var chars = readFileChars(fileName); // read file into list of chars

			var lexer = new Lexer(chars);
			var tokens = lexer.lex();

			//var parser = new Parser(tokens):
			//var ast = parser.parse()

			// for (Token t : tokens) {
			// 	System.out.println(t);
			// }
		}
	}

	/*
	 * Read file into a char Array
	 */
	private static ArrayList<Character> readFileChars(String fileName) {
		var charList = new ArrayList<Character>();
		var encoding = Charset.forName("UTF-8");
		int current = 0;

		try {
			var fileReader = new FileReader(fileName, encoding);
			var reader = new BufferedReader(fileReader);
			while (current != -1) {
				current = reader.read();
				if (current != -1) {
					charList.add((char) current);
				}
			}
		} catch (IOException e) {
			System.out.println("Could not read file: " + fileName);
			charList.clear();
		}

		return charList;
	}
}
