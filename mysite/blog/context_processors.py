from .models import Category

def category_list(request):
    categor = Category.objects.order_by('number')
    return {'categor': categor}