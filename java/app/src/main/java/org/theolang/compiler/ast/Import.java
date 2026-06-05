package org.theolang.compiler.ast;

public class Import extends Node {
	private String path;
	private String name; // package name or alias if given
	private ArrayList<String> items; // specific items to import if any
}
