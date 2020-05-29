# digital_ink_library (Python extension)
This is a Python implementation of the *digital-ink-library*. It provides classes for pen strokes and sketches 
which contain multiple such strokes. Both classes allow to store additional meta-data (standard Python types only)
and can be serialized to JSON which enables cross-platform data exchange, e.g., to the Java implementation of the
*digital-ink-library*.

## Stroke and Sketch Classes
**TODO**

### Metadata
`Stroke` and `Sketch` offer a field `meta` for storing/transferring additional meta-data. For pen strokes, this 
might be  currently unsupported signals of the pen like tilt, for a sketch, this might be the pen's mac address.
The `meta` field is a dictionary and can be used as follows (sample for `Sketch`):

```
from digital_ink_library.stroke import Sketch
sketch = Sketch()

# add meta data entry
sketch.meta['some key'] = 'some value'

# read and print a meta data entry
print(sketch.meta['some key'])  # prints 'some value'
```

### Serialization
The following sample demonstrates how a `Stroke` instance can be serialized and deserialized.
The same pattern can be used with instances of `Sketch`
```
from digital_ink_library.stroke import Stroke
from digital_ink_library.serialization.json import JsonDataSerialization

json_serializer = JsonDataSerialization()
stroke = Stroke(x=[1], y=[1], pressure=[1], timestamp=[1])

# write a stroke object to a json file
file_name = "define_some_filename.json"
with open(file_name, "w", encoding="utf-8") as fp:
    json_serializer.dump(obj=stroke, fp=fp)
    
# load a stroke object from a json file    
with open(file_name, "r", encoding="utf-8") as fp:
    loaded_stroke = json_serializer.load(fp=fp)
```

The JSON data format is compatible to other implementations of the *digital-ink-library*. 
A definition of the data format can be found here: **TODO**

## Installation
run `python setup.py bdist_wheel` and install the resulting `whl` package. 
