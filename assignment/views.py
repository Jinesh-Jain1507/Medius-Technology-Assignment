from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
import os

def send_email(request):
    subject = "Python (Selenium) Assignment - Jinesh Jain"
    body = "Please find attached my assignment submission, including the source code, screenshot of the form submission, my approach to the problem, my past projects and my resume.\n\nGithub link: https://github.com/Jinesh-Jain1507/Medius-Technology-Assignment \n\nLink to my previous projects can be found at my GitHub profile: https://github.com/Jinesh-Jain1507 \n\n I am available to work for the full 6 months internship at the time specified by you."

    email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, ['tech@themedius.ai'], cc=['hr@themedius.ai'])

    screenshot_path = '../../confirmation_page.png'
    if os.path.exists(screenshot_path):
        email.attach_file(screenshot_path)

    resume_path = '../../Resume.pdf'
    if os.path.exists(resume_path):
        email.attach_file(resume_path)

    email.send()

    return render(request, 'email_sent.html')
