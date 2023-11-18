from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

# urlpatterns = [
#     path(
#         route="polls/",
#         view=include("polls.urls"),
#         name="polls",
#         ),
#     path(
#         route="admin/",
#         view=admin.site.urls,
#         name="admin",
#         ),
# ]