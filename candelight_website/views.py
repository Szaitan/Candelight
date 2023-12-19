from django.shortcuts import render, reverse
from django.views import View
import datetime
# Create your views here.


def get_date():
    year = datetime.date.today().year
    return year


class IndexPageView(View):
    def get(self, request):
        year = get_date()
        return render(request, "candelight_website/main_page.html", {
            "year": year
        })
