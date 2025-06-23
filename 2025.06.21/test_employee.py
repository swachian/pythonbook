import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee("Don", "Wirtz", 9000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()

    assert employee.get_salary() == "$14,000"

def test_give_customer_raise(employee):
    employee.give_raise(2000)

    assert employee.get_salary() == "$11,000"