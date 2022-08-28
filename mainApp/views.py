from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    pagetype={'pagetype':'Home'}
    return render(request,'index.html',context=pagetype)

def about(request):
    pagetype={'pagetype':'About'}
    return render(request,'about.html',context=pagetype)

def anime(request):
    pagetype={'pagetype':'Anime'}
    return render(request,'anime.html',context=pagetype)

def movies(request):
    pagetype={'pagetype':'Movies'}
    return render(request,'movies.html',context=pagetype)
def dilluvpn(request):
    pagetype={'pagetype':'DilluVPN'}
    return render(request, 'dilluvpn.html',context=pagetype)

def random(request):
    pagetype={'pagetype':'Maqbool Zinda Pakadna hai Bsdiwale ko',
    'link':'static/stares.jpg'}
    return render(request,'random.html',context=pagetype)
def games(request):
    return HttpResponse('Beep Boop? Page is under construction')
def songs(request):
    return HttpResponse('Beep Boop? Page is under construction')
def test(request):
    return render(request, 'test.html')
class player():

    class anime():

        def yourname(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1-6mdxeJaoYvLZ5mV-MeGeEbPl4v_USV6/preview',
            'linkD':'https://drive.google.com/file/d/1-6mdxeJaoYvLZ5mV-MeGeEbPl4v_USV6'}
            return render(request,'player.html',context=pagetype)
        def tenkinoko(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1-Xt3w4osGyqJhpwxAWoTyFEPgO6rIcuG/preview',
            'linkD':'https://drive.google.com/file/d/1-Xt3w4osGyqJhpwxAWoTyFEPgO6rIcuG'}
            return render(request,'player.html',context=pagetype)
        def spiritedaway(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1g85SHDATt8_YlirMlP9M9mFArUXYqPm9/preview',
            'linkD':'https://drive.google.com/file/d/1g85SHDATt8_YlirMlP9M9mFArUXYqPm9'}
            return render(request,'player.html',context=pagetype)
        def hotarubi(request):
             pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1Vk4g9oH1AnQsxblFF4g7-zVuKakc-rhy/preview',
            'linkD':'https://drive.google.com/file/d/1Vk4g9oH1AnQsxblFF4g7-zVuKakc-rhy'}
             return render(request,'player.html',context=pagetype)
        def demonslayer(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1VmHILc_Fl155rRB5nFWApu1Eb52YuRz8/preview',
            'linkD':'https://drive.google.com/file/d/1VmHILc_Fl155rRB5nFWApu1Eb52YuRz8'}
            return render(request,'player.html',context=pagetype)
        def helloworld(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1vppa6IxqYXlEnc-hBgJkBFfIgap-S9YX/preview',
            'linkD':'https://drive.google.com/file/d/1vppa6IxqYXlEnc-hBgJkBFfIgap-S9YX'}
            return render(request,'player.html',context=pagetype)
        def garden(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1-VWeS48l77WGa3yLrQyt8A7jwhXN-SoL/preview',
            'linkD':'https://drive.google.com/file/d/1-VWeS48l77WGa3yLrQyt8A7jwhXN-SoL'}
            return render(request,'player.html',context=pagetype)
        def silent(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1CzDs49qiMmG83EwEPAvZNyi8ddnauGEH/preview',
            'linkD':'https://drive.google.com/file/d/1CzDs49qiMmG83EwEPAvZNyi8ddnauGEH'}
            return render(request,'player.html',context=pagetype)

    class movie():
        def shangchi(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/11ptO3WhHu6Rhb4RGPlTbLwHhAnXT7ZyU/preview',
            'linkD':'https://drive.google.com/file/d/11ptO3WhHu6Rhb4RGPlTbLwHhAnXT7ZyU'}
            return render(request,'player.html',context=pagetype)
        
        def shershah(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/18cvLA_fuMKXSTPp_5xb4wKZFrpK-8son/preview',
            'linkD':'https://drive.google.com/file/d/18cvLA_fuMKXSTPp_5xb4wKZFrpK-8son'}
            return render(request,'player.html',context=pagetype)

        def venom(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1ZmpGnouTyx0ZeuE2j8AVuE8WeSgyu0SR/preview',
            'linkD':'https://drive.google.com/file/d/1ZmpGnouTyx0ZeuE2j8AVuE8WeSgyu0SR'}
            return render(request,'player.html',context=pagetype)

        def matrix(request):
            pagetype= {'pagetype':'Anime',
            'link':'static/copyright.jpg'}
            return render(request,'random.html',context=pagetype)

        def purge(request):
            pagetype= {'pagetype':'Anime',
            'link':'static/copyright.jpg'}
            return render(request,'random.html',context=pagetype)
        
        def babysitter(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1juEiLM4AfXarTi2_PX-nG0xYh1HsUeFu/preview',
            'linkD':'https://drive.google.com/file/d/1juEiLM4AfXarTi2_PX-nG0xYh1HsUeFu'}
            return render(request,'player.html',context=pagetype)

        def platform(request):
            pagetype= {'pagetype':'Anime',
            'link':'https://drive.google.com/file/d/1_Ocf0vT-CwmP9rzi-LWDx1oxPxVyAw_k/view?usp=sharing',
            'linkD':'https://drive.google.com/file/d/1_Ocf0vT-CwmP9rzi-LWDx1oxPxVyAw_k'}
            return render(request,'player.html',context=pagetype)

        def benjamin(request):
            pagetype= {'pagetype':'Anime',
            'link':'static/copyright.jpg'}
            return render(request,'random.html',context=pagetype)