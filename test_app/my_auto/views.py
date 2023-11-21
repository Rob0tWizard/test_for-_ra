from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from lxml import etree
from .models import Brand, CarModel


#@require_GET
def update_catalog(request):
    Brand.objects.all().delete()
    CarModel.objects.all().delete()
    catalog_url = 'https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml'
    response = requests.get(catalog_url)
    root = etree.fromstring(response.content)

    # Brand.objects.all().delete()
    # CarModel.objects.all().delete()

    if response.status_code != 200:
        return HttpResponse('Что-то пошло не так')


    for brand_element in root.findall('.//mark[@name]'):
        brand_name = brand_element.get('name')
        brand_instance, created = Brand.objects.get_or_create(name=brand_name)

        for mod_element in brand_element.findall('.//folder[@name]'):
            model_name = mod_element.get('name').split(',')[0].strip()
            CarModel.objects.create(name=model_name, brand=brand_instance)

    return HttpResponse('Каталог готов, проверяй')


def home(request):
    brands = Brand.objects.all()
    models = []

    if request.method == 'POST':
        brand_id = request.POST.get('brand')

        if brand_id:
            models = CarModel.objects.filter(brand_id=brand_id)

    return render(request, 'my_auto/home.html', {'brands': brands, 'models': models})


