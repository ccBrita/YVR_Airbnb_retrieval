SELECT host_id, count(host_id)
FROM listings
GROUP BY host_id
ORDER BY host_id
LIMIT 10