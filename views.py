from django.shortcuts import render

def test(request):
    friends = ['kevin', 'erin', 'brett']
    return render(request, 'test.html', {'friends': friends})