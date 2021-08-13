from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(120), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file} )"


class CleanerDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(120), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    services = db.Column(db.String(120))


if __name__ == '__main__':
    db.create_all()
