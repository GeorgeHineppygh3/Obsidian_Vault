---
s:: true
---
Questions for the Meeting: [Meeting Minutes 29-03-23](../Meeting%20Minutes/Meeting%20Minutes%2029-03-23.md)

Link to ToDo: [To do post 29-03-23](../MISC/To%20do%20post%2029-03-23.md)

### What has been done:

- got the server running and ran good spirals (exception of ###24ua)
- started plotting the spirals given the winding angle from the SFT
	- soon realised that this is not going to work
- started looking at isolating the highest amplitude components
- started filtering signal using paper method [2DFFT Paper - B. L. Davis.pdf](../../PDFs/2DFFT%20Paper%20-%20B.%20L.%20Davis.pdf)
- created a function for signal to noise [ISFT and SN - working book](../Code/Code%20description/2Dfft/ISFT%20and%20SN%20-%20working%20book.md)
- decided that this method could be a bit better
- created spectral flatness weighting [ISFT and SN - working book](../Code/Code%20description/2Dfft/ISFT%20and%20SN%20-%20working%20book.md)
- created top 20 components split by significant dominant image modes
- created a function for this to export each SFT / SPS into a fits file
- attempted to use broadcasting to make the ISFT for the creation of the arm traces [need help with this]
- looked up a Bresenham's line function for working out which pixels will intersect the tangents from the fit


===============================================================

### Questions for Steven

-  Using the maths in: [ISFT and SN - working book](../Code/Code%20description/2Dfft/ISFT%20and%20SN%20-%20working%20book.md) how can I make the ISFT?
-  What method would you go with for creating a 'central' line to the ISFT of the dominant image modes?
-  Can you teach me the basics of broadcasting and situations where it would and would not apply?
- After resolving these technical queries the data will then be there for measuring the flux along lines which correspond to directions from the centre of the density wave to the outside shock edges either leading or trailing, what do you think can be learned about a galaxy by this?


===============================================================

### Resolved questions

1.  How would one create a function that identifies all the pixels a line passes through in terms of their image array index?

Answer
===============================================================
The Bresenham's line algorithm. This algorithm is a simple and efficient way to determine which pixels a line passes through on a 2D grid.

The Bresenham's line algorithm works by incrementally determining which pixel is closest to the ideal line at each step of the line drawing process. The algorithm takes two points as inputs, the start and end points of the line, and returns a list of all the pixels that the line passes through between those two points.


Here's an implementation of the Bresenham's line algorithm in Python:
``` run-python
def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    points = []
    while x0 != x1 or y0 != y1:
        points.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    points.append((x0, y0))
    return points
```
The inputs to this function are the starting and ending x and y coordinates of the line. The output is a list of all the pixels that the line passes through, represented as (x, y) tuples.

- http://rb.gy/11pe

===============================================================