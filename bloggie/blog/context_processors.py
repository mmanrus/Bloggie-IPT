# context_processors.py

from .models import Category

def category_menu(request):
    # Retrieve category menu data from the database
    category_menu_list = Category.objects.all()
    
    # Return the category menu data as a dictionary
    return {'category_menu_list': category_menu_list}
