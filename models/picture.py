from db import db


class PictureModel(db.Model):
    __tablename__ = 'pictures'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(100))
    size = db.Column(db.Integer)

    website_id = db.Column(db.Integer, db.ForeignKey('websites.id'))

    def __init__(self, filename, path, size, website_id):
        self.filename = filename
        self.path = path
        self.size = size
        self.website_id = website_id

    def json(self):
        return {'filename': self.filename, 'path': self.path, 'size': self.size}

    @classmethod
    def find_by_name(cls, filename):  # TODO: correct it since there is no picture name
        return cls.query.filter_by(name=filename).first()

    @classmethod
    def find_by_id(cls, _id):  # TODO: correct it since there is no picture name
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
