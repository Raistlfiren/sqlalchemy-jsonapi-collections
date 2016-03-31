# -*- coding: utf-8 -*-


class FieldError(Exception):
    """Exception raised for errors

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message