from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipe_var = Recipe.objects.all()   # gell all data
    context = {
        'title':"Recipe Book",
        'recipes' : recipe_var
    }
    return render(request, 'list.html', context)

# create data:
def create(request):
   # post process
    if request.method == "POST":
        name = request.POST.get('name')     # form ma create gareko name lekhni
        ingredient = request.POST.get('ingredient')
        instruction = request.POST.get('instruction')
        time =request.POST.get('time')
        level = request.POST.get('level') 
        Recipe.objects.create(name = name, ingredients = ingredient, instruction = instruction, time  = time, level = level)    # Recipe ma vako field_name = user bata aako name_variable mathi vako
        return redirect('/recipe/')
   #get process

    return render(request,"create.html")