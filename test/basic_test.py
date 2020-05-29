import unittest


class BasicTestCase(unittest.TestCase):

    def test_meta_extension(self):
        from digital_ink_library.stroke import Stroke
        meta_data = {
            "key1": "value1",
            "key2": 2,
            "key3": [1, 2, 3]
        }

        # initialize stroke with meta data
        stroke = Stroke(x=[1], y=[1], pressure=[1], timestamp=[1], meta=meta_data)

        # check access to meta data
        self.assertDictEqual(meta_data, stroke.meta)

        # change value
        stroke.meta["key1"] = "value2"
        self.assertEqual("value2", stroke.meta["key1"])

        # add value
        stroke.meta["key4"] = "value3"
        self.assertEqual("value3", stroke.meta["key4"])

        # test meta-data integration for sketches (meta initially None)
        from digital_ink_library.sketch import Sketch
        sketch = Sketch()
        sketch.meta["k"] = "v"
        self.assertEqual(sketch.meta["k"], "v")


if __name__ == '__main__':
    unittest.main()
