# tests/test_lavadero_unittest.py

import unittest
# Importamos la clase Lavadero desde el módulo padre
from src.lavadero import Lavadero
# from lavadero import Lavadero este es el fallo

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    def test_reseteo_estado_con_terminar(self):
        """Test : Verifica que terminar() resetea todas las flags y el estado."""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero._cobrar()
        self.lavadero.terminar()
        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
        
    # ----------------------------------------------------------------------
    # TESTS  
    # ----------------------------------------------------------------------
        
    def test1_estado_inicial_correcto(self):
        """Test 1: Verifica que el estado inicial es Inactivo y con 0 ingresos."""
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


    def test3_excepcion_lavado_while_ocupado(self):
        """Test 3: Cuando se intenta hacer un lavado mientras que otro ya está en marcha, se produce una RuntimeError."""
    # Iniciamos un lavado normal (sin extras)
        self.lavadero.hacerLavado(False, False, False)
    
    # Intentamos iniciar otro lavado mientras está ocupado
        with self.assertRaises(RuntimeError) as context:
            self.lavadero.hacerLavado(False, False, False)
    
    # Opcional: comprobar el mensaje de error
        self.assertIn("ocupado", str(context.exception))

    def test4_ingresos_con_prelavado(self):
        """Test 4: Si seleccionamos un lavado con prelavado a mano, los ingresos del lavadero son 6,50€."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=False, encerado=False)
    
    # Simulamos el ciclo completo para que se cobre
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
    
        self.assertEqual(self.lavadero.ingresos, 6.50)


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
    

    # ----------------------------------------------------------------------
    # Tests de flujo de fases
    # Utilizamos la función def ejecutar_y_obtener_fases(self, prelavado, secado, encerado)
    # Estos tests dan errores ya que en el código original hay errores en las las fases esperados, en los saltos.
    # ----------------------------------------------------------------------
    def test9_flujo_rapido_sin_extras(self):
        """Test 9: Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
         
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual( fases_esperadas, fases_obtenidas,
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
    
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
    
 
# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()


