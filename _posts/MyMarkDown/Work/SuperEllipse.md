### Ellipse

$$
|\frac{x_k}{a}|^2 + |\frac{y_k}{b}|^2 =1
$$



### SuperEllipse

$$
|\frac{x_k}{a}|^c + |\frac{y_k}{b}|^c =1
$$

### Distance

$$
r_k = \sqrt{(x_k)^2 + (y_k)^2} \\
R_k = \frac{\sqrt{(x_k)^2 + (y_k)^2} }{(\frac{x_k}{a}|^c + |\frac{y_k}{b}|^c)^{\frac{1}{c}}}
$$

$$
MSE(c) = \frac{1}{n}\sum^n_{k=1}(R_k - r_k)^2
$$

![enter image description here](https://i.stack.imgur.com/BWwWi.gif)

### Incline

$$
x = x'cos\theta - y'sin\theta\\
y = x'sin\theta + y'cos\theta
$$

### Rotation:

$$
\left[
 \begin{matrix}
   u \\   v 
  \end{matrix}
  \right]  = 

  \left[
 \begin{matrix}
   \text{cos } a &  -\text{ sin } a\\
   \text{sin } a & \text{cos } a 
  \end{matrix}
  \right]   \left[
 \begin{matrix}
   x\\ y 
  \end{matrix}
  \right] 
  
  \tag{3}
$$

![https://i.stack.imgur.com/wqd3B.gif](https://i.stack.imgur.com/wqd3B.gif)

### Tilt

Rectangular -> parallelogram

### Affine

$$
\left[
 \begin{matrix}
   u \\   v 
  \end{matrix}
  \right]  = 

  \left[
 \begin{matrix}
   \text{1 }  &  \text{ tan } \phi\\
   \text{tan } \theta & \text{1 }  
  \end{matrix}
  \right]   \left[
 \begin{matrix}
   x\\ y 
  \end{matrix}
  \right] 
  
  \tag{3}
$$













































































