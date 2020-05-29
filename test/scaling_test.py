import unittest


class ScalingTestCase(unittest.TestCase):
    def test_scale_stroke(self):
        from digital_ink_library.stroke import Stroke

        x = [0., 0., 1., 1.]
        y = [0., 1., 1., 0.]
        x_scaled = [0., 0., 4.2, 4.2]
        y_scaled = [0., -1., -1., 0.]

        stroke = Stroke(x, y, [], [])
        stroke.scale(x_factor=4.2, y_factor=-1.)

        self.assertEqual(stroke.x, x_scaled)
        self.assertEqual(stroke.y, y_scaled)

        self.assertEqual(stroke.x_min, 0.)
        self.assertEqual(stroke.x_max, 4.2)
        self.assertEqual(stroke.y_min, -1.)
        self.assertEqual(stroke.y_max, 0.)

    def test_scale_sketch(self):
        from digital_ink_library.stroke import Stroke
        from digital_ink_library.sketch import Sketch

        x = [0., 0., 1., 1.]
        y = [0., 1., 1., 0.]
        x_scaled = [0., 0., 4.2, 4.2]
        y_scaled = [0., -1., -1., 0.]

        stroke_one = Stroke(x, y, [], [])
        stroke_two = Stroke(x.copy(), y.copy(), [], [])
        strokes = [stroke_one, stroke_two]

        sketch = Sketch(strokes)
        sketch.scale(x_factor=4.2, y_factor=-1.)

        self.assertEqual(sketch.strokes[0].x, x_scaled)
        self.assertEqual(sketch.strokes[0].y, y_scaled)
        self.assertEqual(sketch.strokes[1].x, x_scaled)
        self.assertEqual(sketch.strokes[1].y, y_scaled)


if __name__ == '__main__':
    unittest.main()
