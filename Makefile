
%: %.tex
	pdflatex -jobname=$@ $?
	open $@.pdf

clean:
	rm *.pdf *.aux *.log
