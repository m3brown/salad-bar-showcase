from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from healthy_salad_chooser.models import Ingredient

# Create your views here.
def index(request):
	ingredient_list = Ingredient.objects.order_by('-name')
	context = {'ingredient_list': ingredient_list}
	return render(request, 'healthy_salad_chooser/index.html', context)

def about(request):
	context = {}
	return render(request, 'healthy_salad_chooser/about.html', context)

def detail(request, id):
	ingredient = get_object_or_404(Ingredient, pk=id)
	price = '%.2f' % (float(ingredient.weight_in_oz) * (7.99/16.0))
	return render(request, 'healthy_salad_chooser/detail.html', {'ingredient': ingredient, 'price': price})