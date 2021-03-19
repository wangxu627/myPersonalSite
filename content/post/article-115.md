
---
title: JS之==运算符算法
date: 2020-02-13 01:12:08.046916
Description: ""
Tags: []
Categories: []
DisableComments: false
---
  1. ReturnIfAbrupt(x).
  2. ReturnIfAbrupt(y).
  3. If `Type(x)` is the same as `Type(y)`, then
    1. Return the result of performing Strict Equality Comparison `x === y`.
  4. If `x` is `null` and `y` is `undefined`, return `true`.
  5. If `x` is `undefined` and `y` is `null`, return `true`.
  6. If `Type(x)` is Number and `Type(y)` is String, return the result of the comparison `x == ToNumber(y)`.
  7. If `Type(x)` is String and `Type(y)` is Number, return the result of the comparison `ToNumber(x) == y`.
  8. If `Type(x)` is Boolean, return the result of the comparison `ToNumber(x) == y`.
  9. If `Type(y)` is Boolean, return the result of the comparison `x == ToNumber(y)`.
  10. If `Type(x)` is either String, Number, or Symbol and `Type(y)` is Object, then return the result of the comparison `x == ToPrimitive(y)`.
  11. If `Type(x)` is Object and `Type(y)` is either String, Number, or Symbol, then return the result of the comparison `ToPrimitive(x) == y`.
  12. Return `false`.

  

  1. 如果`x`不是正常值（比如抛出一个错误），中断执行。
  2. 如果`y`不是正常值，中断执行。
  3. 如果`Type(x)`与`Type(y)`相同，执行严格相等运算`x === y`。
  4. 如果`x`是`null`，`y`是`undefined`，返回`true`。
  5. 如果`x`是`undefined`，`y`是`null`，返回`true`。
  6. 如果`Type(x)`是数值，`Type(y)`是字符串，返回`x == ToNumber(y)`的结果。
  7. 如果`Type(x)`是字符串，`Type(y)`是数值，返回`ToNumber(x) == y`的结果。
  8. 如果`Type(x)`是布尔值，返回`ToNumber(x) == y`的结果。
  9. 如果`Type(y)`是布尔值，返回`x == ToNumber(y)`的结果。
  10. 如果`Type(x)`是字符串或数值或`Symbol`值，`Type(y)`是对象，返回`x == ToPrimitive(y)`的结果。
  11. 如果`Type(x)`是对象，`Type(y)`是字符串或数值或`Symbol`值，返回`ToPrimitive(x) == y`的结果。
  12. 返回`false`。


