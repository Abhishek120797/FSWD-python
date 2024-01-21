// JavaScript variable name does not support special characters or symbols except $
// or _. Write a function isValidVariable which check if a variable is valid or invalid variable.

function isValidVariable(variable) {
  if (!/^[a-zA-Z_$]/.test(variable.charAt(0))) {
    return false;
  }
  if (!/^[a-zA-Z0-9_$]*$/.test(variable.slice(1))) {
    return false;
  }

  // Check if the variable name is not a reserved keyword
  const reservedKeywords = [
    "break",
    "case",
    "catch",
    "class",
    "const",
    "continue",
    "debugger",
    "default",
    "delete",
    "do",
    "else",
    "enum",
    "export",
    "extends",
    "false",
    "finally",
    "for",
    "function",
    "if",
    "implements",
    "import",
    "in",
    "instanceof",
    "interface",
    "let",
    "new",
    "null",
    "package",
    "private",
    "protected",
    "public",
    "return",
    "super",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "var",
    "void",
    "while",
    "with",
    "yield",
  ];

  if (reservedKeywords.includes(variable)) {
    return false;
  }

  // If all checks pass, the variable name is valid
  return true;
}

const var1 = "My_age";
const var2 = "12Myage";
const var3 = "$myage";
const var4 = "_myage";
const var5 = "@abhi";

console.log(isValidVariable(var1));
console.log(isValidVariable(var2));
console.log(isValidVariable(var3));
console.log(isValidVariable(var4));
console.log(isValidVariable(var5));
