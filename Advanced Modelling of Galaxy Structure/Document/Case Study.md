---
s:: true
---
Your text to be added
Your text to be added
Your text to be added
Your text to be added
## Structure:
- winding angle stability
	- why the region is small + the uncertainty with it
	- why chosen the northern
- fit overlay
	- fit accuracy
	- discuss how the spiral is probably not logarithmic
- normal images + isolated
	- description of features
	- colour images
- radially averaged normals
	- colour gradient sources
		- dust lanes (link to intensity)
		- AMD and the local region
	- link relevant science
		- SF
		- migration
		- pattern speed
		- position relative to co-rotation

## Figures:

- [x] winding angle stability
- [x] Arm overlay
- [ ] unwound arms normal + isolated
- [x] unwound colours
- [ ] calibrated colour gradients
	- [x] original
	- [ ] isolated

![Pasted image 20230518161451.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230518161451.png)
Needs cropped


![Pasted image 20230518161415.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230518161415.png)

**![](https://lh3.googleusercontent.com/u07vU-gy-8BcWegJ7cSUk5b-ohFGgj8qAr2rdNkyw_LwLMZLrabC1LrvXfF8wKtSaNJuePRCeGKktcTj9eUo2-EClauKifOF6hpb-U9vFhbhaaaFrsFu2tKj7WSxXiqV4yTDPi73XcRNR3dSjFuKTWqp=nw)![](https://lh4.googleusercontent.com/6T0g2lyEthJrliK853Dp8Lsn6EHXS0BT69W8imLsA2fXd1424_dIWTa3ERWen7fYd_5YbVVCh1HslNl_NEdIILSB3JCmnqqb2qg-iVMT_ns1jX_2v24K_S-eiEOx35X7yKDJPorgrVkAZ-irA0p4pa4i=nw)**

![Pasted image 20230518163901.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230518163901.png)

![Pasted image 20230519143854.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230519143854.png)

### References:
```
@article{wei2020physical,
  title={Physical Properties of H II Regions in M51 from Spectroscopic Observations},
  author={Wei, Peng and Zou, Hu and Kong, Xu and Zhou, Xu and Hu, Ning and Lin, Zesen and Mao, Yewei and Lin, Lin and Zhou, Zhimin and Liu, Xiang and others},
  journal={Publications of the Astronomical Society of the Pacific},
  volume={132},
  number={1015},
  pages={094101},
  year={2020},
  publisher={IOP Publishing}
}

@article{meidt2008radial,
  title={Radial dependence of the pattern speed of M51},
  author={Meidt, Sharon E and Rand, Richard J and Merrifield, Michael R and Shetty, Rahul and Vogel, Stuart N},
  journal={The Astrophysical Journal},
  volume={688},
  number={1},
  pages={224},
  year={2008},
  publisher={IOP Publishing}
}
```


## Text:


Understanding the intensity and colour distributions within the spiral arms of M51 provides insights into the mechanisms driving the formation and maintenance of its intricate structure. Intensity variations along the arms indicate the presence of star-forming regions, stellar populations, and intricate patterns of dust and gas, shedding light on the interplay between stellar evolution and the interstellar medium. Similarly, examining colour distributions unveils clues about stellar population distributions, their ages, metallicities, and composition. Mapping and analysing colour gradients offer insights into the history of star formation, stellar migration, and potential interactions within M51.

The northern arm of M51 is chosen to be studied in detail due to the dust extinction being lower than the southern counter-part (\\cite{wei2020physical}). The stable region determined in figure \\ref{fig:} is confined over a small radial interval ($0.3<R_e<0.9$) and as a result of the error determination from equation \\ref{eqn:}, has a large pitch angle uncertainty with a final pitch angle determination,  $\\phi= 19.5^\\circ\\pm5.0^\\circ$. The central fitting region is constrained by the spiral appearing to deviate from the logarithmic form at approximately $N\\,R_e$ or $N\\,kpc$ most likely due to the presence of it's companion galaxy M51b. The stable region is confined below estimations of the corotation radius in the literature ($\\sim X\\,kpc$ or $Y\\,R_e$) \\cite{meidt2008radial} limiting the physical regime for the spiral structure to epicycle resonance governed dominantly by linear dynamics.  

The fit overlay, despite its large uncertainty, traces the arms well and is in general agreement with values from the literature over the measured region. \\cite{Davis2012} measured the pitch angle over a similar disk interval (27\\% compared to our 22\\%) quoting a pitch angle of  $\\phi= 16.26^\\circ\\pm3.20^\\circ$ where our combined uncertainty $\\sigma_{c} =5.9$ is less than the difference $\\Delta\\phi=3.2$.  The difference in  winding angle could possibly be explained by employing a less sophisticated model for star subtraction. The pedestal removal process from dilating the star mask is not entirely successful and leaves behind rogue intensity which may have skewed the SFT fitting.

The increased resolution and histogram clipping in the normal sampled images (\\ref{fig:normalM51}) highlights arm interior details such as dust lanes and arm spurs clearly. The presence of the dust lanes can still however be seen in the isolated image despite the features being negative additions to the disk profile.  Figure \\ref{fig:normal_colours} demonstrates the three colour distributions created from the flux ratios $B/V$,$B/R$ and $V/R$ where the reddening affect of the dust extinction can be seen. 

By averaging the unwound arm colour images radially (figure \\ref{fig:colour_gradients}) the relationship of the colour distribution across the arms is revealed. The arm width is visually estimated to be $\\sim150$ pixels with longer normal samples resulting in multiple pixel sampling from overlapping normal lines. The resulting artifacts produced can be seen on the radially interior edge of figure \\ref{fig:} as arcing lines. 

The colour gradients across the arm indicate the trailing edge of the density wave is redder than the leading edge. This supports the density wave theory of \\cite{lindblad} and \\cite{lin and Shu} where stellar fuel is compressed by the arrival of the leading shock front leading to increased star formation and in turn a larger population of young blue stars. However without IFU data to accurately model the local stellar population's metallicity the colour gradient could have resulted from a multitude of other factors. The age metallicity degeneracy colour contribution is unknown for these images however the presence of dust lanes and extinction is evident from plots of the radially averaged intensity and visual inspection of the unwound arm images. Extinction measurments by over the unwound arm region \\cite{wei2020physical} agree with hypothesis finding significant dust over-densities situated in lanes through the centres of the arms. 
