# 70 queries for SQL

> I have used SQL Server for the following queries.

```sql
--1. Find out the ID and salary of the instructors.
select ID, salary from instructor;

--2. Find out the ID and salary of the instructor who gets more than $85,000.
select ID, salary from instructor where salary > 85000;

--3. Find out the department names and their budget at the university.
select dept_name, budget from department;

--4. List out the names of the instructors from Computer Science who have more than $70,000.
select name from instructor where dept_name='Comp. Sci.' and salary>70000;

--5. For all instructors in the university who have taught some course, ﬁnd their names and the course
--ID of all courses they taught.
select name, course_id
from instructor
left join teaches
on instructor.ID=teaches.ID;

--6. Find the names of all instructors whose salary is greater than at least one instructor in the Biology
--department.
select name from instructor 
where salary > (select min(salary)
  from instructor where dept_name='Biology');

--7. Find the advisor of the student with ID 12345
select i_id from advisor where s_ID=12345;

--8. Find the average salary of all instructors.
select avg(salary) from instructor;

--9. Find the names of all departments whose building name includes the substring Watson.
select dept_name from department
where building like '%Watson%';

--10. Find the names of instructors with salary amounts between $90,000 and $100,000.
select name from instructor
where salary between 90000 and 100000;

--11. Find the instructor names and the courses they taught for all instructors in the Biology
--department who have taught some course.
select name, course.title from instructor 
join teaches on instructor.ID=teaches.ID
join course on teaches.course_id=course.course_id
where instructor.dept_name='Biology';

--12. Find the courses taught in Fall-2009 semester.
select course_id from teaches
where semester='Fall' and year=2009;

--13. Find the set of all courses taught either in Fall-2009 or in Spring-2010.
select course_id from teaches
where (semester='Fall' and year=2009)
 or (semester='Spring' and year=2010);

--14. Find the set of all courses taught in the Fall-2009 as well as in Spring-2010.
select course_id from teaches
where (semester='Fall' and year=2009)
 and (semester='Spring' and year=2010);

--15. Find all courses taught in the Fall-2009 semester but not in the Spring-2010 semester.
select course_id from teaches
where (semester='Fall' and year=2009)
 and not (semester='Spring' and year=2010);

--16. Find all instructors who appear in the instructor relation with null values for salary.
select * from instructor where salary is NULL;

--17. Find the average salary of instructors in the Finance department.
select avg(salary) from instructor where dept_name='Finance';

--18. Find the total number of instructors who teach a course in the Spring-2010 semester.
select count(distinct ID) from teaches
where (semester='Spring' and year=2010);

--19. Find the average salary in each department.
select dept_name, AVG(salary)
from instructor
group by dept_name;

--20. Find the number of instructors in each department who teach a course in the Spring-2010
--semester.
select count(distinct ID) from teaches
where (semester='Spring' and year=2010);

--21. List out the departments where the average salary of the instructors is more than $42,000.
select dept_name 
from instructor
group by dept_name
having AVG(salary)>42000;

--22. For each course section offered in 2009, ﬁnd the average total credits (tot cred) of all students
--enrolled in the section, if the section had at least 2 students.
select course_id, sec_id, AVG(tot_cred) as average_tot
from takes join student 
on takes.ID=student.ID 
group by course_id, sec_id
having count(student.ID)>1;

--23. Find all the courses taught in both the Fall-2009 and Spring-2010 semesters.
select course_id from teaches
where (semester='Fall' and year=2009)
 and (semester='Spring' and year=2010);

--24. Find all the courses taught in the Fall-2009 semester but not in the Spring-2010 semester.
select course_id from teaches
where (semester='Fall' and year=2009)
 and not (semester='Spring' and year=2010);

--25. Select the names of instructors whose names are neither &lt;Mozart= nor &lt;Einstein=.
select name from instructor
where name != 'Mozart' and name !='Einstein';

--26. Find the total number of (distinct) students who have taken course sections taught by the
--instructor with ID 110011.
select count(distinct takes.ID)
from instructor
join teaches on teaches.ID=instructor.ID
join takes on
 takes.course_id=teaches.course_id and
 takes.sec_id=teaches.sec_id and
 takes.semester=teaches.semester and
 takes.year=teaches.year
where instructor.ID=10101
group by instructor.ID;

--27. Find the ID and names of all instructors whose salary is greater than at least one instructor in the
--History department.
select ID, name from instructor 
where salary > (select min(salary)
 from instructor where dept_name='History');

--28. Find the names of all instructors that have a salary value greater than that of each instructor in
--the Biology department.
select name 
from instructor
where salary > (
 select min(salary)
 from instructor
 where dept_name='Biology'
);

--29. Find the departments that have the highest average salary.
select top 1
dept_name
from instructor 
group by dept_name
order by avg(salary) desc;

--30. Find all courses taught in both the Fall 2009 semester and in the Spring-2010 semester.
select course_id
from teaches
where semester='Fall' and year=2009 
 and semester='Spring' and year=2010;

--31. Find all students who have taken all the courses offered in the Biology department.
select student.ID, name, count(student.ID)
from student 
join takes 
 on takes.ID=student.ID 
join course 
 on takes.course_id=course.course_id
where course.dept_name='Biology'
group by student.ID, name 
having count(student.ID) = (
 select count(*)
 from course 
 where dept_name='Biology'
);

--32. Find all courses that were offered at most once in 2009.
select teaches.course_id, title
from teaches 
join course on course.course_id=teaches.course_id
where year=2009
group by teaches.course_id, title
having count(*)=1;

--33. Find all courses that were offered at least twice in 2009.
select teaches.course_id, title
from teaches 
join course on course.course_id=teaches.course_id
where year=2009
group by teaches.course_id, title
having count(*)>=2;

--34. Find the average instructors9 salaries of those departments where the average salary is greater
--than $42,000.
select dept_name
from instructor
group by dept_name
having AVG(salary)>42000;

--35. Find the maximum across all departments of the total salary at each department.
select top 1
dept_name, sum(salary)
from instructor
group by dept_name
order by sum(salary) desc;

--36. List all departments along with the number of instructors in each department.
select dept_name, count(*)
from instructor
group by dept_name;

--37. Find the titles of courses in the Comp. Sci. department that has 3 credits.
select title
from course
where dept_name='Comp. SCi.'
 and credits=3;

--38. Find the IDs of all students who were taught by an instructor named Einstein; make sure there
--are no duplicates in the result.
select distinct takes.ID
from instructor
join teaches 
 on teaches.ID=instructor.ID
join takes 
 on takes.course_id=teaches.course_id
 and takes.sec_id=teaches.sec_id
 and takes.semester=teaches.semester
 and takes.year=teaches.year
where name='Einstein';

--39. Find the highest salary of any instructor.
select max(salary)
from instructor;

--40. Find all instructors earning the highest salary (there may be more than one with the same
--salary).
select ID, name
from instructor 
group by ID, name 
order by sum(salary) desc;

--41. Find the enrollment of each section that was offered in Autumn-2009.
select sec_id, course_id
from takes 
where semester='Autumn' and year=2009;

--42. Find the maximum enrollment, across all sections, in Autumn-2009.
select top 1
sec_id, course_id
from takes 
where semester='Autumn' and year=2009
group by sec_id, course_id
order by count(*) desc;

--43. Find the salaries after the following operation: Increase the salary of each instructor in the Comp.
--Sci. department by 10%.
update instructor
set salary = salary * 1.10;
select * from instructor
where dept_name = 'Comp. Sci.';

--44. Find all students who have not taken a course.
select student.ID, name
from student 
left join takes 
 on student.ID=takes.ID
where course_id is NULL;

--45. List all course sections offered by the Physics department in the Fall-2009 semester, with the
--building and room number of each section.
select  teaches.sec_id, teaches.course_id, section.building, room_number
from teaches 
join course 
 on teaches.course_id=course.course_id
join section 
 on teaches.course_id=section.course_id 
 and teaches.sec_id=section.sec_id
 and teaches.semester=section.semester
 and teaches.year=section.year
join department
 on course.dept_name=department.dept_name
where course.dept_name='Physics' 
 and teaches.semester='Fall'
 and teaches.year=2009
group by teaches.sec_id, teaches.course_id, section.building, room_number;

--46. Find the student names who take courses in Spring-2010 semester at Watson Building.
select name 
from student 
join takes 
 on student.ID=takes.ID 
join section
 on takes.course_id=section.course_id
 and takes.sec_id=section.sec_id
 and takes.semester=section.semester
 and takes.year=section.year 
where building='Watson'
 and takes.semester='Spring'
 and takes.year=2010;

--47. List the students who take courses teaches by Brandt.
select distinct takes.ID
from instructor
join teaches 
 on teaches.ID=instructor.ID
join takes 
 on takes.course_id=teaches.course_id
 and takes.sec_id=teaches.sec_id
 and takes.semester=teaches.semester
 and takes.year=teaches.year
where name='Brandt';

--48. Find out the average salary of the instructor in each department.
select dept_name, avg(salary) from instructor group by dept_name;

--49. Find the number of students who take the course titled 8Intro. To Computer Science.
select count(*)
from student 
join takes 
 on takes.ID=student.ID 
join course
 on takes.course_id=course.course_id
where title='Intro. To Computer Science';

--50. Find out the total salary of the instructors of the Computer Science department who take a
--course(s) in Watson building.
select sum(salary) 
from instructor
join teaches
 on instructor.ID=teaches.ID 
join section 
 on teaches.course_id=section.course_id 
 and teaches.sec_id=section.sec_id
 and teaches.semester=section.semester
 and teaches.year=section.year
where dept_name='Comp. Sci.'
 and building = 'Watson';

--51. Find out the course titles which starts between 10:00 to 12:00.
select title 
from course
join section 
 on course.course_id=section.course_id
join time_slot
 on time_slot.time_slot_id=section.time_slot_id
where start_hr = 10
 or (start_hr > 10 and start_hr < 12)
 or (start_hr = 12 and start_min = 0);

--52. List the course names where CS-1019 is the pre-requisite course.
select title 
from course 
join prereq 
 on course.course_id=prereq.course_id
where prereq_id = 'CS-1019';

--53. List the student names who get more than B+ grades in their respective courses.
select name 
from student 
join takes
 on student.ID=takes.ID 
where grade like '%A%';

--54. Find the student who takes the maximum credit from each department.
select student.name, student.dept_name, sum(credits)
from student 
join takes 
 on student.ID = takes.ID 
join course
 on course.course_id = takes.course_id
group by student.dept_name
order by sum(credits) desc;
-- won't work in sql server!

--55. Find out the student ID and grades who take a course(s) in Spring-2009 semester. 
select student.ID, grade
from student 
join takes 
 on student.ID=takes.ID 
where semester='Spring'
 and year=2009;

--56. Find the building(s) where the student takes the course titled Image Processing.
select building
from section 
join course
 on section.course_id = course.course_id 
where title = 'Image Processing';

--57. Find the room no. and the building where the student from Fall-2009 semester can take a
--course(s)
select building, room_number
from section 
where semester = 'Fall'
 and year = 2009;

--58. Find the names of those departments whose budget is higher than that of Astronomy. List
--them in alphabetic order
select dept_name 
from department
where budget > (
 select budget 
 from department
 where dept_name = 'Astronomy'
);

--59. Display a list of all instructors, showing each instructor&#39;s ID and the number of sections
--taught. Make sure to show the number of sections as 0 for instructors who have not taught
--any section
select instructor.ID, count(distinct sec_id)
from instructor 
left join teaches
 on instructor.ID = teaches.ID 
group by instructor.ID;

--60. For each student who has retaken a course at least twice (i.e., the student has taken the
--course at least three times), show the course ID and the student&#39;s ID. Please display your
--results in order of course ID and do not display duplicate rows
select ID, course_id
from takes
group by ID, course_id 
having count(*) > 2;

--61. Find the names of Biology students who have taken at least 3 Accounting courses
select name 
from student 
join takes 
 on student.ID = takes.ID 
where dept_name = 'Biology'
 and course_id in (
  select course_id
  from course 
  where dept_name = 'Accounting'
 )
group by student.ID, name 
having count(*) > 2;

--62. Find the sections that had maximum enrollment in Fall 2010
select top 1
sec_id, course_id
from takes 
where semester='Fall' and year=2010
group by sec_id, course_id
order by count(ID) desc;

SELECT course_id, sec_id 
FROM takes
WHERE semester = 'Fall' AND year = 2010
GROUP BY course_id, sec_id
HAVING COUNT(ID) = (
    SELECT MAX(enrollment_count) 
    FROM (
        SELECT COUNT(ID) AS enrollment_count
        FROM takes
        WHERE semester = 'Fall' AND year = 2010
        GROUP BY course_id, sec_id
    ) AS subquery
);

--63. Find student names and the number of law courses taken for students who have taken at
--least half of the available law courses. (These courses are named things like &#39;Tort Law&#39; or
--&#39;Environmental Law&#39;
select name, count(*)
from student
join takes on student.ID=takes.ID 
join course on takes.course_id=course.course_id
where title like '%Law%'
group by student.ID, name
having count(*) > (
 select count(*)/2
 from course 
 where title like '%Law%'
);

--64. Find the rank and name of the 10 students who earned the most A grades (A-, A, A+).
--Use alphabetical order by name to break ties.
select top 10
row_number() over(order by count(*) desc, name) as rank, name 
from student 
join takes 
 on student.id = takes.id
where grade in ('A-', 'A', 'A+')
group by name, student.ID
order by count(*) desc, name;

--65. Find the titles of courses in the Comp. Sci. department that have 3 credits.
select title 
from course 
where credits = 3 and dept_name = 'Comp. Sci.';

--66. Find the IDs of all students who were taught by an instructor named Einstein; make sure there
--are no duplicates in the result.
select distinct takes.ID
from instructor
join teaches 
 on teaches.ID=instructor.ID
join takes 
 on takes.course_id=teaches.course_id
 and takes.sec_id=teaches.sec_id
 and takes.semester=teaches.semester
 and takes.year=teaches.year
where name='Einstein';

--67. Find the ID and name of each student who has taken at least one Comp. Sci. course; make sure
--there are no duplicate names in the result.
select distinct student.ID, name 
from student 
join takes 
 on student.id = takes.id 
where course_id in (
 select course_id
 from  course 
 where dept_name = 'Comp. Sci.'
);


--68. Find the course id, section id, and building for each section of a Biology course.
select section.course_id, sec_id, building
from section
join course 
 on section.course_id = course.course_id 
where dept_name = 'Biology';

--69. Output instructor names sorted by the ratio of their salary to their department&#39;s budget (in
--ascending order).
select name 
from instructor 
join department
 on instructor.dept_name = department.dept_name
order by (salary / budget);

--70. Output instructor names and buildings for each building an instructor has taught in. Include
--instructor names who have not taught any classes (the building name should be NULL in this
--case).
select distinct name, building 
from instructor 
left join teaches
 on instructor.ID = teaches.ID
left join section 
 on teaches.course_id = section.course_id
 and teaches.sec_id = section.sec_id
 and teaches.year = section.year
 and teaches.semester = section.semester;
```
