""" Holds validator class """


class Validator:
    """ Contains validating methods """

    def validate_int_fields(self, field_value):
        """ validate fields that accept integers """
        if isinstance(field_value, int):
            return float(field_value)
        else:
            raise ValueError

    def validate_string_fields(self, field_value):
        """ validates fields that accept strings """
        if field_value:
            return field_value
        else:
            raise ValueError
