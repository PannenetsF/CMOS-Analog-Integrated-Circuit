all:
	make slide
	make note
	make hw
	make clean

slide:
	cd slides/ \
	&& pwd \
	&& latexmk -xelatex slides.tex \
	&& cd ..

note:
	cd notes/ \
	&& pwd \
	&& latexmk -xelatex notes.tex \
	&& cd ..

hw: 
	cd homework\
	&& make \
	&& cd ..


clean:
	rm `find ./ -regex ".*\.log\|.*\.aux\|.*\.xdv\|.*\.in\|.*\.out\|.*\.lua\|.*\.fdb_latexmk\|.*\.fls\|.*\.toc"`





