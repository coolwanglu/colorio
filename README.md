<p align="center">
  <a href="https://github.com/nschloe/colorio"><img alt="colorio" src="https://nschloe.github.io/colorio/colorio-logo.svg" width="60%"></a>
  <p align="center">Tools for color models.</p>
</p>

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/colorio/master.svg?style=flat-square)](https://circleci.com/gh/nschloe/colorio/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/colorio.svg?style=flat-square)](https://codecov.io/gh/nschloe/colorio)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![colorful](https://img.shields.io/badge/colorful-very-ff69b4.svg?style=flat-square)](https://github.com/nschloe/colorio)
[![PyPi Version](https://img.shields.io/pypi/v/colorio.svg?style=flat-square)](https://pypi.org/project/colorio)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1172995.svg?style=flat-square)](https://doi.org/10.5281/zenodo.1172995)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/colorio.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/colorio)
[![PyPi downloads](https://img.shields.io/pypi/dm/colorio.svg?style=flat-square)](https://pypistats.org/packages/colorio)

All methods in colorio are fully vectorized.

### Color spaces

All color spaces implement the two methods
```python
vals = colorspace.from_xyz100(xyz)
xyz = colorspace.to_xyz100(vals)
```
for conversion from and to XYZ100. Adding new color spaces is as easy as
writing a class that provides those two methods.

The following color spaces are implemented:

 * [XYZ](https://en.wikipedia.org/wiki/CIE_1931_color_space) (`colorio.XYZ()`)
 * [xyY](https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xy_chromaticity_diagram_and_the_CIE_xyY_color_space) (`colorio.XYY()`)
 * [Linear SRGB](https://en.wikipedia.org/wiki/SRGB)  (`colorio.SrgbLinear()`)
   This class has the two additional methods
   ```
   from_srgb1()
   to_srgb1()
   ```
   for conversion from and to standard RGB.
 * [HSL and HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)  (`colorio.HSL()`, `colorio.HSV()`)
   These classes have the two methods
   ```
   from_srgb1()
   to_srgb1()
   ```
   for conversion from and to standard RGB.
 * [CIELAB](https://en.wikipedia.org/wiki/Lab_color_space) (`colorio.CIELAB()`)
 * [CIELUV](https://en.wikipedia.org/wiki/CIELUV) (`colorio.CIELUV()`)
 * [ICtCp](https://en.wikipedia.org/wiki/ICtCp) (`colorio.ICtCp()`)
 * [IPT](http://www.ingentaconnect.com/content/ist/cic/1998/00001998/00000001/art00003)
   (`colorio.IPT()`)
 * [CIECAM02 / CAM02-UCS](https://en.wikipedia.org/wiki/CIECAM02)
   ```python
   import colorio

   L_A = 64 / numpy.pi / 5
   ciecam02 = colorio.CIECAM02(0.69, 20, L_A)
   cam02 = colorio.CAM02('UCS', 0.69, 20, L_A)
   ```
   The implementation contains a few improvements over the CIECAM02 specification (see
   [here](https://arxiv.org/abs/1802.06067)).
 * [CAM16 / CAM16-UCS](https://doi.org/10.1002/col.22131)
   ```python
   import colorio

   L_A = 64 / numpy.pi / 5
   cam16 = colorio.CAM16(0.69, 20, L_A)
   cam16ucs = colorio.CAM16UCS(0.69, 20, L_A)
   ```
   The implementation contains a few improvements over the CAM16
   specification (see [here](https://arxiv.org/abs/1802.06067)).
 * [J<sub>z</sub>a<sub>z</sub>b<sub>z</sub>](https://doi.org/10.1364/OE.25.015131)
   (`colorio.JzAzBz()`)


### Tools

colorio provides a number of useful tools for analyzing and visualizing color spaces.

#### Visualizing the SRGB gamut

<img src="https://nschloe.github.io/colorio/srgb-gamut-cielab.png" width="40%">

The SRGB gamut is a perfect cube in SRGB space, and takes curious shapes when translated
into other color spaces. The above image shows the SRGB gamut in XYZ space. The image
data was created with
```python
import colorio

colorspace = colorio.CIELAB()
colorspace.save_srgb_gamut(colorspace, "srgb.vtk", n=50, cut_000=False)

# The HDR (Rec.2100, Rec.2020) gamut works the same way
colorspace.save_hdr_gamut(colorspace, "hdr.vtk", n=50, cut_000=False)
```
The [VTK](https://www.vtk.org/VTK/img/file-formats.pdf) file can then be opened
in, e.g., ParaView, where the following instructions apply:
1. Open the file in ParaView and execute the following steps in the **Properties** tab
   to the left.
2. Press the **Apply** button.
3. Under the **Coloring** section, change `Solid Color` to `srgb`.
4. If necessary, press the gear button to the right of the search field to activate
   advanced options.
5. Under the **Scalar Coloring** section, uncheck **Map Scalars**.

More images are [in the gh-pages
branch](https://github.com/nschloe/colorio/tree/gh-pages).

The data can be written in most formats supported by
[meshio](https://github.com/nschloe/meshio). (You might have to install additional
packages for some formats.)

#### Visualizing the visible gamut

<img src="https://nschloe.github.io/colorio/visible-d65-xyz.png" width="20%">

Same as above, but with the gamut visible under a given illuminant.
```python
import colorio

colorspace = colorio.XYZ()
illuminant = colorio.illuminants.d65()
observer = colorio.observers.cie_1931_2()
colorspace.save_visible_gamut(observer, illuminant, "visible.vtk")
```
The gamut is shown in grey since SRGB screens are not able to display the colors anyway.

#### The xy-gamut

<img src="https://nschloe.github.io/colorio/xy-gamut.png" width="40%">

Show the classical visible gamut in xy with [Planckian
locus](https://en.wikipedia.org/wiki/Planckian_locus) and the SRGB colors (at maximum
luminosity).

```python
import colorio

colorio.show_xy_gamut()
```


#### Show experimental data

colorio contains lots of experimental data sets some of which can be used to assess
certain properties of color spaces.


###### MacAdam

<img src="https://nschloe.github.io/colorio/macadam.png" width="30%">

The famous MacAdam ellipses (from [this
article](https://doi.org/10.1364%2FJOSA.32.000247)) can be plotted with
```python
import colorio

colorio.show_macadam(
    scaling=10,
    plot_filter_positions=False,
    plot_standard_deviations=False
)
```

###### Luo-Rigg

<img src="https://nschloe.github.io/colorio/luo-rigg.png" width="30%">

Likewise for [Luo-Rigg](https://doi.org/10.1002/col.5080110107).
```python
import colorio

colorio.show_luo_rigg(plot_rgb_triangle=True, ellipse_scaling=1.5)
```

###### Ebner-Fairchild

<img src="https://nschloe.github.io/colorio/ebner_fairchild_jzazbz.png" width="40%">

For example
```python
import colorio

colorspace = colorio.JzAzBz()
colorspace.show_ebner_fairchild()
```
shows constant-hue data from [the Ebner-Fairchild
experiments](https://doi.org/10.1117/12.298269) in the a<sub>z</sub>b<sub>z</sub>-plane
of the J<sub>z</sub>a<sub>z</sub>b<sub>z</sub> color space. (Ideally, all colors in one
set sit on a line.)


###### Hung-Berns
Likewise for [Hung-Berns](https://doi.org/10.1002/col.5080200506):

<img src="https://nschloe.github.io/colorio/hung_berns_jzazbz.png" width="40%">

```python
import colorio

colorspace = colorio.JzAzBz()
colorspace.show_hung_berns()
```

###### Xiao et al.
Likewise for [Xiao et al.](https://doi.org/10.1002/col.20637):

<img src="https://nschloe.github.io/colorio/xiao.png" width="40%">

```python
import colorio

colorspace = colorio.CIELAB()
colorspace.show_xiao()
```

##### Munsell
[Munsell color data](https://www.rit.edu/cos/colorscience/rc_munsell_renotation.php) is visualized with

<img src="https://nschloe.github.io/colorio/munsell_cieluv.png" width="40%">

```python
import colorio

colorspace = colorio.CIELUV()
colorspace.show_munsell(V=5)
```

To simply retrieve the Munsell data in xyY format, use
```python
import colorio

h, V, C, xyy = colorio.get_munsell_data()
```

#### Color differences

Color differences in any space can be computed with `colorio.delta(a, b)`.

### Installation

colorio is [available from the Python Package Index](https://pypi.org/project/colorio/),
so just use
```
pip3 install colorio --user
```
to install.

### Testing

To run the tests, simply check out this repository and run
```
pytest
```

### License
colorio is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).