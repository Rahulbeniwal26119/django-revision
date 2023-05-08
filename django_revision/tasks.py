from django_revision.celery import app

@app.task(
    name="django_revision.tasks.send_mail",
    bind=True,
    autoretry_for=(Exception,),
    max_retries=3, 
    ignore_result=False,
    retry_backoff=3, 
    retry_jitter=0.1,
    retry_backoff_max=60 * 5
)
def send_mail(self, to_user, from_user, subject, message):
    import time
    time.sleep(10)
    print(f"Mail will be sent to {to_user} from {from_user} with subject {subject} and message {message}")
    return "OK"