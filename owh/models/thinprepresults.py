# -*- coding: utf-8 -*-
# owh (c)  Thomas C Hicks

from flask_marshmallow.fields import fields
from flask_diamond import db, ma
from flask_diamond.mixins.crud import CRUDMixin
from flask_diamond.mixins.marshmallow import MarshmallowMixin

class ThinPrepResultsSchema(ma.Schema):
    impressions = fields.Nested("ImpressionsSchema", allow_none=True, many=False)

    class Meta:
        additional = ('id', 'name')

class ThinPrepResults(db.Model, CRUDMixin, MarshmallowMixin):
    "Thin Prep test results for OWH"
    __schema__ = ThinPrepResultsSchema
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40))

    def __str__(self):
        return self.id, self.name
