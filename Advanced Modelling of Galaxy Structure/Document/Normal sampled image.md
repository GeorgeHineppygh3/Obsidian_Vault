---
s:: true
---
---
s:: true
---
---
s:: true
---
## What is it?

- An image generated from a set of $N$ normals to the spiral fit that sample $X$ pixels around the intercept of the normal to the line

## What can this show us?

- Need to speak to steven about this but there is definitely something that can be done statistically or as a case study

Figures:
===============================================================
![Pasted image 20230414102930.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230414102930.png)
The image demonstrates 50 linearly spaced points with their corresponding normals overlayed on top of the spiral fit where the lines are colour-mapped by radius. 

![Pasted image 20230414102938.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230414102938.png)

Explanation:
===============================================================

Sample $N$ linearly spaced points along the spiral points. Calculate the tangent through the line from the two points neighbouring along the spiral fit. From this the normal bisector of these two points is generated and the $X$ pixels either side of the normal-spiral-fit intersect are sampled. The sampled points are stacked into an image array. The y axis represents the distance of the point from the centre of the extracted Sérsic profile in multiples of the effective radius of the profile. The x axis represents the distance along the normal in pixels where the centre is is the fit-normal intersect.



