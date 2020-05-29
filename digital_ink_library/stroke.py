from .meta import MetaExt


class Stroke(MetaExt):
    _x = None
    _y = None
    _timestamp = None
    _pressure = None

    def __init__(self, x, y, timestamp, pressure, meta=None):
        assert len(x) == len(y)
        super().__init__(meta)

        self._x = x
        self._y = y
        self._timestamp = timestamp
        self._pressure = pressure

    def to_tuple(self):
        return self._x, self._y, self._timestamp, self._pressure, self._size

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def pressure(self):
        return self._pressure

    @property
    def x_min(self):
        return min(self._x)

    @property
    def x_max(self):
        return max(self._x)

    @property
    def y_min(self):
        return min(self._y)

    @property
    def y_max(self):
        return max(self._y)

    @property
    def timestamp_min(self):
        return min(self._timestamp)

    @property
    def timestamp_max(self):
        return max(self._timestamp)

    @property
    def pressure_min(self):
        return min(self._pressure)

    @property
    def pressure_max(self):
        return max(self._pressure)

    def offset(self, x_offset=None, y_offset=None):
        """Offset the x/y coordinates by a given offset"""
        if x_offset:
            for i, x in enumerate(self._x):
                self._x[i] += x_offset

        if y_offset:
            for i, y in enumerate(self._y):
                self._y[i] += y_offset

    def scale(self, x_factor=None, y_factor=None):
        """Scale the x/y coordinates by a given factor"""
        if x_factor:
            for i, x in enumerate(self._x):
                self._x[i] *= x_factor

        if y_factor:
            for i, y in enumerate(self._y):
                self._y[i] *= y_factor

    def remove_duplicate_dots(self):
        """Removes subsequent dots with exactly the same x/y coordinates."""
        if len(self) == 0:
            return

        x, y, pressure, timestamp = [self.x[0]], [self.y[0]], [self.pressure[0]], [self.timestamp[0]]
        for i in range(1, len(self)):
            if self.x[i] != self.x[i-1] or self.y[i] != self.y[i-1]:
                x.append(self.x[i])
                y.append(self.y[i])
                pressure.append(self.pressure[i])
                timestamp.append(self.timestamp[i])
        self._x = x
        self._y = y
        self._pressure = pressure
        self._timestamp = timestamp

    def __len__(self):
        return len(self._x)
