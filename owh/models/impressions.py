# -*- coding: utf-8 -*-
# owh (c)  Thomas C Hicks

#from flask_marshmallow.fields import fields
from flask_diamond import db, ma
from flask_diamond.mixins.crud import CRUDMixin
from flask_diamond.mixins.marshmallow import MarshmallowMixin

class ImpressionsSchema(ma.Schema):
    class Meta:
        additional = ("id", "impression")

class Impressions(db.Model, CRUDMixin, MarshmallowMixin):
    "Impressions from the lab come in certain types"
    __schema__ = ImpressionsSchema
    id = db.Column(db.Integer, primary_key=True)
    impression = db.Column(db.String(80), unique=True)
    thinprepresults = db.relationship("ThinPrepResults", backref=db.backref('impressions', lazy='dynamic'))
    thinprepresults_id = db.Column(db.Integer(), db.ForeignKey('thinprepresults_id'))

    def __str__(self):
        return self.impression
