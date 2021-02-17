from animal import dog #animal패키지에서 dog이라는 모듈을 가져온다
from animal import cat

#form animal import * #animal 패키지에서 모든 모듈을 불러온다


d=dog.Dog()#dog모듈에서 Dog클래스를 instance로 만든다
d.hi()

c=cat.Cat()
c.hi()  