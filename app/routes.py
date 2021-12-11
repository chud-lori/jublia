from flask import Blueprint, json, jsonify, redirect, request
from app import db, celery, redis_db
from app.models import *

app_bp = Blueprint("app_bp", __name__)



@app_bp.route("/timer")
def timer_view():
    time_counter = redis_db.mget(["minute", "second"])
    return f"Minute: {time_counter[0]}, Second: {time_counter[1]}"


@app_bp.route("/save_emails", methods=["POST"])
def post_email():
    if request.method == 'POST':
        if request.is_json == False:
            return jsonify({"message": "failed, please input in json format", "status": 0}), 400
        required = ["event_id", "email_subject", "email_content", "timestamp"]
        for req in required:
            if req not in request.json:
                return jsonify({"message": f"failed, {req} is required"}), 400
        email = Email(
            event_id=request.json["event_id"],
            email_subject=request.json["email_subject"],
            email_content=request.json["email_content"],
            timestamp=request.json["timestamp"],
        )
        try:
            db.session.add(email)
            db.session.commit()
            data = {
                "event_id": email.event_id,
                "email_subject": email.email_subject,
                "email_content": email.email_content,
                "timestamp": email.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            }
            return jsonify({"data": data, "message": "email created", "status": 1}), 201

        except:
            return jsonify({"message": "failed creating email"}), 500
        

@app_bp.errorhandler(404)
def page_not_found(e) -> tuple:
    """
        it will render if user got invalid route
    """
    return jsonify({'message': 'not found'}), 404