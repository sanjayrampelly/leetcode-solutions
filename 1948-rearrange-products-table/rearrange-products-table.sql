# Write your MySQL query statement below
select 
    p1.product_id ,
    'store1' as store,
    p1.store1 as price
from Products p1
WHERE p1.store1 IS NOT NULL
UNION
select 
    p1.product_id ,
    'store2' as store,
    p1.store2 as price
from Products p1
WHERE p1.store2 IS NOT NULL
Union
select 
    p1.product_id ,
    'store3' as store,
    p1.store3 as price
from Products p1
WHERE p1.store3 IS NOT NULL