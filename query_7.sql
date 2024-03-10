SELECT s.name, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.id
    WHERE s.id = ? AND subj.id = ?