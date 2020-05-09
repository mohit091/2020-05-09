select id,event_name,people_count from (
select *,count(id) over (partition by event_group) as no_of_consecutive_events
from
(
SELECT *,(id - ROW_NUMBER() OVER (ORDER BY id)) AS event_group
FROM events
WHERE people_count >= 100) a) a
where no_of_consecutive_events >=3
