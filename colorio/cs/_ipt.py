import npx
import numpy as np

from ._color_space import ColorSpace


class IPT(ColorSpace):
    """
    IPT color model from

    Ebner, Fairchild,
    Development and Testing of a Color Space (IPT) with Improved Hue Uniformity.
    """

    def __init__(self):
        super().__init__("IPT", ("I", "P", "T"), 0)
        self.M1 = np.array(
            [
                [0.4002, 0.7075, -0.0807],
                [-0.2280, 1.1500, 0.0612],
                [0.0000, 0.0000, 0.9184],
            ]
        )
        self.M2 = np.array(
            [
                [0.4000, 0.4000, 0.2000],
                [4.4550, -4.8510, 0.3960],
                [0.8056, 0.3572, -1.1628],
            ]
        )

    def from_xyz100(self, xyz):
        lms = npx.dot(self.M1, xyz)
        lms_ = np.sign(lms) * np.abs(lms) ** 0.43
        return npx.dot(self.M2, lms_)

    def to_xyz100(self, ipt):
        lms_ = npx.solve(self.M2, ipt)
        lms = np.sign(lms_) * np.abs(lms_) ** (1 / 0.43)
        return npx.solve(self.M1, lms)
