# Passport Pages

Web application for travel enthusiasts that wishes to share the travel stories.

Fully published website is here: [Passport Pages]("https://passport-pages-4af24cae3d46.herokuapp.com/")

## Table of Contents
- [About](#about)
    - [Site purpose](#site-purpose)
    - [Target audience](#target-audience)
    - [Goals](#goals)
- [Structure](#structure)
    - [Website Pages](#website-pages)
    - [Code Structure](#code-structure)
    - [Database](#database)
    - [User Stories](#user-stories)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Images](#images)
- [Technologies Used](#technologies-used)
    - [Main Languages Used](#languages)
    - [Frameworks, Libraries & Programs Used](#frameworks)
- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Credits](#credits)


## About <a name="about"></a>

Passport Pages is web application that can be used for anyone who wants to share their travel stories with community.


### Site Purpose <a name="site-purpose"></a>
- Create stories, be able to edit stories.
- Leave a comment to the shared stories. 

### Target Audience <a name="target-audience"></a>
- This site is developed for anyone who is passionate about travel.
- This site is developed for anyone who likes to share their travel experiences.
- This site is developed with thaught that it easy accessable to all users. Compatibility with different device sizes makes the contect easy accessible and readable on desktop or the mobile device.


### Goals <a name="goals"></a>
- To bring some positivity and to create fun environtment for its users.
- To offer a user-friendly platform.
- To produce code that complies with best practices.


## Structure <a name="structure"></a>
### Website Pages <a name="website-pages"></a>
Website pages described below

| Page | Description |
| --- | --- |
| Home | Home page displays a hero image and the latest three added stories. There is additional jumbotron with inviting text and a SignUp button. |
| Stories | Show the list of all stories that have been posted by website users. |
| My Blog | Show the list of all stories that the current registered user has been posted. |
| Edit Page | The user can edit or delete the story. |
| Create Story | The user can create a new story. |
| One story page (Public) | Show the full article and allow to add a comment (only if user has been registered). |
| Add comment | The registered website user can add comment to the post they have selected. |
| Login | The website user can login to their account. |
| Logout | The website user can logout of their account. |
| Register | The website user can register a new account. |


### Code Structure <a name="code-structure"></a>
- The project contains one app 'blog'.
- The aprojects app handles all data.
- The project also have files: 
    - templates
    - README.md
    - TESTING.md
    - Procfile
    - requirements.txt
- The project was built on basis of Django Blog project from Code Institute that was part of a walkthrough app.

### Database <a name="database"></a>
The databas diagram is shown below:
![alt text](./assets/docs/wireframes/db-schema.PNG "Database schema that is used for website")

#### Models
- User
    - User model is part of an allauth Django library. 
    - Fields used for this project were: username, email, password

- Post
    - Post model is the main model.
    - Posts can be seen by anyone who is viewing the webiste.
    - The user must register, if they wish to create a post. 
    - Only that posts user can edit or delete the post.
    - Images added to the post are saved within Cloudinary. 

- Comment
    - Comment model is related to Post and a User. 
    - Comments can be made only registered users. 

### User Stories <a name="user-stories"></a>

All website users/visitors: 
As a **user** I can **create an account** so that **I can create, update and delete posts**
As a **user** I can **view posts published** so that **I can select the one I wish to read about more**
As a **user** I can **select and open an individual post** so that **I can read a full story**

Registered website users:
As a **registered user** I can **create my own posts** so that **I can share them on the blog for other users to read them**
As a **registered user** I can **comment on other posts** so that **I can share my own insight on the story. or leave a comment for the creator**
As a **registered user/content creator** I can **edit my own posts** so that **I can fix any typos or misspellings, or even update some information**
As a **registered user/content creator** I can **delete my own posts** so that **I can clear any unwanted content**

Admin:
As an **admin** I can **manage user accounts and posts** so that **no harmful/malicious content has been posted**


## Design <a name="design"></a>
### Wireframes <a name="wireframes"></a>
For this project Figma tool was used to create layout and design for the web application.

<details><summary>Wireframe screenshots</summary> 

- Summary: 
    - Website has a navbar when user is not logged in, they can see four links: Home, Stories, Login and SignUp. When user is logged in, there are two additional drop down menu items, that are linked to the users posts and create post pages.  
        Home page displays a hero image and last three added stories. There is additional jumbotron with inviting text and a SignUp button.
        ![alt text](./assets/docs/wireframes/ppw-home.PNG "Main page screenshot of wireframe")   

    - 'Stories' page is showing the list of all stories that have been posted by website users. 
        ![alt text](./assets/docs/wireframes/ppw-all-stories.PNG "All stories page screenshot of wireframe")  

    - 'Read More' redirects to one stories page where the full article can be read comments are shown (if there are any). Additionally there is a button 'Comment' that allows user to post a comment to the story, this is allowed only if the user has logged in. 
        ![alt text](./assets/docs/wireframes/ppw-one-story.PNG "One story page screenshot of wireframe")  

    - 'Create/Edit' pages will be for use of a new story creations, or editing, respectively
        ![alt text](./assets/docs/wireframes/ppw-create-and-edit-pages.PNG "Create and edit pages screenshot of wireframe")  

    - 'My Blog' page will display only that user stories that have been created
        ![alt text](./assets/docs/wireframes/ppw-user-side-all-stories.PNG "User side stories page screenshot of wireframe")  

    - Mobile layout of the web application
        ![alt text](./assets/docs/wireframes/ppw-mobile-layout.PNG "Mobile layout screenshot of wireframe")  

</details>


### Color Scheme <a name="color-scheme"></a>
The color palette for this project was taken from [coolors.co](https://coolors.co/) website.  
Background drop, linear gradient, for main page jumbotron was taken from [gradients.shecodes.io](https://gradients.shecodes.io/gradients/623).
![alt text](./assets/docs/wireframes/color-palette.PNG "Color palette that is used for website")


### Typography <a name="typography"></a>
The typography for the project was used from [Google Fonts](https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Shadows+Into+Light&display=swap).
These are fonts that are used: Montserrat and Shadows Into Light (for logo only) If the browser does not support these fonts it should fall back to sans-serif.

### Images <a name="images"></a>
Images used in this project are taken from free images source [pexels.com](https://www.pexels.com/).
Placeholder image was custom made with [Canva](https://www.canva.com/).


## Technologies Used  <a name="technologies-used"></a>

### Main Languages Used <a name="languages"></a>

- HTML: Structure and content for the website
- CSS: Style and compatibilaty with different devices
- Python: Functions and logic implementation to features of a website

### Frameworks, Libraries & Programs Used <a name="frameworks"></a>

- [gitpod](https://www.gitpod.io/): To build the project
- [github](https://github.com/): To store files and repositories. Also often used to search thread for similar issues to resolve errors in the code
- [Heroku](https://heroku.com/): To deploy this web application
- [QuickDatabaseDiagrams](https://quickdatabasediagrams.com/): Create database diagram
- [Cloudinary](https://cloudinary.com/): To store saved images that have been posted by the user
- [Pexels](https://pexels.com/): For additional images to store into database
- [Canva](https://www.canva.com/): Create custom placeholder image
- [Figma](https://https://www.figma.com/): Wireframes
- [Bootstrap](https://getbootstrap.com/): Layouts, cards, buttons
- [FontAwesome](https://fontawesome.com/): Icons
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html): Forms
- [Google Fonts](https://fonts.google.com/): For the fonts that are used across the project
- [Am I Responsive](https://ui.dev/amiresponsive): To check, if website looks good across multiple devices
- [Travel Guide](https://www.myirelandtour.com/travelguide/england/index.php): For content
- Google Chrome DevTools: This was used throught the project to debug and see the compatibilaty across multiple device sizes
