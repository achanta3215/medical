from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import Context
from django.template.loader import get_template
from .models import Staff,Customer,Bill,Medicine,Cart
from django.db.models import Max
# Create your views here.
def login(request):
    template = get_template('med/login.html')
    output = template.render()
    return HttpResponse(output)
def customer(request):
    login = request.GET.get('loginid','')
    password = request.GET.get('password','')
    staffLogin = Staff.objects.values_list('username').filter(username=login)[0][0]
    staffpassword = Staff.objects.values_list('password').filter(username=login)[0][0]
    if(staffLogin == login and staffpassword == password):
        template = get_template('med/customer.html')
        output = template.render()
        return HttpResponse(output)
    

def customer_add(request):
    template = get_template('med/customer_add.html')
    output = template.render()
    return HttpResponse(output)

def addtocart(request,*args,**kwargs):
    BillId = 0
    CustomerId = 0
    entry = False
    current_add = []
    all_add =[]
    zippedexternal = 5 
    try: #gets called for the first time
        BillId = args[0]
        CustomerId = args [1]
        
        entry = True
    except: #gets called while adding to cart
        pass
    if not entry:
        
        BillId = request.GET.get('bid','')
        CustomerId = request.GET.get('cid','')
        item = request.GET.get('item','')
        quantity = request.GET.get('qty','')
        # print(type(quantity))
        # html = "%s %s" % (item,quantity)
        # return HttpResponse(html)
        # html = "%s"%BillId
        # return HttpResponse(html)
        CartObject = Cart(bid=Bill(BillId),mid=Medicine(item),qty=quantity)
        CartObject.save()
        prices = []
        items = Cart.objects.values_list('mid').filter(bid=BillId)
        quantities = Cart.objects.values_list('qty').filter(bid=BillId)
        for item in items:
            prices.append(Medicine.objects.values_list('price').filter(mid=item[0])[0])
        
        
        zipped = zip(items,quantities,prices)
        # html = "%s %s %s %s" % (items,quantities,prices,zipped)
        # return HttpResponse(html)
        template = get_template('med/addtocart.html')
        variables = Context({
        'life': all_add,
        'bid' : BillId,
        'cid' : CustomerId,
        'zip' : zipped
        })
        
        output = template.render(variables)
        return HttpResponse(output)
    if entry:
        template = get_template('med/addtocart.html')
        variables = Context({
        'life': all_add,
        'bid' : BillId,
        'cid' : CustomerId,
        })
        output = template.render(variables)
        return HttpResponse(output)

def existingusercheck(request):
    cname = request.GET.get('cname','')
    cid = request.GET.get('cid','')
    ph = request.GET.get('ph','')
    
    customername = Customer.objects.values_list('cname').filter(cname=cname)[0][0]
    customerid = Customer.objects.values_list('cid').filter(cname=cname)[0][0]
    customerph = Customer.objects.values_list('phno').filter(cname=cname)[0][0]
    
    if(cname==customername  and cid==customerid and str(ph)==str(customerph)):
        return addBillId(request,cid)
    
def addBillId(request,cid):
    finalBillId=0
    billId = Bill.objects.all()
    if billId:
        maxBillId = billId.aggregate(maxBillId = Max('bid'))["maxBillId"]
        finalBillId = maxBillId = maxBillId + 1
        billobject = Bill(maxBillId,cid)
        billobject.save()
        
    else:
        finalBillId = 1
        billobject = Bill('1',cid)
        billobject.save()
    return addtocart(request,finalBillId,cid)
def add_database(request):
    cname = request.GET.get('cname','')
    cid = request.GET.get('cid','')
    ph = request.GET.get('ph','')
    p = Customer(cname=cname,cid=cid,phno=ph)
    p.save()
    return addBillId(request,cid)