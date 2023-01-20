# Functional Testing

## Authentication

Description:

Ensure a user can register to the blog.

Steps:

1. Navigate to [Irish Cyber Security Blog](https://icsblogp4.herokuapp.com/) and click Register
2. Enter email, username and password
3. Click Register

Expected:

The user is directed back to login screen to login after entering suitable username and password, registration is successful

Actual:

The user is directed back to login screen to login after entering suitable username and password, registration was successful

<hr>

Description:

Ensure a user can log in to the blog.

Steps:

1. Navigate to [Irish Cyber Security Blog](https://icsblogp4.herokuapp.com/) and click Login
2. Enter login details created during registration
3. Click signin

Expected:

User is successfully logged in and redirected to the posts page.

Actual:

User is successfully logged in and redirected to the posts page.

<hr>

Description:

Ensure a user can log out of the blog.

Steps:

1. Log in to the blog
2. Click the logout button
3. Click confirm on the confirm sign out page

Expected:

User is logged out

Actual:

User is logged out

<hr>

Description:

Ensure a user can log in with the correct credentials

Steps:

1. Navigate to [Irish Cyber Security Blog](https://icsblogp4.herokuapp.com/) and click Login
2. Enter login details for the backupadmin account (username: backupadmin, password )
3. Click sign in

Expected:

User is successfully logged in and redirected to the posts page

Actual:

User is successfully logged in and redirected to the posts page

## Navigation Links

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

<hr>

Description:

Ensure a user can navigate to the Home page

Steps:

Click on the Home link in the navigation bar

Expected:

The user is directed to the Home page

Actual:

The user is directed to the Home page

<hr>

Description:

Ensure a user can navigate to the About page

Steps:

Click on the About link in the navigation bar

Expected:

The user is directed to the About page

Actual:

The user is directed to the About page

<hr>

Description:

Ensure a user can navigate to the Contact Us page

Steps:

Click on the Contact Us link in the navigation bar

Expected:

The user is directed to the Contact us page

Actual:

The user is directed to the Contact us page

<hr>

Description:

Ensure a user can navigate to the Blog Posts page

Steps:

Click on the Blog Posts link in the navigation bar

Expected:

The user is directed to the Blog Posts page

Actual:

The user is directed to the Blog Posts page

<hr>

Description:

Ensure a user can navigate to the Login page, if not logged in.

Steps:

Click on the Login link in the navigation bar, if not logged in.

Expected:

The user is directed to the Login page

Actual:

The user is directed to the Login page

<hr>

Description:

Ensure a user can navigate to the Register page, if not logged in.

Steps:

Click on the Register link in the navigation bar

Expected:

The user is directed to the Register page

Actual:

The user is directed to the Register page

<hr>

Description:

Ensure a user can logout, if logged in.

Steps:

Click on the Logout link in the navigation bar

Expected:

The user is logged out

Actual:

The user is logged out

<hr>

Description:

Ensure user can navigate to the admin page, if they are staff or superuser.

Steps:

Click on the Admin link in the navigation bar

Expected:

The user is directed to the Admin page

Actual:

The user is directed to the Admin page

All navigation links directed to the corect pages as expected.

<hr>

## Post Management

Description:

Ensure a SuperUser can create a new post

Steps:

1. Log in as the backupadmin account
2. Navigate to a post
3. Click on the "Create a post" link
4. Fill in the form with the necessary information (title, content, etc)
5. Click "Save"

Expected:

The new post is successfully created and can be viewed on the blog after the approval process.

Actual:

The new post is successfully created and can be viewed on the blog

<hr>

Description:

Ensure a SuperUser can edit an existing post

Steps:

1. Log in as the backupadmin account
2. Navigate to a post
3. Click on the "Edit this post" link for an existing post
4. Make changes to the post (title, content, etc)
5. Click "Save"

Expected:

The post is successfully edited and the changes can be viewed on the blog

Actual:

The post is successfully edited and the changes can be viewed on the blog

<hr>

Description:

Ensure a SuperUser can delete an existing post

Steps:

1. Log in as the backupadmin account
2. Navigate to a post
3. Click on the "Delete this post" link for an existing post
4. Confirm the deletion when prompted

Expected:

The post is successfully deleted from the blog

Actual:
The post is successfully deleted from the blog

<hr>

Description:

Ensure a staff user can create, edit and delete posts on the Irish Cyber Security Blog.

Steps:

1. Log in as a staff user on Irish Cyber Security Blog
2. Navigate to a post
3. Click on "Create a post"
4. Fill in the form with the appropriate information for the new post, including title, content, and categories
5. Click "Create"
6. Verify that the new post is displayed on the blog
7. Click on the "Edit this post" link for the post
8. Make any necessary changes and click "Save"
9. Verify that the changes have been applied to the post
10. Click on the "Delete this post" link for the post
11. Confirm deletion of the post
12. Verify that the post is no longer displayed on the blog

Expected:

The staff user is able to create, edit and delete posts on the Irish Cyber Security Blog

Actual:

The staff user is able to create, edit and delete posts on the Irish Cyber Security Blog

## User Management

Description:

Ensure a SuperUser can edit a user

Steps:

1. Log in as the backupadmin account
2. Click on the "Edit user" link
3. Navigate to Users in Django Admin
4. Select a user to edit
5. Make changes to the user's information (username, email, etc)
6. Click "Save"

Expected:

The user's information is successfully edited

Actual:

The user's information is successfully edited

## Is Pinned

Description:

Ensure that a post can be pinned to the top of the /all_posts/ page.

Steps:

1. Log in as a user with superuser or staff access
2. Navigate to the edit page for a post
3. Check the "IS_Pinned" checkbox
4. Click "Save"
5. Navigate to the blog page

Expected:

1. The pinned post appears at the top of the /all_posts/ page
2. The pin icon is visable on the information section of the post

Actual:

1. The pinned post appears at the top of the blog page /all_posts/ page.
2. The pin icon is visable on the information section of the page

<hr>

Description:

Ensure that a pinned post can be unpinned

Steps:

1. Log in as a user with superuser or staff access
2. Navigate to the edit page for a pinned post
3. Uncheck the "Pin to top" checkbox
4. Click "Save"
5. Navigate to the blog page

Expected:

1. The post is no longer pinned and appears in its original position on the /all_posts/ page
2. The pin icon is no longer visable on the information section of the post

Actual:

1. The post is no longer pinned and appears in its original position on the /all_posts/ page
2. The pin icon is no longer visable on the information section of the post

<hr>

Description:

Ensure that a non-superuser or staff user cannot pin a post

Steps:

1. Log in as a non-superuser or staff user
2. Navigate to the edit page for a post

Expected:

Page is 403.

Actual:
Page was 403.

## Comment Management

Description:

Ensure a SuperUser can create a comment on a post

Steps:

1. Log in as the backupadmin account
2. Navigate to a post
3. Scroll to bottom of page
4. Enter a comment in the text field, with name and email address.
5. Click "Submit"

Expected:

A message at the bottom of the scren says, "Thank you for Commenting! Please wait for approval?" The comment is successfully posted on the post, after the post approval of published.

Actual:

The comment is successfully posted on the post with the message at the bottom of the screen

<hr>

Description:

Ensure a staff user can create a comment on a post

Steps:

1. Log in as the LiamWolf account
2. Navigate to a post
3. Scroll to bottom of page
4. Enter a comment in the text field, with name and email address.
5. Click "Submit"

Expected:

A message at the bottom of the scren says, "Thank you for Commenting! Please wait for approval?" The comment is successfully posted on the post, after the post approval of published

Actual:

The comment is successfully posted on the post with the message at the bottom of the screen

<hr>

Description:

Ensure a normal can create a comment on a post

Steps:

1. Log in as the standarduser account
2. Navigate to a post
3. Scroll to bottom of page
4. Enter a comment in the text field, with name and email address.
5. Click "Submit"

Expected:

A message at the bottom of the scren says, "Thank you for Commenting! Please wait for approval?" The comment is successfully posted on the post, after the post approval of published.

Actual:

The comment is successfully posted on the post with the message at the bottom of the screen

<hr>

Description:

Ensure a unregistered and not logged in user cannot create a post

Steps:

1. Navigate to [Irish Cyber Security Blog](https://icsblogp4.herokuapp.com/)
2. Navigate to a post

Expected:

A message says, "You must be logged in to post a comment. Login or Register here." at the top of the screen.

Actual:

The comment is successfully posted at the top of the screen.

## Footer

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab and the twitter icon opened twitter in a new tab. These behaved as expected.

## Negative Testing

* A user cannot create a post with a title that is already in use
* A user cannot create a post using special characters in the title
* A user cannot create a post without filling in the required fields (e.g. title, content)
* A user cannot delete a post that does not belong to them
* A user cannot delete a post without being prompted for confirmation
* A user cannot edit a post using special characters in the title
* A user cannot create a comment that contains offensive language or hate speech.
* A user cannot create a comment without filling in the required fields (e.g. comment text)
* A user cannot delete a comment that does not belong to them
* A user cannot delete a comment without being prompted for confirmation.
* A user cannot edit a comment that does not belong to them
* A user cannot edit a comment without being prompted for confirmation

## Unit Testing

Unit tests were created to test some basic functionality such as test posts used and comments. These can be found in the tests.py.

Results:

![unit tests]()

## Accessibility

The blog was designed to provide optimal viewing experience across different screen sizes and resolutions.

During the development process, the WAVE Evaluation Website tool was used to ensure the highest level of accessibility in accordance with the Web Content Accessibility Guidelines (WCAG).

Despite this, testing revealed some issues with contrast errors on the menu in the header and the text in the footer. These errors were caused by the color of the text,
which is larger at high resolutions to make it easier to read, but can cause issues on smaller screens. To address this, a hamburger
menu was implemented as an alternative for users on smaller screens. Despite the error, the website was designed with the user in mind
and includes multiple ways for users to navigate, such as the customized menus for different access levels and navbar links, for added convenience.

![WAVE](/docs/testing/testing-wave.jpg)

## Validator Testing

All pages were run through the *[CI Pep8 Validator](https://pep8ci.herokuapp.com/)* to ensure that all code was Pep8 compliant.

Errors were displayed as a result of blank spacing and overly long lines.

All of these errors were corrected, with the exception of the settings.py file, and the code was validated.

Django's auto-generated code for AUTH PASSWORD VALIDATORS was too long.

![CI Pep8 Result](/docs/testing/test-pep8.jpg)

## HTML

On all pages, the *[w3 HTML Validator](https://validator.w3.org/)* was used. Initially, there were a few errors due to stray script tags,
incorrect use of headings inside spans, and some indentation elements such as div tags.

All of these issues were resolved, and all pages passed validation.
Because of the django structure - directing language code used in the HTML files, which cannot be easily copy and pasted into the validator, pages with login required or a secured view could be validated by direct URI.

To test the file validation, open the page to be checked, right-click, and select View Page Source from the menu that appears.
Because of validator will only accept HTML rendered code, paste the raw HTML code into it.

![HTML Validator](/docs/testing/testing-html.jpg)


## Lighthouse Testing

### Desktop Testing

Desktop Lighthouse testing is showing a perfect score of 96, with SEO of 100 seo.

![Desktop Lighthouse Result](/docs/testing/testing_lh_desktop.jpg)

### Mobile Testing

Mobile Lighthouse Testing is showing a score of 72 due to image sizes, with SEO of 100.

![Mobile Lighthouse Result](/docs/testing/testing_lh_mobile.jpg)

## Responsiveness

Pages were tested on various screen sizes from 320px on a Samsung fold 2, Samsung Galaxy Tab, Nexus 7 and a wide screen Windows machine. However, the website hides all content at 300px or below due to the randomly generated primary game board size.

Pages were tested on most modern browsers, including Microsoft Edge, Chrome, Firefox, Opera and Brave.

Test Steps:

1. Open the corresponding browser and open the ICSBlog website.
2. Open the browser development tools by hitting the corresponding dev tools shortcut.
3. Resize to the desired width.
4. Click and drag the browser window to lower or larger window size.

Expected:

The blog is responsive on all sizes, and no pixelation is accruing. No overlap of text or images.

Actual:

The blog behaved as expected, with an initial issue with the center of text on all pages on a screen size of 320px and WAVE warnings for small text.

The blog was tested on the following physical devices, with no resizing issues seen:

    Samsung fold 2
    Samsung Galaxy Tab
    Nexus 7 with Kali Linux
    Widescreen 4k monitor

The blog was tested on the following screen sizes using Chrome Dev tools, Media Genius and Unicorn Revealer:

    iPhone SE
    iPhone XR
    iPhone 12 PRO
    Pixel 5
    Samsung Galaxy S8+
    Samsung Galaxy S20 Ultra
    iPad Air
    iPad Mini
    Surface Pro 7
    Surface Duo
    Samsung Galaxy A51/71
    Nest Hub
    Nest Hub Max

## Bugs

* ~~Error being displayed that post detail cannot pass the slug for the post which is preventing posts from loading.~~

While testing create post, I created a post which didn't have a slug set. This prevented the {% url 'post_detail' post.slug %} view from opening.

Fixed by adding the following to the post model, that if the slug field is empty, then add spaces to the title with dashes and save to the slug field.

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

* ~~When testing html validation, it was found that the title for the post was accepting special characters, which, in turn, was showing html validation errors.~~

This was fixed by using the RegexValidator provided by Django to validate the input for the title field, with the error message, "Only alphabet, spaces and - characters are allowed." displayed.
