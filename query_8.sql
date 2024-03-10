 SELECT AVG(g.grade) AS average_grade
    FROM grades g
    JOIN subjects s ON g.id = s.id
    JOIN teachers t ON s.id = t.id
    WHERE t.id = ?