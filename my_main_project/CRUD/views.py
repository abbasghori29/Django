import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import *
# Create your views here.

def index(request):
    students= Student.objects.all()
    return render(request, 'home.html',{'students':students})
def home(request):
    students= Student.objects.all()
    return render(request, 'home.html',{'students':students})
def addStudentPage(request):
    return render(request, 'addStudent.html')
def getDetails(request,student_id):
    student=Student.objects.get(roll_no=student_id)
    return render(request,'viewStudentPage.html',{'student':student})
def deleteStudent(request,student_id):
    student=Student.objects.get(roll_no=student_id)
    student.delete()
    students = Student.objects.all()
    return render(request,'home.html',{"students":students})
def editStudent(request,student_id):
    student=Student.objects.get(roll_no=student_id)
    return render(request,"editStudentPage.html",{"student":student})


@require_http_methods(["POST"])
@csrf_exempt
def updateData(request, id):
    if request.method == 'POST':
        try:
            students = Student.objects.all()
            data = json.loads(request.body)
            student = Student.objects.get(id=id)
            student.roll_no = data['roll_no']
            student.name = data['name']
            student.age = data['age']
            student.email = data['email']
            student.address = data['address']
            student.save()

            return JsonResponse({"success": True},status=200)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def addStudent(request):
    print("Request received")  # Debug log

    if request.method == "POST":
        try:
            data= json.loads(request.body)
            id=data.get('roll_no')
            name=data.get('name')
            age=data.get('age')
            email=data.get('email')
            address=data.get('address')
            Student.objects.create(roll_no=id,name=name,age=age,email=email,address=address)
            response_data = {
                'message': 'Data added successfully!',
                'data': data,
            }
            return JsonResponse({"success": True},status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid JSON"}, status=400)
    return JsonResponse({"error": "Error in Request"}, status=405)






