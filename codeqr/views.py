from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import qrcode
import os

# Create your views here.

def qrcode_generator(request):
    qr_code_url = None
    if request.method == "POST":
        data = request.POST.get("data")
        nom = request.POST.get("nom")
        couleur = request.POST.get("couleur")
        code = qrcode.QRCode(version=3.0, box_size=15, border=4)
        code.add_data(data)
        code.make(fit=True)
        if couleur == "blue":
            img = code.make_image(fill_color=couleur, back_color='white')
        else:           
            img = code.make_image(fill_color='black', back_color='white')
        
        qr_code_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', f'{nom}.png')
        os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
        img.save(qr_code_path)
        qr_code_url = f'/media/qrcodes/{nom}.png'
    return render(request, "codeqr/index.html", {'qr_code_url': qr_code_url})
