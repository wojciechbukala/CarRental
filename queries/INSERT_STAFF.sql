INSERT INTO public."Address"(
	"AddressID", "Address1", "Address2", "PostalCode", "City", "Country", "PhoneNumber")
	VALUES (150, 'Lubuska', '78/20', '53-514', 'Wroclaw', 'Poland', '123456789'),
	(151, 'Powstancow', '50/14', .'53-513', 'Wroclaw', 'Poland', '987654321');
)

INSERT INTO public."Staff"(
	"StaffID", "FirstName", "LastName", "Email", "Position", "AddresID")
	VALUES (1, 'Wojciech', 'Bukala', 'wojciech_bukala@outlook.com', 'CEO', 150),
	(2, 'Piotr', 'Omiecina', 'piotrek.omiecina@gmail.com', 'Intern', 151);