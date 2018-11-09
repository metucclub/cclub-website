from .models import CarouselItem

def add_variables_to_context(request):
    return {
        'carousel_items': CarouselItem.objects.all()
    }
