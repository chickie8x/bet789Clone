from bet.models import Category


def passContextToBaseTemplate(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return context
