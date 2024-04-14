# growskill

User Journey:

User: Alice, interested in taking a baking course

1. Alice visits the GrowSkill website.
2. She browses through the available courses and selects the "Baking Basics" course.
3. She views the course details including the schedule, instructor, and course fee.
4. Alice decides to enroll in the course and proceeds to the payment page.
5. She makes the payment using her preferred payment method.
6. After successful payment, Alice receives a confirmation email with the details of the course schedule, Zoom link for the first class, and instructions on how to access the course materials.
7. On the scheduled date and time, Alice attends the live baking class via Zoom.
8. She enjoys the interactive session and learns various baking techniques.
9. After completing the course, Alice receives another email with access to the recorded classes and a downloadable certificate.
10. Alice downloads her certificate and feels accomplished.

Data Model
---------------------------------------
---------------------------------------

Table: User

Attributes:
user_id PrimaryKey,
name,
email,
password,
payment_info

---------------------------------------

Table: Instructor

Attributes:
id PrimaryKey
name 
specialization

---------------------------------------

Table: Course

Attributes:

id PrimaryKey
title
description
fee
instruter_id ForeignKey

---------------------------------------

Table: class

Attributes:

id PrimaryKey
course_id ForeignKey
date
time
topic
zoom_link
is_completed
recording_link

---------------------------------------

Table: Enrollment
Attributes:

id PrimaryKey
user_id ForeignKey
class_id ForeignKey
enrollment_date
payment_status

---------------------------------------

Table: Certificate 

Attributes:

id primary_key, 
enrollment_id ForeignKey, 
is_generated 
download_link
issue_date

Implementation:

-- Create User:
INSERT INTO
    User (name, email, password, payment_info)
VALUES
    (
        'Alice',
        'alice@example.com',
        'password',
        'PaymentInfo'
    );

-- Retrieve Course Details:
SELECT
    *
FROM
    Course
WHERE
    title = 'Baking Basics';

-- Enroll in a Course:
INSERT INTO
    Enrollment (user_id, course_id, enrollment_date, payment_status)
VALUES
    (user_id, course_id, enrollment_date, payment_status);


-- Make Payment(update payment info in user table):
UPDATE
    User
SET
    payment_info = 'NewPaymentInfo'
WHERE
    user_id = user_id;

-- Schedule a Class:

INSERT INTO
    Class (course_id, Date, Time, Topic, Zoom Link)
VALUES
    (
        courseID,
        '2024-04-20',
        '10:00 AM',
        'Introduction to Baking',
        'zoomlink'
    );

-- Attend Live Class: 
-- Provide Zoom link from Class details.

select
    zoom_link
from
    Class  as cls join
    Enrollment  as en 
    on cls.id = en.class_id
where
    cls.course_id = courseID
    and cls.date = '2024-04-20'
    and cls.time = '10:00 AM'
    and en.user_id = '1'

-- Access Recorded Classes:

SELECT
    *
FROM
    Class
WHERE
    CourseID = courseID;

-- Download Certificate: 
-- Provide a download link for the certificate.

select
    download_link
from
    certificate
where
    enrollment_id = EnrollID
