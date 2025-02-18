# Ivan A. Konovalenko, Anna A. Smagina, Dmitry P. Nikolaev, Petr P. Nikolaev,
# ProLab: perceptually uniform projective colour coordinate system,
# https://arxiv.org/abs/2012.07653
import npx
import numpy as np

from ..illuminants import whitepoints_cie1931
from ._color_space import ColorSpace


class PROLAB(ColorSpace):
    def __init__(self, whitepoint=whitepoints_cie1931["D65"]):
        super().__init__("proLab", ("L", "a", "b"), 0)
        # The matrix Q in the article is
        #
        #  Q = ( Q 0 )
        #      ( q 1 )
        #
        self.Q = np.array(
            [
                [75.54, 486.66, 167.39],
                [617.72, -595.45, -22.27],
                [48.34, 194.94, -243.28],
            ]
        )
        self.q = np.array([0.7554, 3.8666, 1.6739])
        self.Qinv = np.linalg.inv(self.Q)
        self.wp = whitepoint

        # P is Q with whitepoint normalization
        # self.P = np.array([
        #     [79.4725, 486.6610, 153.7311],
        #     [649.9038, -595.4477, -20.4498],
        #     [50.8625, 194.9377, -223.4334],
        #     ])
        # self.p = np.array([0.7947, 3.8666, 1.5373])

    def from_xyz100(self, xyz):
        xyz = np.asarray(xyz)
        xyz = (xyz.T / self.wp).T
        return npx.dot(self.Q, xyz) / (npx.dot(self.q, xyz) + 1)

    def to_xyz100(self, lab):
        y = npx.dot(self.Qinv, lab)
        xyz = y / (1 - npx.dot(self.q, y))
        xyz = (xyz.T * self.wp).T
        return xyz
