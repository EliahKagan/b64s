"""Friendly Base64 with str input and output, using UTF-8."""

__all__ = ['encode', 'decode']

import base64


def encode(text: str) -> str:
    """Encode a string from UTF-8 text to Base64."""
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')


def decode(base64_text: str) -> str:
    """Decode a string from Base64 to UTF-8 text."""
    return base64.b64decode(base64_text).decode('utf-8')
