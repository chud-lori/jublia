from app import db

class Event(db.Model):
    """Model for Event"""

    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    emails = db.relationship('Email', backref='event', lazy=True)

    def __init__(self, name):
        self.name = name

class Email(db.Model):
    """Model for emails."""

    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'),
        nullable=False)
    email_subject = db.Column(db.String(255), nullable=False)
    email_content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String, nullable=False, default="Unsend")

    def __init__(self, event_id, email_subject, email_content, timestamp):
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.timestamp = timestamp

    def __repr__(self):
        return '<Email subject {}>'.format(self.email_subject)
        # return {'name': self.name, 'username': self.username, 'gender': self.gender.value, 'birthdate': birthdate}


class Recipient(db.Model):
    """Model for recipients."""

    __tablename__ = 'recipients'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return '<Address {}>'.format(self.address)

