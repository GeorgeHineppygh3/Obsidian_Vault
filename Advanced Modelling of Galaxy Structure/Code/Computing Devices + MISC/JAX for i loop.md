---
s:: true
---
---
s:: true
---
---
s:: true
---

Link to Documentation: https://tinyurl.com/4jwedjc2

```run-python
def fori_loop(lower, upper, body_fun, init_val):
  val = init_val
  for i in range(lower, upper):
    val = body_fun(i, val)
  return val
```

Body function is the function that needs to be called in the loop eg.

```run-python
def func(i, val):
	if val < 10:
		val += i
	else:
		continue
return val
```

setting `lower =` $0$ and `upper =` $10$ and `val` as an array of length 1 (`dtype: int`) as 3 :

```run-python
value = np.array([3])
low = 0
high = 10
export = fori_loop(0,10,func,value)
```
export should be a value greater than ten.

[When can run WSL will try this...]

Parameters:

-   **lower** – an integer representing the loop index lower bound (inclusive)
    
-   **upper** – an integer representing the loop index upper bound (exclusive)
    
-   **body_fun** – function of type `(int, a) -> a`.
    
-   **init_val** – initial loop carry value of type `a`.
    

Returns:

-  Loop value from the final iteration, of type `a`.



