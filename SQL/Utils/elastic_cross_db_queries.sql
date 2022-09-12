--https://stackoverflow.com/questions/6572754/sql-azure-copy-table-between-databases

CREATE MASTER KEY ENCRYPTION BY PASSWORD = '<password>';

CREATE DATABASE SCOPED CREDENTIAL SQL_Credential  
WITH IDENTITY = '<username>',
SECRET = '<password>';

CREATE EXTERNAL DATA SOURCE RemoteReferenceData
WITH
(
    TYPE=RDBMS,
    LOCATION='<server>.database.windows.net',
    DATABASE_NAME='<db>',
    CREDENTIAL= SQL_Credential
);

CREATE EXTERNAL TABLE [dbo].[source_table] (
    [Id] BIGINT NOT NULL,
    ...
)
WITH
(
    DATA_SOURCE = RemoteReferenceData
)

SELECT *
 INTO target_table
FROM source_table
