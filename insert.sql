INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (1, 'JohnDoe', '123 Main St', 09056789922, '2023-11-25 08:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456945, 1, 5000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550298901, '123 Main St', 10, 1);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965920304, 4.44, FALSE,70550298901);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174404598, '2023-11-30 09:00:00', 2000, 60965920304,42510456945);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (2, 'JoelDC', '124 lin St', 09156689422, '2023-10-12 09:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456978, 2, 5000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550298112, '123 Main St', 10, 2);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (6096592005, 10.44, FALSE,70550298112);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174405678, '2023-11-30 09:00:00', 8000, 6096592005,42510456978);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (3, 'MalishaEr', '34 High St', 08056720922, '2023-11-25 15:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510427455, 3, 5000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (20380965901, '123 Main St', 10, 3);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (70895920304, 14.76, FALSE,20380965901);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (23454404598, '2023-11-30 09:00:00', 12000, 70895920304,42510427455);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (4, 'EvaJohnson', '56 Oak St', 09056789922, '2023-12-01 08:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456999, 4, 8000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550299901, '56 Oak St', 15, 4);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965929904, 8.55, FALSE, 70550299901);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174404789, '2023-12-01 09:00:00', 4000, 60965929904, 42510456999);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (5, 'SophiaSmith', '78 Elm St', 08056720002, '2023-12-03 10:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456988, 5, 6000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550298880, '78 Elm St', 7, 5);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965920887, 3.25, FALSE, 70550298880);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174407777, '2023-12-03 11:00:00', 2500, 60965920887, 42510456988);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (6, 'LiamBrown', '92 Pine St', 09156780000, '2023-12-05 08:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456977, 6, 7000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550297771, '92 Pine St', 9, 6);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965927774, 5.75, FALSE, 70550297771);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174408888, '2023-12-05 09:00:00', 3500, 60965927774, 42510456977);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (7, 'EvaJohnson', '15 Oak St', 07056789999, '2023-12-07 09:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456976, 7, 8000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550297662, '15 Oak St', 6, 7);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965927667, 8.5, FALSE, 70550297662);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174409999, '2023-12-07 10:00:00', 4000, 60965927667, 42510456976);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (8, 'NoahWilliams', '20 Maple St', 08056782222, '2023-12-08 08:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456975, 8, 9000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550297553, '20 Maple St', 12, 8);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965927558, 6.75, FALSE, 70550297553);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174406788, '2023-12-08 09:00:00', 5500, 60965927558, 42510456975);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (9, 'SophieClark', '25 Elm St', 09051239999, '2023-12-10 08:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456974, 9, 7000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550297441, '25 Elm St', 15, 9);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965927414, 3.25, FALSE, 70550297441);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174406277, '2023-12-10 09:00:00', 2000, 60965927414, 42510456974);

INSERT INTO USER (user_id, username, address, phone_number, date_joined, Is_active, Is_staff)
VALUES (10, 'OliverMiller', '30 Birch St', 09051119999, '2023-12-11 08:00:00', TRUE, FALSE);
INSERT INTO ACCOUNT (Account_id, User_id, Account_bal)
VALUES (42510456973, 10, 6000);
INSERT INTO METER (Meter_id, location, units, User_id)
VALUES (70550297330, '30 Birch St', 8, 10);
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965927336, 2.5, FALSE, 70550297330);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174406666, '2023-12-11 09:00:00', 3500, 60965927336, 42510456973);


-- Creating new transaction 
INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965920100, 7.8, FALSE, 70550298901);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174400002, '2023-12-16 11:00:00', 3000, 60965920100, 42510456945);

INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965920101, 6.2, FALSE, 70550298112);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174400003, '2023-12-17 09:00:00', 1800, 60965920101, 42510456978);

INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965920102, 5.5, FALSE, 70550297441);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174410004, '2023-12-18 08:00:00', 2500, 60965920102, 42510456974);

INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965920103, 4.9, FALSE, 70550297330);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174400005, '2023-12-19 10:00:00', 2000, 60965920103, 42510456973);

INSERT INTO TOKEN (Token_id, units, Used, Meter_id)
VALUES (60965920104, 6.5, FALSE, 70550298901);
INSERT INTO TRANSACTION (Transaction_id, trans_time, Amount, Token_id, Account_id)
VALUES (26174400006, '2023-12-20 09:30:00', 2200, 60965920104, 42510456945);