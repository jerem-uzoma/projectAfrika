from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import ContactForm
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app1/post_list.html', {'posts': posts})
# Create your views here.
def contact_form(request):
    form_class = ContactForm
    return render(request, 'app1/contact.html',{'form':form_class})

def contact_list(request):
    lists = ContactForm.objects.all
    return render(request, 'app1/list.html', {'list': lists})