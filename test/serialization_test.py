import unittest


class JsonTestCase(unittest.TestCase):
    def test_dump_load(self):
        from digital_ink_library.serialization.json import JsonDataSerialization
        file_name = "serialization.json"
        json = JsonDataSerialization(pretty_print=True)

        # TEST STROKE SERIALIZATION
        from digital_ink_library.stroke import Stroke
        stroke = Stroke(x=[1]*5, y=[1]*5, pressure=[1]*5, timestamp=[1]*5, meta={"test": [1]*5})

        # dump to/load from file
        with open(file_name, "w", encoding="utf-8") as fp:
            json.dump(obj=stroke, fp=fp)
        with open(file_name, "r", encoding="utf-8") as fp:
            loaded_stroke = json.load(fp=fp)
        self.assertDictEqual(stroke.__dict__, loaded_stroke.__dict__)

        # dump to/load from string
        json_stroke = json.dumps(obj=stroke)
        loaded_stroke = json.loads(s=json_stroke)
        self.assertDictEqual(stroke.__dict__, loaded_stroke.__dict__)

        # TEST SKETCH SERIALIZATION
        from digital_ink_library.sketch import Sketch
        sketch = Sketch(strokes=[stroke], meta=None)

        # dump to/load from file
        with open(file_name, "w", encoding="utf-8") as fp:
            json.dump(obj=sketch, fp=fp)
        with open(file_name, "r", encoding="utf-8") as fp:
            loaded_sketch = json.load(fp=fp)
        for s1, s2 in zip(loaded_sketch.strokes, sketch.strokes):
            self.assertDictEqual(s1.__dict__, s2.__dict__)

        # dump to/load from string
        json_sketch = json.dumps(obj=sketch)
        loaded_sketch = json.loads(s=json_sketch)
        for s1, s2 in zip(loaded_sketch.strokes, sketch.strokes):
            self.assertDictEqual(s1.__dict__, s2.__dict__)


if __name__ == '__main__':
    unittest.main()
