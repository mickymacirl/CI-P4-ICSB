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

- Home -> index.html
- 

All navigation links directed to the corect pages as expected.

<hr>

## Footer

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab and the twitter icon opened twitter in a new tab. These behaved as expected.

## Negative Testing

Tests were performed on the create post to ensure that:

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
