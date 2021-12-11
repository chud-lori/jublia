from app import redis_db
from celeryconf import celery

# @celery.task(name='timer_app')
# def timer():
#     second_counter = int(redis_db.get("second")) + 1
#     print(second_counter)
#     if second_counter >= 59:
#         # Reset the counter
#         redis_db.set("second", 0)
#         # Increment the minute
#         redis_db.set("minute", int(redis_db.get("minute")) + 1)
#     else:
#         # Increment the second
#         redis_db.set("second", second_counter)