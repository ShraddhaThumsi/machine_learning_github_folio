with pool as (SELECT 'India' as country union all
SELECT 'Pakistan' as country union all
SELECT 'Afghanistan' as country union all
SELECT 'Iran' as country union all
SELECT 'Russia' as country)
select * from pool where right(lower(country),1) ='n'