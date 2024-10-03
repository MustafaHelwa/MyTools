# HTML Learning Journey Notebook  
**Source:** [freeCodeCamp.org](https://www.freecodecamp.org) and other references.  
**Project:** Learn Typography by Building a Nutrition Label

--- 

### HTML and CSS Step-by-Step Guide

#### Basic Setup
 - Starting with basic head & body:
     <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
  
</head>

<body>
  <h1>Nutrition Facts</h1>
  <p>8 servings per container</p>
  <p>Serving size 2/3 cup (55g)</p>
</body>
</html>

- Adding `styles.css` link and link to font within <head>:
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,700,800">
  <link  rel="stylesheet" href="styles.css"> 

- Use the imported font family to the body in `styles.css`:
  body{
  font-family: "Open Sans", sans-serif;

  }
- make `html` font size 16px:
  html{
  font-size: 16px;
  }
- Wrap <h1> and <p> elements with a <div> element with `class` set to `label`
    <div class="label">
    </div>

  - Set a border to the `.label`:
    .label{
      border: 2px solid black;
      width: 270px;
      margin: 20px auto; 
    padding : 0 7px; 
    }
-  reset the box model by creating a * selector and giving it a box-sizing property of border-box:
  *{ 
  box-sizing: border-box;

  }

- Set h1 font style to font-weight of 800 and center text and make top/bottom margins -4px and letter spacing of 0.15px and remove margins of p :
  h1 {
  font-weight: 800;
  text-align: center;
  margin: -4px 0;
  letter-spacing: 0.15px; 
  }
  p {
    margin: 0;
  }

- Make a <div> element of class equal to divider below <h1> element and set a bottom border for it:
  1. html:
        <div class="divider"></div>
  2. css:
   .divider{
    border-bottom: 1px solid #888989;
    margin: 2px 0;
    }
- adjust the second <p> element to class of bold:
      <p class="bold">Serving size 2/3 cup (55g)</p>

- Adjust font weight of .bold to 800:
  .bold {
  font-weight: 800;
  }
- Adjust <h1> elemment to class of bold:
    <h1 class="bold">Nutrition Facts</h1>
- Wrap serving size with a <span> element for further highlight:
      <p class="bold">Serving size<span> 2/3 cup (55g)</span></p>

- Adjust <p> style:
  p {
  margin: 0;
  display: flex;
  justify-content: space-between;
  }

- Wrap all `.label` elements within a `<header>` and add header to h1 style in css file:
  1. html:
       <div class="label">
    <header>
      <h1 class="bold">Nutrition Facts</h1>
      <div class="divider"></div>
      <p>8 servings per container</p>
      <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
    </header>
  </div>
  3. CSS:
  header h1 {
  text-align: center;
  margin: -4px 0;
  letter-spacing: 0.15px
}
 
- Create a <div> element below the <header>
  <div class="divider large">
  </diV>

- Create a suitable style for `.large` and `.medium`:
  .large {
  height: 10px;

}
.large, .medium{ 
  background-color: black;
    border: 0;
}

- Create a new <div> below `divider large` <div> element and add <h2> within it: 
        <div class="calories-info">
      <div class="left-container">
        <h2 class="bold small-text">Amount per serving</h2>
      </div>
          </div>
- change `.small-text` label `font-size` using `rem` which stands for `root em`. it relatives font size to the html font size (16px in this project):
  .small-text{ 
  font-size: 0.85rem;
  
  }

- Remove all margins for ` .calories-info h2`: 
  .calories-info h2{
  margin: 0;
  }

-  Add `calories` and `230` as below:
      <div class="calories-info">
      <div class="left-container">
        
        <h2 class="bold small-text">Amount per serving</h2>
        <p>Calories</p>
      </div>
      <span>230</span>
    </div>


 - Create the below style for `.calorise-info`:
   .calories-info{ 
  display: flex; 
  justify-content: space-between; 
  align-items: flex-end; 
  }

- Create a new .left-container p selector setting the top and bottom margin to -5px, and the left and right margin to -2px. Also set the font-size to 2em and font-weight to 700:

   .left-container p {
  margin: -5px -2px;
  font-size: 2em; 
  font-weight: 700;
  }

- Create a .calories-info span selector, set its font-size to 2.4em and font-weight to 700 and adjust maring (top and bottom) to -7px and (right and left) to -2px:
  .calories-info span {
  font-size: 2.4em; 
  font-weight: 700;
  margin: -7px -2px;
  }

- add a new <div> below `.calories-info` <div> :

  <div class="divider medium"> 
  </div>

- Create a `.medium` selector and give it a `height` of `5px`:
  .medium{
  height: 5px; 
  } 

- Add a new <div> and add <p> element within it as below:
      <div class="divider medium"></div>
    <div class= "daily-value small-text">
      <p class="bold right">% Daily Value *</p></div>

 - Make <p> always on the right usin `flex-end`:
   .right {
  justify-content: flex-end;
   }

 - Use the same `.divider` used above to add a new divider below <p> element:
       `<div class="divider"></div>

  - Create a new <p> element of text `Total Fat 8g 10%` and wrap `Total Fat` and `10%` with 2 separate <span> elements and make them **bold**: 

        <div class="daily-value small-text">
      <p class="bold right">% Daily Value *</p>
      <div class="divider"></div>
      <p><span class="bold">Total Fat</span> 8g <span class="bold">10%</span></p>
    </div>

- As `Total Fat` and `8g` are not wraped in one text, wrap them both within a new <span> element to make them one element but `8g` is not in bold:
  <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>

- Add another <p> element to show `Saturated Fat` and just keep the percent **bold** and give the new <p> element a class of `indent` for further styling:
  <p>Saturated Fat 1g <span class="bold">5%</span></p>

- Create a `.indent` selector style of a `margin-left` to show it as a subelement:
  .indent{ 
  margin-left: 1em;
  }

- Cleate a `.daily-value p` selector to target all `p` elements in the `daily-value` and give it a bottom border of 1px :
  .daily-value p{ 
  border-bottom: 1px solid #888989;
  }


- 
