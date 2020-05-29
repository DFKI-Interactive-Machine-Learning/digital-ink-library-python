import unittest


class OffsetTestCase(unittest.TestCase):
    def test_offset_stroke(self):
        from digital_ink_library.stroke import Stroke

        x = [0., 0., 1., 1.]
        y = [0., 1., 1., 0.]

        stroke = Stroke(x, y, [], [])
        stroke.offset(x_offset=4.2, y_offset=-1.)

        self.assertEqual(stroke.x, [4.2, 4.2, 5.2, 5.2])
        self.assertEqual(stroke.y, [-1., 0., 0., -1.])

        self.assertEqual(stroke.x_min, 4.2)
        self.assertEqual(stroke.x_max, 5.2)
        self.assertEqual(stroke.y_min, -1.)
        self.assertEqual(stroke.y_max, 0.)

    def test_offset_sketch(self):
        from digital_ink_library.stroke import Stroke
        from digital_ink_library.sketch import Sketch

        x = [0., 0., 1., 1.]
        y = [0., 1., 1., 0.]

        stroke_one = Stroke(x, y, [], [])
        stroke_two = Stroke(x.copy(), y.copy(), [], [])
        strokes = [stroke_one, stroke_two]

        sketch = Sketch(strokes)
        sketch.offset(x_offset=4.2, y_offset=-1.)

        self.assertEqual(sketch.strokes[0].x, [4.2, 4.2, 5.2, 5.2])
        self.assertEqual(sketch.strokes[0].y, [-1., 0., 0., -1.])
        self.assertEqual(sketch.strokes[1].x, [4.2, 4.2, 5.2, 5.2])
        self.assertEqual(sketch.strokes[1].y, [-1., 0., 0., -1.])


if __name__ == '__main__':
    unittest.main()
