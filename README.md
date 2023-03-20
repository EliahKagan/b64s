<!-- SPDX-License-Identifier: CC0-1.0 -->

# b64s - Friendly Base64 with str input and output, using UTF-8

The [`b64s` module](b64s/__init__.py) provides two simple functions, `encode`
and `decode`, that thinly wrap functionality from the [`base64`
module](https://docs.python.org/3/library/base64.html) in the standard library,
so that all arguments and return values are `str` and UTF-8 encoding is assumed
and used.

## License

This software is public domain. It is released under [CC0 1.0
Universal](https://creativecommons.org/publicdomain/zero/1.0/), a public domain
dedication.

See [**`COPYING`**](COPYING) for details.

## Usage

You can install [the PyPI package](https://pypi.org/project/b64s/), or [clone
the repository](https://github.com/EliahKagan/b64s).

```python
>>> import b64s

>>> b64s.encode('The Hebrew phrase for “snowboarder” is גולש סנובורד. 🏂')
'VGhlIEhlYnJldyBwaHJhc2UgZm9yIOKAnHNub3dib2FyZGVy4oCdIGlzINeS15XXnNepINeh16DXldeR15XXqNeTLiDwn4+C'

>>> b64s.decode('VGhlIEhlYnJldyBwaHJhc2UgZm9yIOKAnHNub3dib2FyZGVy4oCdIGlzINeS15XXnNepINeh16DXldeR15XXqNeTLiDwn4+C')
'The Hebrew phrase for “snowboarder” is גולש סנובורד. 🏂'
```


## Acknowledgements

Thanks to [Michael Kagan](https://web.lemoyne.edu/~kagan/index.html) for help
with one of the examples.
