from django.shortcuts import render, get_object_or_404 ,redirect
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post


def index(request):
    # 포스트 목록
    post_list = Post.objects.order_by('-pub_date') #최근 작성일-내림차순
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def detail(request, post_id):
    # 상세 페이지
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(id=post_id)  # 포스트 1개 가져오기
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)

def post_crate(request):
    #포스트 쓰기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save() #db에 저장
            return redirect('blog:index')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)