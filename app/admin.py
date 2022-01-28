from django.contrib import admin
from .models import MainCategory , Category, SubCategory


# Register your models here.


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

# We Have the use jquery as we need ajax;


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["main_category", "name"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["category", "main_category", "name"]
    class Media:
        js = (
            'category-sub-category-dropdown-select.js', # In your static folder and write the logic in this file.
             'https://code.jquery.com/jquery-3.3.1.min.js' # Jquery CDN
        )
