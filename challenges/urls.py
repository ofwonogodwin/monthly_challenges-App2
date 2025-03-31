from django.urls import path
from.import views
urlpatterns = [

    path('',views.jan, name='jan'),
    path('feb/',views.feb,name='feb'),
    path('mar/',views.mar,name='mar'),
    path('apr/',views.apr,name='apr'),
    path('may/',views.may,name='may'),
    path('jun/',views.jun,name='jun'),
    path('jul/',views.jul,name='jul'),
    path('aug/',views.aug,name='aug'),
    path('sep/',views.sep,name='sep'),
    path('oct/',views.oct,name='oct'),
    path('nov/',views.nov,name='nov'),
    path('dec/',views.dec,name='dec'),
    
]