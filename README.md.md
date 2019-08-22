- # Django ORM

  ## Create

  기초설정

  - Shell

  ```bash
  $ python manage.py shell
  ```

  

  - import model 

    ```python
    from articles.models import Article
    ```

    

  데이터를 저장하는 3가지 방법

  1. 첫번째 방식

     - ORM을 쓰는 이유 => DB 조작하는 것을 객체지향 프로그래밍(클래스) 처럼 하기위해서

       ```python
       >>> article = Article()
       >>> article
       <Article: Article object (None)>
       >>> article.title = 'First article'
       >>> article.content = 'Hello, article?'
       >>> article.title
       'First article'
       >>> article.content
       'Hello, article?'
       >>> article.save()
       >>> article
       <Article: Article object (1)>
       ```

  2. 두번째 방식

     - 파이썬에서 인자넘기기 방식과 유사

       ```python
       >>> article = Article(title='Second article', content='hihi')
       >>> article.save()
       >>> article
       <Article: Article object (2)>
       ```

  3. 세번째 방식

     - create를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝

       ```python
       >>> Article.objects.create(title='third', content='Django! Good')
       <Article: Article object (3)>
       ```

  4. 검증

     - full_clean() 함수를 통해 저장하기 전 데이터 검증을 할 수 있다.

       ```python
       >>> article = Article()
       >>> article.title = 'Python is good'
       >>> article.full_clean()
       Traceback (most recent call last):
         File "<console>", line 1, in <module>
         File "C:\Users\student\development\django\django_orm_crud\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
           raise ValidationError(errors)
       django.core.exceptions.ValidationError: {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
       ```

       

  

  ------

  ## Read

  - 모든객체

  ```python
  >>> Article.objects.all()
  <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
  ```

  - 객체 표현 변경

  ```python
  # articles.models.py
  class Article(models.Model):
      ...
  
      def __str__(self):
          return f'{self.id}번 글 - {self.title} : {self.content}'
  
  ```

  - DB에 저장된 글 중에서 title이 Second article인 글만 가지고오기

  ```python
  >>> Article.objects.filter(title='Second article')
  <QuerySet [<Article: 2번 글 - Second article : hihi>]>
  
  ```

  - DB에 저장된 글 중에서 title이 Second article인 글중에서 첫번째만 가지고오기

  ```python
  >>> querySet = Article.objects.filter(title='Second article')
  >>> querySet
  <QuerySet [<Article: 2번 글 - Second article : hihi>, <Article: 4번 글 - Second article : hello hello>]>
  >>> querySet.first()
  <Article: 2번 글 - Second article : hihi>
  >>>
  
  ---
  
  >>> Article.objects.filter(title='Second article').first()
  <Article: 2번 글 - Second article : hihi>
  
  ```

  - DB에 저장된 글 중에서 pk가 1인 글만 가져오기

    PK만  get()으로 가지고 올 수 있다

    ```python
    >>> Article.objects.get(pk=1)
    <Article: 1번 글 - First article : Hello, article?>
    
    ```

  

  데이터에 접근하는 기타방법들

  - 오름차순

  ```python
  >>> articles = Article.objects.order_by('pk')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article : Hello, article?>, <Article: 2번 글 - Second article : hihi>, <Article: 3번 글 - third : Django! Good>, <Article: 4번 글 - Second article : hello hello>]>
  
  ```

  - 내림차순

  ```python
  >>> articles = Article.objects.order_by('-pk')
  >>> articles
  <QuerySet [<Article: 4번 글 - Second article : hello hello>, <Article: 3번 글 - third : Django! Good>, <Article: 2번 글 - Second article : hihi>, <Article: 1번 글 - First article : Hello, article?>]>
  
  ```

  - 인덱스 접근이 가능

  ```python
  >>> article = articles[2]
  >>> article
  <Article: 2번 글 - Second article : hihi>
  >>> articles = Article.objects.all()[1:3]
  >>> articles
  <QuerySet [<Article: 2번 글 - Second article : hihi>, <Article: 3번 글 - third : Django! Good>]>
  
  ```

  

  - LIKE - 문자열을 포함하고 있는 값을 가지고 옴

    장고 ORM은 이름(title)과 필터(contains)를 더블 언더스코어로 구분합니다.

  ```python
  >>> articles = Article.objects.filter(title__contains='Sec')
  >>> articles
  <QuerySet [<Article: 2번 글 - Second article : hihi>, <Article: 4번 글 - Second article : hello hello>]>
  
  ```

  - startswith

  ```python
  >>> articles = Article.objects.filter(title__startswith='first')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article : Hello, article?>]>
  
  ```

  - endswith

  ```python
  >>> articles = Article.objects.filter(title__endswith='article')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article : Hello, article?>, <Article: 2번 글 - Second article : hihi>, <Article: 4번 글 - Second article : hello hello>]>
  
  ```

  - delete

```bash
>>> article = Article.objects.get(pk = 2)
>>> article.delete()
(1, {'articles.Article': 1})
```

- update

- 

  

```bash
>>> article.title
'Thrid'
>>> article.content = 'new contents'
>>> article.save()
>>> article
<Article: 3번글 - Thrid : new contents>
```

