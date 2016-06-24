all: pres.pdf

pres.pdf: pres.tex siganalog.pdf squarewaves.tex filterplot.pdf
	pdflatex pres.tex

siganalog.pdf: makesignals.py
	./makesignals.py

squarewaves.tex: makesquare.py
	./makesquare.py

filterplot.pdf: makeplot.py
	./makeplot.py
