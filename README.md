# 📸 InstaHashtag

<p align="center">

  <a href="https://github.com/column-st/InstaHashtag/actions?query=workflow%3ABuild">
    <img src="https://github.com/column-st/InstaHashtag/workflows/Build/badge.svg?branch=master">
  </a>

  <a href="https://column-st.github.io/InstaHashtag/">
    <img src="https://github.com/column-st/InstaHashtag/workflows/Docs/badge.svg?branch=master">
  </a>

  <a href="https://coveralls.io/github/column-st/InstaHashtag?branch=master">
    <img src="https://coveralls.io/repos/github/column-st/InstaHashtag/badge.svg?branch=master&service=github">
  </a>

  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
  </a>
</p>


Unofficial Python API wrapper for [DisplayPurposes](https://displaypurposes.com/).

## Installing

```
pip install instahashtag
```

## Documentation

Documentation for this module can be found [here](https://column-st.github.io/InstaHashtag/).

## Use

This library is built as a layer-based module and may be used in different ways depending on the use 
case of the user. In this README file only the `wrapper` module is documented, but for further
use cases please check out the docs above.

### Wrapper

A complete Python wrapper around the API.

```python
from instahashtag import Tag, Graph, Maps

tag = Tag(hashtag="instagram")
graph = Graph(hashtag="instagram")
maps = Maps(
    x1=-80.48712034709753,
    y1=25.750749758162012,
    x2=-79.82794065959753,
    y2=25.854604964203453,
    zoom=12,
)
```

Check out the documentation above to understand how the objects behave, and what attributes are accessible.
