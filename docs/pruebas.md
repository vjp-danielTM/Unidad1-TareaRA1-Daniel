# PRUEBAS
#### Esta es la documentacion donde estan los 14 test que hay que hacer en a actividad final

Lo primero que hice fue copiar a mi codigo los test que el profesor me dio para ir empezando poco a poco:
```  
def test1_estado_inicial_correcto(self):
        """Test 1: Verifica que el estado inicial es Inactivocon 0 ingresos."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)



   def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)



    def test9_flujo_rapido_sin_extras(self):
        """Test 9: Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
         
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual( fases_esperadas, fases_obtenidas,
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
 
 ```

Y ahora hay que ejecutar para ver si los test tienen errores `python -m unnittest tests/test_lavadero_unnittest.py -v`.

![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest1.png)

El error que nos da en el 1 y en el 2 es basicamente porque esta llamando a `_hacer_lavado` pero en mi codigo esa funcion de llama  `hacerLavado`.



![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest2.png)



![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest3.png)


Ahora el error que nos queda esta en el test 9 en que cuando **no** hay secado a mano se deberia de ir a secado automatico pero se hacia justo lo contrario, simplemente invirtiendo una por otra estaria solucionado.

![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest4.png)





![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest5.png)



```

    def test3_excepcion_lavado_while_ocupado(self):
        """Test 3: Cuando se intenta hacer un lavado mientras que otro ya está en marcha, se produce una RuntimeError."""
    # Iniciamos un lavado normal (sin extras)
        self.lavadero.hacerLavado(False, False, False)
    
    # Intentamos iniciar otro lavado mientras está ocupado
        with self.assertRaises(RuntimeError) as context:
            self.lavadero.hacerLavado(False, False, False)
    
    # Opcional: comprobar el mensaje de error
        self.assertIn("ocupado", str(context.exception))


    def test5_ingresos_con_secado(self):
        """Test 5: Si seleccionamos un lavado con secado a mano, los ingresos son 6,00€."""
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=False)
    
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
    
        self.assertEqual(self.lavadero.ingresos, 6.00)


    def test6_ingresos_con_secado_y_encerado(self):
        """Test 6: Si seleccionamos un lavado con secado a mano y encerado, los ingresos son 7,20€."""
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=True)
    
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
    
        self.assertEqual(self.lavadero.ingresos, 7.20)


    def test7_ingresos_con_prelavado_y_secado(self):   
        """Test 7: Si seleccionamos un lavado con prelavado a mano y secado a mano, los ingresos son 7,50€."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=False)
    
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
    
        self.assertEqual(self.lavadero.ingresos, 7.50)


    def test8_ingresos_completo_todas_opciones(self):
        """Test 8: Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado, los ingresos son 8,70€."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=True)
    
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
    
        self.assertEqual(self.lavadero.ingresos, 8.70)    
    

```
Estos son los test `3,5,6,7 y 8` cuando los ejecute todos tenian fallos (No tengo captura porque la shell era muy larga).

Uno de los principales fallos era por la funcion de cobrar que estaba invertido el coste de secado y el de encerado simplemente leyendo el comentario que tenia puesto el codigo de lavadero vemos los precios que pone y cambiamos uno por el otro.
![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest6.png)


Y este es el otro fallo que daba es que los tests usan llamadas con keywordsy python solo permite eso si los parámetros tienen nombres en la definición del método. Entonces al cambiar esto:

![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest7.png)


![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest8.png)

Vemos que los test salen todos a ok.


Ahora vamos con los ultimos test que son `10,11,12,13 y 14`.
```
   def test10_flujo_con_prelavado(self):
        """Test 10: Con prelavado a mano, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 6, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=True, secado=False, encerado=False
        )
        self.assertEqual(
            fases_esperadas, fases_obtenidas,
            f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )

    def test11_flujo_con_secado(self):
        """Test 11: Con secado a mano (sin encerado), el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 0."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=False, secado=True, encerado=False
        )
        self.assertEqual(
            fases_esperadas, fases_obtenidas,
            f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )

    def test12_flujo_con_secado_y_encerado(self):
        """Test 12: Con secado a mano y encerado, el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 8, 0."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=False, secado=True, encerado=True
        )
        self.assertEqual(
            fases_esperadas, fases_obtenidas,
            f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )

    def test13_flujo_con_prelavado_y_secado(self):
        """Test 13: Con prelavado a mano y secado a mano (sin encerado), el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=True, secado=True, encerado=False
        )
        self.assertEqual(
            fases_esperadas, fases_obtenidas,
            f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )

    def test14_flujo_completo_todas_opciones(self):
        """Test 14: Con prelavado a mano, secado a mano y encerado, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 8, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=True, secado=True, encerado=True
        )
        self.assertEqual(
            fases_esperadas, fases_obtenidas,
            f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )
    

```

Al ejecutar estos test solo nos daban fallo el 12 y el 14 y daban el mismo problema el problema es que cuando se selecciona encerado (con secado a mano), el lavadero debería pasar por la fase 8 (Encerado) y después terminar (volver a 0).

Esto significa que al llegar a la fase SECADO_MANO (7), termina directamente, sin pasar por la fase ENCERADO (8), incluso cuando el cliente ha pagado encerado.

![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest9.png)


![TEST](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/Unnitest/Unnitest10.png)

Y ahora si  vemos que al ejecutar el `python -m unnittest tests/test_lavadero_unnittest.py -v` por ultima vez compila todo y sale todos los test a ok.