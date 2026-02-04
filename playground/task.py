from time import sleep
from celery import shared_task

@shared_task
def notify_customer(message):
    print("Sending mails 10k...")
    print(message)
    sleep(10)
    print("Emails are successfully sent!")