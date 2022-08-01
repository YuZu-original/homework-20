from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from app.container import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @director_ns.doc(description="get all directors")
    def get(self):
        directors = director_service.get_all()
        return DirectorSchema(many=True).dump(directors), 200

    @director_ns.doc(description="create new director")
    def post(self):
        req_json = request.json
        ent = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{ent.id}"}


@director_ns.route('/<int:bid>')
class DirectorView(Resource):
    @director_ns.doc(description="get director by id")
    def get(self, bid):
        director = director_service.get_one(bid)
        return DirectorSchema().dump(director), 200

    @director_ns.doc(description="update all info about director")
    def put(self, bid):
        req_json = request.json
        req_json["id"] = bid
        director_service.update(req_json)
        return "", 204

    @director_ns.doc(description="partially update info about director")
    def patch(self, bid):
        req_json = request.json
        req_json["id"] = bid
        director_service.partially_update(req_json)
        return "", 204

    @director_ns.doc(description="delete director")
    def delete(self, bid):
        director_service.delete(bid)
        return "", 204
