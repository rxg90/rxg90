-- truncate the table first
use rocio

--drop table if exists dbo.Movie ;
create table dbo.Movie 
(
[Year] varchar(max) null
,[Length] varchar(max) null
,Title varchar(max) null
,Subject varchar(max) null
,Actor varchar(max) null
,Actress varchar(max) null
,Director varchar(max) null
,Popularity varchar(max) null
,Awards varchar(max) null
,[Image] varchar(max) null
)


TRUNCATE TABLE dbo.Movie;
GO
 
-- import the file
BULK INSERT dbo.Movie
FROM 'C:\Users\ASUS-PC\Downloads\CsvFiles\film2.csv'
WITH 
(	FIRSTROW = 2
    ,FIELDTERMINATOR = ';'
    ,ROWTERMINATOR='\n'
)
GO

select top 10*
from dbo.Movie

--drop table if exists dbo.movie_clean;
select 
getdate() as CreatedDate
,cast (year as int) as Year
,cast (length as int) as Length
,rtrim(ltrim(cast(Title as varchar(100)))) as Title
,rtrim(ltrim(cast(Subject as varchar(100)))) as [Subject]
,rtrim(ltrim(cast(Actor as varchar(100)))) as Actor
,rtrim(ltrim(cast(Actress as varchar(100)))) as Actress
,rtrim(ltrim(cast(Director as varchar(100)))) as Director
,cast (Popularity as int) as Popularity
--1 true 0 false
, case when awards = 'No' then 0 else 1 end as Awards
,rtrim(ltrim(cast(Image as varchar(100)))) as [Image]
into dbo.movie_clean
from dbo.movie

select *
from dbo.movie_clean
where title = 'Island of Dr. Moreau, The'

--check if it has duplicates

declare @checkDups int = 0

select @checkDups = count(*)
from dbo.movie_clean
group by title
having count(*) >1

select @checkDups

--declare @checkDups int = 0
if @checkDups > 0 throw 51000, 'There are duplicates in the table.', 1; 
else exec sp_rename 'dbo.movie_clean','movie_new'
--drop table dbo.movie_new





