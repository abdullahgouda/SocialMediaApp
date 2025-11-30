Django Social Media App

This project is a simple social media application built using Django. It was my first real step into learning the framework, and I chose this idea because I wanted something more challenging and practical than the usual beginner projects.

Throughout building it, I learned how Django works behind the scenes: authentication, class-based views, database relationships, templates, and how to connect all of these pieces into a real, functioning application.

Project Features

User System:

  .User registration, login, and logout
  
  .Secure authentication using Django’s built-in system
  
  .Individual user profile pages

Social Features:

  .Follow and unfollow functionality
  
  .Viewing other users’ profiles
  
  .A personalized feed that displays posts only from the users you follow

Posts:

  .Creating posts
  
  .Viewing posts
  
  .Dynamic feed based on your following list

Internal Concepts Used:

  .Proper database relationships
  
  .Class-Based Views (CreateView, ListView, etc.)
  
  .Efficient QuerySets for filtering and retrieving data



What I Learned While Building This Project
Django Structure

Understanding how Django projects are organized, how apps communicate with each other, and how URLs, views, and templates fit together.

Authentication

Learning to work with Django’s authentication system, session handling, and protecting specific pages using login-required mixins.

Class-Based Views

Using and customizing Django’s class-based views, such as CreateView, ListView, DetailView, UpdateView, and others.
I learned how to override view methods to create custom behavior.

Database and ORM

Building different types of relationships:

One-to-many (User to Posts)

Many-to-many (Follow system)

I also learned how to use Django ORM for filtering, querying, and accessing related objects efficiently.

Real Application Logic

The most valuable part was implementing the feed system, which only shows posts from users you follow.
This helped me understand relational data and how to build logic similar to real-world applications.
