---
s:: true
---
---
s:: true
---
---
s:: true
---

# Aims:

Want to create one function that measures pitch angle from an input fits file.

Function Needs to:
- find the image centre
- find the galaxy radius (this one might be harder as there doesn't appear to be automated method) - [speak to steven about using multiples of the effective radii and how to go about this]
- convert the fits to text

### Finding the centre

- need to change the naming convention

```run-python
"""INPUTS:            Files:  X.XXXGyr.fit

                            where X.XXXGyr denotes the time of the snapshot.

                    **NOTE** You can keep cropped fits files in the same

                    folder, as long as your naming scheme is consistently

                    different from the """
```

change to:

```run-python
"""INPUTS:            Files:  <filename><band>a.fits.gz

                            where X.XXXGyr denotes the time of the snapshot.

                    **NOTE** You can keep cropped fits files in the same

                    folder, as long as your naming scheme is consistently

                    different from the """
```