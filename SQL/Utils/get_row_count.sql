--Use to get row count of big tables
SELECT 
        s.name AS SchemaName,
		t.NAME AS TableName,
		t.create_date as creation_date,
		--t.modify_date as modify_date,   
        p.[Rows]
    FROM 
        sys.tables t
    INNER JOIN      
        sys.indexes i ON t.OBJECT_ID = i.object_id
    INNER JOIN 
        sys.partitions p ON i.object_id = p.OBJECT_ID AND i.index_id = p.index_id
    INNER JOIN
        sys.schemas s on s.schema_id = t.schema_id
    WHERE 
        --t.NAME NOT LIKE 'dt%' AND
        i.OBJECT_ID > 255 AND   
        i.index_id <= 1 AND
        s.name ='schema'--add your schema here
    GROUP BY 
        s.name,t.NAME, i.object_id, i.index_id, i.name, p.[Rows],t.create_date
