DROP TABLE IF EXISTS public."Payment";
DROP TABLE IF EXISTS public."Rental";
DROP TABLE IF EXISTS public."Customer";
DROP TABLE IF EXISTS public."Staff";
DROP TABLE IF EXISTS public."Address";
DROP TABLE IF EXISTS public."Car";
DROP TABLE IF EXISTS public."Segment";

--------- CREATE TABLE ADDRESS ---------
CREATE TABLE IF NOT EXISTS public."Address"
(
    "AddressID" SERIAL PRIMARY KEY,
    "Address1" character varying(40) COLLATE pg_catalog."default",
    "Address2" character varying(40) COLLATE pg_catalog."default",
    "PostalCode" character varying(6) COLLATE pg_catalog."default",
    "City" character varying(50) COLLATE pg_catalog."default",
    "Country" character varying(50) COLLATE pg_catalog."default",
    "PhoneNumber" character varying(16) COLLATE pg_catalog."default"
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public."Address"
    OWNER to postgres;
	
---------- CREATE TABLE CUSTOMER ------------
CREATE TABLE IF NOT EXISTS public."Customer"
(
    "CustomerID" SERIAL PRIMARY KEY,
    "FirstName" character varying(40),
    "LastName" character varying(40),
    "Email" character varying(40),
	"Password" character varying(100),
    "AddressID" integer,
    "CreateDate" date,
    CONSTRAINT fk_address FOREIGN KEY ("AddressID")
        REFERENCES public."Address" ("AddressID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public."Customer"
    OWNER to postgres;
	
-------- CREATE TABLE SEGMENT ---------------
CREATE TABLE IF NOT EXISTS public."Segment"
(
    "SegmentID" SERIAL PRIMARY KEY,
    "SegmentSign" "char",
    "PricePerHour" double precision
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public."Segment"
    OWNER to postgres;

---------- CREATE TABLE CAR ---------------
CREATE TABLE IF NOT EXISTS public."Car"
(
    "CarID" SERIAL PRIMARY KEY,
    "Brand" character varying(16) COLLATE pg_catalog."default",
    "YearOfProduction" date,
    "Color" character varying(16) COLLATE pg_catalog."default",
    "Insurance" boolean,
    "Dignostics" boolean,
    "SegmentID" smallint,
    CONSTRAINT fk_segment FOREIGN KEY ("SegmentID")
        REFERENCES public."Segment" ("SegmentID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public."Car"
    OWNER to postgres;
	
---------- CREATE TABLE RENTEAL -------------
CREATE TABLE IF NOT EXISTS public."Rental"
(
    "RentalID" SERIAL PRIMARY KEY,
    "RentalDate" date,
    "ReturnDate" date,
    "CarID" integer,
    "CustomerID" integer,
    CONSTRAINT fk_car FOREIGN KEY ("CarID")
        REFERENCES public."Car" ("CarID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_customer FOREIGN KEY ("CustomerID")
        REFERENCES public."Customer" ("CustomerID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public."Rental"
    OWNER to postgres;
	
---------- CREATE TABLE PAYMENT ------------
CREATE TABLE IF NOT EXISTS public."Payment"
(
    "PaymentID" SERIAL PRIMARY KEY,
    "CustomerID" integer,
    "RentalID" integer,
    "Amount" double precision[],
    "Date" date,
    CONSTRAINT fk_customer FOREIGN KEY ("CustomerID")
        REFERENCES public."Customer" ("CustomerID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_rental FOREIGN KEY ("RentalID")
        REFERENCES public."Rental" ("RentalID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public."Payment"
    OWNER to postgres;
		
		
---------- CREATE TABLE STAFF -------------
CREATE TABLE IF NOT EXISTS public."Staff"
(
    "StaffID" SERIAL PRIMARY KEY,
    "FirstName" character varying(50) COLLATE pg_catalog."default",
    "LastName" character varying(50) COLLATE pg_catalog."default",
    "Email" character varying(50) COLLATE pg_catalog."default",
    "Position" character varying(50) COLLATE pg_catalog."default",
    "AddresID" integer,
    CONSTRAINT fk_address FOREIGN KEY ("AddresID")
        REFERENCES public."Address" ("AddressID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public."Staff"
    OWNER to postgres;