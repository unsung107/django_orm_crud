from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'apple': 'apple',
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 단순히 사용자가 입력 할 수 있는 form이 있는 페이지
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    #ㅅ용자가 form 에서 전달한 정보를꺼낸다.
    print(request.GET)
    title = request.GET.get('title')
    content = request.GET.get('content')
    #해당 정보를 Article 모델을 이용하여 새롭게 데이터를 저장한다.
    article = Article(title=title, content=content)
    article.save()
    # 사용자에게 저장이 완료되었다는 페이지를 보여준다.
    return render(request, 'articles/create.html')