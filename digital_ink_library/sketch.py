from .meta import MetaExt


class Sketch(MetaExt):
    _strokes = None

    def __init__(self, strokes=None, meta=None):
        super().__init__(meta)
        if strokes is None:
            strokes = []
        self._strokes = strokes

    def add_stroke(self, stroke):
        self._strokes.append(stroke)

    @property
    def strokes(self):
        return self._strokes

    @property
    def x_min(self):
        return min([stroke.x_min for stroke in self._strokes])

    @property
    def x_max(self):
        return max([stroke.x_max for stroke in self._strokes])

    @property
    def y_min(self):
        return min([stroke.y_min for stroke in self._strokes])

    @property
    def y_max(self):
        return max([stroke.y_max for stroke in self._strokes])

    @property
    def timestamp_min(self):
        return min([stroke.timestamp_min for stroke in self._strokes])

    @property
    def timestamp_max(self):
        return max([stroke.timestamp_max for stroke in self._strokes])

    @property
    def pressure_min(self):
        return min([stroke.pressure_min for stroke in self._strokes])

    @property
    def pressure_max(self):
        return max([stroke.pressure_max for stroke in self._strokes])

    def offset(self, x_offset=None, y_offset=None):
        """Offset the x/y coordinates by a given offset"""
        for stroke in self.strokes:
            stroke.offset(x_offset, y_offset)

    def scale(self, x_factor=None, y_factor=None):
        """Scale the x/y coordinates by a given factor"""
        for stroke in self.strokes:
            stroke.scale(x_factor, y_factor)

    def normalize(self, new_size=1, keep_aspect_ratio=False):
        """
        Scales the x/y coordinates to `new_size`.
        If aspect ratio shall be kept, the largest dimension is scaled to `new_size`
        """
        if len(self) == 0:
            return

        self.offset(x_offset=-self.x_min, y_offset=-self.y_min)
        x_factor = float(new_size) / self.x_max
        y_factor = float(new_size) / self.y_max
        if keep_aspect_ratio and self.x_max >= self.y_max:
            self.scale(x_factor=x_factor, y_factor=x_factor)
        elif keep_aspect_ratio and self.x_max < self.y_max:
            self.scale(x_factor=y_factor, y_factor=y_factor)
        else:
            self.scale(x_factor=x_factor, y_factor=y_factor)

    def remove_duplicate_dots(self):
        """Removes subsequent dots with same x/y coordinates for each stroke."""
        for stroke in self.strokes:
            stroke.remove_duplicate_dots()

    def remove_single_dot_strokes(self):
        """Removes strokes with 1 or 0 dots."""
        self._strokes = [stroke for stroke in self.strokes if len(stroke) > 1]

    def __len__(self):
        return len(self._strokes)
