/*

Find job positioning from the first quarter that have salary greater than 70K

job_history
    id,
    title,
    salary,
    created_at
*/

select 
    job_title,
    salary
from 
    job_postings_fact
where 
    created_at between '01-01-2026' and '31-03-2026'
group by job_title
having avg(salary) > 70000;