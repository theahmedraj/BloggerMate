from django.shortcuts import render,redirect,get_object_or_404
from .models import Post

from .forms import PostCreateForm,PostEditForm
from django.contrib.auth.decorators import login_required
import random
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect,Http404
# Create your views here.

def post_list(request):
    posts=Post.objects.all().order_by('-id')
    randompost = random.randint(0, len(posts)-1)
    latest = posts[randompost]
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(author__username=query) |
            Q(body__icontains=query)

        )
    paginator = Paginator(posts,6)  
    page = request.GET.get('page')
    totalpost = paginator.get_page(page)

    

    context={
        'posts':totalpost,
        'latest':latest,
    }
    return render(request,'blog/post_list.html',context)



def post_detail(request,id,slug):
    post=Post.objects.get(id=id)
    context={
        'post':post,
        
    }
    return render(request,'blog/post_detail.html',context)


@login_required
def post_create(request):
    form=PostCreateForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        form.save()
        return redirect('post_list')
    else:
        form=PostCreateForm()
    context={
        'form':form
    }
    return render(request,'blog/post_create.html',context)

@login_required
def post_edit(request,id):
    post=get_object_or_404(Post,id=id)
    if post.author != request.user:
        raise Http404()
    if request.method=='POST':
         form = PostCreateForm(request.POST or None, request.FILES or None,instance=post)
         if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form=PostCreateForm(instance=post)
    context={
        'form':form,
        'post':post,
    }
    return render(request,'blog/post_edit.html',context)  

@login_required
def post_delete(request,id):
    post=get_object_or_404(Post,id=id)
    if post.author != request.user:
        raise Http404()
    
    post.delete()
    return redirect('post_list')