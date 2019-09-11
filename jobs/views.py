from django.shortcuts import render
from faker import Faker
from .models import Job
import requests
from decouple import config
# Create your views here.

fake = Faker()

def index(request):
    return render(request, 'jobs/index.html')

def create(request):
    name = request.POST.get('name')
    if not Job.objects.filter(name=name):
        people = Job()
        people.name = name
        people.job = fake.job() 
        people.save()
    else:
        people = Job.objects.get(name=name)

    # 직업 결과에 따라, giphy 요청
    job = people.job
    api_key = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=en'

    response = requests.get(url).json()
    try:
        image_url = response['data'][0]['images']['original']['url']
    except:
        image_url = None

    context = {
        'people': people,
        'image_url': image_url,
    }
    return render(request, 'jobs/create.html', context)