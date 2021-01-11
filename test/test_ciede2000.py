import numpy
import pytest

import colorio


# reference data from http://www2.ece.rochester.edu/~gsharma/ciede2000/
# added more digits
@pytest.mark.parametrize(
    "lab1, lab2, ref",
    [
        ((50.0000, 2.6772, -79.7751), (50.0000, 0.0000, -82.7485), 2.0424596801565738),
        ((50.0000, 3.1571, -77.2803), (50.0000, 0.0000, -82.7485), 2.861510174747494),
        ((50.0000, 2.8361, -74.0200), (50.0000, 0.0000, -82.7485), 3.4411905986907065),
        ((50.0000, -1.3802, -84.2814), (50.0000, 0.0000, -82.7485), 0.9999988647524548),
        ((50.0000, -1.1848, -84.8006), (50.0000, 0.0000, -82.7485), 1.0000047010743256),
        ((50.0000, -0.9009, -85.5211), (50.0000, 0.0000, -82.7485), 1.0000129676236045),
        ((50.0000, 0.0000, 0.0000), (50.0000, -1.0000, 2.0000), 2.3668588191717523),
        ((50.0000, -1.0000, 2.0000), (50.0000, 0.0000, 0.0000), 2.3668588191717523),
        ((50.0000, 2.4900, -0.0010), (50.0000, -2.4900, 0.0009), 7.179172011348979),
        ((50.0000, 2.4900, -0.0010), (50.0000, -2.4900, 0.0010), 7.179162640001562),
        ((50.0000, 2.4900, -0.0010), (50.0000, -2.4900, 0.0011), 7.219472152285754),
        ((50.0000, 2.4900, -0.0010), (50.0000, -2.4900, 0.0012), 7.2194742124714),
        ((50.0000, -0.0010, 2.4900), (50.0000, 0.0009, -2.4900), 4.804521685774751),
        ((50.0000, -0.0010, 2.4900), (50.0000, 0.0010, -2.4900), 4.8045245082117685),
        ((50.0000, -0.0010, 2.4900), (50.0000, 0.0011, -2.4900), 4.746071113806683),
        ((50.0000, 2.5000, 0.0000), (50.0000, 0.0000, -2.5000), 4.306482095827058),
        ((50.0000, 2.5000, 0.0000), (73.0000, 25.0000, -18.0000), 27.14923130074626),
        ((50.0000, 2.5000, 0.0000), (61.0000, -5.0000, 29.0000), 22.897692469806906),
        ((50.0000, 2.5000, 0.0000), (56.0000, -27.0000, -3.0000), 31.903004646863884),
        ((50.0000, 2.5000, 0.0000), (58.0000, 24.0000, 15.0000), 19.453521433392584),
        ((50.0000, 2.5000, 0.0000), (50.0000, 3.1736, 0.5854), 1.000026343370256),
        ((50.0000, 2.5000, 0.0000), (50.0000, 3.2972, 0.0000), 0.999972872973027),
        ((50.0000, 2.5000, 0.0000), (50.0000, 1.8634, 0.5757), 1.0000494989772715),
        ((50.0000, 2.5000, 0.0000), (50.0000, 3.2592, 0.3350), 1.0000347617151735),
        (
            (60.2574, -34.0099, 36.2677),
            (60.4626, -34.1751, 39.4387),
            1.2644200135991919,
        ),
        (
            (63.0109, -31.0961, -5.8663),
            (62.8187, -29.7946, -4.0864),
            1.2629592982622329,
        ),
        ((61.2901, 3.7196, -5.3901), (61.4292, 2.2480, -4.9620), 1.8730705001183627),
        ((35.0831, -44.1164, 3.7933), (35.0232, -40.0716, 1.5901), 1.8644952341594636),
        (
            (22.7233, 20.0904, -46.6940),
            (23.0331, 14.9730, -42.5619),
            2.0372582697089734,
        ),
        ((36.4612, 47.8580, 18.3852), (36.2715, 50.5065, 21.2231), 1.4145779224938044),
        ((90.8027, -2.0831, 1.4410), (91.1528, -1.6435, 0.0447), 1.4441290780930247),
        ((90.9257, -0.5406, -0.9208), (88.6381, -0.8985, -0.7239), 1.538117005439684),
        ((6.7747, -0.2908, -2.4247), (5.8714, -0.0985, -2.2286), 0.6377276718841146),
        ((2.0776, 0.0795, -1.1350), (0.9033, -0.0636, -0.5514), 0.9082328396025249),
    ],
)
def test(lab1, lab2, ref):
    print(lab1, lab2)
    print(ref)
    val = colorio.diff.ciede2000(lab1, lab2)
    print(val)
    assert abs(val - ref) < 1.0e-14 * abs(ref)

    # from colormath.color_objects import LabColor
    # from colormath.color_diff import delta_e_cie2000
    # color1 = LabColor(lab_l=lab1[0], lab_a=lab1[1], lab_b=lab1[2])
    # color2 = LabColor(lab_l=lab2[0], lab_a=lab2[1], lab_b=lab2[2])
    # delta_e = delta_e_cie2000(color1, color2)
    # print(delta_e)
    # assert abs(delta_e - ref) < 1.0e-12 * abs(delta_e)


def test_vector():
    numpy.random.seed(0)
    lab1 = numpy.random.rand(3, 10)
    lab2 = numpy.random.rand(3, 10)
    for l1, l2, ref in zip(lab1.T, lab2.T, colorio.diff.ciede2000(lab1, lab2)):
        val = colorio.diff.ciede2000(l1, l2)
        assert abs(val - ref) < 1.0e-14 * abs(ref)
