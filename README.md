# SVG Parser

This tool is able to extract data points from an SVG image.

SVGs store curves as plain text. In order to use this script, one should create
an SVG image (e.g. open an existing PDF file with Inkscape and save the relevant
curves as SVG file). Next, define the bounds in x- and y-direction and let the 
script figure out the intermediate points.
The result is saved as a csv file.