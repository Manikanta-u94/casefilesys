from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

from login.forms import SignInForm
from django.http.response import JsonResponse

from login.models import LoginPageImage, LogoPolicy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    form_class = SignInForm
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        return super().get_success_url()

@csrf_exempt
def login_images(request):
    log_img_obj = LoginPageImage.objects.filter(is_active=True)

    header = LogoPolicy.objects.get(id=2)
    if header:
        policy_text = header.policy
        company_logo = header.company_logo.name
    else:
        policy_text = ""
        company_logo = ""
    images = []
    names = []
    subtitle = []

    for img in log_img_obj:
        images.append(img.image.name)
        names.append(img.name)
        subtitle.append(img.subtitle)

    context = {"images": images,  "names":names, "subtitle":subtitle, "policy_text":policy_text, "header": company_logo}

    return JsonResponse(context, safe=False)


