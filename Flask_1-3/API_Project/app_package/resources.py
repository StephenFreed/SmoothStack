from flask import jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from app_package import application, api, db
from app_package.models import BlogPostModel


# argument parser
blogpost_post_args = reqparse.RequestParser()
blogpost_post_args.add_argument("author", type=str, help="Name Of Author Missing", required=True)
blogpost_post_args.add_argument("title", type=str, help="Name Of Title Missing", required=True)
blogpost_post_args.add_argument("likes", type=int, help="Likes Of The Post Missing", required=True)

# put to change no fields requred
blogpost_put_args = reqparse.RequestParser()
blogpost_put_args.add_argument("author", type=str, help="Name Of Author Missing", required=False)
blogpost_put_args.add_argument("title", type=int, help="Name of Title Missing", required=False)
blogpost_put_args.add_argument("likes", type=int, help="Likes Of The Post Missing", required=False)


resource_fields = {
    "id": fields.Integer,
    "author": fields.String,
    "title": fields.String,
    "likes": fields.Integer
}


class HelloWorld(Resource):
    def get(self, name):
        return {"Hello": name}


class BlogPost(Resource):
    @marshal_with(resource_fields)  # serializes vs resource_fields dict
    def get(self, post_id):
        result = BlogPostModel.query.filter_by(id=post_id).first()
        if not result:
            abort(404, message="Could Not Find Post Id...")
        return result

    @marshal_with(resource_fields)
    def post(self, post_id):
        args = blogpost_post_args.parse_args()
        in_db = BlogPostModel.query.filter_by(id=post_id).first()
        if in_db:
            abort(409, message="Post ID Already Exists...")
        blog_post = BlogPostModel(id=post_id, author=args["author"], title=args["title"], likes=args["likes"])
        db.session.add(blog_post)
        db.session.commit()
        return blog_post, 201

    @marshal_with(resource_fields)
    def put(self, post_id):
        args = blogpost_put_args.parse_args()
        result = BlogPostModel.query.filter_by(id=post_id).first()
        if not result:
            abort(404, message="Post Does Not Exist - Can't Update")
        if args["author"]:
            result.author = args["author"]
        if args["title"]:
            result.title = args["title"]
        if args["likes"]:
            result.likes = args["likes"]
        db.session.commit()
        return result


    def delete(self, post_id):
        result = BlogPostModel.query.filter_by(id=post_id).first()
        if not result:
            return jsonify({"message": "Can Not Delete, Id Not Found"})
        user_obj = db.session.get(BlogPostModel, post_id)
        db.session.delete(user_obj)
        db.session.commit()
        is_deleted = BlogPostModel.query.filter_by(id=post_id).first()
        if is_deleted:
            return jsonify({"message": "Post Was Not deleted"})
        return jsonify({"message": "Post Successfully Deleted"})



class BlogPostList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = BlogPostModel.query.filter_by(id=1).first()
        if not result:
            abort(404, message="There Are No Posts...")
        all_posts = BlogPostModel.query.all()
        return all_posts


api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(BlogPost, "/api/post/<int:post_id>")
api.add_resource(BlogPostList, "/api/blogpostlist")
