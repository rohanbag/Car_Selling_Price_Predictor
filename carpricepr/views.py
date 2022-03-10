from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import pandas as pd
import pickle

# Create your views here.

def home(request):

	pred_price = 0

	if request.method == 'POST':
		name = request.POST['name']
		year = request.POST['year']
		km = request.POST['km']
		fuel = request.POST['fuel']
		dealer = request.POST['dealer']
		trans = request.POST['trans']
		seats = request.POST['seats']
		rpm = request.POST['rpm']
		mil = request.POST['mil']
		eng = request.POST['eng']
		power = request.POST['power']
		owner = request.POST['owner']
		print('#####################')

		if name != "":
			df = pd.DataFrame(columns=['year','km_driven','fuel',
                                           'seller_type','transmission','seats',
                                           'torque_rpm','mil_kmpl','engine_cc','max_power_new',
                                           'First Owner','Fourth & Above Owner','Second Owner',
                                           'Test Drive Car','Third Owner'])
			a2 = Helper(owner)
        	
			df2 =  {'year': int(year),'km_driven': float(km),
			'fuel': int(fuel),
                       'seller_type': int(dealer),'transmission': int(trans),'seats': int(seats),
                        'torque_rpm': float(rpm),'mil_kmpl': float(mil),'engine_cc': float(eng),
                       'max_power_new': float(power),'First Owner': a2[0],'Fourth & Above Owner':
                        a2[1],'Second Owner': a2[2],'Test Drive Car': a2[3],
                       'Third Owner': a2[4]}

			df = df.append(df2, ignore_index=True)

			path_of_file = "PredictCarPrice.pickel"
			rf_model_load = pickle.load(open(path_of_file,'rb'))

			pred_price = rf_model_load.predict(df)
			print(pred_price)

			for e in pred_price:
				i = round(e)
				q = len(str(i))-5
				w = str(i)[:q]+','+str(i)[q:]

		else:
			return redirect('home.html')

	else:
		return render(request,'home.html')

	return render(request,'home.html',{'result':w})




def Helper(x):
	if x == '1':
		return [1, 0, 0, 0, 0]
	elif x == '2':
		return [0, 0, 1, 0, 0]
	elif x == '3':
		return [0, 0, 0, 0, 1]
	if x == '4':
		return [0, 1, 0, 0, 0]
	if x == '5':
		return [0, 0, 0, 1, 0]



def about(request):

	return render(request,'about.html')
