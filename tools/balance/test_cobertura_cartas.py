"""Pruebas de tools/balance/cobertura_cartas.py.

Uso: python3 -m unittest tools/balance/test_cobertura_cartas.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import cobertura_cartas as cc  # noqa: E402

# Datos redondeados de AC-18c de Cartas (orden Emoción, Bienes, Conflicto, Ambición, Destino).
Q_18C = (0.31, 0.26, 0.31, 0.28, 0.17)
P_18C = (0.23, 0.20, 0.23, 0.21, 0.13)


class Formulas(unittest.TestCase):
    def test_ac_18c(self):
        pp = cc.p_pos(P_18C, Q_18C)
        self.assertAlmostEqual(pp, 0.2755, places=9)
        self.assertAlmostEqual(cc.p_cero(pp, 3), 0.3803, delta=0.0001)
        self.assertAlmostEqual(cc.p_cero_corr(P_18C, Q_18C, 3), 0.3849, delta=0.0001)
        self.assertAlmostEqual(cc.p_cero(pp, 1), cc.p_cero_corr(P_18C, Q_18C, 1), places=9)
        self.assertAlmostEqual(cc.p_cero(0.17, 3), 0.5718, delta=0.0005)

    def test_potencia(self):
        self.assertEqual(cc.potencia(0.5, 3), 0.125)
        self.assertEqual(cc.potencia(0.7, 0), 1.0)

    def test_f2_en_enteros(self):
        self.assertTrue(cc.pasa_f2(8, 72))
        self.assertFalse(cc.pasa_f2(7, 72))
        self.assertTrue(cc.pasa_f2(7, 100, q_mil=70))   # AC-15e
        self.assertFalse(cc.pasa_f2(6, 100, q_mil=70))

    def test_sin_reposicion(self):
        ton, mit = cc.sin_reposicion_extremos(36, 20, 3)
        self.assertAlmostEqual(ton, 0.3641, delta=0.0001)   # C(26,3)/C(36,3)
        self.assertAlmostEqual(mit, 0.3729, delta=0.0001)
        self.assertLess(ton, mit)
        self.assertLess(mit, cc.p_cero(20 / 72, 3))       # sin reponer baja P_cero


class Conteo(unittest.TestCase):
    def test_quince_mazos(self):
        self.assertEqual(len(cc.mazos()), 15)
        self.assertEqual(cc.nombre(cc.mazos()[-1]), "copas+oros+espadas+bastos")

    def test_mayores_copas(self):
        n, o, c = cc.conteos(("copas",))
        self.assertEqual((n, o, c), (36, 72, (22, 19, 22, 20, 12)))
        self.assertAlmostEqual(cc.p_pos(cc.p_aprox(c), [x / o for x in c]), 0.274, delta=0.0005)

    def test_cuatro_palos(self):
        n, o, c = cc.conteos(cc.PALOS)
        self.assertEqual((n, o), (78, 156))
        self.assertEqual(sum(c), sum(sum(v) for v in cc.C_BLOQUE.values()))

    def test_progresion_nunca_un_palo(self):
        self.assertTrue(all(len(m) >= 2 for m, _, _, _ in cc.marcas_progresion()))


if __name__ == "__main__":
    unittest.main()
