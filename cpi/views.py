from django.shortcuts import render
from django.http import HttpResponse
from .models import Projekat, Aktuelnost, ClanTima, Fotografija, Partner, PressClanak, Publikacija, IstorijskaTura, VideoKlip, Izlozba, ArhivskiMaterijal

from users.models import Profil
from itertools import chain
from .forms import PrijavaForm

def home(request):
    projekti = Projekat.objects.all().order_by('-Datum_objave')
    #ovde bi trebala da sledi profilna fotografija udruzenja, sada je neka random.
    # projekat1 = Projekat.objects.get(Ime='Tura 1')
    galerija = Fotografija.objects.all().order_by('-Datum_objave')
    aktuelnosti = Aktuelnost.objects.all().order_by('-Datum_objave')

    count = 1
    projekti_nums = []
    for projekat in projekti:
        if count < 10:
            num = "0" + str(count) + "."   
        else:
            num = str(count) + "." 
        count += 1
        projekti_nums.append(num)

    video_klipovi = VideoKlip.objects.all().order_by('-Datum_objave')
    publikacije = Publikacija.objects.all().order_by('-Datum_objave')
     
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    context = {'projekti': projekti, 
    'galerija': galerija, 'url': url, 'aktuelnosti': aktuelnosti, 
    'video_klipovi': video_klipovi, 'publikacije': publikacije, 'projekti_nums': projekti_nums}
    return render(request, 'cpi/b4.html', context)

def aktuelnosti(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    aktuelnosti_list = Aktuelnost.objects.all().order_by('-Datum_objave')
    aktuelnosti_listX = aktuelnosti_list[1:] #list without the first item
    count = 0
    slides = []
    slide = []
    slideX =[] #here will be first aktuelnosti boxes on each page.
    slideXX = []
    num = 0
    while num < len(aktuelnosti_list):
        slideX = []
        slide = []
        for i in range(count, count + 5):
            if i == count:
                try:
                    slideX.append(aktuelnosti_list[i])
                    num += 1
                except IndexError:
                    break 
            else:
                try:
                    slide.append(aktuelnosti_list[i])
                    num += 1
                except IndexError:
                    break   
        count += 5
        slides.append(slide)
        slideXX.append(slideX)
    print ("slideXX: {}".format(slideXX))
    print ("slides: {}".format(slides))

    context = {'aktuelnosti_list': aktuelnosti_list, 'aktuelnosti_listX': aktuelnosti_listX, 'slides': slides, 'url': url, 'slideXX': slideXX}
    return render(request, 'cpi/aktuelnosti.html', context)

def aktuelnost_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    aktuelnost = Aktuelnost.objects.get(id=pk)
    context = {'aktuelnost': aktuelnost}
    return render(request, 'cpi/aktuelnost_detalji.html', context)


def pretraga(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    print (url)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        projekti = Projekat.objects.filter(Ime__icontains=q)
        tim = ClanTima.objects.filter(Ime__icontains=q)
        foto = Fotografija.objects.filter(Ime__icontains=q)
        partneri = Partner.objects.filter(Ime__icontains=q)
        tekst = Publikacija.objects.filter(Naslov__icontains=q)
        clanak = PressClanak.objects.filter(Naslov__icontains=q)
        rezultati= list(chain(projekti, tim, foto, partneri, tekst, clanak))
        context = {'rezultati': rezultati, 'query': q, 'url': url}
        return render(request, 'cpi/rezultati_pretrage.html', context)
    else:
        context = {'url': url, 'error': True}
        return render(request, 'cpi/rezultati_pretrage.html', context )

def prijava(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    if request.method == 'POST':
        formular = PrijavaForm(request.POST)
        if formular.is_valid():
            formular.save()
            return render(request, 'cpi/potvrda_prijave.html')

    else:
        formular = PrijavaForm()
        context ={'url': url, 'formular': formular}
        return render(request, 'cpi/prijava.html', context)

def projekti(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    projekti = Projekat.objects.all().order_by('-Datum_objave')
    count = 0
    slides = []
    slide = []
    num = 0
    num_list =[]
    num_lists =[]
    num_num = num + 1
    while num < len(projekti):
        slide = []
        num_list =[]
        for i in range(count, count + 9):
            try:
                slide.append(projekti[i])
                if num_num < 10:
                    num_list.append("0" + str(num_num) + ".")
                else:
                    num_list.append(str(num_num) + ".")
            except IndexError:
                break
            num += 1
            num_num += 1
        count += 9
        slides.append(slide)
        num_lists.append(num_list)
    print (num_lists)
    print(slides)

    projekti = Projekat.objects.all().order_by('-Datum_objave')
    count = 0
    slidesM = []
    slide = []
    num = 0
    num_list =[]
    num_listsM =[]
    num_num = num + 1
    while num < len(projekti):
        slide = []
        num_list =[]
        for i in range(count, count + 5):
            try:
                slide.append(projekti[i])
                if num_num < 10:
                    num_list.append("0" + str(num_num) + ".")
                else:
                    num_list.append(str(num_num) + ".")
            except IndexError:
                break
            num += 1
            num_num += 1
        count += 5
        slidesM.append(slide)
        num_listsM.append(num_list)
    print (num_listsM)
    print(slidesM)

    context = {'projekti': projekti, 'slides': slides, 'url': url, 'num_lists': num_lists, 'slidesM': slidesM, 'num_listsM': num_listsM}
    return render(request, 'cpi/projekti.html', context)

def projekat_galerija(request, pk):
    projekat = Projekat.objects.get(id = pk)
    galerija = Fotografija.objects.filter(Projekat = projekat)

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    
    print (galerija)
    context = {'galerija': galerija, 'url': url}
    return render(request, 'cpi/projekat_galerija.html', context)

def o_nama(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    profil = Profil.objects.get(ime="Centar za Primenjenu Istoriju")
    context = {'profil': profil, 'url': url}
    return render(request, 'cpi/o_nama.html', context)

def tim(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    ekipa = ClanTima.objects.all()
    context = {'ekipa': ekipa, 'url': url}
    return render(request, 'cpi/tim.html', context)
 
def clanovi_detalji(request):
    return render(request, 'cpi/clanovi_detalji.html', context)

def partneri(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    prijatelji = Partner.objects.all()
    context = {'prijatelji': prijatelji, 'url': url}
    return render(request, 'cpi/partneri.html', context)

def galerija(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    galerija = Fotografija.objects.all()
    context = {'galerija': galerija, 'url': url}
    return render(request, 'cpi/galerija.html', context)

def press(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    clanci = PressClanak.objects.all()
    context = {'clanci': clanci, 'url': url}
    return render(request, 'cpi/press.html', context)

def istorijske_ture(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    ture = IstorijskaTura.objects.all().order_by('-Datum_objave')

    count = 0
    slides = []
    slide = []
    num = 0
    num_list =[]
    num_lists =[]
    num_num = num + 1
    while num < len(ture):
        slide = []
        num_list =[]
        for i in range(count, count + 9):
            try:
                slide.append(ture[i])
                if num_num < 10:
                    num_list.append("0" + str(num_num) + ".")
                else:
                    num_list.append(str(num_num) + ".")
            except IndexError:
                break
            num += 1
            num_num += 1
        count += 9
        slides.append(slide)
        num_lists.append(num_list)
    print (num_lists)
    print(slides)

    count = 0
    slidesX = []
    slide = []
    num = 0

    while num < len(ture):
        slide = []
        for i in range(count, count + 5):
            try:
                slide.append(ture[i])
            except IndexError:
                break
            num += 1
        count += 5
        slidesX.append(slide)
    print(slidesX)
    
    context = {'slides': slides, 'slidesX': slidesX, 'ture': ture, 'url': url}
    return render(request, 'cpi/istorijske_ture.html', context)

def tura_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    tura = IstorijskaTura.objects.get(id=pk)
    context = {'tura': tura, 'url': url}
    return render(request, 'cpi/tura_detalji.html', context)


def publikacije(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    publikacije = Publikacija.objects.all().order_by('-Datum_objave')

    count = 0
    slides = []
    slide = []
    num = 0
    num_list =[]
    num_lists =[]
    num_num = num + 1
    while num < len(publikacije):
        slide = []
        num_list =[]
        for i in range(count, count + 9):
            try:
                slide.append(publikacije[i])
                if num_num < 10:
                    num_list.append("0" + str(num_num) + ".")
                else:
                    num_list.append(str(num_num) + ".")
            except IndexError:
                break
            num += 1
            num_num += 1
        count += 9
        slides.append(slide)
        num_lists.append(num_list)
    print (num_lists)
    print(slides)

    count = 0
    slidesX = []
    slide = []
    num = 0
    while num < len(publikacije):
        slide = []
        
        for i in range(count, count + 5):
            try:
                slide.append(publikacije[i])
            except IndexError:
                break
            num += 1
        count += 5
        slidesX.append(slide)
    print("SlidesX:", slidesX)

    for slide in slides:
        print (len(slide))

    context = {'publikacije': publikacije, 'slides': slides, 'slidesX': slidesX,'url': url}
    return render(request, 'cpi/publikacije.html', context)  

def projekti_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    publikacije = Publikacija.objects.all().order_by('-Datum_objave')

    projekat = Projekat.objects.get(id=pk)
    izlozbe = Izlozba.objects.filter(Projekat = projekat)
    publikacije = Publikacija.objects.filter(Projekat = projekat)
    galerija = Fotografija.objects.filter(Projekat = projekat)
    arhiva = ArhivskiMaterijal.objects.filter(Projekat = projekat) 
    press = PressClanak.objects.filter(Projekat = projekat)
    
    meni_list = []
    menu_list = []
    if len(izlozbe) != 0:
        meni_list.append("IZLOŽBE")
        menu_list.append("EXHIBITIONS")

    if len(publikacije) != 0:
        meni_list.append("PUBLIKACIJE")
        menu_list.append("PUBLICATIONS")

    if len(arhiva) != 0:
        meni_list.append("ARHIVSKI MATERIJAL")
        menu_list.append("ARCHIVE")

    if len(press) != 0:
        meni_list.append("PRESS")
        menu_list.append("PRESS")

    if len(galerija) != 0:
        meni_list.append("GALERIJA")
        menu_list.append("GALLERY")
        
    print (meni_list)
    print (menu_list)

    context = {'projekat': projekat, "meni_list": meni_list, "menu_list": menu_list, 'url': url}
    return render(request, 'cpi/projekat_detalji.html', context)

def publikacije_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    publikacija = Publikacija.objects.get(id=pk)
    context = {'publikacija': publikacija, 'url': url}
    return render(request, 'cpi/publikacija_detalji.html', context)

def press_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    clanak = PressClanak.objects.get(id=pk)
    context = {'clanak': clanak, 'url': url}
    return render(request, 'cpi/press_detalji.html', context)

def galerija_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    galerija = Fotografija.objects.all().order_by('Datum_objave')
    fotka = Fotografija.objects.get(id=pk)

    count = 0
    for foto in galerija:
        if foto.id == fotka.id:
            fotka_num = count
        count += 1
        
    print (fotka.Ime)
    print (fotka.Slika.url)
    context = {'fotka': fotka, 'galerija': galerija, 'fotka_num': fotka_num, 'url': url}
    return render(request, 'cpi/galerija_detalji.html', context)

def tim_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    clan_tima = ClanTima.objects.get(id=pk)
    context = {'clan_tima': clan_tima, 'url': url}
    return render(request, 'cpi/tim_clan.html', context)

def partneri_detalji(request, pk):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    partner = Partner.objects.get(id=pk)
    context = {'partner': partner, 'url': url}

    return render(request, 'cpi/projekat_detalji.html', context)


