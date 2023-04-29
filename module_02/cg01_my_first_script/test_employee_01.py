from module_02.cg00_apps.employee import Employee


def test_base_annual_salary():
    employee = Employee("Peter", "Parker")
    employee.base_annual_salary = 100000.00
    base_salary = employee.base_annual_salary
    assert base_salary == 100000.00


def test_base_annual_salary_less_than_45k():
    employee = Employee("Peter", "Parker")
    employee.base_annual_salary = 30000.00
    base_salary = employee.base_annual_salary
    assert base_salary == 0


def test_base_annual_salary_greater_than_120k():
    employee = Employee("Peter", "Parker")
    employee.base_annual_salary = 130000.00
    base_salary = employee.base_annual_salary
    assert base_salary == 0
