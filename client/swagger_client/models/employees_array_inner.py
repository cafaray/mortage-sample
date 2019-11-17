# coding: utf-8

"""
    Employees API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@apigee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmployeesArrayInner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uuid': 'str',
        'type': 'str',
        'name': 'str',
        'created': 'int',
        'modified': 'int',
        'birth_date': 'str',
        'city': 'str',
        'department': 'str',
        'email': 'str',
        'gender': 'str',
        'is_active': 'bool',
        'metadata': 'EmployeesArrayInnerMetadata',
        'phone': 'str',
        'postal': 'int',
        'state': 'str',
        'street': 'str'
    }

    attribute_map = {
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

    def __init__(self, uuid=None, type=None, name=None, created=None, modified=None, birth_date=None, city=None, department=None, email=None, gender=None, is_active=None, metadata=None, phone=None, postal=None, state=None, street=None):  # noqa: E501
        """EmployeesArrayInner - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._type = None
        self._name = None
        self._created = None
        self._modified = None
        self._birth_date = None
        self._city = None
        self._department = None
        self._email = None
        self._gender = None
        self._is_active = None
        self._metadata = None
        self._phone = None
        self._postal = None
        self._state = None
        self._street = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if birth_date is not None:
            self.birth_date = birth_date
        if city is not None:
            self.city = city
        if department is not None:
            self.department = department
        if email is not None:
            self.email = email
        if gender is not None:
            self.gender = gender
        if is_active is not None:
            self.is_active = is_active
        if metadata is not None:
            self.metadata = metadata
        if phone is not None:
            self.phone = phone
        if postal is not None:
            self.postal = postal
        if state is not None:
            self.state = state
        if street is not None:
            self.street = street

    @property
    def uuid(self):
        """Gets the uuid of this EmployeesArrayInner.  # noqa: E501


        :return: The uuid of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this EmployeesArrayInner.


        :param uuid: The uuid of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def type(self):
        """Gets the type of this EmployeesArrayInner.  # noqa: E501


        :return: The type of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmployeesArrayInner.


        :param type: The type of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this EmployeesArrayInner.  # noqa: E501


        :return: The name of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmployeesArrayInner.


        :param name: The name of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """Gets the created of this EmployeesArrayInner.  # noqa: E501


        :return: The created of this EmployeesArrayInner.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EmployeesArrayInner.


        :param created: The created of this EmployeesArrayInner.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this EmployeesArrayInner.  # noqa: E501


        :return: The modified of this EmployeesArrayInner.  # noqa: E501
        :rtype: int
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this EmployeesArrayInner.


        :param modified: The modified of this EmployeesArrayInner.  # noqa: E501
        :type: int
        """

        self._modified = modified

    @property
    def birth_date(self):
        """Gets the birth_date of this EmployeesArrayInner.  # noqa: E501


        :return: The birth_date of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this EmployeesArrayInner.


        :param birth_date: The birth_date of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._birth_date = birth_date

    @property
    def city(self):
        """Gets the city of this EmployeesArrayInner.  # noqa: E501


        :return: The city of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EmployeesArrayInner.


        :param city: The city of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def department(self):
        """Gets the department of this EmployeesArrayInner.  # noqa: E501


        :return: The department of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this EmployeesArrayInner.


        :param department: The department of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def email(self):
        """Gets the email of this EmployeesArrayInner.  # noqa: E501

        test  # noqa: E501

        :return: The email of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmployeesArrayInner.

        test  # noqa: E501

        :param email: The email of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def gender(self):
        """Gets the gender of this EmployeesArrayInner.  # noqa: E501


        :return: The gender of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this EmployeesArrayInner.


        :param gender: The gender of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def is_active(self):
        """Gets the is_active of this EmployeesArrayInner.  # noqa: E501


        :return: The is_active of this EmployeesArrayInner.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this EmployeesArrayInner.


        :param is_active: The is_active of this EmployeesArrayInner.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def metadata(self):
        """Gets the metadata of this EmployeesArrayInner.  # noqa: E501


        :return: The metadata of this EmployeesArrayInner.  # noqa: E501
        :rtype: EmployeesArrayInnerMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this EmployeesArrayInner.


        :param metadata: The metadata of this EmployeesArrayInner.  # noqa: E501
        :type: EmployeesArrayInnerMetadata
        """

        self._metadata = metadata

    @property
    def phone(self):
        """Gets the phone of this EmployeesArrayInner.  # noqa: E501


        :return: The phone of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this EmployeesArrayInner.


        :param phone: The phone of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postal(self):
        """Gets the postal of this EmployeesArrayInner.  # noqa: E501


        :return: The postal of this EmployeesArrayInner.  # noqa: E501
        :rtype: int
        """
        return self._postal

    @postal.setter
    def postal(self, postal):
        """Sets the postal of this EmployeesArrayInner.


        :param postal: The postal of this EmployeesArrayInner.  # noqa: E501
        :type: int
        """

        self._postal = postal

    @property
    def state(self):
        """Gets the state of this EmployeesArrayInner.  # noqa: E501


        :return: The state of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EmployeesArrayInner.


        :param state: The state of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def street(self):
        """Gets the street of this EmployeesArrayInner.  # noqa: E501


        :return: The street of this EmployeesArrayInner.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this EmployeesArrayInner.


        :param street: The street of this EmployeesArrayInner.  # noqa: E501
        :type: str
        """

        self._street = street

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EmployeesArrayInner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmployeesArrayInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other