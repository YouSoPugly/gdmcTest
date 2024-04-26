# Perlin noise generator
from math import floor
import gdpc.vector_tools as vt
from glm import fract


class Noise:

    def __init__(self, grid_size=10.0, seed=0):
        self.GRID_SIZE = grid_size >= 2.0 and grid_size or 2.0
        self.SEED = seed

    def get_value(self, x, z):
        p = vt.vec2(x, z) / self.GRID_SIZE

        i = vt.vec2(floor(p.x), floor(p.y))
        f = p - i

        c00 = self.hash22(i)
        c10 = self.hash22(i + vt.vec2(1, 0))
        c01 = self.hash22(i + vt.vec2(0, 1))
        c11 = self.hash22(i + vt.vec2(1, 1))

        u = f * f * f * (f * (f * 6 - 15) + 10)

        d00 = self.dot(c00, f)
        d10 = self.dot(c10, f - vt.vec2(1, 0))
        d01 = self.dot(c01, f - vt.vec2(0, 1))
        d11 = self.dot(c11, f - vt.vec2(1, 1))

        return d00 + u.x * (d10 - d00) + u.y * (d01 - d00) + u.x * u.y * (d00 - d10 - d01 + d11)

    def hash22(self, n: vt.vec2):
        k = vt.vec2(self.hash11(self.SEED)*16, self.hash11(self.SEED + 1)*16)
        n = n * k + k.yx
        n = 16.0 * k * fract(n.x * n.y * (n.x + n.y))
        n = vt.vec2(fract(n.x), fract(n.y))
        return vt.vec2(n.x * 2.0 - 1.0, n.y * 2.0 - 1.0)

    def hash11(self, n: float):
        n = (n << 13) ^ n
        n = n * (n * n * 15731.0 + 789221.0) + 1376312589.0
        return -1.0 + 2.0 * fract(n / 1073741824.0)

    def dot(self, v1: vt.vec2, v2: vt.vec2):
        return v1.x * v2.x + v1.y * v2.y
