---
s:: true
---
### Disclaimers:


## Relations:
- Paper: [Galaxy Zoo Builder - Four-component Photometric Decomposition of Spiral Galaxies Guided by Citizen Science - Lingard et. al.pdf](../../../PDFs/Galaxy%20Zoo%20Builder%20-%20Four-component%20Photometric%20Decomposition%20of%20Spiral%20Galaxies%20Guided%20by%20Citizen%20Science%20-%20Lingard%20et.%20al.pdf)

### Un-defined Terms:
- SDSS: Sloan Digital Sky Survey
- ML: Machine Learning

### Abstract:

- Applied new Multicomponent analysis method on 198 galaxies from SDSS
- demonstrated that it is possible to consistently recover accurate models that either show good agreement with, or improve on, prior work

### Conclusion:

- Galaxy Builder leverages the power of crowdsourcing for the parts of image fitting that are hardest to automate: number of model components and finding regions of parameter space close to the global optima
- spiral arm fitting recovered spiral pitch angles to within $9^\\circ$ 
- systematic tendency for volunteers to incorporate more bulges and fewer bars than necessary for photometric models of strongly barred spirals
- improved clustering algorithm and an improved user interface to address the failures of bar model clustering
- bulge and bar Sérsic $n$, bar boxiness not recovered well using model because a wide range of values fit the light profile well
- unable to obtain reliable physical results with our optimization algorithm (gradient decent gets stuck in local minima) - could be solved by Bayesian optimization with priors obtained from volunteer input, or using a more robust algorithm (Basin-hoppign Wales & Doyle 1998)
- demonstrated our ability to obtain physically motivated models with comparable reduced chi-squared values (between 1 and 5) to results in the literature
- Galaxy Builder may serve an important role in the generation of training catalogs for ML
- obtained aggregate models for 296 images with an average rate of one galaxy per day, and fit photometric models for 294 images
- number of photometric models obtained here is still significantly larger than the largest sample obtained through purely computational photometric fitting of a disc
