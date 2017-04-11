NAME= finalreport

# -----------------------------------------------------------
all: $(NAME).pdf

$(NAME).pdf: $(NAME).tex
	pdflatex $(NAME).tex
	pdflatex $(NAME).tex
	bibtex $(NAME)
	bibtex $(NAME)
	pdflatex $(NAME).tex
	pdflatex $(NAME).tex

# -----------------------------------------------------------
.PHONY: clean
clean:
	rm $(NAME).aux $(NAME).log $(NAME).bbl $(NAME).blg
# -----------------------------------------------------------
