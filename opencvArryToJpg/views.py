from django.shortcuts import render, HttpResponse
import cv2
import urllib
import numpy as np
from PIL import Image
from io import StringIO
import base64
# Create your views here.
def index(request):
    return render(request, 'index.html')

def opencv_to_img(request):
    return render(request, 'opencvToImg/index.html')

def img_to_opencv(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        imageB64 = request.POST.get('image')

        imgb64_decode = base64.b64decode(imageB64) 

        npimg = np.fromstring(imgb64_decode, np.uint8); 

        result = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        print(result)
        # pillImage = Image.open(StringIO(image))
        # return HttpResponse(pillImage)

        resp = urllib.request.urlopen('http://images.summitmedia-digital.com/cosmo/images/2017/11/10/5-best-things-about-having-a-round-face-main2-1510299634.jpg')
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return render(request, 'imgToOpencv/index.html', {'result':image})
    else:
        return render(request, 'imgToOpencv/index.html')