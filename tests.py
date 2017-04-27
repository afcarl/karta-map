import matplotlib
import matplotlib.pyplot
import karta
import mapping

import unittest

class TestMappingFunctions(unittest.TestCase):

    def setUp(self):

        self.ll = (1404428.2170640533, -3011806.030852761)
        self.lr = (2722173.529195537, -1906086.4254576433)
        self.ur = (1975578.9630772884, -1383315.2822752385)
        self.ul = (1019243.9280694319, -2185775.6574322423)
        self.axes_crs = karta.crs.NSIDCNorth

    def test_axes_extent(self):

        ax = matplotlib.pyplot.axes()
        ax.set_xlim(self.ll[0], self.lr[0])
        ax.set_ylim(self.ll[1], self.ur[1])
        bbox = mapping.get_axes_extent(ax, self.axes_crs)

        self.assertAlmostEqual(bbox.vertices[0][0], -20, places=4)
        #self.assertAlmostEqual(bbox.vertices[0][1], 60, places=4)
        self.assertAlmostEqual(bbox.vertices[1][0], -2.89164, places=4)
        #self.assertAlmostEqual(bbox.vertices[1][1], 53.73597, places=4)
        self.assertAlmostEqual(bbox.vertices[2][0], 18.06188, places=4)
        #self.assertAlmostEqual(bbox.vertices[2][1], 62.34066, places=4)
        self.assertAlmostEqual(bbox.vertices[3][0], 0.433920, places=4)
        #self.assertAlmostEqual(bbox.vertices[3][1], 71.94728, places=4)
        return

    def test_isbetween(self):
        self.assertTrue(mapping.isbetween(3, 1, 4))
        self.assertTrue(mapping.isbetween(3.2, 1.0, 4.0))
        self.assertTrue(mapping.isbetween(-2.7, -5.0, -1.0))
        self.assertFalse(mapping.isbetween(-5.0, -5.0, -1.0))
        self.assertFalse(mapping.isbetween(1.0, 1.0, 4.0))
        return

if __name__ == "__main__":
    unittest.main()

