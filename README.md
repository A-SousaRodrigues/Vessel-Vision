# Vessel Vision


<p align="center">
| <a href="https://vessel-vision-1ed5aef8a6ed.herokuapp.com/" target="_blank">Live Project</a> |
</p>

## Introduction 

The Circle of Willis Learning Game is an interactive, educational platform designed to teach users about the anatomy and function of the Circle of Willis, a critical arterial structure in the human brain. This web-based application combines gamification and user progress tracking to create an engaging and effective learning experience. Users will answer questions, track their progress, and receive feedback to deepen their understanding of the Circle of Willis. Additionally, testimonials from other users will be displayed to encourage engagement and build credibility.

The website will feature a responsive design to ensure usability on various devices and adhere to accessibility standards, making it inclusive for all users.

The live project can be found here: <a href="https://vessel-vision-1ed5aef8a6ed.herokuapp.com/" target="_blank">Vessel Vision</a>

<h2 align="center" id="TOC">Table of Contents</h2>

* [Vessel Vision](#vessel-vision)
  - [Introduction](#introduction)
  - [Table of Contents](#TOC)
  - [Project Ouline](#project-outline)
* [Project Planning](#project-planning)
  - [UX Design](#ux-design)
    - [User Stories](#user-stories)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Wireframes](#wireframes)
* [Features](#features)
  - [General Features](#general-features)
* [Built With](#built-with)
  - [Technology and Languages](#technologies-and-languages)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Tools & Programs](#tools-and-programs)
* [Development](#deployment)
* [Testing](#testing)
* [AI Implementation and Orchestration](#ai-implementation-and-orchestration)
* [Credits](#credits)
  - [Code](#code)
  - [Content](#content)


<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## Project Outline

### External User’s Goal: 

- Learn about the anatomy and function of the Circle of Willis in an interactive and engaging manner.
- Test their knowledge through a structured quiz and track their progress over time.
- Receive immediate feedback to identify areas for improvement.
- Gain motivation and encouragement through performance summaries and testimonials from other users.

### Site Owner’s Goal: 

- Provide an educational platform that simplifies learning complex anatomical structures.
- Ensure users return and engage with the site through gamification and progress tracking.
- Collect and showcase user testimonials to build credibility and encourage new users to participate.
- Achieve high user satisfaction by creating an intuitive, responsive, and visually appealing design.

### Key Objectives

- Interactive Game: Develop an engaging game that teaches users about the Circle of Willis through sequential questions with feedback.
- User Authentication: Allow users to register, log in, and save their progress securely.
- Progress Tracking: Enable users to see their score, progress percentage, and performance summary upon completion of the game.
- Responsive Design: Ensure the site is fully responsive and works seamlessly across all devices.
- Testimonials Section: Create a carousel on the homepage to display user testimonials dynamically.
- Accessibility: Adhere to WCAG accessibility standards to make the site inclusive for all users.
- Maintainability: Use a scalable structure with Django models, views, and templates for long-term maintainability and ease of updates.


## Project Planning

### UX Design

### User Stories 

<details>
  <summary>Must Have</summary>

- As a user, I want to register for an account so that I can track my progress in the game.
- As a user, I want to log in to my account so that I can continue my progress where I left off.
- As a user, I want to view a question about the Circle of Willis so that I can test my knowledge.
- As a user, I want to submit my answer and receive immediate feedback so that I can learn from my mistakes.
- As a user, I want to see a summary of my performance after completing the game so that I know my strengths and weaknesses.
- As a user, I want my progress to be saved as I play so that I can continue where I left off.
- As a user, I want to see testimonials at the bottom of the homepage so that I can read other users' experiences.

</details>

<details>
  <summary>Should Have</summary>

- As a user, I want to see a visual progress bar so that I know how far I’ve progressed in the game.
- As a user, I want to reset my progress so that I can start the game over from the beginning.
- As a user, I want the game to adapt to different screen sizes so that I can play on both desktop and mobile devices.
- As an admin, I want to moderate testimonials by approving or rejecting submissions so that the content remains appropriate.
- As a user, I want to review the correct answers for each question after the game ends so that I can identify gaps in my knowledge.

</details>

<details>
  <summary>Could Have</summary>

- As a user, I want to see motivational feedback based on my performance so that I feel encouraged to improve.
- As a user, I want to leave a testimonial without logging in so that I can quickly share my feedback.
- As a user, I want to see random testimonials every time I visit the homepage so that I get a variety of opinions.
- As a user, I want to read a brief explanation about each artery during the game so that I can learn more about the anatomy.

</details>


<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## Colors



### Main Palette

With the help of ChatGPT, acting as my UX designer, the following colour pallete was decided.

- Primary Colour	Strong Blue	(#0077B6)	
- Secondary Colour	Dark Blue	(#005F80)	
- Accent Colour	Medium Green	(#4CAF50)	
- Text Colour	Very Dark Gray	(#212121)	
- Background Colour	Off-White	(#F4F4F4)	

![Color Palette](/documentation/images/pallete.png)
<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## Fonts

Similar to colour, the font should be easy to read. [Google Fonts](https://fonts.google.com) using a direct import code within the style.css file should supply the fonts.

[Roboto](https://fonts.google.com/specimen/Roboto) for body text.
[Lato](https://fonts.google.com/specimen/Lato) for headings.



<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

### Wireframes

Wireframes designed by ChatGPT

**Homepage Layout**

-----------------------------------
| Logo | Home | Game | Testimonials | Login/Sign Up |
-----------------------------------
| Banner (Circle of Willis Image)                     |
| "Explore the Circle of Willis – A Fun Way to Learn!" |
| [Start the Game]                                    |
-----------------------------------
| About the Game (Description, Benefits)              |
-----------------------------------
| Testimonials Carousel                               |
| [User 1 feedback] [User 2 feedback] ...              |
-----------------------------------
| Footer                                              |
| Privacy | Terms | Contact                           |
| Social Media Icons                                  |
-----------------------------------

**Game Page Layout**

----------------------------------------------------------
| Logo | Home | Game | Testimonials | Logout |
----------------------------------------------------------
| Circle of Willis Map (Interactive)                     |
| [Highlighted arteries based on progress]               |
----------------------------------------------------------
| Question: What artery branches off the vertebral?      |
| [ ] A) Internal Carotid                                |
| [ ] B) Anterior Spinal Artery                          |
| [ ] C) Posterior Cerebral Artery                       |
| [Submit Answer]                                        |
----------------------------------------------------------
| Progress: 4/10 [|||||---] Score: 6/10                 |
----------------------------------------------------------
| Feedback: Correct! The Anterior Spinal Artery...       |
----------------------------------------------------------

**Testimonial Page Layout**

----------------------------------------------------------
| Logo | Home | Game | Testimonials | Logout |
----------------------------------------------------------
| Submit a Testimonial                                   |
| [Text Box for feedback]                                |
| [Star Rating System]                                   |
| [Submit Button]                                        |
----------------------------------------------------------
| Testimonials List                                      |
| User 1: "Great game! Learned a lot!" ⭐⭐⭐⭐⭐            |
| User 2: "Nice interactive learning tool." ⭐⭐⭐⭐         |
| [View More Testimonials]                               |
----------------------------------------------------------


<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>



<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## Features

### General Features




<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

### Responsive Design


![Responsive Design]

<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>


## Built With

### Technologies and Languages

![Static Badge](https://img.shields.io/badge/HTML5-language-red)
![Static Badge](https://img.shields.io/badge/CSS3-language-%23663399)
![Static Badge](https://img.shields.io/badge/Javascript-language-yellow)
![Static Badge](https://img.shields.io/badge/Python-language-blue)

![Static Badge](https://img.shields.io/badge/Heroku-deployment-%2379589f)
![Static Badge](https://img.shields.io/badge/GitHub-repo_hosting-black)
![Static Badge](https://img.shields.io/badge/VS_Code-IDE-yellow)

![Static Badge](https://img.shields.io/badge/PostgreSQL-DBMS-blue)

### Libraries and Frameworks

![Static Badge](https://img.shields.io/badge/Bootstrap-frontend_dev_framework-purple)
![Static Badge](https://img.shields.io/badge/FontAwesome-icon_library-navy)
![Static Badge](https://img.shields.io/badge/GoogleFonts-typography_library-blue)

![Static Badge](https://img.shields.io/badge/Django-web_framework-%green)
![Static Badge](https://img.shields.io/badge/Django_AllAuth-authentication_package-%green)
![Static Badge](https://img.shields.io/badge/Django_Whitenoise-static_file_serving_package-%green)
![Static Badge](https://img.shields.io/badge/Django_Summernote-rich_text_editor_package-%green)

All Django packages installed are listed in grequirements.txt

### Tools and Programs

![Static Badge](https://img.shields.io/badge/Favicon.io-icons-red)
![Static Badge](https://img.shields.io/badge/Coolers-colour_palette_testing-red)

![Static Badge](https://img.shields.io/badge/MSCopilot-AI-blue)
![Static Badge](https://img.shields.io/badge/ChatGPT-AI-blue)
![Static Badge](https://img.shields.io/badge/GitHubCopilot-AI_pair_programming-blue)

<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## Deployment

- **Platform:** Heroku
- **High-Level Deployment Steps:** 
  1. Clone the repository
  2. Set up the Heroku environment with a PostgreSQL database.
  3. Configure environment variables for sensitive data (e.g., secret keys).
  4. Deploy using Heroku Git or GitHub integration.
- **Security Measures:**
  - Sensitive data is stored in environment variables.
  - DEBUG mode is disabled in the production environment to enhance security.


<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## Testing

### Validation

#### CSS


#### HTML


### Lighthouse


<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## AI Implementation and Orchestration

### Use Cases and Reflections:

  - **Code Creation:** 
    - Reflection: The AI implementation in code creation played a significant role in accelerating development. By automating repetitive tasks and providing code suggestions, AI tools helped maintain focus on higher-level design decisions, including accessibility and inclusivity. This was especially valuable for creating flexible and scalable models and views for the application.
    - Examples: AI was used to generate base code for models, views, and URLs, allowing myself to focus on refining functionality rather than writing boilerplate code.
  - **Debugging:** 
    - Reflection:  AI tools were invaluable during debugging, offering automated solutions to common errors and logic issues. While AI suggestions provided a solid foundation, manual refinement ensured that the implementation was aligned with the project's objectives. By reducing the time spent on resolving minor errors, AI enabled a more efficient debugging process.
  - **Performance and UX Optimisation:** 
    - Reflection: AI-assisted tools contributed to enhancing the performance of the application by suggesting ways to optimise database queries and reduce the load on the server. The optimisation suggestions also helped enhance the user experience (UX) by ensuring smoother transitions and faster response times, which is especially beneficial for users with SEND or ALN.
  - **Automated Unit Testing:**
    - Reflection: 

- **Overall Impact:**
  - Efficiency Gains:
The use of AI tools significantly sped up the development process by automating repetitive tasks such as code generation, debugging, and unit testing. AI also provided valuable insights into improving performance and user experience, allowing developers to focus on creating high-quality features.

  - Challenges:
  Contextual Adjustments: One of the challenges faced during AI implementation was ensuring that the suggestions provided by AI were fully aligned with the specific project requirements. While AI-generated solutions were often useful, manual adjustments were necessary to adapt them to the project’s unique needs and the desired user experience.

<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>

## Credits

### Code

Authorisation templates used the same as the Codestar Blog in the LMS, but customised to fit this project.
AI was heavily used to create models, views and templates.

### Content
Questions suggested by AI, refined and corrceted by me.

<hr>
<p align="right"><a href="#vessel-vision">Back To Top</a></p>