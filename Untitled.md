# Django ORM

## Create

### 기초설정

- shell

  ```python
  $ python manage.py shell
  ```

- import model

  ```python
  >>> from articles.models import Article
  ```

- 

  ```python
  >>> Article.objects.all()
  <QureySet []>
  ```


## 데이터를 저장하는 3가지 방법

1 .첫번째 방식

- ORM을 쓰는 이유는 => DB 조작하는 것을 객체지향 프로그래밍(클래스) 처럼 하기위해서

```bash
article = Article()
article.title = 'First article'
article.content = '안녕하세요'
article.save()
```



2. 두번째 방식

- 함수에서 keyword 인자넘기기 방식과 동일

```bash
article = Article(title='Second', content='hihi')
article.save()
```

3. 세번째 방식

- create() 를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝

```bash
Article.objects.create(title='Thrid', content='Django! good')
```

4. 검증

- full_clean() 함수를 통해 저장하기전 데이터 검증을 할 수 있다.

```bash
>>> article = Article()
>>> article.title = 'Python is good'
>>> article.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\development\django\django_orm_crud\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
```

---

## READ

### 모든 객체

```python
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```



#### 객체 표현 변경

```python
# articles/models.py
class Article(models.Model):
    ...
    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'
```



- DB에 저장된 글 중에서 title이 second 인 것만 가져오기

  ```python
  >>> Article.objects.filter(title='third')
  <QuerySet [<Article: 3번 글 - third : Django>]>
  
  >>> Article.objects.create(title='third', content='GOOD')
  <Article: 4번 글 - third : GOOD>
  >>> Article.objects.filter(title='third')
  <QuerySet [<Article: 3번 글 - third : Django>, <Article: 4번 글 - third : GOOD>]>
  
  
  >>> querySet.first()
  <Article: 3번 글 - third : Django>
  >>> Article.objects.filter(title='third').first()
  <Article: 3번 글 - third : Django>
  ```

  

- DB에 저장된 글 중에서 pk 가 1인 글만 가지고 오기

  - PK 만 get() 으로 가져올 수 있다.

  ```python
  >>> Article.objects.get(pk=1)
  <Article: 1번 글 - First article : Hello, article>
  >>>
  ```

  