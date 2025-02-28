# from django.urls import path
# from django.shortcuts import redirect
# from .views import chatbot_query
#
#
# urlpatterns = [
#     path("chatbot/", chatbot_query, name="chatbot_query"),
#     path("", chatbot_query, name="chatbot_query"),
#
# ]
from django.urls import path
from .views import chatbot_query_api, chatbot_page

urlpatterns = [
    path("", chatbot_page, name="chatbot_page"),  # Web UI
    # path("query/", chatbot_query_api, name="chatbot_query_api"),  # ✅ API response URL
    path("api/chatbot/", chatbot_query_api, name="chatbot_query_api"),  # API response
]
