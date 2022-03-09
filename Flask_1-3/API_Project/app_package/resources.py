from flask import jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from app_package import api, db
from app_package.models import VideoModel

# argument parser
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name Of The Video Missing", required=True)
video_put_args.add_argument("views", type=int, help="Views Of The Video Missing", required=True  )
video_put_args.add_argument("likes", type=int, help="Likes Of The Video Missing", required=True)


video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name Of The Video Missing", required=False)
video_update_args.add_argument("views", type=int, help="Views Of The Video Missing", required=False)
video_update_args.add_argument("likes", type=int, help="Likes Of The Video Missing", required=False)



resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

class HelloWorld(Resource):
    def get(self, name):
        return {"Hello": name}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could Not Find Id...")
        return result

    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_put_args.parse_args()
        in_db = VideoModel.query.filter_by(id=video_id).first()
        if in_db:
            abort(409, message="Video id taken...")
        video = VideoModel(id=video_id, name=args["name"], views=args["views"], likes=args["likes"],)
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, Can't Patch")
        if args["name"]:
            result.name = args["name"]
        if args["views"]:
            result.views = args["views"]
        if args["likes"]:
            result.likes = args["likes"]
        db.session.commit()
        return result



    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            return jsonify({"message": "Can't Delete, Id Not Found"})
        user_obj = db.session.get(VideoModel, video_id)
        db.session.delete(user_obj)
        db.session.commit()
        is_deleted = VideoModel.query.filter_by(id=video_id).first()
        if is_deleted:
            return jsonify({"message": "User Was Not deleted"})
        return jsonify({"message": "User Deleted"})


api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")
