with sal_CTE as
(
 select e.Id as emp_id,
    d.Name as dept_name,
    e.Name as emp_name,
    e.Salary as emp_sal,
    DENSE_RANK() OVER(PARTITION BY d.ID Order By  e.Salary desc) as rank
 from Employee e inner join department d
 ON (e.DepartmentId = d.Id)
)

select dept_name as Department,
emp_name as Employee,
emp_sal as Salary from sal_CTE
where rank <=3
order by dept_name;