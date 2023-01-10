# Stellar Web-Library

## Website – library for information about star systems and objects within

### Author: A.V. Saganenko

#### Saint Petersburg State University of Telecommunications

### Description

Internet library for star systems and objects within them. The site presents the user with information from various sources and different formats for study. Information formats: vector image of the star system, text with tables and hyperlinks, raster images, embedded video and audio. The main goal is to increase the user's awareness of the structure of space, in particular star systems. Main advantages: modularity, visibility and simplicity of navigation.

### Dev-stack

* CSS/SCSS
* HTML5
* JavaScript
* Python
* Django

### Launch conditions

Be sure to have packages listed in requirements.txt installed. Use any IDE able to interpret Python code. Launch from manage.py, settings in settings.py.

First launch from new machine

``` python3
python ./manage.py migrate
```

Launch server

``` python3
python ./manage.py runserver
```

### Packages list

* Django is a framework.
* Python Decouple to work with envs.

### Future scope

* Transfer CSS classes of planets to JS. That would be much more effective and open new ways of content creation, representation.
* Alter vector image of systems, now using not CSS classes but JS's.
* Tie the website with SQLite in order to store star systems in DBs.
* Set up admin page.
* Set up manual star systems creating (and objects within) through admin page, considering star systems are stored in DB.
* Optimize Welcome page.
* Update about page.
* Turn off Django debug.
* Set up GET request for static content, using Python package whitenoise.
