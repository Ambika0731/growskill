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
