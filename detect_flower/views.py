from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.conf import settings
import os
import pandas as p
import joblib 
from sklearn.preprocessing import LabelEncoder
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
m=os.path.join(settings.BASE_DIR,'detect_flower','flomodel.pkl')
ansopr=os.path.join(settings.BASE_DIR,'detect_flower','ans.pkl')
model=joblib.load(m)
l=joblib.load(ansopr)
# Create your views here.
def detect_flower(request):
    if request.method=='POST':
        v1=request.POST.get('val1')
        v2=request.POST.get('val2')   
        v3=request.POST.get('val3')
        v4=request.POST.get('val4')
        dat={
            'sepal-length': [v1],
            'sepal-width':[v2],
            'petal-length':[v3],
            'petal-width':[v4],
        }
        df=p.DataFrame(dat)
        r=model.predict(df)
        v=l.inverse_transform(r)#to tansform this into the string again
        return render(request,'home.html',{'ans':v[0]})
    return render(request,'home.html')
