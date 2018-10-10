# User Driven Sorting Program
Using the power of Python, this script lets a user sort a list of objects with their inputs.

#### Input
> <table>
>     <tr>
>         <td>A</td>
>         <td>B</td>
>         <td>C</td>
>         <td>D</td>
>         <td>E</td>
>         <td>F</td>
>         <td>G</td>
>         <td>H</td>
>     </tr>
> </table>

The user can decide if these values are more important than the other by the program asking, "Is *x* more important than *y*?"

It requires a seeding of deciding on a first two items. A seeded array will look like,

#### Seeded Sorting Table
> <table>
>     <tr>
>         <td>A</td>
>         <td>B</td>
>     </tr>
> </table>

The next items will do their comparison on the median,

# Question Pattern
#### Inputs
> <table>
>     <tr>
>         <td>A</td>
>         <td>B</td>
>         <td>C</td>
>         <td><span style="color: red">D</span></td>
>         <td>E</td>
>         <td>F</td>
>         <td>G</td>
>         <td>H</td>
>     </tr>
> </table>

#### Comparing To Table
> <table>
>     <tr>
>         <td>A</td>
>         <td><span style="color: red">B</span></td>
>         <td>C</td>
>     </tr>
> </table>

#### Question
> Is D more important than B?

#### Results
> If "y"
> #### Output
> <table>
>     <tr>
>         <td>A</td>
>         <td><span style="color: red">D</span></td>
>         <td>B</td>
>         <td>C</td>
>     </tr>
> </table>

> If "n"
> #### Output
> <table>
>     <tr>
>         <td>A</td>
>         <td>B</td>
>         <td><span style="color: red">D</span></td>
>         <td>C</td>
>     </tr>
> </table>

# Sorting Coverage
To cover all possible sorting positions, this will sort out from the median to an end or the next encountered different answer.

> If "y" twice and at end
> #### Output
> <table>
>     <tr>
>         <td><span style="color: red">D</span></td>
>         <td>A</td>
>         <td>B</td>
>         <td>C</td>
>     </tr>
> </table>

---
> If "n" twice and at end
> #### Output
> <table>
>     <tr>
>         <td>A</td>
>         <td>B</td>
>         <td>C</td>
>         <td><span style="color: red">D</span></td>
>     </tr>
> </table>

---
> If "y" then "n"
> #### Output
> <table>
>     <tr>
>         <td>A</td>
>         <td><span style="color: red">D</span></td>
>         <td>B</td>
>         <td>C</td>
>     </tr>
> </table>

---
> If "n" then "y"
> #### Output
> <table>
>     <tr>
>         <td>A</td>
>         <td>B</td>
>         <td><span style="color: red">D</span></td>
>         <td>C</td>
>     </tr>
> </table>