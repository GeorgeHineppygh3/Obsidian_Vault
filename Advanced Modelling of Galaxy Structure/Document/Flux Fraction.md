---
s:: true
---
Your text to be added
Your text to be added
Your text to be added
Your text to be added

## Structure:

- How the extraction allows morphological classification
- Demonstration of the strong and weak arms from histogram
- discussion of the histogram features (means trend?)
- Weaknesses of the program
- mention background (will address in discussion)


Galaxy Zoo morphological assessment


By applying the Sérsic subtraction the non parametric image contains only the positive features to the disk. By applying a radial exclusion mask beneath $0.3\\,R_e$ the non-parametric image can be separated into images containing only the arms and the bulge. By summing the flux in the non parametric images and dividing by the total background subtracted flux from the original image the fraction of the flux from each morphological feature can be calculated. In doing so the visual prominence of the features, when viewed with linear scaling, can be quantitatively assessed. This approach allows for an automatic bias free classification of spiral morphology which can be compared to the Galaxy Zoo 2 classifications. Due to our data set selection being based on the weighted fractions from Galaxy Zoo \\cite{willet}, there is little correlation between the weighted fractions and the flux fractions calculated. 


### Results

Figure \\ref{fig:} demonstrates the statistical distribution of the 1000 

Representing the resulting fractions across the 5 bands in histograms allows for selection of galaxies based on their position in the prominence distribution. By selecting galaxies at the extremities of the distribution as in figure \\ref{fig:} \\& \\ref{fig:} and comparing them to the normalised reduced set of prominence classification in Galaxy Zoo 2 visual confirmation of the techniques effectiveness is revealed.  

Due to inaccurate background estimation by Sloan the technique has been ineffective in the bands U and Z where negative flux has been summed and contributed to a smaller total for the original image than the extraction. The resulting flux fractions are non-physical suggesting more flux in the arms than the total galaxy. The implications and possible remedies for this are discussed in section \\ref{sec:discussion}.

Ignoring the U and Z bands, as expected the average arm flux fraction is greater at shorter wavelengths. This is consistent with arms being recognisably blue structures and regions of enhanced star formation with many young blue stars.  Each band shows consistent limited spread with the standard deviation being approximately the same ($\\sim 13.5\\%$) in each suggesting a fairly uniform stellar population.   



While this system has been successful on the set of non barred face on local spiral galaxies the lack of selectivity in the non parametric extraction means that flux from non arm components such as rings or from incorrectly masking the bulge could be misidentified as arm flux. Furthermore barred galaxies would not be possible to assess arm prominence through this method. Adaptations to the extraction process could allow for bulge/bar removal by successive fitting to the non parametric image. In doing so, modelling the bulge and bar as Sérsic profiles, further component isolation may be possible. However other disk typical spatial structures such as rings or halos have no method of isolation and so distinguishing arm prominence to ring or halo remains a human or computer vision task.

- Failing point - prominence and flux are not entirely the same as continuity is not considered