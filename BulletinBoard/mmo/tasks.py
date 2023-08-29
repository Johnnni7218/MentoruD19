from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import render

from .models import Post, Feedback


@shared_task
def accept_alert():
    user = Feedback.objects.get(id=id).user.email
    send_mail(
        subject='Реакция на Ваш отзыв',
        message='Ваш отзыв принят автором объявления',
        from_email='Maclac1267@yandex.ru',
        recipient_list=[user.email],
    )


@shared_task
def new_post():
    for users in Post.objects.all():
        send_mail(
            subject='Навости нашего портала',
            message='На нашем портале создано новое объявление',
            from_email='Maclac1267@yandex.ru',
            recipient_list=[users.email],
        )
