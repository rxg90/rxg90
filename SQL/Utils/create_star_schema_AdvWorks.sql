--DROP schema IF EXISTS dw;
--CREATE SCHEMA dw;

DROP TABLE IF EXISTS dw.fact_sales;
--CREATE TABLE dw.fact_sales as
--Re-calculate subtotal as it wasn't the sum of the lines ammount.
WITH CTE_TOTALS AS
(
select SalesOrderID
,sum (LineTotal) as SubTotal
from [SalesLT].[SalesOrderDetail]
group by SalesOrderID
)
SELECT 
      oh.[SalesOrderID]
   --,[SalesOrderDetailID]
   --,[RevisionNumber]
      ,[OrderDate]
      ,[DueDate]
      ,[ShipDate]
    --,[Status]
    --,[OnlineOrderFlag]--They are all zero
      ,[SalesOrderNumber]
      ,[PurchaseOrderNumber]
    --,[AccountNumber]
      ,[CustomerID]
      ,[ShipToAddressID]
      ,[BillToAddressID]
      ,[ShipMethod]
    --,[CreditCardApprovalCode]
     --,oh.[SubTotal] as orig_subtotal
	  ,[ProductID]
	  ,[OrderQty]
      ,[UnitPrice]
      ,[UnitPriceDiscount]
	  ,[LineTotal]
	  ,t.[SubTotal] as SalesOrderSubtotal
      ,[TaxAmt]
      ,[Freight]
    --,[TotalDue]
	  ,t.[SubTotal]+[TaxAmt]+[Freight] SalesOrderTotalDue
    --,[Comment]
    --,[rowguid]
	  ,od.[ModifiedDate] as DetailModifiedDate
      ,oh.[ModifiedDate] as HeaderModifiedDate
  INTO dw.fact_sales
  FROM [SalesLT].[SalesOrderHeader] oh
  left join CTE_TOTALS t
  ON oh.SalesOrderID = t.SalesOrderID
  left join [SalesLT].[SalesOrderDetail] od
  ON oh.SalesOrderID = od.SalesOrderID
 -- where 1=1
 -- and oh.SalesOrderID = 71780


--Create dim product table 
DROP TABLE IF EXISTS dw.dim_product;
SELECT [ProductID]
      ,[Name]
      ,[ProductNumber]
      ,[Color]
      ,[StandardCost]
      ,[ListPrice]
	  , null as PrevListPrice
      ,[Size]
      ,[Weight]
      ,[ProductCategoryID]
      ,[ProductModelID]
	  ,case when SellStartDate is not null and SellEndDate is null then 1
	  else 0 end as Active
      --,[SellStartDate]
      --,[SellEndDate]
      --,[DiscontinuedDate]
      --,[ThumbNailPhoto]
      --,[ThumbnailPhotoFileName]
      --,[rowguid]
      ,[ModifiedDate]
  into dw.dim_product
  FROM [SalesLT].[Product]
;
--Add table PK
  ALTER TABLE dw.dim_product
  ADD CONSTRAINT PK_Product_ProductID PRIMARY KEY (ProductID);


  ALTER TABLE dw.fact_sales
  ADD CONSTRAINT FK_Product_ProductID Foreign KEY (ProductID)
  REFERENCES dw.dim_product (ProductID)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

--Create dim customer table
DROP TABLE IF EXISTS dw.dim_customer;
SELECT [CustomerID]
      --,[NameStyle]
      ,[Title]
      ,[FirstName]
      ,[MiddleName]
      ,[LastName]
      ,[Suffix]
      ,[CompanyName]
      ,[SalesPerson]
      ,[EmailAddress]
      ,[Phone]
      --,[PasswordHash]
      --,[PasswordSalt]
      --,[rowguid]
      ,[ModifiedDate]
  INTO dw.dim_customer
  FROM [SalesLT].[Customer]

  --Add table PK
  ALTER TABLE dw.dim_customer
  ADD CONSTRAINT PK_Customer_CustomerID PRIMARY KEY (CustomerID);

  ALTER TABLE dw.fact_sales
  ADD CONSTRAINT FK_Customer_CustomerID Foreign KEY (CustomerID)
  REFERENCES dw.dim_customer (CustomerID)
  ON DELETE CASCADE
  ON UPDATE CASCADE;


