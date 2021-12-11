"""
run from python using flask run
"""

# from app import create_app

# # create instance app
# app = create_app()

# if __name__ == '__main__':
#     # run in debug mode
#     app.run(debug=True)

from flask.cli import FlaskGroup

from app import db, create_app
from app.models import Event

app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    # try:
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("tables created")
    # except:
    #     print("creating tables failed")

@cli.command("seed_db")
def seed_db():
    try:
        db.session.add(Event(name="Seminar"))
        db.session.commit()
        print("data seeded")
    except:
        print("seed failed")


if __name__ == "__main__":
    cli()