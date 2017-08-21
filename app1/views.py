from django.shortcuts import render
from django.utils import timezone
from .models import Post, Contact
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app1/post_list.html', {'posts': posts})
# Create your views here.
def contact_form(request):
    form_class = Contact
    return render(request, 'app1/contact.html',{'form':form_class})

def contact_list(request):
    lists = Contact.objects.all.order_by('first')
    return render(request, 'app1/list.html', {'list': lists})