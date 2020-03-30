
Basic overview of website functions:

-Logins:
	admin user- username: admin, password: administrator
	username: usernamei, password: testuseri
where 1<=i<=5
-Home shows a user their recent reviews, profs and courses included and links to dedicated review pages for each which show all reviews, and splits them into pages if there are multiple. Also contains a search bar, which returns course and prof results.
-Login authenticates the user if the user is not in the banned list/ user ban duration has expired
-Register creates a new user and logs the user immediately if the registration is succesful else redirects back to the register page if unsuccesful.
-Courses and Professors pages show a list of courses/professors, with links to their individual pages and display their reviews, with a link showing all recent/helpful reviews, along with the option for a user to post their own review if they haven't already.
-Review list pages show reviews in a page format, similar to the home page except it's only reviews of that particular course/review.
-Admin can add users to banned list, delete reviews.
-Settings page for now only has password change as a feature.
-All review <textarea> elements use third party editor TinyMCE.

Database structure:

-Inbuilt User model from Django
-Professor table with columns id, Name, Department, Rating
-Course table with Course code as primary key, course name, course description, department, rating
-Course and professor reviews with student(User) as foreign key,Professor/Course as foreign key, Anonymous as a boolean field, Review as a char field. 
-BannedList with id, User as foreign key, End date(datetime).

Additional tables for implementing a rating and upvotes system were also created, however, implementation wasn't possible.

Possible improvements:
-Implement an error message block for the base template, which informs the user of basic errors such as 	 reason for an invalid login. Can be done using session variables in server-side, but is more easily  implemented in client side.
-Implementation of rating and upvote system. Upvote system would be far 'cleaner' if client-side would    be used too i.e without refreshing the page. The database idea was to have a table for both professors  and courses with id as primary key, student and Review id as foreign key and the point  contributed by the user(1, 0 or -1) depending on whether it was upvoted or not voted or downvoted.
-A query can be executed as above for the all entries of Review ids of a particular user and can be  added to display that user's "points". An alternative approach would be to add a column for points to    the User model and simultaneously update that too when a Review is upvoted, downvoted.
-Similarly, the implementation of the rating system can also be executed.
-Overall CSS and structuring of the website. 					

 