all: $(patsubst home%.tex,home%.pdf,$(wildcard home*.tex))

# Generalized rule: how to build a .pdf from each .tex
home%.pdf: home%.tex
	latexmk -xelatex $<


