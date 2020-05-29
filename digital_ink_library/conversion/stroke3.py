from . import BaseDataConversion
from ..sketch import Sketch
from ..stroke import Stroke
import numpy as np


class Stroke3Converter(BaseDataConversion):
    def from_sketch(self, sketches):
        return [Stroke3Converter.convert_sketch_to_stroke3(s) for s in sketches]

    def to_sketch(self, ext_sketches):
        return [Stroke3Converter.convert_stroke3_to_sketch(s) for s in ext_sketches]

    @staticmethod
    def convert_sketch_to_stroke3(sketch: Sketch):
        """Lossy conversion from sketch to stroke3: timestamps and pressure values are lost."""
        x = None
        y = None
        pen_up_indices = [0]

        for stroke in sketch.strokes:
            assert isinstance(stroke, Stroke)
            if x is None:
                x = np.array(stroke.x)
                y = np.array(stroke.y)
            else:
                x = np.concatenate((x, np.array(stroke.x)))
                y = np.concatenate((y, np.array(stroke.y)))
            pen_up_indices.append(pen_up_indices[-1] + len(stroke.x))

        # remove first index (helper index); shift by -2: 0 based indices & differences instead of absolute positions
        pen_up_indices = np.array(pen_up_indices[1:]) - 2

        stroke3 = np.zeros((x.size - 1, 3), dtype=np.float16)
        stroke3[:, 0] = np.diff(x)
        stroke3[:, 1] = np.diff(y)
        stroke3[:, 2][pen_up_indices] = 1

        return stroke3

    @staticmethod
    def convert_stroke3_to_sketch(stroke3_sketch):
        """Creates sketch instances from stroke3 data. Timestamps and pressure values are dummy values."""
        abs_sketch = np.cumsum(stroke3_sketch[:, 0:2], axis=0)
        stroke_bounds = np.where(stroke3_sketch[:, 2] == 1)[0] + 1
        abs_strokes = np.split(abs_sketch, stroke_bounds[:-1])
        strokes = [Stroke(x=s[:, 0].tolist(), y=s[:, 0].tolist(), timestamp=None, pressure=None) for s in abs_strokes]
        # TODO: simple replacement for monotonically increasing timestamp and constant pressure
        sketch = Sketch(strokes=strokes)

        raise NotImplementedError()
        return sketch
