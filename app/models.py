from app import db

class Film(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	year = db.Column(db.Integer)
	genre = db.Column(db.String)
	platform = db.Column(db.String)
	summary = db.Column(db.String)
	image_url = db.Column(db.String)
	watched = db.Column(db.Boolean)

	def __repr__(self):
		return self.title