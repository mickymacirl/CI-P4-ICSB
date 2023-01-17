# Functional Testing

## Authentication

Description:

Ensure a user can register to the blog.

Steps:

1. Navigate to [Irish Cyber Security Blog](https://icsblogp4.herokuapp.com/) and click Register
2. Enter email, username and password
3. Click Register

Expected:

An email is recieved with a link to sign up, upon clicking the link, registration is successful

Actual:

An email is recieved with a link to sign up, upon clicking the link, registration is successful
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

The comment is successfully posted on the post, after the post approval of published.

Actual:

The comment is successfully posted on the post

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

The comment is successfully posted on the post, after the post approval of published.

Actual:

The comment is successfully posted on the post

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

The comment is successfully posted on the post, after the post approval of published.

Actual:

The comment is successfully posted on the post

<hr>

Description:

Ensure a unregistered and not logged in user cannot create a post

Steps:

1. Navigate to [Irish Cyber Security Blog](https://icsblogp4.herokuapp.com/)
2. Navigate to a post

Expected:

Ensure a message says, "You must be logged in to post a comment. Login or Register here."

Actual:

The message said, "You must be logged in to post a comment. Login or Register here."

## Footer

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab and the twitter icon opened twitter in a new tab. These behaved as expected.

## Negative Testing

A user cannot create a post with a title that is already in use
A user cannot create a post using special characters in the title
A user cannot create a post without filling in the required fields (e.g. title, content)
A user cannot delete a post that does not belong to them
A user cannot delete a post without being prompted for confirmation
A user cannot edit a post using special characters in the title
A user cannot create a comment that contains offensive language or hate speech.
A user cannot create a comment without filling in the required fields (e.g. comment text)
A user cannot delete a comment that does not belong to them
A user cannot delete a comment without being prompted for confirmation.
A user cannot edit a comment that does not belong to them
A user cannot edit a comment without being prompted for confirmation

## Unit Testing

Unit tests were created to test some basic functionality such as test posts used and comments. These can be found in the tests.py.

Results:

![unit tests]()

## Accessibility

WAVE Web Accessibility Evaluation Tool was used to test each page, with one alert related to Titles.

![WAVE Result Index](/assets/readme/waveresultindexrm.jpg)

![WAVE Result Game](/assets/readme/waveresultgamerm.jpg)

## Lighthouse Testing

### Desktop Testing

Desktop Lighthouse testing is showing a perfect score of 100 across the board.

![Desktop Lighthouse Result](/assets/readme/desktoplhtrm.jpg)

### Mobile Testing

Mobile Lighthouse Testing is showing a score of 95, with SEO having a score of 92.

![Mobile Lighthouse Result](/assets/readme/mobilelhtrm.jpg)

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

1. ~~Error being displayed that post detail cannot pass the slug for the post which is preventing posts from loading.~~

While testing create post, I created a post which didn't have a slug set. This prevented the {% url 'post_detail' post.slug %} view from opening.

Fixed by adding the following to the post model, that if the slug field is empty, then add spaces to the title with dashes and save to the slug field.

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)
