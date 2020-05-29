import unittest
from digital_ink_library.sketch import Sketch
from digital_ink_library.stroke import Stroke

def generate_sketch():
    s1 = Stroke(x=[1, 2], y=[0.9, 0.3], timestamp=None, pressure=None)
    s2 = Stroke(x=[1.2, 1.5], y=[0.6, 0.7], timestamp=None, pressure=None)
    return Sketch(strokes=[s1, s2])


class NomalizeTestCase(unittest.TestCase):
    def test_default_normalization(self):
        sketch = generate_sketch()
        s1, s2 = sketch.strokes[0], sketch.strokes[1]
        sketch.normalize()

        self.assertEqual(0., s1.x[0])
        self.assertEqual(1., s1.x[1])
        self.assertEqual(0., s1.y[1])
        self.assertEqual(1., s1.y[0])
        for (x, y) in zip(s2.x, s2.y):
            self.assertGreater(x, 0.)
            self.assertGreater(y, 0.)
            self.assertLess(x, 1.)
            self.assertLess(y, 1.)

        sketch.normalize(new_size=2)
        self.assertEqual(2., s1.x[1])
        self.assertEqual(2., s1.y[0])

    def test_aspect_ration_preserving_normalization(self):
        sketch = generate_sketch()
        s1, s2 = sketch.strokes[0], sketch.strokes[1]
        sketch.normalize(keep_aspect_ratio=True)
        self.assertEqual(s1.x[1], 1.)
        self.assertLess(s1.y[0], 1.)

        sketch = generate_sketch()
        sketch.strokes[1].y[1] = 20.
        sketch.normalize(keep_aspect_ratio=True)
        self.assertLess(sketch.strokes[0].x[1], 1.)
        self.assertLess(sketch.strokes[0].y[0], 1.)
        self.assertEqual(sketch.strokes[1].y[1], 1.)

if __name__ == '__main__':
    unittest.main()
