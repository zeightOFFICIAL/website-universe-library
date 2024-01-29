## <p align="center"> Website – interactive library for information about universe, space and objects within</p>

### Created by Artemii "Zeight" Saganenko

#### Saint Petersburg State University of Telecommunications

### Description

The online library of the universe, objects in it, patterns and other scientific facts. The site provides the user with information from various sources and different formats to study and gain knowledge. The information presented on this site can be used to obtain basic knowledge about the Universe, both in educational institutions and for personal purposes. Information formats: visual representation of various star systems, text describing individual facts or general information about some objects, raster images of some particularly important objects, embedded video and audio. The main goal is to increase the user's awareness of the structure of the Universe, galaxies, and star systems within it. Main advantages: modularity, simplicity and ease of navigation. Level of knowledge: between basic and intermediate. This is a simple, heavily bugged Django web-site, which implements some of its features. It uses native and custom backend scripts, backend database.

### Features

#### Star system page

The first and primal goal of this project is to improve people's awareness of the structure and content of the Universe. The star system page was the first thing created during development. This is one of the most important pages that allows the user to look at various space systems, gain some knowledge, learn. It features a three panel view which allows users to learn about space using various types of information. Audio, video, text, images, etc.

Currently, implemented database and predefined python instances, allows watching over several star systems. Two of them are completely ready, one is almost completed, and one has a backbone and some additional info. This proves the technical consistency, and general modularity in the project's subsection. Since half of the systems are predefined and half is generated based on DB content.

<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/5d14701d-192e-42d5-94dc-5cadad559673" width="49%"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/7fade4e1-cbe9-482c-b7e3-b5958e73831f" width="49%"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/5fae56a0-ac07-47b9-8413-d93d8a59498a" width="49%"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/7e403369-f652-429f-a492-0ad959d77afa" width="49%"></img>

The page is divided into three parts from left to right: the navigation bar, the information bar, and the visual system layout. Each panel provides a convenient way to explore and learn. Three of them combined creates a user-friendly, convenient experience with simple navigation and laconic interface. Which in the end makes it enjoyable and easy to learn about space. The leftmost panel is the navigation panel, which contains three buttons, from top to bottom: open object side panel, open star side panel, return to universe page. The middle panel is information panel, it displays the details about various objects within special frames, using different information types. The rightmost panel, is the visual representation panel, which shows a visual imitation of the system's top-down view.

The objects' sidebar lists the most prominent objects (the ones detailed in DB or predefined instance) in the stellar system. Each name is clickable and will eventually display information about the selected item in the center and right panels. Additionally, when you hover over an object, it will be highlighted in the system layout panel. It utilizes simple JS scripts and forced styles to open/close, hover-highlight, click/show. The star sidebar lists all available star systems (the ones that are listed in DB or is an instance), it allows jumping to other's star system pages. It uses HTML's anchor, href, JS's scripts for hovering animation. Both utilizes server side script that gets information from DB, or instances.

The information panel, is the prime section which displays sets of different frames that hold various facts, texts and so on. The modular way of interpreting information from DB or instances have been implemented, the transformation cycle will be displayed further. Simply speaking, it allows representing different types of information in a specially designed way. Each frame, the container of information is script-generated, depending on columns (in case of DB) or fields (in case of predefined instance), values. So frame is generated and embedded into the HTML with a help of server side scripts. It can store images, texts, titles, sliders, audio, video, tables, based in the way author was intended to display this particular part. HTML, JS scripts and Python scripts are responsible for proper representation. 

The visual representation panel allows users to observe the stellar system from a top-down view. Scaling was not implemented, but timing is partially. Roughly, one day of real time was narrowed down to one second. So 365 days equals 365 seconds. This mostly does not concern moons and other objects with orbiting time less than day. The entire visual representation with animation is generated with a help of server side script which parses for objects, orbit and spin that are described in DB's columns or instance's fields.

<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/3ec8fd11-ef0f-478b-b43d-cf97c37788f4" height="170px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/3f732b81-385a-49e4-8a63-34e780951896" height="170px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/919e996b-61b6-492c-ade3-3ce2f8d8cc04" height="170px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/f8a6563f-add9-4b67-b1bc-4d80f1a3627b" height="160px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/ad31080d-8b1c-47a1-9eaa-87aeeddd2257" height="160px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/e3e00fd2-e91c-4ded-9cd7-14509a8a43b4" height="160px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/c74ad5b5-5a88-49d9-a23c-af6e4cb33a12" height="160px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/01134aa0-f82e-41b4-84a6-9ec17804aba5" height="148px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/7c543244-da08-437b-bb6d-495d4d5be9ce" height="148px"></img><br>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/0ccb7099-da80-4dc1-81a9-b6931ea722ca" height="73px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/fd0078cf-efd7-4d03-b506-9599e623ff6c" height="73px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/1a63907e-22da-4e66-b3c1-1ac1accc5a5c" height="73px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/003afaf7-c524-4fba-aa4b-fac9f6c95b5d" height="73px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/63d8282a-10db-40a7-a25b-be230d5e611d" height="73px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/2d40a8bc-1847-444c-a20e-5c2df9f12e5b" height="293px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/160789b9-2fce-4f31-aec0-d2741a1cfd1a" height="293px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/b1ebc309-57e5-4fdb-bb65-ddfbb45d1599" height="293px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/85df344c-a23c-43fe-a195-9a21a54f33ee" height="293px"></img>

#### Universe page

In order to navigate through systems successfully and with no delays, a special page has been designed, so that user can jump to desired systems instantly. The most important goal in this task, is to create a user-friendly, simple interface to interact with. So the simple idea of cards was implemented. This page allows jumping to various implemented stellar systems as well as to navigate through web-site with a help of navigation panel in the top of the page. It also features anchors to about page and index page at the bottom.

<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/414a5590-d283-492d-a534-f225bcf9fafa" width="100%"></img>

The universe page consist of two parts. The first one is the navigation panel at the top of the page. It is the main tool to navigate on the website. It features links to different pages as well as the index one, simply allowing to quickly navigate through the entire site. The second part, lower one, is the main aspect of this page. Representing cards with stellar system information, it allows jumping to all the represented systems. It uses SwiperJS's library as a backbone to show the deck of cards. The user can select either card from the deck using keys (left and right), using mouse dragging, mouse scrolling, or by clicking on the pagination below. It uses different JS scripts for hovering effects and selection events. A combination of SwiperJS and custom JS scripts represents the deck, card selection in order to effectively help with user's navigation. The page utilizes the DB and scripts to fetch a list of systems and all required fields to represent each card. In the end, it features simple anchors to index page and about page.

<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/92a85f1a-6154-4bcd-b0fa-4e800a37d749" height="273px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/02d23d20-e857-4926-9cef-b1dd037b398b" height="273px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/e0585a0f-a8e4-47a7-aa99-9a3d01b83d19" height="273px"></img>
<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/3c0af5eb-c246-4b13-b9d7-d0146fce1b2d" height="273px"></img>

### Stack

Descending order

* HTML5
* CSS3
* JavaScript
* Python3
* Django
* SQLite
* GitHub

### Technologies

* Visual Studio Code (https://code.visualstudio.com/)
* SQLiteStudio (https://sqlitestudio.pl/)
* DBeaver (https://dbeaver.io/)
* Draw.io (https://app.diagrams.net/)
* Mozilla (https://www.mozilla.org/)

### Launch conditions
Follow standard procedures. Don't forget to add .env, which must contain SECRET_KEY, to makemigrations/migrate, to manage your own DB (template is provided). Please note that this website does not contain any configurations and/or content for deployment. Use your own techniques for efficient deployment.

### Packages list

* Django
* Django-compressor
* Django-libsass

### Development notes

#### System types UML

<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/81c3904b-4e25-4856-a63d-9668cf89aa1c" width="100%"></img>

#### Systems ERD

<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/45db7b66-fe53-476a-a432-f241632dbf30" width="100%"></img>

### System transform diagram

<img src="https://github.com/zeightOFFICIAL/website-universe-library/assets/50341618/a64d5406-755d-49b1-bb0d-a23b50541ac2" width="100%"></img>


#### Deployment notes
No deployment is configured or implemented. Use your own techniques for efficient deployment.

#### Deploy stack
No deployment is configured or implemented. Use the technologies of your choice for deployment. Please note that Django works with WSGI/ASGI, which must be implemented on the web server.

### Copyrights

1. Program license: MIT License, conditions listed in LICENSE (https://github.com/zeightOFFICIAL/website-universe-library/blob/master/LICENSE)
2. Font <i>Ostrovsky</i> belongs to its rightful owner. Sasha Pavljenko. (Distribution: https://fonts-online.ru/fonts/ostrovsky)
3. Font <i>Earthorbiter</i> belongs to its rightful owner. Iconian Fonts and Daniel Zadorozny. (Original source: http://www.iconian.com and it's distribution mirror: https://fonts-online.ru/fonts/earth-orbiter)
4. Font <i>Vanadine</i> belongs to its rightful owner. Axel Lymphos. (Original source: https://www.dafont.com/vanadine.font and mirror: https://fonts-online.ru/fonts/vanadine)
5. Font <i>Alienleague</i> belongs to its rightful owner. Iconian Fonts and Daniel Zadorozny. (Original source: http://www.iconian.com and mirror: https://fonts-online.ru/fonts/alien-league)
6. CodePen <i>Solar System Pure CSS by Shaahin Hosseini</i> (dist at: https://codepen.io/Falcon9901/pen/pbpzdG) used as inspiration and concept
7. CodePen <i>Solar System Animation by Vivian Zhang</i> (dist at: https://codepen.io/taiwei426/pen/azObRN) used as inspiration and concept
8. Library <i>SwiperJS</i> belongs to it's contributors, and distributed under MIT License (https://github.com/nolimits4web/swiper, https://swiperjs.com/)
9. Part of images used are distributed separetely, and either NASA's national heritage, open source, or, if any, are distributed under non-commercial base. If images are served by another websites, they belong to the rightful owners of the sites' content. In any case, contributor of this repo is not in position of ownerships for any of represented images. Please inform me via any means possible if displayed (stored, ref'ed, linked) image violates your rights.
