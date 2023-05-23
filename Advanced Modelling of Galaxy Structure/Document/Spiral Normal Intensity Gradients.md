---
s:: true
---
Your text to be added
Your text to be added
Your text to be added
Your text to be added

## Plan:

- How do we find the normals to sample

create equally spaced points along spiral fit
calculate tangents through 2 point line equation sampling the $n-1$ and $n+1$ points
calculate normal to tangent line though the bisector of the  $n-1$ and $n+1$ points
sample $N$ pixels either side of spiral fit normal intersection
stack pixels into unwound arm image

- How the gradient divergence is handled

In order to generate line equations - the length of the line diverges when spiral fit tangent approaches zero 
to combat this when the gradient of the normal crosses 0 and -1 the equation of the line is re written in terms of y instead of x to stop the line length diverging, the line as a result is 'backwards'

- pixel sampling and stacking

The $N$ pixels either side of the intersect are sampled and stack into an image array where the lines written in y are reversed 
The resulting image allows the arm to be viewed in an unwound state

Text
===============================================================

To investigate the colour and intensity distributions across the spiral arms of galaxies the resulting fits from the SFT section (\\ref{sec:SFT}) can be used to sample pixels along equally spaced normals to the fit. The normal points are found by sampling equally space tangent points along the fit and taking the line equation through the $n-1$ and $n+1$ points. The normal to this line through the bisector of the line equation points forms the normal to the tangent point sampled. The program then overlays the line equation and samples the $N$ pixels either side of the fit-normal intersect. The pixels are then stacked into an image array where the arm can be viewed in an unwound state.

The tool overlays every tenth normal line demonstrated in figure \\ref{fig:} by taking inputs the normal gradient $m_n$ and intercept $c_n$. The line equation is then produced over an appropriately scaled range of $x$ values, however as the tangent to the spiral fit approaches zero the gradient, and so line length, diverges. To resolve this gradients in the range $m_n>>1$ and $m_n<<-1$ are plotted by varying the $y$ value and re-writing the equation in $x$. Due to the reversed array plotting in Matplotlib the resulting pixel arrays are reversed before stacking to ensure consistency.

The unwound arm image (see figure \\ref{fig:unwound}) at Sloan resolutions provides little insight into the unwound structure of the arm.  The program is best suited for higher resolution images where interior arm structure is visible (see section \\ref{sec{Case_Sudy}). Due to the figures reduced dynamic range discontinuities throughout the arm are evident throughout the radii progression. These discontinuities present themselves as intensity dips in figure \\ref{fig:}.