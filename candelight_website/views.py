from django.shortcuts import render, reverse
from django.views import View

# Create your views here.


class IndexPageView(View):
    def get(self, request):
        return render(request, "candelight_website/index_page.html")
