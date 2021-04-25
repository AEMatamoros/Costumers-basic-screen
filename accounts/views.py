from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .filters import OrderFilter
from .models import Product,Costumer,Order
from .forms import OrderForm

# Create your views here.
def home(request):
    order = Order.objects.all()
    costumer = Costumer.objects.all()

    total_costumers= costumer.count()
    total_order = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {"orders":order,"costumers":costumer,'total_costumers':total_costumers,'total_orders':total_order,'delivered':delivered,'pending':pending}

    return render(request,'accounts/base.html',context);

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{"products":products});

def costumer(request,pk):
    costumer = Costumer.objects.get(id=pk)
    orders = costumer.order_set.all()

    myFilter= OrderFilter(request.GET, queryset=Order.objects.all())
    orders  =myFilter.qs

    context = {"costumer":costumer,'orders':orders,'myFilter':myFilter}
    return render(request,'accounts/costumers.html',context);

def create_order(request, pk):

    OrderFormSet = inlineformset_factory(Costumer,Order, fields=('product','status'))
    costumer = Costumer.objects.get(id=pk)
    formset = OrderFormSet( queryset=Order.objects.none() ,instance=costumer)

    if(request.method=="POST"):
        #form = OrderForm(request.POST) 
        formset= OrderFormSet(request.POST, instance=costumer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context={'formset':formset}

    return render(request,'accounts/order_form.html',context)

def update_order(request, pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if(request.method=="POST"):
        form = OrderForm(request.POST, instance= order) 
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'accounts/order_form.html',context)

def delete_order(request, pk):
    order = Order.objects.get(id = pk)
    context = {'item':order}
    if(request.method=="POST"):
        order.delete()
        return redirect('/')
    return render(request,'accounts/delete.html', context)