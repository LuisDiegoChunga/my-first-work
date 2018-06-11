from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def ingresar_variables(request):
    return render(request, 'blog/ingresar_variables.html', {})

def resultado(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('resultado', pk=resultado.pk)
    else:
        form = PostForm()
    return render(request, 'blog/resultado.html', {'form': form})
