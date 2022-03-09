from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
api = Api(application)
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLite development database // use PostgreSQL for production
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
db = SQLAlchemy(application)

class VideoModel(db.Model):
    pass

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name Of The Video Missing", required=True)
video_put_args.add_argument("views", type=int, help="Views Of The Video Missing", required=True  )
video_put_args.add_argument("likes", type=int, help="Likes Of The Video Missing", required=True)

videos = {}

def abort_if_not_found(video_id):
    if video_id not in videos:
        abort(404, message="Video ID Not Found")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video Already Exists With That ID...")

class HelloWorld(Resource):
    def get(self, name):
        return {"Hello": name}

class Video(Resource):
    def get(self, video_id):
        abort_if_not_found(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_not_found(video_id)
        del videos[video_id]
        return "Error", 204
        


api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")



if __name__ == "__main__":
    db.create_all()  # creates DB if there is not one
    application.run(debug=True)
