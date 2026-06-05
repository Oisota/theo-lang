package org.theolang.compiler.ast;

class TheoString extends Expr {
	private String value;

	public TheoString(String value) {
		this.value = value;
	}
}
