--https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/azure-ad-authentication-sql-server-setup-tutorial?view=sql-server-ver16
--https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addrolemember-transact-sql?source=recommendations&view=sql-server-ver16
-- login creation for Azure AD user
-- Create user [User] from external provider
use master;
CREATE LOGIN [roland.sencial@craftlabs.net] FROM EXTERNAL PROVIDER;
CREATE LOGIN [franco.romanazzi@craftlabs.net] FROM EXTERNAL PROVIDER;
CREATE LOGIN [diego.pasquini@craftlabs.net] FROM EXTERNAL PROVIDER;
CREATE LOGIN [martin.trobo@craftlabs.net] FROM EXTERNAL PROVIDER;
CREATE LOGIN [rocio.gonzalez@craftlabs.net] FROM EXTERNAL PROVIDER;

	
--This query will add a User, Application or Group out of Azure Active Directory to the SQL Server Users. 

--To list the Azure AD logins in master database, execute the T-SQL command:

SELECT * FROM sys.server_principals;

--By adding the user it  does not have read rights on the Azure SQL Database. Perform the next query to give the user the data reader role.

ALTER ROLE db_datareader ADD MEMBER [User]



--Adding a database user 
--USE AdventureWorks2012;  
--CREATE USER Mary5 FOR LOGIN [Contoso\Mary5] ; 

USE TOSE_POC;
CREATE USER roland FOR LOGIN [roland.sencial@craftlabs.net] ; 
CREATE USER franco FOR LOGIN [franco.romanazzi@craftlabs.net] ; 
CREATE USER diego FOR LOGIN [diego.pasquini@craftlabs.net] ; 
CREATE USER martin FOR LOGIN [roland.sencial@craftlabs.net] ; 
CREATE USER rocio FOR LOGIN [rocio.gonzalez@craftlabs.net]  ; 

--Add user to role
--The following example adds the database user UserMary to the Production database role in the current database.
--EXEC sp_addrolemember 'Production', 'UserMary'  

EXEC [sys].[sp_addrolemember] 'db_owner','roland'; 
EXEC [sys].[sp_addrolemember] 'db_owner','franco'; 
EXEC [sys].[sp_addrolemember] 'db_owner','diego'; 
EXEC [sys].[sp_addrolemember] 'db_owner','martin'; 
EXEC [sys].[sp_addrolemember] 'db_owner','rocio'; 
