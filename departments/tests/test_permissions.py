import pytest

from departments.api.permissions import DepartmentManagerPermission
from departments.models import Department


@pytest.mark.django_db
def test_employee_can_read_department(employee, engineering_department):
    department = engineering_department

    department.manager = employee
    department.save()

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": employee.user,
        "method": "GET",
    })()

    assert permission.has_permission(request, None)
    assert permission.has_object_permission(request, None, department)


@pytest.mark.django_db
def test_employee_cannot_creat_department(user):
    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": user,
        "method": "POST",
    })()

    assert not permission.has_permission(request, None)


@pytest.mark.django_db
def test_employee_cannot_modify_department(employee, engineering_department):
    department = engineering_department
    
    department.manager = employee
    department.save()

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": employee.user,
        "method": "PATCH",
    })()

    assert not permission.has_permission(request, None)
    assert not permission.has_object_permission(request, None, department)


@pytest.mark.django_db
def test_manager_can_modify_own_department(manager_user, manager_employee, engineering_department):
    department = engineering_department
    
    department.manager = manager_employee
    department.save()

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": manager_user,
        "method": "PATCH",
    })

    assert permission.has_permission(request, None)
    assert permission.has_object_permission(request, None, department)


@pytest.mark.django_db
def test_manager_cannot_modify_another_managers_department(manager_user, second_manager_employee, finance_department):
    department = finance_department
    
    department.manager = second_manager_employee
    department.save()

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": manager_user,
        "method": "PATCH",
    })()

    assert permission.has_permission(request, None)
    assert not permission.has_object_permission(request, None, department)


@pytest.mark.django_db
def test_admin_can_modify_any_department(admin_user,employee, engineering_department):
    department = engineering_department
    
    department.manager = employee
    department.save()

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": admin_user,
        "method": "PATCH",
    })()

    assert permission.has_permission(request, None)
    assert permission.has_object_permission(request, None, department)
