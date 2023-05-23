---
s:: true
---
Your text to be added
Your text to be added
Your text to be added
Your text to be added

## Structure:

- FICL and GAX
	- Gradient decent minimise the Chisq
- How GAX is different to GALFIT3 or PROFIT
- non parametric extraction + demonstration




## Real Text:

FICL and GAX are programs developed by Steven Bamford that employ progressive Sérsic profile fitting to extract non-parametric components and create disk profile subtracted images. The programs create estimates of sources and model parameters and then generates test images containing the Simulated profiles. The galaxy modeller GAX measures the $\\chi^2$ between the working image and the expected model parameters. $\\chi^2$ is calculated as the sum of the squared differences between the observed and expected parameters, divided by the squared uncertainty. 
$$\\chi^2 = \\sum_i\\frac{(O_i-E_i)^2}{S_i^2}$$

Where $O_i$ is the observed value of pixel $i$, $E_i$ is the expected value (given the current parameters of the model), and $S_i$ is the uncertainty on $O_i$. By calculating the gradients of the $\\chi^2$ parameter space, the fitting algorithm can determine the direction that leads to a decrease in $\\chi^2$. The gradient decent algorithm takes steps in the parameter space  that move "downhill" towards the minimum $\\chi^2$. This iterative approach allows the model to progressively converge towards the best fit by continuously refining the parameter values and improving the match between the model and observed data. Through successive iteration, the algorithm effectively finds the model parameters that provide the best possible fit to the observed data while considering the uncertainties associated with each data point.

GAX uses JAX NumPy vectorisation to to increase the computational efficiency of single band fitting replacing older systems such as GALFIT3 or PROFIT with an approximate $50\\times$ reduction in time costs. GAX differs from it's predecessor GALFIT3 in terms of the gradient decent algorithm used. GALFIT3 utilizes Levenberg-Marquardt gradient decent and is designed for fitting a small number of sources/components with good initial parameters, while GAX employs a simpler gradient descent algorithm that is slower but better suited for iterative updates of the non-parametric model and fitting large numbers of galaxies simultaneously. Although GALFIT3 and GAX have both been tested on simulated data and demonstrated consistent parameter estimation without the non-parametric component, GAX shows higher accuracy in producing model images resulting in more precise fit parameters. However, GAX is still under development and does not currently output parameter uncertainties. 

The non-parametric component allows for flexibility, assuming a smooth light distribution described by a Sérsic profile with additional positive features at a different spatial scale. The resulting non parametric image contains the positive features which can be be studied isolated from the Sérsic distribution. Due to many other structures being described by positive inhomogeneities to the Sérsic, features such as bars, bulges and rings are extracted into the image as well. To study isolated spiral arms the non parametric image employs a radial exclusion mask with radius $0.3\\,R_e$ to isolate images containing only the arms and the bulge. Other less desirable morphological features were excluded using the filtering criteria laid out in section \\ref{sec:DATA}. A demonstration of the non-parametric component extraction on a sample of 3 galaxy zoo blue spirals is shown in figure \\ref{fig:demonstration}.  

![Pasted image 20230513152232.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230513152232.png)









## Sim Text:

FICL and GAX are programs developed by Steven Bamford that employ progressive Sérsic profile fitting to extract non-parametric components and create disk profile subtracted images.

In the fitting process, measuring the Chi squared (chisq) between the observed image and the uncertainty improves the fit in the next iteration. Chisq is calculated as the sum of the squared differences between the observed and expected parameters, divided by the squared uncertainty. Minimizing chisq allows the model to closely match the observed data while considering the uncertainties. 


The chi squared (chisq) between the observed and expected parameters is a crucial metric used in the fitting process. By calculating the gradients of the chisq parameter space, the fitting algorithm can determine the direction that leads to a decrease in chisq. Gradient descent algorithms, such as Levenberg-Marquardt (L-M) or simpler gradient descent methods, utilize these gradients to iteratively adjust the model parameters. The algorithm takes steps in the parameter space that move "downhill" towards the minimum chisq. This iterative approach allows the model to progressively converge towards the best fit by continuously refining the parameter values and improving the match between the model and observed data. By minimizing chisq, the fitting algorithm effectively finds the model parameters that provide the best possible fit to the observed data, considering the uncertainties associated with each data point.


By using gradient descent algorithms like Levenburg-Marquardt (L-M) or simpler gradient descent algorithms, the fitting process iteratively adjusts the model parameters in the direction that minimizes chisq. 

GAX differs from it's predecessor GALFIT3 in terms of the gradient decent algorithm used. GALFIT3 utilizes  Levenburg-Marquardt L-M and is designed for fitting a small number of sources/components with good initial parameters, while GAX employs a simpler gradient descent algorithm that is slower but better suited for iterative updates of the non-parametric model and fitting large numbers of galaxies simultaneously. One advantage of GAX is that it generates more accurate model images, resulting in more precise fit parameters and uncertainty estimates. However, GAX is still under development and does not currently output parameter uncertainties. The main sources of error in the fitting process arise from the errors in the input data. 

Multiple local minima can also pose challenges, and the assumptions made by the fitting process include assuming that the model profile, typically an elliptical Sersic profile, reasonably represents the galaxies. The non-parametric component allows for flexibility, assuming a smooth light distribution described by a Sersic profile with additional positive features at a different spatial scale. Although GALFIT3 and GAX have both been tested on simulated data and demonstrated consistent parameter estimation without the non-parametric component, GAX shows higher accuracy in producing model images. Further testing and development of GAX are ongoing to refine the fitting algorithm and assess the balance between the parametric and non-parametric components.