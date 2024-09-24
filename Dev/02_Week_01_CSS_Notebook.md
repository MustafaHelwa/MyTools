# CSS Learning Journey Notebook  
**Source:** [freeCodeCamp.org](https://www.freecodecamp.org) and other references.

---
## Learn Basic CSS by Building a Cafe Menu


- as learned with html basics file, html starts with: 
  <!DOCTYPE html>
  <html lang="en">
  </html>
- adding head and title (head title is not visible but used for search engin):
  <head> 
  <title>Cafe Menu</title>
  </head>
- add meta characters encoder: 
    <head>
    <meta charset="utf-8">
    <title>Cafe Menu</title>
    </head>
- adding body below head:
    <head>
    <meta charset="utf-8" />
    <title>Cafe Menu</title>
    </head>
    <body>
    </body>
- adding main element into body:
  ```
    <body>
    <main>
    </main>
    </body>
  ````
- adding <h1> to the main body as the first printable / visible text:
  ```html
    <main>
    <h1>CAMPER CAFE</h1>
    </main>
  ```
- adding element below h1
    ```html
      <h1>CAMPER CAFE</h1>
      <p>Est. 2020</p>
    ```
- adding another section, to put h2 menu within it and below h1:
  ```
      <h1>CAMPER CAFE</h1>
      <p>Est. 2020</p>
      <section>
        <h2>Coffee</h2>
      </section>
  ```
- adding style to head element:
    <head>
      <meta charset="utf-8" />
      <title>Cafe Menu</title>
      <style>
      </style>
    </head>
- adding h1 style settings:
      <style>
      h1 {
        text-align: center;
        }
      </style>
- adding styles for h2 and p (i found that I can use h2, p instead of make 2 type selectors):
    <style>
      h1 {
        text-align: center;
      }
      h2 {
        text-align: center;
      }
      p {
        text-align: center;
      }
    </style>
- To avoid duplicated type selectors: 
    <style>
      h1, h2, p {
        text-align: center;
      }
    </style>
- make this css code in file called `styles.css` and rewrite the styling code:
    h1, h2, p {
      text-align: center;
    }
- now, I can remove <style> element from `index.html` file: 
    <style>
      h1, h2, p {
        text-align: center;
      }
    </style>
- to link index.html to styles.css use the below link in head element:
   <link rel="stylesheet" href="styles.css">
- Make meta adjust window size for mobile and browser:
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cafe Menu</title>
    <link href="styles.css" rel="stylesheet"/>
  </head>
- in styles.css, add a style for background element to make it brown :
    body {
      background-color: brown;
    }
- as it is not good, change it to burlywood:
    body {
    background-color: burlywood;
    }
- for design layout purpose, add div and name it menu:
    <body>
      <div id="menu">
      <main>
        <h1>CAMPER CAFE</h1>
        <p>Est. 2020</p>
        <section>
          <h2>Coffee</h2>
        </section>
      </main>
      </div>
    </body>
- using div id, change css format width:
    #menu {
    width: 300px;
    }
- comment in css: /* comment here */
- Change color for id instead of full page:
    #menu {
      background-color: burlywood; 
      width: 300px;
    }
- make width 80% of the body:
  #menu {
    width: 300px;
    background-color: burlywood;
    width: 80%; 
  }
- add auto margin for left and right:
  #menu {
    width: 80%;
    background-color: burlywood;
    margin-left:auto;
    margin-right: auto; 
  }
- instead of calling id (#menu) use class selector (.menu)
- thus, change id to class:
     <div class="menu">
- make body background as an image:
  body {
    background-image: url(https://cdn.freecodecamp.org/curriculum/css-cafe/beans.jpg);
  }
- add article under h2:
    <h2>Coffee</h2>
    <article>
    </article>
  - within article, add             <p>French Vanilla</p> <p>3.00</p>
  - adding class name in `p`
      <p class="flavor">French Vanilla</p>
      <p>3.00</p>
  - in css, aligning class name: 
      .flavor{
      text-align: left;
      }
  - same, adding price name: 
      <p class="price">3.00</p>
  - aligning price to the right: 
      .price{
      text-align: right;
      }
  - 
