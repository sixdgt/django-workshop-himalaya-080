from django.shortcuts import render
from secondapp.forms import ContactForm
from secondapp.models import Contact
# Create your views here.
def contact_form(request):
    cf = ContactForm()
    context = {
        "title": "Day 5: Contact Form",
        "form": cf
    }
    if request.method == "POST":
        """ pass
        Pass statement in Python is a null operation or a placeholder. It is used when a statement is syntactically required but we don't want to execute any code. It does nothing but allows us to maintain the structure of our program.
        """
        req_first_name = request.POST.get('first_name')
        req_last_name = request.POST.get('last_name')
        req_email = request.POST.get('email')
        req_phone_no = request.POST.get('phone_no')
        req_address = request.POST.get('address')
        req_message = request.POST.get('message')
        c = Contact()
        c.first_name = req_first_name
        c.last_name = req_last_name
        c.email = req_email
        c.phone_no = req_phone_no
        c.address = req_address
        c.message = req_message
        c.save()
    data = Contact.objects.all() # fetch all data from Contact
    context.setdefault("data", data)
    return render(request, "contact_form.html", context)
