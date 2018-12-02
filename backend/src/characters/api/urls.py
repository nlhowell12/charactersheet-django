from characters.api.views import CharacterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CharacterViewSet, base_name='characters')
urlpatterns = router.urls

# from django.urls import path

# from .views import (
#     CharacterListView,
#     CharacterDetailView,
#     CharacterCreateView,
#     CharacterUpdateView,
#     CharacterDeleteView
# )


# urlpatterns = [
#     path('', CharacterListView.as_view()),
#     path('create/', CharacterCreateView.as_view()),
#     path('<pk>', CharacterDetailView.as_view()),
#     path('<pk>/update/', CharacterUpdateView.as_view()),
#     path('<pk>/delete/', CharacterDeleteView.as_view())
# ]
