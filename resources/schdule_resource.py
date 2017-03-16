from flask_restful import Resource, reqparse
import mlab
from models.schdule_teacher import Schdule


class SchduleRes(Resource):
    def get(self):
        schdule = Schdule.objects();
        return mlab.item2json(schdule)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="date_start", type=str, location="json")
        parser.add_argument(name="date_end", type=str, location="json")
        parser.add_argument(name="time_study", type=str, location="json")
        parser.add_argument(name="class_room", type=str, location="json")
        body = parser.parse_args()

        name = body.name
        date_start = body.date_start
        date_end = body.date_end
        time_study = body.time_study
        class_room = body.class_room
        schdule = Schdule(name=name, date_start=date_start, date_end=date_end, time_study=time_study,
                         class_room=class_room)
        schdule.save()
        add_schdule=Schdule.objects().with_id(schdule.id)
        return mlab.item2json(add_schdule)
