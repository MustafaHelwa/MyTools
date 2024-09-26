# CSS Learning Journey Notebook  
**Source:** [freeCodeCamp.org](https://www.freecodecamp.org) and other references.

---

## Learn CSS Colors by Building a Set of Colored Markers

- Html file should start with <!DOCTYPE html> and can be followed by <html lang="en"> and should be closed by </html>
- head and body needs to be created respectively using <head> </head> and   <body>  </body>
- within the head, title is used to help SEOs using <title> "Colored Markers" <title>
- within the head, utf-8 char encoding needs to be specified using <meta charset="utf-8">
- to have the same page look through devices, meta code can be used in head element:
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
- Next, moving to the body to write <h1></h1> and other content 
- back to <head>, `index.html` needs to be linked to stylesheet called `styles.css` using     <link rel="stylesheet" href="styles.css">
- moving to 1stylels.css`, a new rule needs to be creating to align h1 element using:
    h1 {
      text-align: center;
    }
- start now by adding a new element of div container below h1 using     <div class="container"></div>
- in css, Call .marker class to change background color and diminsions:
    .marker{
      background-color: red;
      height: 25px;
      width: 200px;
       margin: 10px auto;
    }
- add 2 more <div> containers with class of markers  
- to adjust each and marker separately while keeping some styles matching, additional class can be added:
      <div class="marker one">
      </div>
      <div class="marker two">
      </div>
      <div class="marker three">
      </div>
- Css can be adjusted to the following:
      .marker {
        width: 200px;
        height: 25px;
        margin: 10px auto;
      }
      
      .one {
        background-color: red;
      }
      
      .two{
        background-color: green;
      }
      .three{
        background-color: blue;
      }
- Note: "There are two main color models: the additive RGB (red, green, blue) model used in electronic devices, and the subtractive CMYK (cyan, magenta, yellow, black) model used in print."
- Change background container color to rgb(0, 0, 0) eg. black:
    .container{
    background-color: rgb(0, 0, 0);
    }
- using shorthand padding `  padding: 10px 0;` this will give 10px padding to top and bot while 0 to left and righ
- a hex color code with the values 00 for red, FF for green, and 00 blue
- With hex colors, 00 is 0% of that color, and FF is 100%. So #00FF00 translates to 0% red, 100% green, and 0% blue, and is the same as rgb(0, 255, 0).
- HSL color model, or hue, saturation, and lightness. The CSS hsl function accepts 3 values: a number from 0 to 360 for hue, a percentage from 0 to 100 for saturation, and a percentage from 0 to 100 for lightness.
 	background-color: hsl(240, 100%, 50%);
- linear-gradient(gradientDirection, color1, color2, ...);
-   background: linear-gradient(90deg, rgb(255, 0, 0), rgb(0, 255, 0));
-   
