SELECT 'ALTER SCHEMA PVRC_DM_TI TRANSFER [' + SysSchemas.Name + '].[' + DbObjects.Name + '];'
FROM sys.Objects DbObjects
INNER JOIN sys.Schemas SysSchemas ON DbObjects.schema_id = SysSchemas.schema_id
WHERE SysSchemas.Name = 'schema'--add your schema
AND (DbObjects.Type IN ('U', 'P', 'V'))
