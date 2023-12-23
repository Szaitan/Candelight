from django.shortcuts import render, reverse
from django.views import View
import datetime
from candelight_website.models import RealisationsProject, RealisationsType
from django.http import JsonResponse
from candelight_website.forms import ContactMeForm
import os
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
            print(os.environ.get("TEST"))
            return render(request, "candelight_website/contact_page.html", {
                "form": form
            })

        def post(self, request):
            form = ContactMeForm(request.POST)
            if form.is_valid():
                return render(request, "candelight_website/contact_page.html", {
                    "form": form
                })
            else:
                return render(request, "candelight_website/contact_page.html", {
                    "form": form
                })
