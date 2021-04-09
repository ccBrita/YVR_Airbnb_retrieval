SELECT host_id, count(list_id)
                    FROM review
                    GROUP BY host_id
                    ORDER BY count(host_id)
                    LIMIT 10