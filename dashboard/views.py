from django.shortcuts import render
from users.models import Costumer
from .chat import chats, status_desc

def zip_messages(a,b):
    message = []
    for i,j in zip(a,b):
        message.extend([i,j])
    return message


def risktest_view(request):
    context = {}
    return render(request, "chatbot/test.html", context)

status = ["", "conservative", "aggressive"]
user_chat = []
response = []
# Create your views here.
def messenger_view(request, username):
    message = []
    obj = Costumer.objects.get(username=username)
    pic = status[obj.investing_style]
    if request.method == "POST":
        data = request.POST.get('chat')
        user_chat.append(data)
        response.append(chats(data))
        message = zip_messages(user_chat,response)
    context = {
        "lists":["hi","ho","hey"],
        "message": message,
        "picture": pic,
        "obj": obj,
        "status": status[obj.investing_style],
        "description": status_desc(obj.investing_style)
    }
    return render(request, "chatbot/index.html",context)