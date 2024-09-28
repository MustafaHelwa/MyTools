# HTML Learning Journey Notebook  
**Source:** [freeCodeCamp.org](https://www.freecodecamp.org) and other references.  
**Project:** Learn HTML Forms by Building a Registration Form

---
## starting with html file:

- making document type, adding language, head and body:
      <!DOCTYPE html>
    <html lang="en">
      <head>
        
      </head>
      <body>
      </body>
    </html>

- adding title and meta format:
    <head>
    <meta charset="UTF-8">
    <title>Registration Form</title>
    </head>
- Linkit to styles.css withing head element: 
      <link rel="stylesheet" href="styles.css">
- adding heading within the body using:    <h1>Registration Form</h1>
- adding a paragraph within the 1st heading: <p>Please fill out this form with the required information</p>
- move to css file, use vh unit of height which is equal to 1% of height:
- Get rid of horizontal scroll bar using margin:
    body {
    width: 100%;
    height: 100vh;
    margin: 0;
  }
- Adjust background and text color using   `background-color: #1b1b32;` and `color: #f5f6f7;`
- add a form to the body of the html code using:     <form action="https://register-demo.freecodecamp.org"></form>
- Then add a form to get responce from URL using:     <form method="post" action='https://register-demo.freecodecamp.org'>
- add three fieldsets within the form using:         <fieldset></fieldset>
- within the field, create for labels to hold name, email, password using: <label></label> and final outcome:
        <label>Enter Your First Name:</label>
        <label>Enter Your Last Name:</label>
        <label>Enter Your Email:</label>
        <label>Create a New Password:</label>
- 
