# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from django.template.loader import render_to_string
#
# from project import settings
# from simpleapp.models import PostCategory
#
#
# def send_notifications(preview, pk, article, subscribers):
#     html_content = render_to_string(
#         'postcreate_mail.html',
#         {
#            'text':preview,
#             'link':f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=article,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(pk):

#        categories = instance.category.all()
#        subscribers: list[str] = []
#
#        for category in categories:
#            subscribers += category.subscribers.all()
#        subscribers = [s.email for s in subscribers]
#
#        send_notifications(instance.preview(), instance.pk, instance.article, subscribers)
