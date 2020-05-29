class BoundingBox:
    """
        A bounding box around an ink object (e.g., stroke).

        Assumes the following coordinate system:

            y
            ^                   (xMax|yMax)
            |        +---------------+
            |        |               |
            |        |               |
            |        |               |
            |        +---------------+
            |   (xMin|yMin)
            |
            +------------------------> x
          (0|0)
    """

    def __init__(self, x_min, y_min, x_max, y_max):
        if x_min > x_max:
            raise ValueError('xMin value ({}) should be less than xMax value ({})'.format(x_min, x_max))
        if y_min > y_max:
            raise ValueError('yMin value ({}) should be less than yMax value ({})'.format(y_min, y_max))

        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

        self.width = x_max - x_min
        self.height = y_max - y_min

    def merge(self, bounding_box):
        x_min = min(self.x_min, bounding_box.x_min)
        y_min = min(self.y_min, bounding_box.y_min)
        x_max = max(self.x_max, bounding_box.x_max)
        y_max = max(self.y_max, bounding_box.y_max)

        return BoundingBox(x_min, y_min, x_max, y_max)

    def contains(self, x, y):
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max

    def intersects(self, bounding_box):
        return self.contains(bounding_box.x_min, bounding_box.y_max) \
               or self.contains(bounding_box.x_min, bounding_box.y_min) \
               or self.contains(bounding_box.x_max, bounding_box.y_max) \
               or self.contains(bounding_box.x_max, bounding_box.y_min) \
               or bounding_box.contains(self.x_min, self.y_max) \
               or bounding_box.contains(self.x_min, self.y_min) \
               or bounding_box.contains(self.x_max, self.y_max) \
               or bounding_box.contains(self.x_max, self.y_min)

    def get_intersection(self, bounding_box):
        if not self.intersects(bounding_box):
            return None

        x_min = max(self.x_min, bounding_box.x_min)
        x_max = min(self.x_max, bounding_box.x_max)
        y_min = max(self.y_min, bounding_box.y_min)
        y_max = min(self.y_max, bounding_box.y_max)

        return BoundingBox(x_min, y_min, x_max, y_max)

    def area(self):
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BoundingBox):
            return False
        return self.x_min == other.x_min and self.y_min == other.y_min and self.x_max == other.x_max \
               and self.y_max == other.y_max and self.width == other.width and self.height == other.height

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
