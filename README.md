# Backend Recruitment Task
## Description of solution

Final solution of the web API is divided into 3 apps:
- **recruitTask** - main app which consists all configuration and providing admin functionality
- **account** - app which provides Profile model and login/logout functionality
- **grades** - app which provides Task and Grade models, and required end-points

Instead of creating Candidate and Recruiter models, the Profile model was created. It extends User model using a one-to-one link and consist is_recruiter field, which diffrentiate Candidates and Recruiters.
In order to test functionality in the SQlite database there is some test data. 

## Login/logout functionality
In order to grade the task you must to login to recruiter account to do that you must go to */account/login* end-point and POST the recruiter account credentials. 
There are 2 accounts for recruiters (recruiter1 and recruiter2). The POST for recruiter1 should look like this:
```
{
"username": "recruiter1",
"password": "recr1234"
}
```
And for the recruiter2 account, you should change username for *recruiter2*.
To logout from account go to */account/logut* end-point.

## Required end-points
First one was the form to allow grading tasks by recruiters. It is avaivable on *grades/api/add-mark* end-point. Forms checks if task for the specific candidate has been graded. In the Recruiter ForeignKey field, the PrimaryKey of the user, who is currently logged in, is saved.

The second end-point is available on */grades/summary*, and it provides a summary of the grades for all of the candidates.
