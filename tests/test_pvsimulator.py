import unittest

from commonpvs import resolution
from pvsimulator import simulator


class TestPVSimulator(unittest.TestCase):

    def test_simulator_without_noise(self):
        self.assertEqual(simulator(0, 0.0), 0)
        self.assertEqual(simulator(11 * resolution, 0.0), 2156.59)
        self.assertEqual(simulator(36 * resolution, 0.0), 727.88)
        self.assertEqual(simulator(-40000, 0.0), 0)
        with self.assertRaises(TypeError):
            simulator([0, 40000], 0.0)
        with self.assertRaises(ValueError):
            simulator('asd', 0.0)

    def test_simulator_with_noise(self):
        self.assertTrue(simulator(0, 0.05) == 0)
        self.assertTrue(2156.59 * (1-0.05) <= simulator(11 * resolution, 0.05) <= 2156.59 * (1+0.05))
        self.assertTrue(727.88 * (1-0.05) <= simulator(36 * resolution, 0.05) <= 727.88 * (1+0.05))
        self.assertTrue(simulator(-40000, 0.05) == 0)


if __name__ == '__main__':
    unittest.main()
