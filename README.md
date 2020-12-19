# Blog Web Application

#### The project is a website where users can create or update blogs. The implementation is fairly simple, to keep the project scope in check. I wanted to make a project like this to expand my knowledge of python flask and of techniques like  database, user authentications, etc.

#### I have used Flask, Bootstrap, sqlite3 other libraries or packages.

#### How the webpage works?
The idea is simple. The user can register themselves, during registration you need to enter these fields:
  username
  Email
  Password: it is checked to match and is hashed after checks are done
after registration it allows you to access dashboard, where you can see or create new posts. You can update your account info, update your profile picture.


#### Routing
Each route checks if the user is authenticated, a user cannot access his/her account without logging in.

#### Sessions
The webpage uses sessions to confirm that user is registered.

#### Database
Database stores all users, posts, user info.

#### Possible improvements
As all applications this one can also be improved.

Possible improvements:
Have a ability for user to upload videos or pictures in the post.
Notificaitons to email about new posts.


![Image](https://github.com/Anshika15/Blog/blob/master/blog.gif)
