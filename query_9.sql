  SELECT DISTINCT subj.name
    FROM grades g
    JOIN subjects subj ON g.subject_id = subj.id
    WHERE g.student_id = ?