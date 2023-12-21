from django.shortcuts import render, reverse
from django.views import View
import datetime
from candelight_website.models import RealisationsProject, RealisationsType
from django.http import JsonResponse
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
        print(request.path)
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

