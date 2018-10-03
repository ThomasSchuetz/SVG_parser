#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np

def get_values(input_string, 
               x_limits=(0,1), 
               y_limits=(0,1)):
    """
    This function splits a given SVG path input string and scales the curve
    to be in the given x- and y-limits.
    
    Parameters
    ----------
    input_string : String
        Path that complies with the SVG standards:
        
        https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d
        
        Currently, this function only interprets relative and absolute 
        `moveto`-commands.
    x_limits : 2-entry tuple/list, optional
        The first entry holds the minimum x-value of the input curve and the 
        second entry holds the maximum x-value.
    y_limits : 2-entry tuple/list, optional
        The first entry holds the minimum y-value of the input curve and the 
        second entry holds the maximum y-value.
    """
    
    # Split the given input_string at each space
    f = input_string.split(" ")
    
    # Initialize lists for x and y values
    x = []
    y = []
    
    # Initialize counter variables (performance is not an issue ...)
    i = 0 # Counts values in f
    j = 0 # Counts skipped entries of f
    
    # Is the following coordinate a relative or an absolute coordinate?
    relative = True
    
    while i < len(f):
        # Apparently, Inkscape uses relative (m) and absolute (M) coordinates
        # to define a path. Check if the next coordinate is given in as a 
        # relative or as absolute coordinate:
        if f[i] == "m":
            relative = True
            j += 1
        elif f[i] == "M":
            relative = False
            j += 1
        elif relative and f[i] == "0,0": 
            # Skip relative coordinates that duplicate the previous value
            j += 1
        else:
            if relative:
                if x == []:
                    # The first relative coordinates have to be handled like 
                    # absolute coordinates:
                    x.append(float((f[i].split(",")[0])))
                    y.append(float((f[i].split(",")[1])))
                    j += 1
                else:
                    # Otherwise, relativ coordinates are computed based on the
                    # previous coordinates
                    x.append(x[i-j] + float((f[i].split(",")[0])))
                    y.append(y[i-j] + float((f[i].split(",")[1])))
            else:
                # Absolute coordinates can be stored directly
                x.append(float((f[i].split(",")[0])))
                y.append(float((f[i].split(",")[1])))
        i += 1

    # Combine both lists to one array
    data = np.array((x,y))
    # Sort the array
#    data = np.transpose(np.sort(data.T, axis=-1))
    
    # Scale x and y values to be 0 <= x,y <= 1
    data[0,:] = ((data[0,:] - np.min(data[0,:])) / 
                 (np.max(data[0,:]) - np.min(data[0,:])))
    
    data[1,:] = ((data[1,:] - np.min(data[1,:])) / 
                 (np.max(data[1,:]) - np.min(data[1,:])))
    
    # Scale x and y values to be in the given limits
    data[0,:] = data[0,:] * (x_limits[1] - x_limits[0]) + x_limits[0]
    data[1,:] = data[1,:] * (y_limits[1] - y_limits[0]) + y_limits[0]
    
    # Return scaled results
    return data


# Example on how to use this script:
if __name__ == "__main__":
    d="m 89.3672,647.2354 m 1.212,10.909 2.555,17.271 3.707,23.473 1.452,7.828 2.907,12.341 4.359,16.984 1.455,4.643 2.907,7.808 4.362,10.874 1.452,3.062 2.907,5.348 4.359,7.511 1.455,2.163 2.907,3.866 4.362,5.467 1.452,1.598 2.907,2.906 4.359,4.132 1.455,1.223 2.906,2.249 4.362,3.209 1.314,0.869 2.054,1.489 4.358,2.548 2.546,1.169 7.269,3.257 10.902,4.466 3.633,1.209 7.266,2.024 10.902,2.79 3.633,0.763 7.265,1.305 10.898,1.802 3.633,0.497 7.269,0.855 10.902,1.179 3.633,0.32 7.265,0.551 10.902,0.753 3.633,0.2 7.265,0.34 10.898,0.456 3.636,0.112 7.269,0.184 10.902,0.235 3.632,0.051 7.265,0.068 10.902,0.071 3.633,0 7.265,-0.023 10.898,-0.057 3.636,-0.038 7.269,-0.092 10.902,-0.157 3.632,-0.068 7.269,-0.147 10.902,-0.239 3.632,-0.088 7.265,-0.19 10.898,-0.303 3.636,-0.109 7.269,-0.228 10.902,-0.354 3.632,-0.126 7.269,-0.262 10.901,-0.402 3.633,-0.14 7.266,-0.286 10.902,-0.44 3.633,-0.149 7.266,-0.306 10.899,-0.469 m 0.234,-0.011"

    # x and y limits
    x_limits = (0.012962027, 1)
    y_limits = (85, 97.64934013)
    
    # Call the function
    result = get_values(d, x_limits, y_limits)

    # Plot resulting curve
    from matplotlib.pyplot import plot, xlim, ylim
    plot(result[0,:], result[1,:])
    xlim(x_limits)
    ylim(y_limits)
    
    np.savetxt("Example/output.csv", result)
