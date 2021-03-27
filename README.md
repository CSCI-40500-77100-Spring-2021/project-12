# Conveniote

Group Members: Samuel Khong (samdundun), Rachel Tan (RachelTan07 / raycheli, Manal Zneit (mZneit)

#### What is Conveniote?

Conveniote is a convenient note taking app for educators and students. Users can create courses to keep track of their notes, deadlines, resources, and course information. Users can also create their own custom sections to store any other information.

Additional Features:

- Calendar: for keeping track of events for each course
- Reminder system: for when a calendar event is about to take place or a class is about to start
- Customizable interface
- Support for PDF and video files
- Grade calculator

#### Running The Project

- install django: `python -m pip install Django`
- install video embed: `python install django-embed-video`
- cd into app and run: `python manage.py runserver`
- site will be running at: http://localhost:8000/conveniote/index.html

## Software Architecture

#### Important Qualities

- Software Reuse: Users can create new sections to take notes and store information. Each newly created section functions simarly to each other, reusing the same code.
- Product Lifetime: The app is expected to be used throughout a student's education career and an educator's teaching career. The app is also expected to have new users on a consistent basis, further increasing its lifetime.
- Software Compatibility: Features of the app include note taking, support for video and pdf, assignment submission, and possible Blackboard integration. As such, it is important for the app to be compatible with other software that supports these features.
- The organization of the web app into modules reduces its complexity and thus improves its usability. The users can also create their own version of the modules and extend the system beyond its standard interface. This add flexibility to the architecture of Conveniote.
- Any new changes and added functionality made by the user occurs only at the user’s end and are not hard-wired into the app. In this case, other users of the app will not be affected by those changes. 

#### Architecture

- User Interface: web browser, Conveniote app
- User Interface Management: login
- Application Services: note taking, assignment submission, calendar, reminder system, PDF embed, video embed, section creation and customization
- Integrated Services: Blackboard
- Shared Infrastructure Services: authentication, search, user storage

#### Technologies

- Database: NoSQL database
- Platform: web platform
- Server: public cloud (Amazon or Google)
- Open Source: N/A
- Development Tools: Python + Django
