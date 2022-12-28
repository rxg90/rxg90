 -- Monitor active queries
SELECT *
FROM sys.dm_pdw_exec_requests
WHERE status not in ('Completed','Failed','Cancelled')
  AND session_id <> session_id()
ORDER BY status;
 


SELECT * FROM sys.dm_pdw_exec_sessions
 where [status] = 'Active' and not sql_spid = @@SPID
 GO


 kill 'SID7172773'
 GO

--usar cuando haya una query colgada.
--lock waits
SELECT *,DATEDIFF(MINUTE,acquire_time,GETDATE()) AS acquire_duration FROM sys.dm_pdw_lock_waits WHERE object_type = 'OBJECT'
SELECT * FROM sys.dm_pdw_lock_waits WHERE state <> 'Granted'
--SELECT * FROM sys.dm_pdw_lock_waits WHERE object_name = 'rpt.ARIES_PROD_ADMIN_AC_PROPERTY'

SELECT object_name, COUNT(*) FROM sys.dm_pdw_lock_waits WHERE state <> 'Granted' AND object_type = 'OBJECT' GROUP BY OBJECT_NAME

--SELECT * FROM [sys].[dm_pdw_exec_requests] WHERE session_id = 'SID7426270'
--SELECT * FROM [sys].[dm_pdw_exec_requests] WHERE request_id = 'QID479318148'

--select * from [sys].[dm_pdw_exec_sessions] WHERE session_id = 'SID7426270'-- order by login_time desc

--kill 'SID7426270';
