SELECT id,
       CASE
           WHEN id % 2 = 1 THEN
               COALESCE((SELECT student FROM Seat WHERE id = s.id + 1), student)
           ELSE
               (SELECT student FROM Seat WHERE id = s.id - 1)
       END AS student
FROM Seat s
ORDER BY id;
