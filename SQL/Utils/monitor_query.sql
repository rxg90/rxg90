PRINT '--top 10 Active CPU Consuming Queries by sessions--';
SELECT TOP 10 req.session_id, req.start_time
, cpu_time 'cpu_time_ms'
, OBJECT_NAME(ST.objectid, ST.dbid) 'ObjectName', SUBSTRING(REPLACE(REPLACE(SUBSTRING(ST.text, (req.statement_start_offset / 2)+1, ((CASE statement_end_offset WHEN -1 THEN DATALENGTH(ST.text)ELSE req.statement_end_offset END-req.statement_start_offset)/ 2)+1), CHAR(10), ' '), CHAR(13), ' '), 1, 512) AS statement_text
FROM sys.dm_exec_requests AS req
CROSS APPLY sys.dm_exec_sql_text(req.sql_handle) AS ST
ORDER BY cpu_time DESC;


-------------------------------------------------------------

select
     r.session_id,
     s.login_name,
     c.client_net_address,
     s.host_name,
     s.program_name,
     st.text, s.status
 from sys.dm_exec_requests r
 inner join sys.dm_exec_sessions s
 on r.session_id = s.session_id
 left join sys.dm_exec_connections c
 on r.session_id = c.session_id
 outer apply sys.dm_exec_sql_text(r.sql_handle) st
 where client_net_address is not null and text is not null and s.status = 'running';
