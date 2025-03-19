"# Python problems" 
Explicacion problema  de convinaciones

Función count_change(money, coins)
-----------------------------------
Esta función calcula cuántas maneras diferentes hay de obtener una cantidad de dinero (money) usando monedas de diferentes denominaciones (coins). Es un problema clásico de programación dinámica llamado "Coin Change Problem".

Explicación del código
-------------------------
1. **Inicialización de la lista ways**  
   ```python
   ways = [1] + [0] * (money + 1)
   ```
   - Se crea una lista llamada `ways` de tamaño `money + 1`.
   - `ways[i]` representa cuántas formas hay de formar el monto `i` con las monedas dadas.
   - Se inicializa `ways[0] = 1`, porque hay **una sola manera** de formar 0 monedas (no usando ninguna moneda).
   - Los demás valores de `ways` se inicializan en 0.

2. **Recorrer cada tipo de moneda**  
   ```python
   for coin in coins:
   ```
   - Se recorre cada moneda disponible en la lista `coins`.

3. **Actualizar la cantidad de formas de hacer cada monto**  
   ```python
   for i in range(coin, money + 1):
       ways[i] += ways[i - coin]
       print(ways)  # Muestra la lista ways en cada iteración
   ```
   - Se recorre desde `coin` hasta `money` (porque no tiene sentido intentar formar un monto menor que el valor de la moneda).
   - Se actualiza `ways[i]` sumando `ways[i - coin]`.  
     **¿Por qué?** Porque si podemos hacer `i - coin`, entonces agregando una moneda `coin` más, podemos hacer `i`.

4. **Devolver el resultado final**  
   ```python
   return ways[money]
   ```
   - Al final, `ways[money]` tendrá el número total de formas de formar el monto `money` con las monedas dadas.

Ejemplo de ejecución
---------------------
```python
count_change(5, [1, 2, 5])
```
**Paso a paso**
1. Inicialmente, `ways = [1, 0, 0, 0, 0, 0]`
2. Para la moneda `1`:
   - Se actualiza `ways` en cada índice sumando `ways[i - 1]`.
   - Resultado después de la moneda `1`:  
     ```
     [1, 1, 1, 1, 1, 1]
     ```
3. Para la moneda `2`:
   - Se actualiza `ways` en cada índice sumando `ways[i - 2]`.
   - Resultado después de la moneda `2`:  
     ```
     [1, 1, 2, 2, 3, 3]
     ```
4. Para la moneda `5`:
   - Se actualiza `ways[5]` sumando `ways[5 - 5]` → `3 + 1 = 4`
   - Resultado final:  
     ```
     [1, 1, 2, 2, 3, 4]
     ```
   - `ways[5] = 4`, por lo que hay **4 maneras** de hacer `5` con monedas `[1, 2, 5]`.

Conclusión
----------
Este código usa **programación dinámica** para calcular cuántas combinaciones de monedas pueden sumar `money`. La idea clave es que cada `ways[i]` se construye a partir de los valores anteriores de la lista.

Conclusión

Este código usa programación dinámica para calcular cuántas combinaciones de monedas pueden sumar money. La idea clave es que cada ways[i] se construye a partir de los valores anteriores de la lista.



"# SnailSort problems" 
Explicacion problema  de ordenamiento serpiente

Función snail(array)
-----------------------------------
Este código implementa la función snail, que recibe una matriz cuadrada y devuelve sus elementos en orden de espiral (siguiendo un patrón en el sentido de las agujas del reloj).

Explicación del código
-------------------------
1. **Convertir la matriz a un array de NumPy**  
   ```python
   array = np.array(array)
   ```
   - Esto facilita las operaciones matriciales.
   
2. **Inicializar la lista m donde se almacenará la salida en orden espiral**  
   ```python
   m = []
   ```
   
3. **Bucle principal**  
   ```python
   while len(array) > 0:
   ```
   - Mientras la matriz tenga elementos, se ejecuta el siguiente proceso:.
   
        -**Agregar la primera fila de la matriz a la lista**    `m`.
	 
		   ```python
			m += array[0].tolist()
			```
			
		-** Se toma la primera fila (`array[0]`) y se agrega a `m` como una lista.**
		 
     **Eliminar la primera fila y rotar la matriz 90 grados en sentido antihorario.**
	 
		   ```python
			array = np.rot90(array[1:])
			```
			
		 -`array[1:]` elimina la primera fila de la matriz.
		 
         -`np.rot90(...)` rota la matriz restante 90 grados en sentido antihorario.
		 
4. **Cuando el bucle termina, `m` contiene los elementos de la matriz en orden espiral y se retorna:**  

   ```python
		return m
   ```

Ejemplo de ejecución
---------------------
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(snail(matrix))
```
**Paso a paso**
1. Se extrae, `[1, 2, 3]
2. Se rota la matriz restante:
		```python
		[[6, 9],
		 [5, 8],
		 [4, 7]]
		```

3. Se extrae `[6, 9]`

4. Se rota la matriz restante:
		```python
			[[8, 7],
			 [5, 4]]
		```
5. Se extrae `[8, 7]`

6. Se rota la matriz restante:
		```python
			[[4, 5]]
		```

5. Se extrae `[4, 5]`

**Salida:**
```python
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```
Conclusión
----------
Este código usa NumPy para manipular la matriz y extraer sus elementos en orden espiral de manera eficiente.