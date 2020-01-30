from django.urls import path, include
import analytics.views

app_name = 'analytics'

urlpatterns = [
            path('', analytics.views.index, name='index'),
            path('analytics/<int:id>/', analytics.views.detail, name='detail'),
            path('analytics/search/', analytics.views.search, name='search'),
        ]


