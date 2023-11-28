use ezpower;
SELECT *
FROM USER u
INNER JOIN ACCOUNT a ON u.user_id = a.user_id
INNER JOIN METER m ON u.user_id = m.user_id;


SELECT *
FROM METER m
INNER JOIN TOKEN t ON m.Meter_id = t.Meter_id
INNER JOIN TRANSACTION tn ON t.Token_id = tn.Token_id;

-- select * from USER
-- select * from ACCOUNT
-- select * from METER
-- select * from TRANSACTION
-- select * from TOKEN