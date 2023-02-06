from rest.viewset import UserViewSets, UserModelViewSet
from rest_framework.routers import DefaultRouter

############ Binding UserViewSets to http views ##############
# user_list = UserViewSets.as_view({"post": "listed"})
# user_detail = UserViewSets.as_view({"post": "retrieve"})

########### No Need of UserModelViewSet to http views ##########

router = DefaultRouter()

router.register(r'users', UserViewSets, basename="user")
router.register(r'mo-user', UserModelViewSet, basename="mo_user")

urlpatterns = router.urls
