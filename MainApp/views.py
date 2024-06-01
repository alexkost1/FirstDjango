from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home(request):
   
    return render(request, 'index.html')

def about(request):
    text = """
    <p>Имя: <b>Алексей</b><br>
    Отчество: <b>Дмитриевич</b><br>
    Фамилия: <b>Костюкович</b><br>
    Телефон: <b>914-2091152</b><br>
    email: <b>tennohi@yandex.ru</b></p>
    <nav>
    <ul>
      <li><a href="items">Товары</a></li>
      <li><a href="/">Главная</a></li>
    </ul>
  </nav>
    """
    return HttpResponse(text)



def get_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(f"Item with id={id} not found")
    else:
        context = {"item": item}
        return render(request, "item.html", context)
    
            

def get_items(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'items.html', context)


