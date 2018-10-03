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
    d="m 0,0 m 0.543,17.502 1.254,30.238 1.445,33.417 1.04,17.248 2.779,28.233 4.166,36.353 1.093,6.395 3.074,9.952 4.167,12.377 1.387,3.081 2.777,4.496 4.166,6.105 1.388,1.609 2.776,2.583 4.166,3.553 3.514,2.451 8.293,3.925 12.498,4.83 2.157,0.464 5.769,1.047 8.332,1.261 2.429,0.204 6.944,0.55 10.415,0.692 12.488,0.513 29.014,-0.142 41.662,-0.735 20.671,-0.969 41.836,-2.418 62.491,-3.879 17.375,-1.23 34.709,-2.525 52.077,-3.825"

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
    
    np.savetxt("datei3.csv", result)
