#1)
select FIRST_NAME as  worker_name from Worker
#2)
SELECT UPPER(FIRST_NAME) FROM Worker
#3)
select distinct department from Worker
#4)
SELECT SUBSTRING(FIRST_NAME,1,3) FROM Worker 
#5)
Select INSTR(FIRST_NAME, BINARY'a') from Worker where FIRST_NAME = 'Amitabh';
#6)
select RTRIM(FIRST_NAME) FROM Worker
#7)
Select LTRIM(DEPARTMENT) from Worker;	
#8)
select distinct length(department)  from Worker 
#9)
Select REPLACE(FIRST_NAME,'a','A') from Worker
#10)
SELECT concat(FIRST_NAME,' ' ,LAST_NAME) AS COMPLETE_NAME FROM Worker
#11)
SELECT * FROM Worker order by FIRST_NAME ASC
#12)
SELECT * FROM Worker ORDER BY FIRST_NAME asc , DEPARTMENT DESC
#13)
select * from Worker where FIRST_NAME in ("Vipul","Satish")
#14)
SELECT * FROM Worker WHERE FIRST_NAME NOT IN ("Vipul","Satish")
#15)
SELECT * FROM Worker where department = "admin"
Select * from Worker where DEPARTMENT like 'Admin%';
#16)
SELECT * FROM Worker where FIRST_NAME like '%a%'
#17)
SELECT * FROM Worker where FIRST_NAME like '%a'
#18)
Select * from Worker where FIRST_NAME like '______h';
#19)
SELECT * FROM Worker WHERE SALARY BETWEEN 100000 AND 500000
#20)
SELECT * FROM Worker WHERE YEAR(JOINING_DATE) =  2014 AND MONTH(JOINING_DATE) = 2
#21)
SELECT COUNT(*) FROM Worker GROUP BY DEPARTMENT  HAVING DEPARTMENT = "Admin"
SELECT COUNT(*) FROM Worker WHERE DEPARTMENT = 'Admin';
#22)
select * from Worker where SALARY >= 50000 AND SALARY <= 100000
SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) As Worker_Name, Salary
FROM Worker 
WHERE WORKER_ID IN 
(SELECT WORKER_ID FROM Worker 
WHERE Salary BETWEEN 50000 AND 100000);
#23
SELECT count(*) AS No_Of_Workers FROM Worker GROUP BY DEPARTMENT ORDER BY No_Of_Workers  DESC 
SELECT DEPARTMENT, count(WORKER_ID) No_Of_Workers 
FROM Worker 
GROUP BY DEPARTMENT 
ORDER BY No_Of_Workers DESC;
#24)
select * from Worker join Title on WORKER_ID = WORKER_REF_ID WHERE WORKER_TITLE = "Manager"
SELECT DISTINCT W.FIRST_NAME, T.WORKER_TITLE
FROM Worker W
INNER JOIN Title T
ON W.WORKER_ID = T.WORKER_REF_ID
AND T.WORKER_TITLE in ('Manager');
#25)
SELECT WORKER_TITLE, AFFECTED_FROM, COUNT(*)
FROM Title
GROUP BY WORKER_TITLE, AFFECTED_FROM
HAVING COUNT(*) > 1;
#26)
SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) <> 0;
#27)
SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) = 0;
#28)
create table WorkerClone
SELECT * FROM Worker;
CREATE TABLE WorkerClone LIKE Worker;
#29)
(SELECT WORKER_ID
FROM Worker)
INTERSECT
(SELECT  WORKER_ID
FROM Worker);
#30)
SELECT * FROM Worker MINUS SELECT * FROM Title;
#31)
SELECT CURDATE();
SELECT NOW();
#32)
SELECT * FROM Worker ORDER BY Salary DESC LIMIT 10;
SELECT TOP 10 * FROM Worker ORDER BY Salary DESC;
SELECT * FROM (SELECT * FROM Worker ORDER BY Salary DESC)
WHERE ROWNUM <= 10;
#33)
SELECT Salary,FIRST_NAME FROM Worker ORDER BY Salary DESC LIMIT 4,1;
#34)
SELECT *
FROM Worker W1
WHERE 4 = (
 SELECT COUNT( DISTINCT ( W2.Salary ) )
 FROM Worker W2
 WHERE W2.Salary >= W1.Salary
 ); 
 SELECT SALARY,FIRST_NAME  
 FROM  
 (SELECT SALARY ,FIRST_NAME,ROW_NUMBER() OVER (order by SALARY DESC) AS ROWNUMBER FROM Worker) AS A
 WHERE A.ROWNUMBER IN(5)
 #35)
 select distinct W1.WORKER_ID ,W1.SALARY,W1.FIRST_NAME FROM Worker W1, Worker W2
 Where W1.SALARY = W2.SALARY AND W1.WORKER_ID != W2.WORKER_ID 
#36)
 SELECT SALARY,FIRST_NAME  
 FROM  
 (SELECT SALARY ,FIRST_NAME,ROW_NUMBER() OVER (order by SALARY DESC) AS ROWNUMBER FROM Worker) AS A
 WHERE A.ROWNUMBER IN(2)
 
Select max(Salary) from Worker 
where Salary not in (Select max(Salary) from Worker);

SELECT SALARY FROM (SELECT SALARY,dense_rank() over (order by SALARY DESC) AS DR FROM Worker ) AS TAB WHERE TAB.DR = 2

#37)
select FIRST_NAME, DEPARTMENT from Worker W where W.DEPARTMENT='HR' 
union all 
select FIRST_NAME, DEPARTMENT from Worker W1 where W1.DEPARTMENT='HR';

#38)
(SELECT * FROM Worker)
INTERSECT
(SELECT * FROM WorkerClone);

#39)
SELECT * FROM Worker where WORKER_ID <= (SELECT COUNT(WORKER_ID) / 2  FROM Worker)

#40)
SELECT DEPARTMENT,COUNT(DEPARTMENT)AS DCOUNT FROM Worker GROUP BY DEPARTMENT HAVING DCOUNT < 5

#41)
SELECT DEPARTMENT ,COUNT(DEPARTMENT) FROM Worker GROUP BY DEPARTMENT

#42)
SELECT * FROM Worker ORDER BY WORKER_ID desc limit 1;
Select * from Worker where WORKER_ID = (SELECT max(WORKER_ID) from Worker);

#43)
SELECT * FROM Worker order by WORKER_ID LIMIT 1;
Select * from Worker where WORKER_ID = (SELECT min(WORKER_ID) from Worker);

#44)
SELECT * FROM Worker WHERE WORKER_ID <=5
UNION
SELECT * FROM (SELECT * FROM Worker W order by W.WORKER_ID DESC) AS W1 WHERE W1.WORKER_ID <=5;

#45)
SELECT MAX(SALARY),DEPARTMENT  FROM Worker GROUP BY DEPARTMENT
SELECT MAX(SALARY),DEPARTMENT  FROM Worker GROUP BY DEPARTMENT

SELECT t.DEPARTMENT,t.FIRST_NAME,t.Salary from(SELECT max(Salary) as TotalSalary,DEPARTMENT from Worker group by DEPARTMENT) as TempNew 
Inner Join Worker t on TempNew.DEPARTMENT=t.DEPARTMENT 
 and TempNew.TotalSalary=t.Salary;
 
 #46)
 SELECT DISTINCT SALARY FROM Worker ORDER BY SALARY desc limit 3
 
 SELECT distinct Salary from Worker a 
 WHERE 3 >= (SELECT count(distinct Salary) from Worker b WHERE a.Salary <= b.Salary) order by a.Salary desc;
 
#47)
SELECT DISTINCT SALARY FROM Worker ORDER BY SALARY ASC LIMIT 3

SELECT distinct Salary from Worker a 
WHERE 3 >= (SELECT count(distinct Salary) 
from Worker b WHERE a.Salary >= b.Salary) order by a.Salary desc;

SELECT COUNT(DISTINCT a.Salary) 
FROM Worker b,Worker a WHERE a.Salary <= b.Salary ORDER BY a.Salary DESC;

#48)
SELECT distinct Salary from Worker a 
WHERE 1 >= (SELECT count(distinct Salary) 
from Worker b WHERE a.Salary <= b.Salary) order by a.Salary desc;

#49)
SELECT SUM(SALARY) AS TOTAL ,DEPARTMENT FROM Worker GROUP BY DEPARTMENT 

#59)
SELECT DISTINCT SALARY,FIRST_NAME FROM Worker WHERE SALARY = (SELECT MAX(SALARY) FROM Worker )