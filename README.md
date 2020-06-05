# Solution_Set

1. AGM:
  Generates 3-D Plot for AGM of a range. 
  Input Parameters: Lower limit and Upper Limit of the range.
  Input in demo: Lower limit = 1. 
                 Upper limit = 10.

2. Voltage Divider:
  Input Parameters: 
  f: frequency.
  Vm: Max Voltage/Amplitude.
  R1, R2: Resistor values.
  Input in demo:
  f = 4Hz; Vm = 10V; R1 = 1200 Ohm; R2 = 4700 Ohm
  
3. RC Divider:
  Input Parameters: 
  f: frequency.
  Vm: Max Voltage/Amplitude.
  R1: Resistor values.
  C: Capacitance Value.
  Input in demo:
  f = 4Hz; Vm = 10V; R1 = 1200 Ohm; C = 120 uF

4. Chaos Game:
  a. Sierpinski Triangle:
    Generates Sierpinski triangle inside an equilateral triangle with vertices:
    (0,0);(0.5,0.866);(4,0)
  
  b. More Generic code which also considers a square:
     For generating a fractal in a square, an additional condition was introduced. No vertex would be repeated during the random selection.
     For making the code applicable for a triangle, the set of vertices selected can be limited to three points only.
     The corresponding change which was needed was the change in random selection of a vertex.
     The resulting fractal of a triangle uses the vertices (0,0);(1,0);(0,1)
     The fractal for square uses the vertices (0,0);(1,0);(0,1);(1,1)
  
  Number of iterations considered for both codes was 1000. However, a different number can be considered
  
