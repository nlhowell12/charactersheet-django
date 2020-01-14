from characters.api.views import (
    CharacterViewSet
    )
from equipment.views import (
    EquipmentViewset
)
from spells.views import (
    SpellViewset
)
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='characters')
router.register(r'equipment', EquipmentViewset, basename='equipment')
router.register(r'spells', SpellViewset, basename='spells')
router.register(r'users', UserViewSet, basename='users')
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
