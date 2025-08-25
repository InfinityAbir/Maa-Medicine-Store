from .models import Dealer, Employee, Customer, Medicine, Purchase
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages


def medformview2(request):
    return render(request, 'pharma/medformview2.html')


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'pharma/index.html')


# ---------------- Dealer ----------------
def dealerform(request):
    return render(request, 'pharma/dealer.html', {'add': True})


def dealerforminsert(request):
    try:
        dealer = Dealer(
            dname=request.POST['dname'],
            address=request.POST['address'],
            phn_no=request.POST['pno'],
            email=request.POST['email']
        )
        dealer.save()
        messages.success(request, "✅ New dealer added successfully.")
    except IntegrityError:
        return render(request, "pharma/new.html")
    return redirect('dealertable')


def dealerformupdate(request, foo):
    try:
        dealer = Dealer.objects.get(pk=foo)
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
        messages.success(request, "✅ Dealer details updated.")
    except IntegrityError:
        return render(request, "pharma/new.html")
    return redirect('dealertable')


def dealerformview(request, foo):
    return render(request, 'pharma/dealer.html', {'dealer': Dealer.objects.get(pk=foo)})


def dealerformdelete(request, foo):
    Dealer.objects.get(pk=foo).delete()
    messages.success(request, "✅ Dealer deleted.")
    return redirect('dealertable')


def dealertable(request):
    return render(request, 'pharma/dealertable.html', {"dealer": Dealer.objects.all()})


# ---------------- Employee ----------------
def empform(request):
    return render(request, 'pharma/emp.html', {'add': True})


def empforminsert(request):
    if request.method == "POST":
        try:
            emp = Employee(
                e_id=request.POST.get('eid'),
                fname=request.POST.get('fname'),
                lname=request.POST.get('lname'),
                address=request.POST.get('address'),
                email=request.POST.get('email'),
                sal=request.POST.get('sal'),
                phn_no=request.POST.get('pno')
            )
            emp.save()
            messages.success(request, "✅ New employee added successfully.")
        except IntegrityError:
            messages.error(request, "❌ Employee with this ID/Email/Phone already exists.")
            return render(request, "pharma/empform.html", {"add": True})
        return redirect('emptable')

    return render(request, "pharma/empform.html", {"add": True})

def empformupdate(request, foo):
    try:
        emp = Employee.objects.get(pk=foo)
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
        messages.success(request, "✅ Employee details updated.")
    except IntegrityError:
        return render(request, "pharma/new.html")
    return redirect('emptable')


def empformview(request, foo):
    return render(request, 'pharma/emp.html', {'emp': Employee.objects.get(pk=foo)})


def empformdelete(request, foo):
    Employee.objects.get(pk=foo).delete()
    messages.success(request, "✅ Employee deleted.")
    return redirect('emptable')


def emptable(request):
    return render(request, 'pharma/emptable.html', {"emp": Employee.objects.all()})


# ---------------- Customer ----------------
def custform(request):
    return render(request, 'pharma/cust.html', {'add': True})


def custforminsert(request):
    try:
        cust = Customer(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            address=request.POST['address'],
            phn_no=request.POST['pno'],
            email=request.POST['email']
        )
        cust.save()
        messages.success(request, "✅ New customer added successfully.")
    except IntegrityError:
        return render(request, "pharma/new.html")
    return redirect('custtable')


def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(pk=foo)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
        messages.success(request, "✅ Customer details updated.")
    except IntegrityError:
        return render(request, "pharma/new.html")
    return redirect('custtable')


def custformview(request, foo):
    return render(request, 'pharma/cust.html', {'cust': Customer.objects.get(pk=foo)})


def custformdelete(request, foo):
    Customer.objects.get(pk=foo).delete()
    messages.success(request, "✅ Customer deleted.")
    return redirect('custtable')


def custtable(request):
    return render(request, 'pharma/custtable.html', {"cust": Customer.objects.all()})


# ---------------- Medicine ----------------
def medform(request):
    # Get all dealers for dropdown
    dealers = Dealer.objects.all()
    return render(request, 'pharma/med.html', {'add': True, 'dealers': dealers})
def medforminsert(request):
    try:
        dealer_name = request.POST['dname']

        # Check if dealer exists
        if not Dealer.objects.filter(dname=dealer_name).exists():
            messages.error(request, "🚫 Dealer not found. Please add dealer first.")
            return redirect('medtable')

        # Add medicine if dealer exists
        med = Medicine(
            m_id=request.POST['mid'],
            mname=request.POST['mname'],
            dname=dealer_name,
            desc=request.POST['desc'],
            price=request.POST['price'],
            stock=request.POST['stock']
        )
        med.save()
        messages.success(request, "✅ New medicine added successfully.")

    except IntegrityError:
        return render(request, "pharma/new.html")

    return redirect('medtable')

def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(pk=foo)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
        messages.success(request, "✅ Medicine details updated.")
    except IntegrityError:
        return render(request, "pharma/new.html")
    return redirect('medtable')

def medformview(request, foo):
    med = Medicine.objects.get(pk=foo)
    dealers = Dealer.objects.all()  # Pass dealers for dropdown
    return render(request, 'pharma/med.html', {'med': med, 'dealers': dealers})

def medformdelete(request, foo):
    Medicine.objects.get(pk=foo).delete()
    messages.success(request, "✅ Medicine deleted.")
    return redirect('medtable')

def medtable(request):
    return render(request, 'pharma/medtable.html', {"med": Medicine.objects.all()})

# ---------------- Purchase ----------------
def purchaseform(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharma/purchase.html', {'add': True, 'medicines': medicines})


def purchaseforminsert(request):
    if request.method == "POST":
        pname = request.POST['pname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        qty = int(request.POST['qty'])
        pno = request.POST['pno']
        price = int(request.POST['price'])

        try:
            medicine = Medicine.objects.get(mname=pname)
        except Medicine.DoesNotExist:
            messages.error(request, f"❌ '{pname}' is not available right now.")
            return redirect('purchaseform')

        if medicine.stock < qty:
            messages.error(request, f"❌ Only {medicine.stock} units of '{pname}' are available.")
            return redirect('purchaseform')

        try:
            purchase = Purchase(
                pname=pname,
                fname=fname,
                lname=lname,
                qty=qty,
                phn_no=pno,
                price=price,
                total=price * qty
            )
            purchase.save()

            medicine.stock -= qty
            medicine.save()

            messages.success(request, f"✅ Purchased {qty} units of '{pname}'.")

            # Low stock alert threshold
            LOW_STOCK_THRESHOLD = 10
            if medicine.stock < LOW_STOCK_THRESHOLD:
                messages.warning(request, f"⚠️ Stock for '{pname}' is low: only {medicine.stock} units left.")

        except IntegrityError:
            return render(request, "pharma/new.html")

        return redirect('purchasetable')

    return redirect('purchaseform')

def purchaseformupdate(request, foo):
    if request.method == "POST":
        try:
            purchase = Purchase.objects.get(pk=foo)
        except Purchase.DoesNotExist:
            messages.error(request, "❌ Purchase record not found.")
            return redirect('purchasetable')

        pname = request.POST['pname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        qty = int(request.POST['qty'])
        pno = request.POST['pno']
        price = int(request.POST['price'])

        # Restore old stock first
        try:
            old_medicine = Medicine.objects.get(mname=purchase.pname)
            old_medicine.stock += purchase.qty
            old_medicine.save()
        except Medicine.DoesNotExist:
            pass

        try:
            medicine = Medicine.objects.get(mname=pname)
        except Medicine.DoesNotExist:
            messages.error(request, f"❌ '{pname}' is not available right now.")
            return redirect('purchaseform')

        if medicine.stock < qty:
            messages.error(request, f"❌ Only {medicine.stock} units of '{pname}' are available.")
            return redirect('purchaseform')

        try:
            purchase.pname = pname
            purchase.fname = fname
            purchase.lname = lname
            purchase.qty = qty
            purchase.phn_no = pno
            purchase.price = price
            purchase.total = price * qty
            purchase.save()

            medicine.stock -= qty
            medicine.save()

            messages.success(request, f"✅ Purchase updated successfully.")

            # Low stock alert threshold
            LOW_STOCK_THRESHOLD = 10
            if medicine.stock < LOW_STOCK_THRESHOLD:
                messages.warning(request, f"⚠️ Stock for '{pname}' is low: only {medicine.stock} units left.")

        except IntegrityError:
            return render(request, "pharma/new.html")

        return redirect('purchasetable')

    return redirect('purchaseform')


def purchaseformview(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    medicines = Medicine.objects.all()   # also send medicines for dropdown
    return render(request, 'pharma/purchase.html', {
        'purchase': purchase,
        'medicines': medicines
    })


def purchaseformdelete(request, foo):
    try:
        purchase = Purchase.objects.get(pk=foo)
        try:
            medicine = Medicine.objects.get(mname=purchase.pname)
            medicine.stock += purchase.qty
            medicine.save()
        except Medicine.DoesNotExist:
            pass

        purchase.delete()
        messages.success(request, "✅ Purchase deleted and stock restored.")
    except Purchase.DoesNotExist:
        messages.error(request, "❌ Purchase record not found.")

    return redirect('purchasetable')


def purchasetable(request):
    # Get all purchases ordered by ID descending (newest first)
    purchase = Purchase.objects.all().order_by('-id')
    return render(request, 'pharma/purchasetable.html', {"purchase": purchase})
