from marshmallow import Schema, fields, validate, ValidationError 

class UserSchema(Schema):
    name = fields.Str(
        required=True,
        validate=[validate.Length(min=3, max=15)]
    )
    lastname = fields.Str(
        required=False
    )