#
# Project:   retdec-python
# Copyright: (c) 2015-2016 by Petr Zemek <s3rvac@gmail.com> and contributors
# License:   MIT, see the LICENSE file for more details
#

"""Matchers for tests."""

import abc


class Matcher(metaclass=abc.ABCMeta):
    """A base class of all matchers."""

    @abc.abstractmethod
    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        name = self.__class__.__name__
        attr_list = ', '.join(
            '{}={!r}'.format(key, value) for key, value in self.__dict__.items()
        )
        return '{}({})'.format(name, attr_list)


class Anything(Matcher):
    """A matcher that matches anything."""

    def __eq__(self, other):
        return True


class AnyDictWith(Matcher):
    """A matcher that matches and ``dict`` with the given keys and values.

    The ``dict`` may also have other keys and values, which are not considered
    during the matching.
    """

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __eq__(self, other):
        if not isinstance(other, dict):
            return False
        for name, value in self.__dict__.items():
            if name not in other or other[name] != value:
                return False
        return True
