---
s:: true
---
Your text to be added
Your text to be added
A stellar population model is a theoretical framework used to describe the properties and evolution of a group of stars in a given region or galaxy. These models are used to predict the observed properties of stellar populations, such as their colours, luminosities, and ages, based on the physical processes that govern their formation and evolution.

The mathematical formalism of a stellar population model can vary depending on the specific assumptions and physical processes included in the model. However, a common approach is to use a set of equations that describe the evolution of the population in terms of its star formation history (SFH), initial mass function (IMF), and chemical enrichment history.

One common formalism is the so-called "instantaneous burst model", which assumes that all stars in the population were formed in a single, short burst of star formation at some time in the past. In this case, the model can be described by a simple set of equations that relate the observed properties of the population to its age, metallicity, and IMF.

For example, the luminosity function of a stellar population can be described by:

$\\Phi(L,t,Z) = \\int_{M_{min}}^{M_{max}} \\psi(t - \\tau_M) \\phi(M) dM$

where $\\Phi(L,t,Z)$ is the luminosity function of the population at time $t$ and metallicity $Z$, $\\psi(t-\\tau_M)$ is the star formation rate (SFR) at time $t - \\tau_M$, where $\\tau_M$ is the lifetime of a star of mass $M$, and $\\phi(M)$ is the IMF, which describes the distribution of masses of stars formed in the population.

Similarly, the spectral energy distribution (SED) of a stellar population can be described by:

$F_{\\nu}(t,Z) = \\int_{M_{min}}^{M_{max}} \\psi(t - \\tau_M) L_{\\nu}(M,Z) \\phi(M) dM$

where $F_{\\nu}(t,Z)$ is the SED of the population at time $t$ and metallicity $Z$, $L_{\\nu}(M,Z)$ is the spectral energy distribution of a star of mass $M$ and metallicity $Z$, and the other terms have the same meaning as in the previous equation.

These equations can be used to predict the observed properties of a stellar population, such as its colours, luminosities, and ages, based on the SFH, IMF, and chemical enrichment history of the population. More complex models can be constructed by including additional physical processes, such as radial mixing, inflow/outflow of gas, and mergers, which can affect the evolution of the population over longer timescales.

#### IMF:

The Salpeter IMF is a power-law function that describes the distribution of stellar masses in a population, and it is given by:

$\\xi(M) = A M^{-\\alpha}$

where $\\xi(M)$ is the number of stars per unit mass interval, $M$ is the stellar mass, $\\alpha = 2.35$ is the power-law index, and $A$ is a normalization constant.

The Kroupa IMF is a two-part power-law function that describes the IMF as a broken power-law with different slopes for high-mass and low-mass stars, and it is given by:

$\\xi(M) = A \\times \\begin{align}\\begin{cases} M^{-\\alpha_1} & \\text{for } 0.08M_{\\odot} < M < 0.5M_{\\odot}\\\\ M^{-\\alpha_2} & \\text{for } 0.5M_{\\odot} < M < M_{max} \\end{cases}\\end{align}$

where $\\alpha_1 = 1.3$, $\\alpha_2 = 2.3$, $M_{\\odot}$ is the mass of the Sun, $M_{max}$ is the maximum stellar mass, and $A$ is a normalization constant.

Which IMF function would best fit an OBDS galaxy of a known age depends on various factors, such as the galaxy's metallicity, star formation history, and environment. Observations have shown that the Salpeter IMF tends to overestimate the number of high-mass stars compared to observations of OBDS galaxies, while the Kroupa IMF provides a better match to observed stellar mass functions in these galaxies. However, it is important to note that the choice of IMF can have a significant impact on the predicted properties of a galaxy, so it is important to carefully consider the observations and physical processes involved before selecting an IMF for a particular study.