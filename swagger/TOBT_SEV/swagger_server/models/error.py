# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Error(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code: int=None, message: str=None, fields: str=None):
        """
        Error - a model defined in Swagger

        :param code: The code of this Error.
        :type code: int
        :param message: The message of this Error.
        :type message: str
        :param fields: The fields of this Error.
        :type fields: str
        """
        self.swagger_types = {
            'code': int,
            'message': str,
            'fields': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'fields': 'fields'
        }

        self._code = code
        self._message = message
        self._fields = fields

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this Error.
        :rtype: Error
        """
        return deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """
        Gets the code of this Error.

        :return: The code of this Error.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """
        Sets the code of this Error.

        :param code: The code of this Error.
        :type code: int
        """

        self._code = code

    @property
    def message(self) -> str:
        """
        Gets the message of this Error.

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this Error.

        :param message: The message of this Error.
        :type message: str
        """

        self._message = message

    @property
    def fields(self) -> str:
        """
        Gets the fields of this Error.

        :return: The fields of this Error.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields: str):
        """
        Sets the fields of this Error.

        :param fields: The fields of this Error.
        :type fields: str
        """

        self._fields = fields

