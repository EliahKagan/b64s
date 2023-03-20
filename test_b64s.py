#!/usr/bin/env python

# Written in 2023 by Eliah Kagan <degeneracypressure@gmail.com>.
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

"""Tests for the b64s module."""

# pylint: disable=missing-function-docstring

import sys

import pytest

import b64s


_parametrize_examples = pytest.mark.parametrize('plain, coded', [
    ('a', 'YQ=='),
    ('ab', 'YWI='),
    ('孫子兵法', '5a2r5a2Q5YW15rOV'),
    ('The Hebrew phrase for “snowboarder” is גולש סנובורד. 🏂',
     'VGhlIEhlYnJldyBwaHJhc2UgZm9yIOKAnHNub3dib2FyZGVy4oCdIGlzINeS15XXnNepINeh'
     '16DXldeR15XXqNeTLiDwn4+C'),
    ('Fourscore and seven years ago our fathers brought forth, on this '
     'continent, a new nation, conceived in liberty, and dedicated to the '
     'proposition that all men are created equal. Now we are engaged in a '
     'great civil war, testing whether that nation, or any nation so '
     'conceived, and so dedicated, can long endure. We are met on a great '
     'battle-field of that war. We have come to dedicate a portion of that '
     'field, as a final resting-place for those who here gave their lives, '
     'that that nation might live. It is altogether fitting and proper that '
     'we should do this. But, in a larger sense, we cannot dedicate, we '
     'cannot consecrate—we cannot hallow—this ground. The brave men, living '
     'and dead, who struggled here, have consecrated it far above our poor '
     'power to add or detract. The world will little note, nor long remember '
     'what we say here, but it can never forget what they did here. It is for '
     'us the living, rather, to be dedicated here to the unfinished work '
     'which they who fought here have thus far so nobly advanced. It is '
     'rather for us to be here dedicated to the great task remaining before '
     'us—that from these honored dead we take increased devotion to that '
     'cause for which they here gave the last full measure of devotion—that '
     'we here highly resolve that these dead shall not have died in vain—that '
     'this nation, under God, shall have a new birth of freedom, and that '
     'government of the people, by the people, for the people, shall not '
     'perish from the earth.',
     'Rm91cnNjb3JlIGFuZCBzZXZlbiB5ZWFycyBhZ28gb3VyIGZhdGhlcnMgYnJvdWdodCBmb3J0'
     'aCwgb24gdGhpcyBjb250aW5lbnQsIGEgbmV3IG5hdGlvbiwgY29uY2VpdmVkIGluIGxpYmVy'
     'dHksIGFuZCBkZWRpY2F0ZWQgdG8gdGhlIHByb3Bvc2l0aW9uIHRoYXQgYWxsIG1lbiBhcmUg'
     'Y3JlYXRlZCBlcXVhbC4gTm93IHdlIGFyZSBlbmdhZ2VkIGluIGEgZ3JlYXQgY2l2aWwgd2Fy'
     'LCB0ZXN0aW5nIHdoZXRoZXIgdGhhdCBuYXRpb24sIG9yIGFueSBuYXRpb24gc28gY29uY2Vp'
     'dmVkLCBhbmQgc28gZGVkaWNhdGVkLCBjYW4gbG9uZyBlbmR1cmUuIFdlIGFyZSBtZXQgb24g'
     'YSBncmVhdCBiYXR0bGUtZmllbGQgb2YgdGhhdCB3YXIuIFdlIGhhdmUgY29tZSB0byBkZWRp'
     'Y2F0ZSBhIHBvcnRpb24gb2YgdGhhdCBmaWVsZCwgYXMgYSBmaW5hbCByZXN0aW5nLXBsYWNl'
     'IGZvciB0aG9zZSB3aG8gaGVyZSBnYXZlIHRoZWlyIGxpdmVzLCB0aGF0IHRoYXQgbmF0aW9u'
     'IG1pZ2h0IGxpdmUuIEl0IGlzIGFsdG9nZXRoZXIgZml0dGluZyBhbmQgcHJvcGVyIHRoYXQg'
     'd2Ugc2hvdWxkIGRvIHRoaXMuIEJ1dCwgaW4gYSBsYXJnZXIgc2Vuc2UsIHdlIGNhbm5vdCBk'
     'ZWRpY2F0ZSwgd2UgY2Fubm90IGNvbnNlY3JhdGXigJR3ZSBjYW5ub3QgaGFsbG934oCUdGhp'
     'cyBncm91bmQuIFRoZSBicmF2ZSBtZW4sIGxpdmluZyBhbmQgZGVhZCwgd2hvIHN0cnVnZ2xl'
     'ZCBoZXJlLCBoYXZlIGNvbnNlY3JhdGVkIGl0IGZhciBhYm92ZSBvdXIgcG9vciBwb3dlciB0'
     'byBhZGQgb3IgZGV0cmFjdC4gVGhlIHdvcmxkIHdpbGwgbGl0dGxlIG5vdGUsIG5vciBsb25n'
     'IHJlbWVtYmVyIHdoYXQgd2Ugc2F5IGhlcmUsIGJ1dCBpdCBjYW4gbmV2ZXIgZm9yZ2V0IHdo'
     'YXQgdGhleSBkaWQgaGVyZS4gSXQgaXMgZm9yIHVzIHRoZSBsaXZpbmcsIHJhdGhlciwgdG8g'
     'YmUgZGVkaWNhdGVkIGhlcmUgdG8gdGhlIHVuZmluaXNoZWQgd29yayB3aGljaCB0aGV5IHdo'
     'byBmb3VnaHQgaGVyZSBoYXZlIHRodXMgZmFyIHNvIG5vYmx5IGFkdmFuY2VkLiBJdCBpcyBy'
     'YXRoZXIgZm9yIHVzIHRvIGJlIGhlcmUgZGVkaWNhdGVkIHRvIHRoZSBncmVhdCB0YXNrIHJl'
     'bWFpbmluZyBiZWZvcmUgdXPigJR0aGF0IGZyb20gdGhlc2UgaG9ub3JlZCBkZWFkIHdlIHRh'
     'a2UgaW5jcmVhc2VkIGRldm90aW9uIHRvIHRoYXQgY2F1c2UgZm9yIHdoaWNoIHRoZXkgaGVy'
     'ZSBnYXZlIHRoZSBsYXN0IGZ1bGwgbWVhc3VyZSBvZiBkZXZvdGlvbuKAlHRoYXQgd2UgaGVy'
     'ZSBoaWdobHkgcmVzb2x2ZSB0aGF0IHRoZXNlIGRlYWQgc2hhbGwgbm90IGhhdmUgZGllZCBp'
     'biB2YWlu4oCUdGhhdCB0aGlzIG5hdGlvbiwgdW5kZXIgR29kLCBzaGFsbCBoYXZlIGEgbmV3'
     'IGJpcnRoIG9mIGZyZWVkb20sIGFuZCB0aGF0IGdvdmVybm1lbnQgb2YgdGhlIHBlb3BsZSwg'
     'YnkgdGhlIHBlb3BsZSwgZm9yIHRoZSBwZW9wbGUsIHNoYWxsIG5vdCBwZXJpc2ggZnJvbSB0'
     'aGUgZWFydGgu')
])


@_parametrize_examples
def test_encode_converts_to_base64(plain: str, coded: str) -> None:
    result = b64s.encode(plain)
    assert result == coded


@_parametrize_examples
def test_decode_converts_from_base64(plain: str, coded: str) -> None:
    result = b64s.decode(coded)
    assert result == plain


@_parametrize_examples
def test_encode_decode_round_trips(plain: str, coded: str) -> None:
    del coded  # Not used in this test.
    result = b64s.decode(b64s.encode(plain))
    assert result == plain


@_parametrize_examples
def test_decode_encode_round_trips(plain: str, coded: str) -> None:
    del plain  # Not used in this test.
    result = b64s.encode(b64s.decode(coded))
    assert result == coded


if __name__ == '__main__':
    sys.exit(pytest.main([__file__, *sys.argv[1:]]))
