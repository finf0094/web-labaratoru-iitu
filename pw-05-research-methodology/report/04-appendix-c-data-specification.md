# Appendix C. Data extraction specification

| Source | Field | Type | Transformation |
|---|---|---|---|
| AIS | student_id | string | Salted SHA-256 hash; the salt is kept by the IT department only |
| AIS | programme, year of study, form of study (grant/paid), language of instruction | category | Used as features and for fairness analysis |
| AIS | prior GPA, number of previous FX/F | numeric | Calculated at the start of the semester |
| AIS | course_id, teacher_id (hashed), academic group | category | Control variables |
| AIS | weekly current-control points (0–100) | numeric | Cumulative average up to week *w* |
| AIS | midterm 1 / midterm 2 points | numeric | Used only for weeks after they are published (no leakage) |
| AIS | attendance marks per class | binary | Attendance rate up to week *w*; consecutive absences |
| LMS | log events (view, submit, forum post, quiz attempt) | timestamp | Weekly counts, days since last activity, share of on-time submissions |
| AIS | final course grade (letter, 0–100) | category / numeric | Target: 1 if FX/F or admission rating < 50, otherwise 0 |

Excluded fields: names, IIN, phone numbers, e-mail, addresses, health and social-status data.
