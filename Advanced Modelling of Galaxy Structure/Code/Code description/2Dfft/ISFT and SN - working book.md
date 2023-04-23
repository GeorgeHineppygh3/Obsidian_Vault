---
s:: true
---

### Information taken from papers listed in [Creating Spiral fourier transform](Creating%20Spiral%20fourier%20transform.md)

### Signal to noise ratio for weighting power spectrum

This angle, as well as the line of nodes position, can be determined following the procedure outlined by CA82, which consists in calculating the $|A(p, m)|$ spectra for the main component, disregarding secondary ones, for all possible values of P.A. and w. The $S/N$, for each spectrum,
is given by the expression:
$$\\frac{S}{N} = (|A(p,m)|_{max} - L)/\\sigma$$

where $A(p, m) _{max}$ is the maximum amplitude of the Fourier coefficients, $L$ is the mean level out of the main peak and σ is a rms estimate of the spectrum given by:
$$\\sigma^2 = \\langle(|A(p,m)|-L)^2\\rangle$$ 
The adopted pair of values P.A. and is the one that gives the higher S/N.

Implementing into code,
```run-python
def SN(A):
    """This function calculates the signal to noise for the global maxima as well as a weighting list for each component
  
    Args:
        A (numpy array): A complex array representing the spiral fourier transform of an image

    Returns:
        SN_max (float): Signal to noise on the global maxima
        SN_weightings (numpy array): Signal to noise for each p
    """

    # get average of power spectrum
    L = np.average(np.abs(A))

    # Calculate rms estimate of the spectrum
    sigma = np.sqrt(np.average((np.abs(A)-L)**2))

    # Calculate signal to noise of global maxima using sigma and L
    SN_max = (np.abs(A[np.argmax(np.abs(A))])-L)/sigma

    # Calculate signal to noise of all values to provide a weighting list
    SN_weightings = (np.abs(A)-L)/sigma

    return SN_max, SN_weightings
```

This code creates a list of weightings for signal to noise for each $p$ in $A(p,m)$ as well as the signal to noise on the global maxima.

### 5.2. Two-Dimensional Inverse Fast Fourier Transform

One of the most powerful tools provided by 2DFFT is the ability to run an Inverse FFT. After having de-projected the images and identified the dominant harmonic modes, we can calculate the inverse of the transforms according to Seigar et al. (2005).
The inverse transform can be written as:
$$S(u, \\theta) = \\sum_m S_m(u) e^{im\\theta} \\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;(9)$$
where 
$$S_m(u) = \\frac{D}{e^{2u}4π^2} \\int_{-p}^{+p} G_m(p)A(p, m)e^{ipu}\\;dp \\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;(10)$$

Gm(p) is a high-frequency filter used by Puerari & Dottori (1992). For the logarithmic spiral governed by Equation 4, it has the form:

$$G_m(p) = e^{ − \\frac{1}{2} (\\frac{p−p_{max}}{25})^2} \\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\; (11)$$

This filter is also used to smooth the $A(p, m)$ spectra at the interval ends ($p− = −50$ and $p+ = 50$ with $dp = 0.25$) (Puerari & Dottori 1992). Equation 9 is designed as such, to allow the user to create an inverse transform for a selected number of harmonic components. For example, the inverse transform can be calculated for one component, e.g., $m = 2$, or any number of components can be combined to yield a composite result, e.g., $m = 2, 3,\\, \\& \\, 4$. Once an Inverse FFT is created, it can be directly compared to the de- projected image of the galaxy, allowing us to effectively observe what the code is seeing. Figure 16a and Figure 20 show images of spiral galaxies overlaid with contours representing the results of Inverse FFTs of the same galaxy. The contours are the real part of the complex spatial function of Equation 9. The use of these images to analyse a galaxy can lead to more confident determination of pitch angle.

## Alternative filtering idea:

Create power spectrums for `m : 1-6` and select most dominant spatial frequencies by S/N and use these as components to ISFT.

Would need a way of seeing if the spectrum is too flat and small to ignore it.
```run-python
import numpy as np
import gax_fits as gfits

# Generate power spectrum
A, p, SN_w, p_max, SN_m, phi = gfits.Spiral_power_spec(tes_im,tes_tab,1.4,m)

P = np.abs(A) 'Spiral Power spectrum'
L = np.mean(P) 'Average Power'



```

This has the same structure as `number_of_arms` should implement there.

### Discretising the integrals:

$$S_m(u) = \\frac{D}{e^{2u}4π^2} \\sum_{-p}^{+p} G_m(p)A(p, m)e^{ipu}\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;\\;(10)$$
The signal $A(p,m)$ has shape `500,` 

Once this function has been made we can overlay the dominant components on the image like this:

![Pasted image 20230325110213.png](../../../../AA%20%20-%20%20Assets/Pasted%20image%2020230325110213.png)

After this we can find the centroid of these and then create a smooth line between all the components to match the arm structure.

### Implementing into code:
```run-python
def ISFT(A,p,p_max):
    # First create high frequency filter
    G_p = np.exp(-0.5*((p.ravel()-p_max)/25)**2)

    # Apply filter to A
    filtered_A = np.array([G_p*A](G_p*A.md)).T # attempting broadcasting

	# create weights for IFT
    weight = np.exp(1j*p*lnr)

    # Integrate
    S_u =  np.sum(filtered_A* weight,axis=0) * ((D)/(np.exp(2*lnr)*4*np.pi**2))

    # Create array of theta
    theta = np.linspace(0,2*np.pi,S_u.shape[0])

    # Sum over fourier components
    S_u_theta = S_u*np.exp(1j*m*theta) # there is no sum here...? what is going on

    return np.abs(S_u_theta) # this is meant to be an image array but its complex (hence abs)
```

This is clearly not quite doing what I think it is.

===============================================================

### Weighting by S/N:

So $A(p,m)$ is our output of the spiral Fourier transform $\\therefore$  input that into discretised sum over p:

- Want to create a filter out of the `SN_w` list to select components grouped around the dominant 20  spatial frequencies
- This could later be expanded to look at the S/N of other harmonic modes ($m$) to look at getting the plotting as good as it can look
- 


