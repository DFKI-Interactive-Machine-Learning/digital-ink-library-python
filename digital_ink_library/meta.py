class MetaExt:

    _meta = None

    def __init__(self, meta):
        if meta is not None:
            self._meta = meta
        else:
            self._meta = {}

    @property
    def meta(self):
        return self._meta