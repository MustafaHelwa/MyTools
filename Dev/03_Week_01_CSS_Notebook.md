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
-   create a new <div> element within the red div, called sleeve and set the below style to it (note that it will overlap red):
        .sleeve {
          width: 110px;
          height: 25px;
          background-color: white;
          opacity: 0.5;
        }
- instead, an `rbga` can be used to include opacity value:   background-color: rgba(255, 255, 255, 0.5);
- if 2 elements are blocking each other, you can put them inline using :  display: inline-block ; to bith elements style
- Styling border using:
          border-left-width: 10px;
          border-left-style: solid;
          border-left-color: black;
- Hint, all three properties can be set using: border-left: width style color; (border-left: 10px solid black;)
- another styles can be found (such as double)
- to make round elements, use `box-shadow: offsetX offsetY color;` style
- additional optional value "blurRadius" and "spreadRadius" is within `box-shadow` can be used by the following syntacs box-shadow: offsetX offsetY blurRadius spreadRadius color;
- Final color shadow will be like this:
        .red {
                background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
                box-shadow: 0 0 20px 0 rgba(83, 14, 14, 0.8);
        }
        
        .green {
                background: linear-gradient(#55680D, #71F53E, #116C31);
                box-shadow: 0 0 20px 0 #3B7E20CC;
        }
        
        .blue {
                background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%), hsl(240, 56%, 42%));
                box-shadow: 0 0 20px 0 hsla(223, 59%, 31%, 0.8);
        }

- Note that hex and hsl used to get colors in a different syntacs but a similar logic (red, green, blue, Opacity/alpha channel)



---
## Final HTML Code: 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container">
      <div class="marker red">
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
      <div class="marker green">
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
      <div class="marker blue">
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
    </div>
  </body>
</html>
```

---

## Final CSS code:

```css
h1 {
  text-align: center;
}

.container {
  background-color: rgb(255, 255, 255);
  padding: 10px 0;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.cap {
  width: 60px;
  height: 25px;
}

.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left: 10px double rgba(0, 0, 0, 0.75);
}

.cap, .sleeve {
  display: inline-block;
}

.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
  box-shadow: 0 0 20px 0 rgba(83, 14, 14, 0.8);
}

.green {
  background: linear-gradient(#55680D, #71F53E, #116C31);
  box-shadow: 0 0 20px 0 #3B7E20CC;
}

.blue {
  background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%), hsl(240, 56%, 42%));
  box-shadow: 0 0 20px 0 hsla(223, 59%, 31%, 0.8);
}
```
