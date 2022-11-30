from django.shortcuts import render, get_object_or_404
from store.models import Pet, Category, BannerImage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# def Index(request):
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return render(request, 'store/navbar.html', context)


def home(request):
    # pets = Pet.objects.all()
    banner_images = BannerImage.objects.all()
    items = []
    categories = Category.objects.all()
    for category in categories:
        items.extend(list(Pet.objects.filter(category=category)[:2]))
    context = {'pets': items,
               'banner_images': banner_images,
               'categories': categories}
    return render(request, 'home.html', context)


def store(request):
    pets = Pet.objects.all()
    pet_count = Pet.objects.all().count
    categories = Category.objects.all()
    context = {'pets': pets, 'pet_count': pet_count, 'categories': categories}
    return render(request, 'store/store.html', context)


def Pet_Details(request, id):
    pet = Pet.objects.get(pk=id)
    categories = Category.objects.all()
    return render(request, 'store/pet_details.html', context={'pet': pet, 'categories': categories})


def Pet_Details_Categorised(request, id):
    category = Category.objects.get(pk=id)
    categories = Category.objects.all()
    pets = Pet.objects.filter(category=category)
    section_title = category.title
    return render(request, 'store/single_pet.html', context={'pets': pets, 'section_title': section_title, 'categories': categories})


# def home(request):
#     animals = Animal_Details.objects.all().order_by('-animal_id')[:8]
#     banner_images = BannerImage.objects.all()
#     contex = {
#         'animals':animals,
#         'banner_images':banner_images,
#     }
#     return render(request, 'home.html', contex)


# def store(request,animalcategory_slug = None):
#     animal_categories = None
#     animals = None
#     if animalcategory_slug != None:
#         animal_categories = get_object_or_404(AnimalCategory, slug = animalcategory_slug)
#         animals = Animal_Details.objects.all().filter(animal_type = animal_categories)
#         paginator = Paginator(animals, 8)
#         page = request.GET.get('page')
#         paged_animals = paginator.get_page(page)


#     else:
#         animals = Animal_Details.objects.all()
#         paginator = Paginator(animals, 8)
#         page = request.GET.get('page')
#         paged_animals = paginator.get_page(page)


#     animals_count = animals.count()
#     contex = {
#         'animals': paged_animals,
#         'animals_count':animals_count,
#     }
#     return render(request, 'store/store.html', contex)

# def animal_detial(request, animal_category_slug, animal_slug ):
#     try:
#         single_animal = Animal_Details.objects.get(animal_type__slug = animal_category_slug, slug = animal_slug)
#     except Exception as e:
#         raise e

#     context = {
#         'single_animal' : single_animal
#     }
#     return render (request, 'store/animal_detail.html', context)

# def search(request):
#     animals = None
#     animals_count = None
#     print('one test')
#     if 'keyword' in request.GET:
#         print('one get')
#         keyword = request.GET['keyword']
#         if keyword:
#             animals = Animal_Details.objects.order_by('-animal_id').filter(Q(breed__icontains=keyword) | Q(animal_type__animal_cat__icontains=keyword))
#             animals_count = animals.count()
#     context = {
#         'animals':animals,
#         'animals_count':animals_count,
#     }
#     return render(request, 'store/store.html', context)

# def sign_up(request):
