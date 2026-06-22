import json
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Sum, Count, Max, Min
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):

    search = request.GET.get('search')

    employees = Employee.objects.all()

    if search:
        employees = employees.filter(
            name__icontains=search
        )

    return render(
        request,
        'employee_list.html',
        {'employees': employees}
    )

def employee_create(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(
        request,
        'employee_form.html',
        {'form': form}
    )

def employee_update(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:

        form = EmployeeForm(
            instance=employee
        )

    return render(
        request,
        'employee_form.html',
        {'form': form}
    )

def employee_delete(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(
        request,
        'employee_delete.html',
        {'employee': employee}
    )

def analytics(request):
    employees = Employee.objects.all()
    total_employees = employees.count()
    
    # Department distribution & average salary
    dept_stats = Employee.objects.values('department').annotate(
        count=Count('id'),
        avg_salary=Avg('salary')
    )
    
    dept_names = [d['department'] for d in dept_stats]
    dept_counts = [d['count'] for d in dept_stats]
    dept_avg_salaries = [float(d['avg_salary'] or 0) for d in dept_stats]
    
    highest_salary = Employee.objects.aggregate(Max('salary'))['salary__max'] or 0
    lowest_salary = Employee.objects.aggregate(Min('salary'))['salary__min'] or 0
    avg_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg'] or 0
    top_earners = Employee.objects.order_by('-salary')[:5]
    
    context = {
        'total_employees': total_employees,
        'total_departments': len(dept_names),
        'dept_names': json.dumps(dept_names),
        'dept_counts': json.dumps(dept_counts),
        'dept_avg_salaries': json.dumps(dept_avg_salaries),
        'highest_salary': highest_salary,
        'lowest_salary': lowest_salary,
        'avg_salary': avg_salary,
        'top_earners': top_earners,
    }
    return render(request, 'analytics.html', context)

def payroll(request):
    employees = Employee.objects.all()
    headcount = employees.count()
    total_monthly_payroll = Employee.objects.aggregate(Sum('salary'))['salary__sum'] or 0
    total_annual_payroll = float(total_monthly_payroll) * 12
    
    avg_monthly_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg'] or 0
    
    dept_payroll = Employee.objects.values('department').annotate(
        total=Sum('salary')
    )
    dept_payroll_labels = [d['department'] for d in dept_payroll]
    dept_payroll_values = [float(d['total'] or 0) * 12 for d in dept_payroll]
    
    context = {
        'employees': employees,
        'headcount': headcount,
        'total_annual_payroll': total_annual_payroll,
        'avg_monthly_salary': avg_monthly_salary,
        'dept_payroll_labels': json.dumps(dept_payroll_labels),
        'dept_payroll_values': json.dumps(dept_payroll_values),
    }
    return render(request, 'payroll.html', context)

def attendance(request):
    employees = Employee.objects.all()
    total_employees = employees.count()
    return render(request, 'attendance.html', {
        'employees': employees,
        'total_employees': total_employees
    })

def preferences(request):
    return render(request, 'preferences.html')