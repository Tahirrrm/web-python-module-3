def apply_bonus(
        salary:int,
        bonus_percent:float
) -> float:
    return salary*(1+bonus_percent/100)
result = apply_bonus(1000,10.0)

# ----
def uppercase_name(name:str) -> str:
    return name.upper()
print(uppercase_name("1"))
# 3
course_title:str = "Python"
students_count: int = 20
os_open: bool = True

class Employee:
    company: str = "Tech"
    def __init__ (self,emp_id:int,name:str,salary:int) -> None:
        self.emp_id:int = emp_id
        self.name:str = name
        self.salary:int = salary


# 4
names: list[str] = ["Alice","Bob"]
salaries: dict [str,int] = {"Alice": 1000, "Bob":1200}
user_pair: tuple[str,int] = ("Alice",1)
permissions:set[str] = {"read","write"}
# 5
from typing import Any
def stringify(value:Any) -> str:
    return str(value)

# 6
from typing import Optional, Union
def find_emp_name(emps: dict[int,str], emp_id:int) -> Optional[str]:
    return emps.get(emp_id)
def parse_emp_id(raw: Union [str,int]) -> int:
    return int(raw)
# 7 
from typing import Sequence, Mapping,Iterable
def print_names(items:Iterable[str]) -> None:
    for item in items:
        print(item)
def first_two(items: Sequence[str]) -> list [str]:
    return list (items [:2])
def get_salary(data: Mapping[str,int],name:str) -> int:
    return data[name]
# 8 
from typing import Callable
def apply_formatter( text: str, formatter: Callable [[str], str]) -> str:
    return formatter(text)
# 9
EmployeeId = int
SalaryMap =  dict [str,int]
Taglist = list [str]
emp_id: EmployeeId = 20
skills: Taglist = ["tag"]

# 10
from typing import TypedDict
class Employee(TypedDict):
    emp_id:int
    name:str
    salary:int
payload:Employee = {
    "emp_id" :1,
    "name":"Alice",
    "salary": 1000
}