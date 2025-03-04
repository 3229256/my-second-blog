from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

#creo la prima vista
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) #Quando un utente visita una pagina associata a questa view, 
                                                      #Django carica e mostra il file blog/post_list.html.