from django.shortcuts import render
from productapp.models import Product
from django.shortcuts import redirect

# Create your views here.
def home(request):
    
    return render(request,'index.html')
    

def addproduct(request):
    return render(request, 'addproduct.html')
    
    

def allproduct(request):
    context={}
    data=Product.objects.all()
    print(type(data))
    context['products']=data
    return render (request,'allproduct.html',context)

def saveproduct(request):
    print(request.method)
    n=request.POST['Name']
    c=request.POST['Company']
    p=int(request.POST['Price'])
    #print(n,c,p)
    print(type(n),type(c),type(p))
    pr=Product.objects.create(name=n,company=c,price=p)
    pr.save()
    return redirect ('/all')

def deleteproduct(request, rid):
    product=Product.objects.filter(id=rid)
    print(type(product))
    product.delete()
    context={'success':'Product deleted!!'}
    return redirect('/all')



def editproduct(request,rid):
    product=Product.objects.filter(id=rid)
    context={}
    if request.method=="GET":
        context['product']=product[0]
        return render(request,'editproduct.html',context)
    else:
        n=request.POST['Name']
        c=request.POST['Company']
        p=int(request.POST['Price'])
        product.update(name=n,company=c,price=p)
        return redirect('/all')



