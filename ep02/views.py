from django.http import HttpResponse
from django.shortcuts import render, redirect

from django_htmx.http import retarget, reswap

from ep02.forms import (
    BasicForm,
    BasicForm2,
    BasicForm3,
    CommentForm,
    EmployeeForm,
    EmployeeForm2,
)


def home(request):
    return render(
        request, 'ep02/home.html', {}
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


def htmx1(request):
    return render(
        request, "ep02/htmx1.html", {'form': BasicForm()}
    )


def htmx1_post(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)

        if form.is_valid():
            return render(request, 'ep02/partials/htmx1-success.html', {})

        return render(
            request, "ep02/partials/htmx1-form.html", {'form': form}
        )


def htmx2(request):
    initial_comment = {'comment': 'I ❤️ ghost pepper', 'author': 'Adam'}

    return render(
        request,
        "ep02/htmx2.html",
        {'form': CommentForm(), 'comments': [initial_comment]}
    )


def htmx2_post(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            response = render(
                request,
                "ep02/partials/htmx2-comment.html",
                {'comment': form.cleaned_data}
            )
            retarget(response, '#comments')

            return response

        # if form not valid
        response = render(
            request,
            "ep02/partials/htmx2-form.html",
            {'form': form,}
        )
        retarget(response, '#comment-form')
        reswap(response, 'innerHTML')

        return response


def form_success(request):
    return render(request, "ep02/success.html", {})
