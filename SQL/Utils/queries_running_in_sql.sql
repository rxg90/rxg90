select * from [sys].[dm_exec_requests] r join [sys].[dm_exec_sessions] s on r.session_id = s.session_id
WHERE end_time IS null
order by submit_time desc
