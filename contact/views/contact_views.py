from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }
    return render(request, 'contact/index.html',context=context)

def search(request):
    search_value = request.GET.get('q','').strip()

    if search_value == '':
        return redirect('contact:index')
    full_name = search_value.split(' ')
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(first_name__icontains=full_name[0]) |
            Q(last_name__icontains=full_name[-1])
        )\
        .order_by('-id')
    
    context = {
        'contacts': contacts,
        'site_title': 'Procurar - ',
        'search_value': search_value
    }
    return render(request, 'contact/index.html',context=context)

def contact(request,contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404()
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True)

    context = {
        'contact': single_contact,
        'site_title': f'{single_contact.first_name} {single_contact.last_name} - '
    }
    return render(request, 'contact/contact.html',context=context)