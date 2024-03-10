SELECT g.id, AVG(g.grade) AS average_grade
    FROM grades g
    JOIN subjects s ON g.id = s.id
    WHERE s.id = ?
    GROUP BY g.id