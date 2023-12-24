from django.shortcuts import render, reverse, redirect
from django.views import View
import datetime
from candelight_website.models import RealisationsProject, RealisationsType
from django.http import JsonResponse
from candelight_website.forms import ContactMeForm
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# Create your views here.


def get_date():
    year = datetime.date.today().year
    return year


def get_realizations(request, type_id):

    if type_id is not None and type_id != 0:
        realizations = RealisationsProject.objects.filter(category_id=type_id)
    else:
        realizations = RealisationsProject.objects.all()

    realization_data = [{'title': realization.title,
                         'category': str(realization.category),
                         'description': realization.description,
                         'image_url': realization.image.url} for realization in realizations]
    return JsonResponse(realization_data, safe=False)


class IndexPageView(View):
    def get(self, request):
        year = get_date()
        return render(request, "candelight_website/main_page.html", {
            "year": year
        })


class AboutPageView(View):
    def get(self, request):
        year = get_date()
        return render(request, "candelight_website/about_page.html", {
            "year": year,
        })


class RealisationsPageView(View):
    def get(self, request):
        year = get_date()
        button_types = RealisationsType.objects.all()
        realization_data = [
            {'title': realization.title,
             'category': realization.category,
             'description': realization.description,
             'image_url': realization.image.url} for
            realization in RealisationsProject.objects.all()]

        return render(request, "candelight_website/realisations_page.html", {
            "button_types": button_types,
            "realization_data": realization_data,
            "year": year
        })


class ContactPageView(View):
        def get(self, request):
            form = ContactMeForm()
            year = get_date()
            print(os.environ.get("TEST"))
            return render(request, "candelight_website/contact_page.html", {
                "form": form,
                "tear": year
            })

        def post(self, request):
            year = get_date()
            form = ContactMeForm(request.POST)
            if form.is_valid():
                clean_data = form.cleaned_data
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=os.environ.get("michal_mail"),
                                     password=os.environ.get("google_app_access_password"))

                    name = clean_data["name"]
                    last_name = clean_data["last_name"]
                    phone_number = clean_data["phone_number"]
                    email = clean_data["email"]
                    message = clean_data["message"]

                    msg = MIMEText(
                        f"Name: {name}\nLast Name: {last_name}\nPhone Number: {phone_number}\nEmail: {email}\n\n{message}",
                        'plain', 'utf-8')
                    msg['Subject'] = Header(name, 'utf-8').encode()
                    connection.sendmail(from_addr=os.environ.get("michal_mail"), to_addrs=os.environ.get("michal_mail"),
                                        msg=msg.as_string())

                return redirect(reverse("contact_page"))
            else:
                return render(request, "candelight_website/contact_page.html", {
                    "form": form,
                    "year": year,
                })
