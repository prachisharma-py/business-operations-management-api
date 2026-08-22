import pytest

from departments.api.permissions import DepartmentManagerPermission
from departments.models import Department


@pytest.mark.django_db
def test_employee_can_read_department(employee):
    department = Department.objects.create(
        name="Engineering",
        description="Engineerring Department",
        manager=employee,
    )

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
def test_employee_cannot_modify_department(employee):
    department = Department.objects.create(
        name="Engineering",
        description="Engineering Department",
        manager=employee,
    )

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": employee.user,
        "method": "PATCH",
    })()

    assert not permission.has_permission(request, None)
    assert not permission.has_object_permission(request, None, department)


@pytest.mark.django_db
def test_manager_can_modify_own_department(manager_user, manager_employee):
    department = Department.objects.create(
        name="Engineering",
        description="Engineering Department",
        manager=manager_employee,
    )

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": manager_user,
        "method": "PATCH",
    })

    assert permission.has_permission(request, None)
    assert permission.has_object_permission(request, None, department)


@pytest.mark.django_db
def test_manager_cannot_modify_another_managers_department(manager_user, second_manager_employee):
    department = Department.objects.create(
        name="Finance",
        description="Finanace Department",
        manager=second_manager_employee,
    )

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": manager_user,
        "method": "PATCH",
    })()

    assert permission.has_permission(request, None)
    assert not permission.has_object_permission(request, None, department)


@pytest.mark.django_db
def test_admin_can_modify_any_department(admin_user,employee):
    department = Department.objects.create(
        name="Engineering",
        description="Engineering Department",
        manager=employee,
    )

    permission = DepartmentManagerPermission()

    request = type("Request", (), {
        "user": admin_user,
        "method": "PATCH",
    })()

    assert permission.has_permission(request, None)
    assert permission.has_object_permission(request, None, department)
