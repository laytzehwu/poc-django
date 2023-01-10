from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello, World!")

def abcPageView(request):
    print(request)
    print("Receiving call")
    return HttpResponse("This is abc: {}".format(request.scheme))

def abcPageWithInputView(request, intInput = None, title = None):
    if(input is not None and title is not None):
        return HttpResponse("Received both integer input:{intInput} and title:{textInput}".format(textInput = title, intInput = intInput))
    if(input is not None):
        return HttpResponse("Received integer input:{}".format(intInput))
    if(title is not None):
        return HttpResponse("Received title:{}".format(title))
    return HttpResponse("You are not suppose to call me!")

def userDetectorView(request, username):
    return HttpResponse("Your username is:{}".format(username))