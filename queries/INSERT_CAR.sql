INSERT INTO public."Car"(
	"CarID", "Brand", "Model", "YearOfProduction", "Color", "Insurance", "Diagnostics", "SegmentID")
	VALUES (1, 'Peugot', '208', '2022-01-01', 'Red', TRUE, TRUE, 2),
	(2, 'Seat', 'Leon', '2023-01-01', 'White', TRUE, TRUE, 3),
	(3, 'Toyota', 'Corolla', '2024-01-01', 'Black', TRUE, TRUE, 3),
	(4, 'Hyundai', 'Elantra', '2023-01-01', 'White', TRUE, TRUE, 4),
	(5, 'Peugot', '508', '2023-01-01', 'White', TRUE, TRUE, 5),
	(6, 'Toyota', 'Camry', '2021-01-01', 'Blue', TRUE, TRUE, 5),
	(7, 'Hyundai', 'Tucson', '2023-01-01', 'Grey', TRUE, TRUE, 6),
	(8, 'Toyota', 'RAV4', '2022-01-01', 'White', TRUE, TRUE, 6),
	(9, 'Peugeot', 'Partner', '2024-01-01', 'Black', TRUE, TRUE, 7);

ALTER TABLE public."Car"
ADD COLUMN "Status" VARCHAR(20) DEFAULT 'available';