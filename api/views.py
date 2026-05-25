from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def welcome_index(request):
    return Response({
        "message": "Welcome to Betternship Backend API",
        "status": "200 OK",
        "stage": "Technical Assessment"
    })


tasks_db = {}
employees_db = {}

task_id_counter = 1
employee_id_counter = 1


# 1. create task
@api_view(['POST'])
def create_task(request):
    global task_id_counter
    title = request.data.get('title')
    priority = request.data.get('priority')
    
    if not title or not priority:
        return Response({"error": "Both 'title' and 'priority' are required."}, status=400)
        
    task = {
        "id": task_id_counter,
        "title": title,
        "priority": priority,
        "assigned_to": None  
    }
    
    tasks_db[task_id_counter] = task
    task_id_counter += 1
    
    return Response(task, status=201)


# 2. register an employee
@api_view(['POST'])
def register_employee(request):
    global employee_id_counter
    name = request.data.get('name')
    
    if not name:
        return Response({"error": "The 'name' field is required."}, status=400)
        
    employee = {
        "id": employee_id_counter,
        "name": name,
        "active_tasks": []  # list of task IDs assigned to this employee
    }
    
    employees_db[employee_id_counter] = employee
    employee_id_counter += 1
    
    return Response(employee, status=201)


# 3. assign a task
@api_view(['POST'])
def assign_task(request):
    emp_id = request.data.get('employeeId')
    task_id = request.data.get('taskId')
    
    if not emp_id or not task_id:
        return Response({"error": "'employeeId' and 'taskId' are required."}, status=400)
        
    employee = employees_db.get(emp_id)
    task = tasks_db.get(task_id)
    
    # validating IDs exist
    if not employee:
        return Response({"error": "Employee not found."}, status=404)
    if not task:
        return Response({"error": "Task not found."}, status=404)
        
    # Rule 1: Task can only be assigned to one employee
    if task['assigned_to'] is not None:
        return Response({"error": "This task is already assigned to another employee."}, status=400)
        
    # Rule 2: Employee cannot have more than 3 active tasks
    if len(employee['active_tasks']) >= 3:
        return Response({"error": "Employee cannot have more than 3 active tasks."}, status=400)
        
    # execute assignment
    task['assigned_to'] = emp_id
    employee['active_tasks'].append(task_id)
    
    return Response({"message": "Task assigned successfully"}, status=200)


# 4. list tasks assigned to an employee
@api_view(['GET'])
def employee_tasks(request, id):
    employee = employees_db.get(id)
    
    if not employee:
        return Response({"error": "Employee not found."}, status=404)
        
    # retrieve the actual task objects using the IDs stored in the employee's active_tasks list
    assigned_task_objects = [tasks_db[t_id] for t_id in employee['active_tasks']]
    
    return Response(assigned_task_objects, status=200)
