from .models import Pet, Category


def menu_links(request):
    links = Pet.objects.all()
    return dict(links=links)
