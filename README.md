### Coding Challenge Guidelines

Please solve the following problem in Python. You are free to choose a web
framework of your choice and any number of libraries that you see fit. Please
include a file that states
the dependencies.

When something is unclear, either come back to us with a question or try to make
a reasonable assumption, document it and carry on.

Please include a readme file that tells us how we can run your program.


### Color Product API

We run a little shop for handicraft goods and are currently trying to expand
our business. We sell paper in basically every color. In order to increase our
sales, we want to suggest additional paper colors after a user has added a
sheet of paper to their cart.

For the frontend implementation we need an API that returns the matching paper
products for a given color (hex code).

Here is an example request:

```
GET /suggest_paper_product/?color=940505&count=1

[
  {
    "product_id": 1,
    "name": "Some name",
    "main_color": "112233"
  }
]
```

There is an API that gives you matching colors for a color: 

```
GET https://ryym3ua1el.execute-api.eu-central-1.amazonaws.com/prod/?color=ff0022

{"inputColor": "FF0022", "matchingColors": ["54F707", "0718F7"]}
```

The API endpoint you need to implement should query the color API and then find
products in these colors. If we do not have a product that exactly matches the
color from the API, use products with colors *close* to the color we are
looking for. There are different notions of "close colors" (see
[wikipedia](https://en.wikipedia.org/wiki/Color_difference)). It is ok to use a
simple approach like euclidean distance in RGB.

There is a stub implementation of the paper products database in
`color_suggest/products.py`. Feel free to alter and move the file so that it
fits your needs. 


### Evaluation Criteria

We evaluate your solution based on the following criteria:

1) Design: Are the parts of the solution well abstracted? Are they testable?
1) Maintainability: Can we understand the solution? Is it easy to fix problems or add features?
1) Idioms: Does the code follow common Python idioms?
1) Functionality: Does the solution work?

These criteria are weighted according to their order. That means "it works" is
not enough. Please use the task to show us how well you understand your craft.


### CodeSubmit

Please organize, design, test and document your code as if it were
going into production - then push your changes to the master branch.

All the best,

The Alasco Team
