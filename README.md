# Metaheuristics

Simple implementation of the Hill-Climbing and Iterated Local Search metaheuristics to minimize 2 functions, each function with 2 different domains. 
Each metaheuristic is executed 30 times for every domain, adding up to 120 times. The functions can be changed to any function in the functions.py file, and the number of times each metaheuristic is executed, as well as their stop conditoin can be changed for different results. 
In the end the program outputs the following things for every domain:

 + Best result.
 + Worst result.
 + Avarage result.
 + Standard deviation.

The program shows a BoxPlot of the results as well.

## Function 1:

 $$f(x,y)=x^2+y^2+25(sin^2(x)+sin^2(y))$$
 
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/73348806/235327861-9043d97b-9f6e-48e2-b19e-d25a1cac936b.png"/>
 </p>
 
 <p align="center">
  Domain A: $-5 ≤ x, y ≤ 5$
 </p>
 <p align="center">
  Domain B: $-2 ≤ x, y ≤ 2$
 </p>
 
## Function 2:
  
 $$f(x,y)=-(y+47)sin(\sqrt{|y+0.5y+47|})-x sin(\sqrt{|x-(y+47)|})$$
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/73348806/235328113-928ffeda-64c5-4894-a7ed-e897fa92d9fa.png"/>
 </p>
 
 <p align="center">
  Domain C: $-512 ≤ x, y ≤ 512$
 </p>
 <p align="center">
  Domain D: $400 ≤ x, y ≤ 512$
 </p>
 
## Running the program: 

Just run main.py:

```
python3 main.py
```
