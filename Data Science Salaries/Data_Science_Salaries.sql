SELECT * FROM ds_salaries;

-- 1. Check NULL Values

SELECT * 
FROM ds_salaries 
WHERE work_year IS NULL
OR experience_level IS NULL
OR employment_type IS NULL
OR job_title IS NULL
OR salary IS NULL
OR salary_currency IS NULL
OR salary_in_usd IS NULL
OR employee_residence IS NULL
OR remote_ratio IS NULL
OR company_location IS NULL
OR company_size IS NULL;

-- 2. How many different Job Titles?

SELECT job_title
FROM ds_salaries
GROUP BY job_title;

-- 3. Which Job Title Relates to Data Analyst and How Many People in that Job Title?

SELECT job_title, COUNT(*) AS jumlah
FROM ds_salaries
WHERE job_title LIKE '%Data Analyst%'
GROUP BY job_title;

-- 4. Average Salary for Data Analyst based on Job Title and Experience Level?

SELECT job_title, experience_level, ROUND(AVG(salary_in_usd),2) AS average_salary_per_year, ROUND(AVG(salary_in_usd) / 12 ,2) AS average_salary_per_month
FROM ds_salaries
WHERE job_title LIKE '%Data Analyst%'
GROUP BY job_title, experience_level;

-- 4.1 Average Salary for Data Analyst based on Experience Level and Employment Type?

SELECT experience_level, employment_type, ROUND(AVG(salary_in_usd),2) AS average_salary_per_year, ROUND(AVG(salary_in_usd) / 12 ,2) AS average_salary_per_month
FROM ds_salaries
WHERE job_title LIKE '%Data Analyst%'
GROUP BY experience_level, employment_type;

-- 5. Countries with Competitive Salary (Above 40K per year) for Data Analyst, Full Time with Entry Level or Middle Experience Level.

SELECT company_location, experience_level, ROUND(AVG(salary_in_usd),2) as average_salary
FROM ds_salaries
WHERE job_title LIKE '%Data Analyst%' AND employment_type = 'FT' AND experience_level IN ('EN','MI')
GROUP BY company_location, experience_level
HAVING average_salary >= 40000;

-- 6. In Which Year does the Salary Rise the Most From Mid Experience Level to the Expert Experience Level (For Full Time Data Analyst)?

WITH ds_1 AS (
	SELECT work_year, ROUND(AVG(salary_in_usd),2) as average_salary_expert
	FROM ds_salaries
	WHERE job_title LIKE '%Data Analyst%' AND employment_type = 'FT' AND experience_level = 'EX'
	GROUP BY work_year
), ds_2 AS (
	SELECT work_year, ROUND(AVG(salary_in_usd),2) as average_salary_mid
	FROM ds_salaries
	WHERE job_title LIKE '%Data Analyst%' AND employment_type = 'FT' AND experience_level = 'MI'
	GROUP BY work_year
) SELECT ds_1.work_year, ds_1.average_salary_expert, ds_2.average_salary_mid, ds_1.average_salary_expert - ds_2.average_salary_mid differences
FROM ds_1 LEFT OUTER JOIN ds_2 ON ds_1.work_year = ds_2.work_year