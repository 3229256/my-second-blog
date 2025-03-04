from django.shortcuts import render

# Create your views here.

#creo la prima vista
def post_list(request):
    return render(request, 'blog/post_list.html', {}) #Quando un utente visita una pagina associata a questa view, 
                                                      #Django carica e mostra il file blog/post_list.html.