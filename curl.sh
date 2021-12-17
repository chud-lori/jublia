curl -X POST -H "Content-Type: application/json"  http://localhost:5001/save_emails --data '{"event_id": "1", "email_subject": "A good seminar", "email_content": "You should come to this seminar", "timestamp": "2021-12-16 13:05:00"}'
curl -X GET -H "Content-Type: application/json"  http://localhost:5000/test
curl -X GET -H "Content-Type: application/json"  http://localhost:5000/send