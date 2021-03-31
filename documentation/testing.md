# Sionnach Scenes

[Sionnach Scenes](https://sionnachscenes.herokuapp.com/) can be found here.
[Sionnach Scenes Repository](https://github.com/Gwen-of-lynn/sionnachscenes) can be found here. 
[Sionnach Scenes README](https://github.com/Gwen-of-lynn/sionnachscenes/blob/master/README.md) can be found here.

---
---
---
## Automated Testing
---
---
### Validation Services
---
The following validation services and linter were used to check the validity of the website code.
- [W3C Markup](https://validator.w3.org/) Validation was used to validate HTML.
- [W3C CSS](https://validator.w3.org/) validation was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate JavaScript.
- Lighthouse in Devtools
- Flake8

---
### Python Testing
---
Python was tested by the debugger in app.py. The debugger is currently set to False.

---
---
### Manual Testing
---
---

Below is an account of the manual testing that has been done to confirm all areas of the site work as expected.

---
### Testing undertaken
---

All buttons and links on all pages were tested to ensure opertation. All registration processes, all product addition, changes, deletions, login, logout, adding to cart, removing from cart, increasing quantity, checking out, adding post, and commenting were all tested.
    
---
---
## Bugs discovered:
### stripe_elements_js
- 34	'template literal syntax' is only available in ES6 (use 'esversion: 6').
- 98	'template literal syntax' is only available in ES6 (use 'esversion: 6').
Action taken: did not change as it does work with manual testing.

### index.html
- 9    <meta charset="utf-8">
    - Element meta is missing one or more of the following attributes: content, itemprop, property. 
- 10    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    - Attribute name not allowed on element meta at this point.
Action taken: none. As this was the meta block given by the tutorial and the page is working. It was also not picked up by lighthouse
- 50 Validator says Body tag is the 2nd found and recommends removal
Action taken: changed tag to a div, page no longer behaved as expected. At this time, since the page is working as expected with the "body" where it is I will leave it there.

### Common bugs

Many bugs that are being picked up are because of the inclusion of non-html elements like jinja and django. 

---
---
### Solved bugs

Bug:
The input buttons for images on the add and edit product pages was edited to be a button that ended up taking up the whole form and not allowing for input in the other feilds. 
Solution:
Checked what the button was in the tutorial and switched it back to Input. This does make styling tricker and makes it less attractive but it does work. 
Similar was found for the "Sign up" button on the registration page, and the "reset my password" button on the password reset page. However these were able to be more easily styled. 

Bug:
Summernote and sionnachscenes deployed site disconnected causing the deletion of posts and inability to make new posts.

Solution:
X_FRAME_OPTIONS = 'SAMEORIGIN' was added in settings.py. This solved the issue. The stories that were already posted were unable to be recovered.


---
### Terminal Listed Errors
---

There are warnings and 'errors' listed in the gitpod console. These are not actually bugs. The primary source of these is because the parts that are coming up missing are in the base template rather than the individual html files. Others are because some of the lines are too long.

Products.html has multiple {
	"message": "Special characters must be escaped : [ > ].",
No action taken as this error was inherited from Boutique Ado Tutorial

---
### Areas for Improvement
---
- The images in the products would be better in smaller file sizes for ease of download and speed.
---
---