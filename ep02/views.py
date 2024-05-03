from django.http import HttpResponse
from django.shortcuts import render, redirect

from ep02.forms import (
    BasicForm,
    BasicForm2,
    BasicForm3,
    EmployeeForm,
    EmployeeForm2,
)


def form1(request):
    if request.method == 'GET':
        return render(
            request, "ep02/form1.html", {'form': BasicForm()}
        )
    elif request.method == 'POST':
        form = BasicForm(request.POST)

        if form.is_valid():
            return redirect('ep02:success')

        return render(
            request, "ep02/form1.html", {'form': form}
        )


def modelform1(request):
    if request.method == 'GET':
        return render(
            request, "ep02/modelform1.html", {'form': EmployeeForm()}
        )
    elif request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ep02:success')
        else:
            return render(
                request, "ep02/modelform1.html", {'form': form}
            )


def modelform2(request):
    if request.method == 'GET':
        return render(
            request, "ep02/modelform2.html", {'form': EmployeeForm2()}
        )
    elif request.method == 'POST':
        print(request.POST)
        form = EmployeeForm2(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ep02:success')
        else:
            return render(
                request, "ep02/modelform2.html", {'form': form}
            )


def widgettweaks1(request):
    if request.method == 'GET':
        return render(
            request, "ep02/widgettweaks1.html", {'form': BasicForm2()}
        )
    elif request.method == 'POST':
        form = BasicForm2(request.POST)

        if form.is_valid():
            return redirect('ep02:success')

        return render(
            request, "ep02/widgettweaks1.html", {'form': form}
        )


def crispyforms1(request):
    if request.method == 'GET':
        return render(
            request, "ep02/crispyforms1.html", {'form': BasicForm3()}
        )
    elif request.method == 'POST':
        form = BasicForm3(request.POST)

        if form.is_valid():
            return redirect('ep02:success')

        return render(
            request, "ep02/crispyforms1.html", {'form': form}
        )


def form_success(request):
    return render(request, "ep02/success.html", {})
