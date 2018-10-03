# Documentation

This is example data to illustrate how to use this tool.
I have therefore taken a data sheet of an inverter (it could be any data.
There is no intention behind this chosen set of data other than illustrating
on how to use this script. In case that any rights are violated, I will gladly
replace this example!).

The second page of this data sheet displays different curves, that can be
parsed with this tool. Open this PDF file with Inkscape (or any comparable
tool that can create SVGs) and make your desired line "recognizable".
In this case, this means changing the color to #00ffff.

Now open this SVG file with any text editor and search for the path with this 
color. 
In this example, there is one line within this path that reads like this:
d="m 89.3672,647.2354 c 1.212,10.909 2.555,17.271 3.707,23.473 1.452,7.828 2.907,12.341 4.359,16.984 1.455,4.643 2.907,7.808 4.362,10.874 1.452,3.062 2.907,5.348 4.359,7.511 1.455,2.163 2.907,3.866 4.362,5.467 1.452,1.598 2.907,2.906 4.359,4.132 1.455,1.223 2.906,2.249 4.362,3.209 1.314,0.869 2.054,1.489 4.358,2.548 2.546,1.169 7.269,3.257 10.902,4.466 3.633,1.209 7.266,2.024 10.902,2.79 3.633,0.763 7.265,1.305 10.898,1.802 3.633,0.497 7.269,0.855 10.902,1.179 3.633,0.32 7.265,0.551 10.902,0.753 3.633,0.2 7.265,0.34 10.898,0.456 3.636,0.112 7.269,0.184 10.902,0.235 3.632,0.051 7.265,0.068 10.902,0.071 3.633,0 7.265,-0.023 10.898,-0.057 3.636,-0.038 7.269,-0.092 10.902,-0.157 3.632,-0.068 7.269,-0.147 10.902,-0.239 3.632,-0.088 7.265,-0.19 10.898,-0.303 3.636,-0.109 7.269,-0.228 10.902,-0.354 3.632,-0.126 7.269,-0.262 10.901,-0.402 3.633,-0.14 7.266,-0.286 10.902,-0.44 3.633,-0.149 7.266,-0.306 10.899,-0.469 l 0.234,-0.011"

Hereby, m stands for a relative path. Capital letters stand for absolute paths. 
C and L describe the curvature. Therefore, replace any " c " and " l " with " m ".
Copy and paste this string into line 99 of the SVG parser and set the limits for
x- and y-values and run the script. It produces a figure of the extracted x- and
y-values and saves the data in "Example/output.csv".

