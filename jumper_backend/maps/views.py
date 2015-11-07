from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import cPickle
from jumper_backend.settings import *
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from maps.forms import MyRegistrationForm




def index(request):
    if request.POST:
        form = MyRegistrationForm(request.POST)
        
        if form.is_valid():
            ride_num = form.cleaned_data['ride_num']
            runopt = form.cleaned_data['runopt']
            run_input = {}
            run_input['ride_num'] = int(ride_num)
            run_input['runopt'] = int(runopt)
            cPickle.dump(run_input,open('run_input.dat','w'))
            os.system("python run.py")
        else:
            print "Not valid"    
        t = loader.get_template('maps/index.html')

        markers_ds = cPickle.load(open(BASE_DIR+"/tmp.dat","r"))
        c = Context(markers_ds)
        c.update(csrf(request))
        return HttpResponse(t.render(c))
    else:
        t = loader.get_template('maps/index.html')
        markers_ds = cPickle.load(open(BASE_DIR+"/tmp.dat","r"))
        c = Context(markers_ds)
        c.update(csrf(request))
        return HttpResponse(t.render(c))
        