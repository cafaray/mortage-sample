# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EmployeesArrayInnerMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, path: str=None, size: int=None):  # noqa: E501
        """EmployeesArrayInnerMetadata - a model defined in Swagger

        :param path: The path of this EmployeesArrayInnerMetadata.  # noqa: E501
        :type path: str
        :param size: The size of this EmployeesArrayInnerMetadata.  # noqa: E501
        :type size: int
        """
        self.swagger_types = {
            'path': str,
            'size': int
        }

        self.attribute_map = {
            'path': 'path',
            'size': 'size'
        }

        self._path = path
        self._size = size

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeesArrayInnerMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmployeesArray_inner_metadata of this EmployeesArrayInnerMetadata.  # noqa: E501
        :rtype: EmployeesArrayInnerMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path(self) -> str:
        """Gets the path of this EmployeesArrayInnerMetadata.


        :return: The path of this EmployeesArrayInnerMetadata.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this EmployeesArrayInnerMetadata.


        :param path: The path of this EmployeesArrayInnerMetadata.
        :type path: str
        """

        self._path = path

    @property
    def size(self) -> int:
        """Gets the size of this EmployeesArrayInnerMetadata.


        :return: The size of this EmployeesArrayInnerMetadata.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this EmployeesArrayInnerMetadata.


        :param size: The size of this EmployeesArrayInnerMetadata.
        :type size: int
        """

        self._size = size
