from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from calender.models import Case
from calender.forms import CaseForm

# Create your views here.
@login_required(login_url='accounts/login/')
def dashboard(request):
    context = {}
    return render(request, 'calender/dashboard.html', context)

def all_cases(request):
    all_cases = Case.objects.all()                                                                                   
    out = []                                                                                                             
    for case in all_cases:
        out.append({
            "id": case.id,
            "alien_number": case.alien_number,
            "first_name": case.first_name,
            "middle_name": case.middle_name,
            "last_name": case.last_name,
            "phone_number": case.phone_number,
            "email": case.email,
            "Address": case.Address,
            "city": case.city,
            "zipcode": case.zipcode,
            "country": case.country,
            "type_of_case": case.type_of_case,
            "i_589_filed": str(case.i_589_filed),
            "erop": str(case.erop),
            "e_28_filed": str(case.e_28_filed),
            "biometrics_filed": str(case.biometrics_filed),
            "foia_submitted": str(case.foia_submitted),
            "foia_uploaded": str(case.foia_uploaded),
            "work_permit_applied": str(case.work_permit_applied),
            "hearing_location": case.hearing_location,
            "total_billing_amount": case.total_billing_amount,
            "amount_paid": case.amount_paid,
            "date":case.date.strftime("%Y-%m-%d %H:%M:%S") if case.date else None ,                                                                          
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False)


def calender(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CaseForm()
    context = {'form': form}
    return render(request, 'calender/calender.html', context)


def update_case(request, case_id):
    case_instance = get_object_or_404(Case, id=case_id)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case_instance)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CaseForm(instance=case_instance)
    return render(request, 'calender/calender.html', {'form': form})







