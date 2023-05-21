terms_file = open('used_terms.md')

terms = {}

in_table = False
for line in terms_file:
    if line.startswith('|') and not in_table:
        in_table = True
    elif in_table and "--" not in line:
        temp = line.split("|")
        if len(temp) != 5:
            continue
        term = temp[1].strip()
        definition = temp[2].strip()
        terms[term] = definition

glsentry = """
\\newglossaryentry{{{term}}}{{
	name = {{{term}}},
	description = {{{description}}}
}}
"""
with open("../chapters/glossar.tex", 'w') as file:
	for term in terms:
		file.write(glsentry.format(term = term, description = terms[term]))