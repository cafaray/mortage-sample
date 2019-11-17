# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Employee(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, type: str=None, name: str=None, created: int=None, modified: int=None, birth_date: str=None, city: str=None, department: str=None, email: str=None, gender: str=None, is_active: bool=None, metadata: EmployeesArrayInnerMetadata=None, phone: str=None, postal: int=None, state: str=None, street: str=None):  # noqa: E501
        """Employee - a model defined in Swagger

        :param uuid: The uuid of this Employee.  # noqa: E501
        :type uuid: str
        :param type: The type of this Employee.  # noqa: E501
        :type type: str
        :param name: The name of this Employee.  # noqa: E501
        :type name: str
        :param created: The created of this Employee.  # noqa: E501
        :type created: int
        :param modified: The modified of this Employee.  # noqa: E501
        :type modified: int
        :param birth_date: The birth_date of this Employee.  # noqa: E501
        :type birth_date: str
        :param city: The city of this Employee.  # noqa: E501
        :type city: str
        :param department: The department of this Employee.  # noqa: E501
        :type department: str
        :param email: The email of this Employee.  # noqa: E501
        :type email: str
        :param gender: The gender of this Employee.  # noqa: E501
        :type gender: str
        :param is_active: The is_active of this Employee.  # noqa: E501
        :type is_active: bool
        :param metadata: The metadata of this Employee.  # noqa: E501
        :type metadata: EmployeesArrayInnerMetadata
        :param phone: The phone of this Employee.  # noqa: E501
        :type phone: str
        :param postal: The postal of this Employee.  # noqa: E501
        :type postal: int
        :param state: The state of this Employee.  # noqa: E501
        :type state: str
        :param street: The street of this Employee.  # noqa: E501
        :type street: str
        """
        self.swagger_types = {
            'uuid': str,
            'type': str,
            'name': str,
            'created': int,
            'modified': int,
            'birth_date': str,
            'city': str,
            'department': str,
            'email': str,
            'gender': str,
            'is_active': bool,
            'metadata': EmployeesArrayInnerMetadata,
            'phone': str,
            'postal': int,
            'state': str,
            'street': str
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'type': 'type',
            'name': 'name',
            'created': 'created',
            'modified': 'modified',
            'birth_date': 'birthDate',
            'city': 'city',
            'department': 'department',
            'email': 'email',
            'gender': 'gender',
            'is_active': 'isActive',
            'metadata': 'metadata',
            'phone': 'phone',
            'postal': 'postal',
            'state': 'state',
            'street': 'street'
        }

        self._uuid = uuid
        self._type = type
        self._name = name
        self._created = created
        self._modified = modified
        self._birth_date = birth_date
        self._city = city
        self._department = department
        self._email = email
        self._gender = gender
        self._is_active = is_active
        self._metadata = metadata
        self._phone = phone
        self._postal = postal
        self._state = state
        self._street = street

    @classmethod
    def from_dict(cls, dikt) -> 'Employee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this Employee.

        Beschreibung des  # noqa: E501

        :return: The uuid of this Employee.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this Employee.

        Beschreibung des  # noqa: E501

        :param uuid: The uuid of this Employee.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def type(self) -> str:
        """Gets the type of this Employee.


        :return: The type of this Employee.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Employee.


        :param type: The type of this Employee.
        :type type: str
        """

        self._type = type

    @property
    def name(self) -> str:
        """Gets the name of this Employee.


        :return: The name of this Employee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Employee.


        :param name: The name of this Employee.
        :type name: str
        """

        self._name = name

    @property
    def created(self) -> int:
        """Gets the created of this Employee.


        :return: The created of this Employee.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created: int):
        """Sets the created of this Employee.


        :param created: The created of this Employee.
        :type created: int
        """

        self._created = created

    @property
    def modified(self) -> int:
        """Gets the modified of this Employee.


        :return: The modified of this Employee.
        :rtype: int
        """
        return self._modified

    @modified.setter
    def modified(self, modified: int):
        """Sets the modified of this Employee.


        :param modified: The modified of this Employee.
        :type modified: int
        """

        self._modified = modified

    @property
    def birth_date(self) -> str:
        """Gets the birth_date of this Employee.


        :return: The birth_date of this Employee.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: str):
        """Sets the birth_date of this Employee.


        :param birth_date: The birth_date of this Employee.
        :type birth_date: str
        """

        self._birth_date = birth_date

    @property
    def city(self) -> str:
        """Gets the city of this Employee.


        :return: The city of this Employee.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this Employee.


        :param city: The city of this Employee.
        :type city: str
        """

        self._city = city

    @property
    def department(self) -> str:
        """Gets the department of this Employee.


        :return: The department of this Employee.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """Sets the department of this Employee.


        :param department: The department of this Employee.
        :type department: str
        """

        self._department = department

    @property
    def email(self) -> str:
        """Gets the email of this Employee.


        :return: The email of this Employee.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Employee.


        :param email: The email of this Employee.
        :type email: str
        """

        self._email = email

    @property
    def gender(self) -> str:
        """Gets the gender of this Employee.


        :return: The gender of this Employee.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this Employee.


        :param gender: The gender of this Employee.
        :type gender: str
        """

        self._gender = gender

    @property
    def is_active(self) -> bool:
        """Gets the is_active of this Employee.


        :return: The is_active of this Employee.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """Sets the is_active of this Employee.


        :param is_active: The is_active of this Employee.
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def metadata(self) -> EmployeesArrayInnerMetadata:
        """Gets the metadata of this Employee.


        :return: The metadata of this Employee.
        :rtype: EmployeesArrayInnerMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: EmployeesArrayInnerMetadata):
        """Sets the metadata of this Employee.


        :param metadata: The metadata of this Employee.
        :type metadata: EmployeesArrayInnerMetadata
        """

        self._metadata = metadata

    @property
    def phone(self) -> str:
        """Gets the phone of this Employee.


        :return: The phone of this Employee.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this Employee.


        :param phone: The phone of this Employee.
        :type phone: str
        """

        self._phone = phone

    @property
    def postal(self) -> int:
        """Gets the postal of this Employee.


        :return: The postal of this Employee.
        :rtype: int
        """
        return self._postal

    @postal.setter
    def postal(self, postal: int):
        """Sets the postal of this Employee.


        :param postal: The postal of this Employee.
        :type postal: int
        """

        self._postal = postal

    @property
    def state(self) -> str:
        """Gets the state of this Employee.


        :return: The state of this Employee.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this Employee.


        :param state: The state of this Employee.
        :type state: str
        """

        self._state = state

    @property
    def street(self) -> str:
        """Gets the street of this Employee.


        :return: The street of this Employee.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """Sets the street of this Employee.


        :param street: The street of this Employee.
        :type street: str
        """

        self._street = street