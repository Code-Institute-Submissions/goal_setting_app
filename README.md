# Goal Keeper

Goal Keeper is an app that allows users to set and track goals. The aim of Goal Keeper is to increase the success rates for users of sticking with and achieving their goals. 

Each goal has associate “steps” which are essentially a list of steps that need to be completed in order for the user to achieve their goals. Throughout the process, users mark the steps as “done” as they complete each step. 

There is also a progress page which displays a list of goals that are in progress, i.e. still have steps that need to be completed in order to achieve the goal. It also displays a list of completed goals, i.e. goals whose steps have all been marked as done.  This page is essentially an overview page of the user’s activity.

By physically marking steps as done throughout the process and by having a visual representation of their progress, users are motivated to complete their goals and feel a sense of achievement each time they mark a step as done, reinforcing this motivation.

A live version of the site is available [here](https://katiemodonnell88-goal-app.herokuapp.com/)

There have been a number of goals already added for the purpose of this project. More goals and categories can be added by the user.

# UX

The colour theme is primarily grey and white throughout the site which is modern and attractive to the user. The colour orange is also used in small amounts which makes certain features pop and is also associated with meanings of enthusiasm, creativity and success. The use of inspirational and meaningful images throughout the site pairs well with the theme and is attractive to users. The overall layout is quite simple and users can access all parts of the site by using any of the three links on the navigation bar. 

In addition, there are no sections which overload the user with too much text or information. Goal keeper aims to inform the user about how to use it with as little text as possible. 

## User story:

1. As a first-time user, I will arrive on the home page and can immediately see an inspirational image and option to learn about why to use Goal Keeper as well as a callout button to “get started today”. These options are kept short and are there for a reason – to immediately grab the user’s attention and to take them directly to where they need to go. If I select “get started today”, I am informed about how the site works in four simple steps. If I chose “why use Goal Keeper”, I am shown three core reasons why to use it. 

2.	As an existing user of Goal Keeper, once I arrive at the site, I either want to have a look at my current progress, my current goals or to add a new goal. Each of these options is immediately available to me through the navigation bar - a very efficient way for users to get to where they want to go as easily and fast as possible.

If I want to add a new goal or a new category, the forms are very easy to find and use with a minimalist design, another feature that makes for a positive user experience.

The design of Goal Keeper leaves the user feeling satisfied with their experience on the site.

# Wireframing

Wireframes were drawn manually and can be found in the wireframes folder.

# Features

## Existing Features

* linkable sections on the site from the navbar
* linkable sections on the home page to other parts of the site
* keyframe bouncing arrows 
* progress page which links in all goals that are in progress as well as those that have been completed. The user can click these goals and will be taken directy to the goal detail page.
* Modals are used to display the list of goals in a category when the user selects the category. This is an efficient use of space on the page.
* Each goal detail page pulls in the “goals status”, “reasons for doing the goal” and the “goals steps” from the database, displaying all information about the goal for the user.

Various forms: 
* add new category
* add new goal
* add new step
* mark steps as done/not done



## Features Left to Implement

* In the future I would like to add the option to add different types of goals. For example, a “habit” could be used to track small daily goals as opposed to one large goal which has a due date.
* Have a reminder for users when their goal due date is near.
* Options to delete and edit goals to be added.

# Technologies Used

* HTML
* CSS
* Materialize - front-end framework used due to its user experience focus and ease of use. (https://materializecss.com/).
* Font Awesome used to displays the arrows on the home page (https://fontawesome.com/).
* JQuery -  used to simplify DOM manipulation.
* JavaScript used to allow dynamic content to get executed in the site, for example the dropdowns, model and datepicker.  (https://www.javascript.com/).
* Python3 – the language used (https://www.python.org/).
* Flask - Flask is a microframework for Python and was used due to its flexibility and simplicity, making it a suitable framework for this app. (http://flask.pocoo.org/).
* MongoDB - MongoDB is a document database (https://www.mongodb.com/what-is-mongodb).
* mLab – Database-as-a-Service for MongoDB, used to store goals and their data (https://mlab.com/welcome/).
* Popper.js - a JavaScript library for enabling dropdowns.
* Google Fonts for downloading different font styles (https://fonts.google.com/).
* Hover.css - library for creating effects on hovering over an image.

# Testing

The site was tested on 21" monitors, 15" and 13" laptop screens and on the following phone screens: iPhone 6/7/8; Galaxy S5, Pixel 2; Pixel 2XL; iPhone 5/SE; and iPhone x. It was also tested on iPad and iPad Pro screen sizes. The site is responsive and working on all screen sizes. 

Media queries and CSS were used to adapt the sizes of forms across devices and to keep the modal responsive on smaller screens. On small screen sizes, the layout of the modal needed to be changed in order for it to work (the image sits on top on small screens as opposed to adjacent on larger screens). In addition, on small screens the text is hidden and only the callout buttons are displayed on the home page.

The site was also tested using Internet Explorer, Firefox and Chrome.

User testing was done to ensure:

* All links work correctly.
* All navbar links work correctly.
* Model relationships work effectively on all devices and screen sizes.
* The site is responsive across all screen sizes and devices.

The following forms are posted correctly and the database is updated accordingly:
a. Add category
b. Add new goal
c. Add new step
d. Mark step done/not done

* Form submission works across all devices and screen sizes.
* User is redirected to the correct pages after forms are posted.
* The progress page updates accordingly when new goals are added and old goals have been completed.
* All goals appear on the “View Goal” page under their category. Newly added goals also appear. Each goal links correctly to its “Goal Detail” page when it’s selected.
* The “Goal Detail” page is updated correctly when steps are marked as done and not done. The correct information about the goal’s status and reasons for the goal is displayed.

## Issues 

An interesting bug when viewing app on internet explorer only  (within the desktop view). Home page text is push down to second section of the page but when the page is inspected, it moves back up the correct part of the page.

# Deployment

The site is hosted on Heroku (https://katiemodonnell88-goal-app.herokuapp.com/).

Run locally

To run this site locally, in your terminal enter: git clone https://github.com/katiemodonnell/goal_setting_app 

# Credits

## Content

* Reasons for setting goals taken from https://the-happy-manager.com/tips/benefits-of-goal-setting/   

## Media

* The photos used in this site were obtained from https://unsplash.com/ and https://pixabay.com/en/. 
