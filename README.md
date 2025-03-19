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
