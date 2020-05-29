import unittest


class ProcessingTestCase(unittest.TestCase):
    def test_processing_functions(self):
        from digital_ink_library.stroke import Stroke
        from digital_ink_library.sketch import Sketch
        s1 = Stroke(x=[1, 2, 3, 4], y=[1, 2, 3, 4], pressure=[2]*4, timestamp=[1, 2, 3, 4])
        s2 = Stroke(x=[2, 3, 3, 5], y=[5, 3, 3, 1], pressure=[1]*4, timestamp=[1, 2, 3, 4])
        s3 = Stroke(x=[], y=[], pressure=[], timestamp=[])
        sketch = Sketch(strokes=[s1, s2, s3])
        sketch.remove_duplicate_dots()
        self.assertEqual(len(s1), 4)
        self.assertEqual(len(s2), 3)

        sketch.remove_single_dot_strokes()
        self.assertEqual(len(sketch), 2)


if __name__ == '__main__':
    unittest.main()
