from django.shortcuts import render, reverse, redirect
from django.views import View
import datetime
from candelight_website.models import RealisationsProject, RealisationsType, ProductsProduct, ProductsInternalExternal
from django.http import JsonResponse
from candelight_website.forms import ContactMeForm
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# Create your views here.

def get_year():
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


def get_products(request, type_id):
    print(type_id)
    if type_id == "Internal" or type_id == "External":
        products = ProductsProduct.objects.filter(main_group__name=type_id)
    elif type_id == "All":
        products = ProductsProduct.objects.all()
    else:
        products = ProductsProduct.objects.filter(sub_group__name=type_id)

    products_data = [{'name': product.name,
                      'main_image': product.main_image.url} for product in products]
    return JsonResponse(products_data, safe=False)


class IndexPageView(View):
    def get(self, request):
        year = get_year()
        return render(request, "candelight_website/main_page.html", {
            "year": year
        })


class AboutPageView(View):
    def get(self, request):
        year = get_year()
        return render(request, "candelight_website/about_page.html", {
            "year": year,
        })


class RealisationsPageView(View):
    def get(self, request):
        year = get_year()
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
        year = get_year()
        print(os.environ.get("TEST"))
        return render(request, "candelight_website/contact_page.html", {
            "form": form,
            "tear": year
        })

    def post(self, request):
        year = get_year()
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


class ProductsPageView(View):
    def get(self, request):
        main_group_list = []
        sub_group_list = []
        sub_group_dic = {}

        main_group_data = ProductsInternalExternal.objects.all()
        for group in main_group_data:
            # Names of main group
            main_group_list.append(group.name)

            # Names of the subgroup for each main group
            sub_group = group.productsproduct_set.all()

            sub_group_to_add = []
            for sub_product in sub_group:
                x = sub_product.sub_group.name
                if x not in sub_group_to_add:
                    sub_group_to_add.append(x)
            sub_group_list.append(sub_group_to_add)

        for n in range(len(main_group_list)):
            sub_group_dic[main_group_list[n]] = sub_group_list[n]

        year = get_year()
        all_products = ProductsProduct.objects.all()
        return render(request, "candelight_website/products_page.html", {
            "year": year,
            "all_products": all_products,
            "main_group_list": main_group_list,
            "sub_group_dic": sub_group_dic,
        })
