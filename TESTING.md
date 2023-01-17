# Functional Testing

## Authentication

Description:

Ensure a user can register to the blog.

Steps:

1. Navigate to [iscblog](https://icsblogp4.herokuapp.com/) and click Register
2. Enter email, username and password
3. Click Register

Expected:

An email is recieved with a link to sign up, upon clicking the link, registration is successful

Actual:

An email is recieved with a link to sign up, upon clicking the link, registration is successful

## Navigation Links

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

Navigation Links

Functional Testing

Description:

Ensure a user can navigate to the Home page

Steps:

Click on the Home link in the navigation bar

Expected:

The user is directed to the Home page

Actual:

The user is directed to the Home page

Description:

Ensure a user can navigate to the About page

Steps:

Click on the About link in the navigation bar

Expected:

The user is directed to the About page

Actual:

The user is directed to the About page

Description:

Ensure a user can navigate to the Contact us page

Steps:

Click on the Contact us link in the navigation bar

Expected:

The user is directed to the Contact us page

Actual:

The user is directed to the Contact us page

Description:

Ensure a user can navigate to the Blog Posts page

Steps:

Click on the Blog Posts link in the navigation bar

Expected:

The user is directed to the Blog Posts page

Actual:

The user is directed to the Blog Posts page

Description:

Ensure a user can navigate to the Login page

Steps:

Click on the Login link in the navigation bar

Expected:

The user is directed to the Login page

Actual:

The user is directed to the Login page

Description:

Ensure a user can navigate to the Register page

Steps:

Click on the Register link in the navigation bar

Expected:

The user is directed to the Register page

Actual:

The user is directed to the Register page

Description:

Ensure a user can logout

Steps:

Click on the Logout link in the navigation bar

Expected:

The user is logged out

Actual:

The user is logged out

Description:

Ensure user can navigate to the admin page

Steps:

Click on the Admin link in the navigation bar

Expected:

The user is directed to the Admin page

Actual:

The user is directed to the Admin page

Description:

Ensure user can navigate to the new post page

Steps:

Click on the New Post link in the navigation bar

Expected:

The user is directed to the New Post page

Actual:

The user is directed to the New Post page
All navigation links directed to the corect pages as expected.

<hr>

## Footer

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab and the twitter icon opened twitter in a new tab. These behaved as expected.

## Negative Testing

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

    Open the corresponding browser and open the ICSBlog website.
    Open the browser development tools by hitting the corresponding dev tools shortcut.
    Resize to the desired width.
    Click and drag the browser window to lower or larger window size.

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
