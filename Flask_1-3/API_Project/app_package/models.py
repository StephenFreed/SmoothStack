from app_package import db

class BlogPostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Post(id = {self.id}, author = {self.author}, title = {self.title}, likes = {self.likes})"
