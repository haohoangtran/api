from flask_restful import Resource, reqparse,request
from mongoengine import *



class Schdule(Document):
    name=StringField()
    date_start=StringField()
    date_end=StringField()
    time_study=StringField()
    class_room=StringField()