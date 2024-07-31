#!/bin/bash
pdflatex -jobname=out "$1" && open out.pdf
