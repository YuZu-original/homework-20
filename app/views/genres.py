from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from app.container import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @genre_ns.doc(description="get all genres")
    def get(self):
        genres = genre_service.get_all()
        return GenreSchema(many=True).dump(genres), 200

    @genre_ns.doc(description="create new genre")
    def post(self):
        req_json = request.json
        ent = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{ent.id}"}


@genre_ns.route('/<int:bid>')
class GenreView(Resource):
    @genre_ns.doc(description="get genre by id")
    def get(self, bid):
        genre = genre_service.get_one(bid)
        return GenreSchema().dump(genre), 200

    @genre_ns.doc(description="update all info about genre")
    def put(self, bid):
        req_json = request.json
        req_json["id"] = bid
        genre_service.update(req_json)
        return "", 204

    @genre_ns.doc(description="partially update info about genre")
    def patch(self, bid):
        req_json = request.json
        req_json["id"] = bid
        genre_service.partially_update(req_json)
        return "", 204

    @genre_ns.doc(description="delete genre")
    def delete(self, bid):
        genre_service.delete(bid)
        return "", 204
