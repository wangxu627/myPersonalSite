
---
title: ES6的Number.isNaN和isNaN的区别
date: 2020-03-23 05:52:52.370130
Description: ""
Tags: []
Categories: []
DisableComments: false
---
To quote from a [ponyfoo article on numbers in
ES6](https://ponyfoo.com/articles/es6-number-improvements-in-depth):

> Number.isNaN is almost identical to ES5 global isNaN method. Number.isNaN
> returns whether the provided value equals NaN. This is a very different
> question from “is this not a number?”.

So `isNaN` just checks whether the passed value is not a number or cannot be
converted into a Number. `Number.isNaN` on the other hand only checks if the
value is equal to `NaN` (it uses a different algorithm than `===` though).

The String `'ponyfoo'` for example is not a number and cannot be converted
into a number, but it is not `NaN`.

Example:

    
    
    Number.isNaN({});
    // <- false, {} is not NaN
    Number.isNaN('ponyfoo')
    // <- false, 'ponyfoo' is not NaN
    Number.isNaN(NaN)
    // <- true, NaN is NaN
    Number.isNaN('pony'/'foo')
    // <- true, 'pony'/'foo' is NaN, NaN is NaN
    
    isNaN({});
    // <- true, {} is not a number
    isNaN('ponyfoo')
    // <- true, 'ponyfoo' is not a number
    isNaN(NaN)
    // <- true, NaN is not a number
    isNaN('pony'/'foo')
    // <- true, 'pony'/'foo' is NaN, NaN is not a number


