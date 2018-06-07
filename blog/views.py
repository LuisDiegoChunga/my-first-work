from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    return render(request, 'blog/ingresar_variables.html', {})

def post_detail(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/resultado.html', {'form': form})
