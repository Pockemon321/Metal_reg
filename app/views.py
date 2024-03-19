from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from Metal.settings import DOMAIN_URL
from django.views.decorators.csrf import csrf_exempt
from app.forms import ProductForm
from app.models import Product

# Create your views here.


def index(request):
    context = {
        "DOMAIN_URL": DOMAIN_URL,
    }
    try:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path_info)
        else:
            form = ProductForm()

        products = Product.objects.all()
        context.update({
            "products": products,
            "form": form  # Добавляем форму в контекст
        })
        return render(request, 'app/index.html', context)
    except Exception as e:
        return HttpResponse(f"<h1>Произошла ошибка: </h1> {e}")
    
    
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm(instance=product)

    return render(request, 'index.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'message': 'Продукт успешно удален!'})

    return render(request, 'app/index.html', {'product': product})


def delivery(request):
    return render(request, 'app/delivery.html')


def about(request):
    return render(request, 'app/about.html')

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(cotext.items()) + list(c_def.items()))
