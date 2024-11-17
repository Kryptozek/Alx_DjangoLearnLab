from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import  redirect

@permission_required('app_name.can_view', raise_exception=True)
def view_instance(request, instance_id):
    # Logic to view an instance
    pass

@permission_required('app_name.can_create', raise_exception=True)
def create_instance(request):
    # Logic to create an instance
    pass

@permission_required('app_name.can_edit', raise_exception=True)
def edit_instance(request, instance_id):
    # Logic to edit an instance
    pass

@permission_required('app_name.can_delete', raise_exception=True)
def delete_instance(request, instance_id):
    # Logic to delete an instance
    pass

