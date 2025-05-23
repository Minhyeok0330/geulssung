from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

# /test로 연결 되는 테스트 페이지 입니다.
def test_page_view(request):
    return render(request, "test.html")

# /geulssung으로 연결 되는 메인 페이지 입니다.
def home_view(request):
    return render(request, "base.html")

# /geulssung/write로 연결 되는 글쓰기 페이지 입니다.
@login_required
def write_post_view(request):
    if request.method == 'POST':
        genre = request.POST['genre']
        if genre == 'column':
            step1 = request.POST.get('column_step1', '')
            step2 = request.POST.get('column_step2', '')
            step3 = request.POST.get('column_step3', '')
        elif genre == 'analysis':
            step1 = request.POST.get('analysis_step1', '')
            step2 = request.POST.get('analysis_step2', '')
            step3 = request.POST.get('analysis_step3', '')
        elif genre == 'essay':
            step1 = request.POST.get('essay_step1', '')
            step2 = request.POST.get('essay_step2', '')
            step3 = request.POST.get('essay_step3', '')
        elif genre == 'poem':
            step1 = request.POST.get('poem_step1', '')
            step2 = request.POST.get('poem_step2', '')
            step3 = request.POST.get('poem_step3', '')
        else:
            step1 = step2 = step3 = ''
        # 필수값 누락 등으로 저장 실패 시 기존 값 유지
        if not request.POST.get('title') or not genre or not request.POST.get('category'):
            return render(request, 'post/write_form.html', {
                'selected_category': request.POST.get('category', ''),
                'selected_genre': genre,
                'topic': request.POST.get('topic', ''),
                'title': request.POST.get('title', ''),
                'final_text': request.POST.get('final_text', ''),
                'step1': step1,
                'step2': step2,
                'step3': step3,
            })
        post = Post(
            author=request.user,
            title=request.POST['title'],
            category=request.POST['category'],
            genre=genre,
            topic=request.POST['topic'],
            step1=step1,
            step2=step2,
            step3=step3,
            final_content=request.POST.get('final_text', ''),
            is_public='is_public' in request.POST
        )
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'post/write_form.html')

# 글 상세 페이지입니다.
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/post_detail.html', {'post': post})

# 유저 글 보기 페이지입니다.
def public_posts_by_user(request, nickname):
    author = get_object_or_404(User, nickname=nickname)
    # 로그인한 사용자가 해당 nickname의 주인일 때는 모든 글, 아니면 공개글만
    if request.user.is_authenticated and request.user.nickname == nickname:
        posts = Post.objects.filter(author=author).order_by('-created_at')
    else:
        posts = Post.objects.filter(author=author, is_public=True).order_by('-created_at')
    return render(request, 'post/public_user_posts.html', {
        'author': author,
        'posts': posts,
    })


