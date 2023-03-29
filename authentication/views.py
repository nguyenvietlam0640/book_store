from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView, Response
from .models import User
from django.forms.models import model_to_dict

import hashlib
from .serializers import UserSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
from django.conf import settings
import jwt
import datetime

url = 'https://lamnv-bookstore.netlify.app'
def passwordEncryption(password: str):
    encypted = hashlib.sha256(password.encode()).hexdigest()
    return encypted


def sendEmail(subject, textContent, fromEmail, toEmail, htmlContent):
    msg = EmailMultiAlternatives(
        subject=subject, body=textContent, from_email=fromEmail, to=[toEmail])
    msg.attach_alternative(htmlContent, 'text/html')
    msg.send()


def sendActivateEmail(request, user):
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    link = f'{url}/activate/{token}'
    # send email reset password
    subject = 'BookStore Activate'
    textContent = None
    fromEmail = 'settings.EMAIL_HOST_USER'
    toEmail = user.email
    context = {'user': user, 'link': link}

    htmlContent = render_to_string(
        'activate.html', context=context, request=request)

    sendEmail(subject=subject, textContent=textContent,
              fromEmail=fromEmail, toEmail=toEmail, htmlContent=htmlContent)


def sendResetPassEmail(request, user):
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    link = f'{url}/change_password/{token}'
    # send email reset password
    subject = 'BookStore forgot password'
    textContent = None
    fromEmail = 'settings.EMAIL_HOST_USER'
    toEmail = user.email
    context = {'user': user, 'link': link}

    htmlContent = render_to_string(
        'forgotpassword.html', context=context, request=request)

    sendEmail(subject=subject, textContent=textContent,
              fromEmail=fromEmail, toEmail=toEmail, htmlContent=htmlContent)


class RegisterApi(APIView):

    def post(self, request, format=None):
        data = request.data
        data['password'] = passwordEncryption(data['password'])
        user = UserSerializer(data=data)
        user.is_valid(raise_exception=True)
        user.save()
        user = User.objects.filter(email=data['email']).first()
        sendActivateEmail(request, user)
        return Response({'message': 'Account created successfully, Please check your email to verify your account'})


class SendActivateEmailApi(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if user:
            sendActivateEmail(request, user)
            return Response({'message': 'email sent successfully'})
        return Response({'message': 'user not found'}, status=403)


class ActivateApi(APIView):
    def post(self, request):

        data = request.data
        token = data['token']
        if token:
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user = User.objects.filter(id=payload['id']).first()
                if not user.is_activated:
                    user.is_activated = True
                    user.save()
                    return Response({'message': 'Your account had activated succesfully, please login.'})
                return Response({'message': 'your account had activated, please login.'}, status=403)
            except:
                pass
        return Response({'message': 'Your request invalidation or expired, just login and send a request again.'}, status=403)


class LoginApi(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:

            return Response({'message': 'Wrong email or password'}, status=403)

        if passwordEncryption(password) == user.password:
            if user.is_activated:
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=1),
                    'iat': datetime.datetime.utcnow()
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256')

                response = Response()
                response.set_cookie(key='jwt', value=token, httponly=True)
                response.data = {'message': 'success', 'jwt': token}

                return response

            return Response({'message': 'Your account was not activated, please check your email for confirming. In case there is notthing was sent,'}, status=403)

        return Response({'message': 'Wrong email or password'}, status=403)


class UserApi(APIView):
    def get(self, request):
        
        token = request.headers.get('Authorization')

        if token:
            token = token[3:]
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user = User.objects.filter(id=payload['id']).first()

                userSerializer = UserSerializer(user)
                return Response(userSerializer.data)
            except:
                pass
        return Response({'message': 'Unauthenticated'}, status=403)


class ResetPassApi(APIView):
    def post(self, request):
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        if user:
            sendResetPassEmail(request, user)
        return Response(
            {'message': 'A confirm password link had sent to your email, please check your inbox'})


class ChangePassApi(APIView):
    def post(self, request):
        data = request.data
        token = data['token']
        if token:
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user = User.objects.filter(id=payload['id']).first()
                user.password = passwordEncryption(data['password'])
                user.save()
                return Response({'message': 'Password changed successfully, please login.'})
            except:
                pass
        return Response({'message': 'Your request invalidation or expired, please send your request again.'}, status=403)
