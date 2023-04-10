from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from project import settings
from .models import Post, Category
import datetime


def send_notifications(preview, pk, article, subscribers):
    html_content = render_to_string(
        'postcreate_mail.html',
        {
           'text':preview,
            'link':f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=article,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def notify_about_new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers = []

    for category in categories:
        subscribers += category.subscribers.all()
    subscribers = [s.email for s in subscribers]

    send_notifications(post.preview(), post.pk, post.article, subscribers)


@shared_task
def notify_every_week():
   # today = datetime.datetime.now()
   last_week = datetime.datetime.now() - datetime.timedelta(days=7)
   posts = Post.objects.filter(time_in__gte=last_week)
   categories = set(posts.values_list('category__name', flat=True))
   subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

   html_content = render_to_string(
       'weekly_post.html',
       {
           'link': settings.SITE_URL,
           'news': posts,
       }
   )

   msg = EmailMultiAlternatives(
       subject='Статьи за неделю',
       body='',
       from_email=settings.DEFAULT_FROM_EMAIL,
       to=subscribers,
   )

   msg.attach_alternative(html_content, 'text/html')
   msg.send()
