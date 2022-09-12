select schema_name(t.schema_id) as schema_name, t.name as table_name, t.create_date, t.modify_date 
from sys.tables t 
where schema_name(t.schema_id) = 'Production' -- put schema name here order by table_name;

--Views:

select schema_name(schema_id) as schema_name,
       name as view_name
from sys.views
where schema_name(schema_id) = 'pa'
order by schema_name,
         view_name;
