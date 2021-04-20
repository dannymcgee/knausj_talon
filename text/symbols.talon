question [mark]: "?"
(downscore | underscore): "_"
double dash: "--"
(brace | left brace): "{"
(rbrace | are brace | right brace): "}"
triple quote: "'''"
(dot dot | dotdot): ".."
#ellipses: "…"
ellipses: "..."
(comma and | spamma): ", "
plus: "+"
arrow: "->"
fat arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty dubstring:
    '""'
    key(left)
empty escaped (dubstring|dub quotes):
    '\\"\\"'
    key(left)
    key(left)
empty string:
    "''"
    key(left)
empty escaped string:
    "\\'\\'"
    key(left)
    key(left)
(inside parens | args):
	insert("()")
	key(left)
inside (brackets | list):
	insert("[]")
	key(left)
inside braces:
	insert("{}")
	key(left)
inside handlebars:
    insert("{{}}")
    key(left)
    key(left)
inside percent:
	insert("%%")
	key(left)
inside quotes:
	insert('""')
	key(left)
angle that:
    text = edit.selected_text()
    user.paste("<{text}>")
brace that:
    text = edit.selected_text()
    user.paste("{{text}}")
dub brace that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
(parens | args) that:
    text = edit.selected_text()
    user.paste("({text})")
percent that:
    text = edit.selected_text()
    user.paste("%{text}%")
quote that:
    text = edit.selected_text()
    user.paste('"{text}"')

