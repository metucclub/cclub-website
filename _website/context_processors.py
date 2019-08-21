from django.utils import translation

from .models import *

def add_variables_to_context(request):
    lang = translation.get_language()

    options = Option.objects.all()

    if len(options) != 0: options = options[0]

    main_carousel_items = CarouselItem.objects.all()

    main_site_menu_pages_left = FlatPage.objects.filter(site='main', item_place='l', add_to_menu=True)
    main_site_menu_pages_right = FlatPage.objects.filter(site='main', item_place='r',  add_to_menu=True)

    contest_site_menu_pages_left = FlatPage.objects.filter(site='contest', item_place='l',  add_to_menu=True)
    contest_site_menu_pages_right = FlatPage.objects.filter(site='contest', item_place='r', add_to_menu=True)

    contest_site_sponsors_page = FlatPage.objects.get(site='contest', name='sponsors')

    return {
        'lang': lang,
        'options': options,
        'main_carousel_items': main_carousel_items,
        'main_site_menu_pages_left': main_site_menu_pages_left,
        'main_site_menu_pages_right': main_site_menu_pages_right,
        'contest_site_menu_pages_left': contest_site_menu_pages_left,
        'contest_site_menu_pages_right': contest_site_menu_pages_right,
        'contest_site_sponsors_page': contest_site_sponsors_page,
    }
