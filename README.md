# Sionnach Scenes: Stories and Sundries
---
### What does the fox see?
---
---
Sionnach Scenes: Stories and Sundries is a combination of a story prompt page and a satirical store of spoons and related.

#### Sionnach Scenes: Stories  

Stories is a story prompt site where users can add to the original story prompt and users can take turns telling the story in the comments, or start their own story inspired by the prompt.

#### Sionnach Scenes: Sundries 

Sundries is a satirical store jokingly selling things that either don’t really exist, or at least not in a way they can be packaged and sold. Many of the products are based on old jokes, puns, or references. 

This store is for a project for school and won’t actually charge customers for it’s fictitious merchandise.

The current product in the store is spoons. This was inspired by "Spoon Theory". 

>“The Spoon Theory”, a personal story by Christine Miserandino, is popular among many people dealing with chronic illness. >It describes perfectly this idea of limited energy, using “spoons” as a unit of energy.

The above quote is this [Healthline Article](https://www.healthline.com/health/spoon-theory-chronic-illness-explained-like-never-before#1) where you can read more about spoon theory.

A common question amoung Spoonies is "how are your spoons?" You may also find them commenting about the lack of spoons, or a particular type of spoons, or a need for more spoons. 

---
---
## UX
---
---
### Project Goals
---
Sionnach Scenes: Stories will allow for imaginative banter and stories while the Silliness and Sundries will be joke products based mostly on old jokes or puns.

Sionnach Scenes: Sundries allows the site owner a place to share and connect with others over story and light hearted humour.

---
#### Target Audience
---

##### Sionnach Scenes: Stories

The target audiences:

Users:
-	Writers who are...	
	-	of all levels but mostly beginner, amatuer, and aspiring
    -	looking for inspiration
    -	looking for a creative outlet
    - 	looking for a writing community

-	Readers who are... 
	- 	interested in reading short stories
	-	interested in reading ongoing projects
	- 	interested in reading less professional writing

Site Owner:
-	Readers or writers who are…
-	interested in cultivating more of an interest in writing in themselves and 
 	others
-	interested in getting their own ideas out there
-	interested in building a community around writing
-	interesting in reading others takes on story prompts


###### Sionnach Scenes: Sundries


The target audiences:

-	Users would be people who…
	-	enjoy a good pun or satire

-	Site Owner:
    -	enjoys a good pun and satire
    -	enjoys making people laugh

 
---
#### User Stories

To navigate to the User Stories please click the links below or find them in the [Documentation Folder](https://github.com/Gwen-of-lynn/sionnachscenes/tree/master/documentation) for this page.

- [Sionnach Scenes: Stories: User Stories](https://github.com/Gwen-of-lynn/sionnachscenes/blob/master/documentation/UserStories_Sionnach_Scenes_Stories_310321.pdf) 
- [Sionnach Scenes: Sundries: User Stories](https://github.com/Gwen-of-lynn/sionnachscenes/blob/master/documentation/UserStories_Sionnach_Scenes_Sundries_310321.pdf)

---
---
### Design Choices
---
---
#### Fonts

My font for this site is [Lato](https://fonts.google.com/specimen/Lato?preview.text_type=custom) and came from [Google Fonts](https://fonts.google.com/).

#### Icons

The icons used were the [Font Awesome](https://fontawesome.com/) icons. 
 
#### Styling

Colours were chosen with the help of: 
- [Adobe Color](https://color.adobe.com/create/color-wheel), 
- [Color-hex Red Fox Color Palette](https://www.color-hex.com/color-palette/6851)
- [Color-hex Arctic Fox Color Palette](https://www.color-hex.com/color-palette/62083)
- [Color-hex Fox house Color Palette](https://www.color-hex.com/color-palette/68110)
- [Bootstrap](https://getbootstrap.com/docs/4.0/utilities/colors/)
- [Webdesigner Depot: The Dos and Don'ts of Dark Web Design](https://www.webdesignerdepot.com/2009/08/the-dos-and-donts-of-dark-web-design/#:~:text=The%20sans-serif%20font%20is,makes%20the%20text%20very%20legible.)

---
---
 ### Wireframes
 ---
 ---

To navigate to the Wireframes please click the links below or find them in the [Documentation Folder](https://github.com/Gwen-of-lynn/sionnachscenes/tree/master/documentation)

- [Sionnach Scenes: Wireframes](https://github.com/Gwen-of-lynn/sionnachscenes/blob/master/documentation/Sionnach.WF.15.03.21.pdf)

 
---
---

## Features
---
---

### Current Features

#### Common Features
- Interactive bouncing balls javascript overlay

#### [Introduction Page](https://sionnachscenes.herokuapp.com/)
- The main page has simple and clear navigation to both sides of the page, the Stories and the Sundries.

#### [Stories](https://sionnachscenes.herokuapp.com/storystarters/)
##### Header
- Sionnach Scenes Logo 
    - upper left 
    - navigates back to the intro page, in mobile this is just the fox icon at the end of the logo.
- Menu Dropdown
    - lower left 
    - is both Font Awesome bars and Menu text when larger than mobile and the bars when mobile.
    - When signed in or not as a regular user it drops down to: 
        - Stories  
        - Sundries 
    - When signed in as superuser it drops down to: 
        - Stories  
        - Sundries 
        - Add Story (coming soon) 
        - Add Product
- Stories Logo
    - lower center
    - navigates back to main Stories page
- My Account Dropdown
    - lower right 
    - is both the Font Awesome person icon and My Account text when larger than mobile and the person icon when on mobile
    -  When not signed in it drops down to:
        - Register
        - Login
    - When signed in as regular user:
        - My Profile
        - Logout
    - When signed in as Superuser:
        - Add Story (coming soon) 
        - Add Product
        - My Profile
        - Logout
        
##### Stories Main Page 
Story starters are listed here as blog posts, 3 per page with an easily visable next page navigation at the bottom
Each Story Starter has:
- Story Title
- Poster's name
- Date and time stamp of post
- Easily visable Read More button which brings you to...

##### Read More 
The read more section has: 
- an extended version of the story post including:
    - Story Title
    - Poster's name
    - Date and time stamp of post
- a comments section
- an add comments section
    - comments added are moderated by the Superuser in the backend and not added immediately
    - the bottom of the page has a button to return to the main Stories page
    - On the right there's a sidebar with a quirky comment

#### [Sundries](https://sionnachscenes.herokuapp.com/products/)
##### Header
This is the same as the Header in the stories section, with the exception of:
- Sundries Logo
    -lower center
    -navigates back to main Sundries page
- Shopping bag icon with amount currently in bag, 
##### [Main Sundries Page](https://sionnachscenes.herokuapp.com/products/)
- There is a free delivery cost bar
- Droop down sort menu
- Products are arranged in lines of 4, 3, 2, or 1 based on screensize
- The descriptions under the product images have product information
- Clicking on the product brings you do the product detail page

##### [Product Detail](https://sionnachscenes.herokuapp.com/products/10/)
- This page has the product image that can be clicked for a larger view
- The product information is listed beside on most screens, and below on mobile
- Superusers can edit/delete
- All users, logged in and not can increased quantity, return to the main products page, or add to bag

##### [Shopping Bag](https://sionnachscenes.herokuapp.com/bag/)
The shopping bag shows an editable summary of all items added with: 
- Images, 
- Name, 
- Price, 
- Quantity(editable), 
- Subtotal,
- Bag total,
- Delivery cost,
- Total,
- Free delivery information
- and options of:
    - returning to main Sundries page
    - and continuing to Secure Checkout

##### [Secure Checkout](https://sionnachscenes.herokuapp.com/checkout/)
The checkout page consists of:
- a form for to either add or update personal and delivery depending on registration status,
- an option to add information to profile or start profile, pending registration status,
- secure credit card input,
- options to:
    - Adjust Bag
    - Complete Order
- Amount card will be charged, if the site was actually real, for demo purposes a repeating pattern of 42 can be used
- Order Summary

##### Checkout Success
Upon checkout all users will see a page that thanks the user, and summarises the order including:
- Email address used
- Order informaion
- Item summary
- User's information
- Total amounts

At the bottom of the page the user will also see a button to return to Sundries

##### [Add Product](https://sionnachscenes.herokuapp.com/products/add/) and [Edit Product](https://sionnachscenes.herokuapp.com/products/edit/10/)
Add and edit product pages are very similar except for the edit product is filled in with a product's information already and the heading above the card.

Superuser can assign the following:
- Category
- Sku
- Name
- Description
- If product has sizes
- Price
- Rating
- Image URL
- Image
    - Current Image(for edit product)
    - Choose file
- Cancel Button(which returns to Sundries)
- Add/Update Product

#### Toast Alerts
Actions such as adding items to bag, signing in, signing out, completing actions like adding posts all result in a drop down alert in the upper right under the header. 

#### [Admin- Backend](https://sionnachscenes.herokuapp.com/admin)
When signed in as superuser you have access to:
- ACCOUNTS
    - Email addresses	
- AUTHENTICATION AND AUTHORIZATION
    - Groups	
    - Users	
- CHECKOUT
    - Orders	
- DJANGO SUMMERNOTE
    - Attachments	
- PRODUCTS
    - Categories	
    - Products	
- SITES
    - Sites	
- SOCIAL ACCOUNTS (Not active)
    - Social accounts	
    - Social application tokens	
    - Social applications	
- STORYSTARTERS
    - Comments	
    - Posts

---

---
### Features Left to Implement
---
In future I would like this site to have:

- the ability to add a story starter post from the frontend for the superuser
- a link to admin options from the frontend for the admin options for the superuser
- the possibility of threads of story where people adding to the same story are all in the same line and stories inspired by the same prompt are in a different comment thread under the same starter.
- a contact page, primarily for story and product suggestions

If this site went live I would have the 'checkout' in Sundries as a donation page to a drop down list of charities for health and wellbeing.

---
---
## Technologies Used
---
---

#### Tools:

- [Balsalmiq](https://balsamiq.com/) to make the wireframes
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project
- [GitHub](https://github.com/) to store and share all project code remotely
- [Gitpod](https://www.gitpod.io/) to compile and create code
- [Dillinger](https://dillinger.io/0) to make this readme file
- [Stripe](https://stripe.com/en-ie) to accept and manage payments
- [Amazon Web Services S3](https://aws.amazon.com/) to store static and media files
- [Heroku](https://dashboard.heroku.com/apps) to build, run, and operate applications entirely in the cloud. To allow Flask, Python, Jinja, Github to work together

#### Libraries

- [JQuery](https://jquery.com/) to simplify DOM manipulation
- [Bootstrap](https://getbootstrap.com/) to simplify the structure of the website and make the website responsive easily
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The Essential Oil Database
- [PyMongo](https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible
- [Flask](https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages
- [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in html

##### Other Resources

- [Pin Clip Art](https://www.pinclipart.com/) used for royalty free clip art.
- [Public Domain Images](https://www.publicdomainpictures.net) used for free public domain images used for product pictures.
- [Happy bouncing balls :-D](https://codepen.io/b4rb4tron/pen/wjyXNJ) used as interactive background overlay.
- [Django Project](https://www.djangoproject.com/) for reference on how to avail of aspects of django
- [W3Schools](https://www.w3schools.com/) for reference on various aspects of coding
- [Django Centeral](https://djangocentral.com/building-a-blog-application-with-django/) Storystarters blog and comments models are based on this tutorial series

#### Languages

This project uses HTML, CSS, JavaScript, Django, and Python programming languages.

---
---
## Testing
---
---

Testing information can be found in a separate [testing.md](https://github.com/Gwen-of-lynn/ ) file.

---
---
## Deployment
---
---
### Heroku
Please see below link from Heroku for an excellent tutorial for deployment:
>This Heroku Showcase demonstrates several deployment methods available on the Heroku Platform.  In this, the first of three >deployment showcases, you'll see how app can be deployed from the terminal using "git push heroku master", how to deploy >branches on GitHub from the Heroku Dashboard, and the one-click Heroku Button.
>
>Reading list:
>  "Git push heroku master" 0:09​ -  https://devcenter.heroku.com/articles...​
>  GitHub Deploys  1:10​ -  https://devcenter.heroku.com/articles...​
>  Heroku Button  2:37​ - https://devcenter.heroku.com/articles...​
>
>For documentation, visit the Heroku Dev Center: https://devcenter.heroku.com/​

>[Heroku Deployment Methods](https://www.youtube.com/watch?v=fW3yWiRd4E4)

### Stripe 

To get started with Stripe I recommend their excellent [Development Quickstart Guide](https://stripe.com/docs/development/quickstart)

### AWS S3

To get started with AWS S3 I recommend the getting started guides linked below:
- [AWS Quick Start Guide: Back Up Your Files to Amazon Simple Storage Service](https://docs.aws.amazon.com/quickstarts/latest/s3backup/welcome.html)
- [Getting started with Amazon S3](https://aws.amazon.com/s3/getting-started/)
- [Getting started with Amazon S3 - Demo Youtube Video](https://www.youtube.com/watch?v=e6w9LwZJFIA)

---
---
## Credits and Acknowledgements
---
---

For this project I followed a tutorial from Code Institute for [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) to build my own MSP4 ECommerce project, Sionnach Scenes, styling and project needs.

The structure of this readme is based on [A Greave’s Picflip and Familyhub readme files](https://github.com/AJGreaves) and my previous MSP3 Project 9[Essential Oils Database](https://github.com/Gwen-of-lynn/EssentialOilsDatabase).
 
##### Special thanks to:
- Aaron Sinnott, my Code Intstitute mentor for this milestone project.
- The wonderfully patient and helpful members of the Code Institute Tutorial Support and Student Care teams.

##### Disclaimer:

Sionnach Silliness and Sundries was a satirical page made for Code Institute’s Milestone Project 4 and won’t actually charge customers for it’s fictitious merchandise.