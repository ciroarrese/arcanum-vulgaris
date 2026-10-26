# Economía del MVP — Mapa B, Sedes 1 a 3

> **Estado: EN RECALIBRACIÓN** (D-35 aprobó esta versión; D-57 y D-59 la reabren). El precio por tirada y el pago limitado por lo que tiene el cliente (`design/gdd/tiradas.md` F3a) reemplazan la tarifa plana de §1; el script todavía no los modela. El modelo provisorio está en `prototypes/nucleo/plan-hipotesis-tiradas.md`. Números provisorios para el prototipo; el rebalanceo completo se hace con datos de juego real.
> **Simulación:** `tools/balance/economia_mvp.py` (Monte Carlo, 2.000 partidas por perfil). Si un valor cambia acá, cambia en el script.

## 1. Regla de Tarifas (resuelve la contradicción de la v1.3)
La tarifa ya no es fija por arquetipo ni fija por sede: es el **producto de las dos**.

$$T_{\text{base}} = \text{Tarifa}_{\text{sede}} \times \text{Estatus}_{\text{arquetipo}}$$

Así un mismo arquetipo paga más en una sede más cara, y la tabla de arquetipos (§7.3 del GDD) deja de chocar con la de sedes (§7.5).

## 2. Sedes

| Sede | Tarifa de sede | Renta | Peaje | Vela | Costo fijo diario | Mudanza a la siguiente | Fama req. | Reputación req. | Población (peso) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. La Boca del Subte** | 4 | 5 | 2 | 2 | 9 | 100 | 20 | 30% | Vagabundo 5, Estibador 3, Apostador 2 |
| **2. La Lavandería 24 Horas** | 10 | 18 | 6 | 4 | 28 | 350 | 45 | 45% | Apostador 4, Estibador 3, Viuda 2, Detective 1 |
| **3. El Local de la Galería** | 25 | 45 | 15 | 8 | 68 | — (fin del MVP) | — | — | Viuda 4, Detective 3, Apostador 2, Estibador 1 |

Cambios frente a la v1.3: mudanza a la Sede 2 de 50 → **100**; a la Sede 3 de 150 → **350**; Fama requerida 15 → **20** y 35 → **45**. Con los valores viejos, un jugador medio llegaba a la Sede 3 en 9 jornadas.

## 3. Arquetipos del MVP

| Arquetipo (Mapa B) | Estatus | K de propina | Recompensa del Doble Fondo |
| :--- | :---: | :---: | :--- |
| **El Vagabundo** | 0.5 | 0.2 | Bonos al portador: **25 a 40 monedas** (antes 120 a 250, que pagaban hasta 25 días de la Sede 1). |
| **El Estibador** | 1.0 | 0.5 | Salvoconducto sindical (evita el boicot). |
| **El Apostador** | 0.8 | 0.8 | Dossier del cliente VIP de mañana. |
| **La Viuda** | 1.5 | 1.8 | **60 a 100 monedas** por complicidad (antes 200 a 400). |
| **El Detective** | 1.2 | 0.5 | Inmunidad: anula multas por 5 días. |

El Doble Fondo además aplica $M_{\text{DF}} = 2.5$ a $4.0$ sobre el ingreso de la sesión (GDD §7.2).

## 4. Ingreso por Sesión
$$I = \left(T_{\text{base}} \times M_{\text{intención}} + T_{\text{base}} \times \frac{\text{Credulidad}}{100} \times K_{\text{propina}}\right) \times Q_{\text{Resonancia}}$$

* **Nuevo:** $Q_{\text{Resonancia}}$ escala el pago según la calidad de la lectura (simulado: 0.9 floja, 1.0 correcta, 1.3 excelente). Ver hallazgo 2.
* Fallo: $0.2 \times T_{\text{base}}$.
* Multiplicadores de intención simulados: Consolar 1.0, Acusar 3.0, Paranoia 2.0, Extorsionar 5.0.

## 5. Resultados de la Simulación

| Perfil | Acierto | Jornadas en Sede 1 | Jornadas en Sede 2 | Llega a la Sede 3 en | Jornadas en negativo (promedio) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Novato** | 45% | 16 | 12 | jornada 29 | 1.8 |
| **Medio** | 60% | 7 | 6 | jornada 13 | 0.4 |
| **Experto** | 75% | 5 | 4 | jornada 10 | 0.2 |

Con unos 8 a 12 minutos por jornada (a medir en el prototipo), un jugador medio completa el MVP en **2 a 3 horas**.

## 6. Hallazgos
1. **El Doble Fondo de la v1.3 rompía la economía.** Un solo Vagabundo pagaba hasta 25 días de la Sede 1. Ahora paga 3 a 4 días.
2. **Sin $Q_{\text{Resonancia}}$, el experto no avanzaba más rápido que el jugador medio.** El experto hace más preguntas (gasta más vela) y atiende menos clientes; si una lectura excelente paga igual que una correcta, investigar a fondo no rinde. **El pago tiene que crecer con la calidad de la lectura, no solo con acertar o fallar.** Esto afecta la fórmula de la Resonancia del GDD (§5.8).
3. **El Usurero casi no aparece.** Incluso el novato pasa menos de 2 jornadas en negativo. La simulación no modela las pérdidas por fallos con clientes peligrosos (Deudas de Sangre del Detective, robos del Apostador); con eso la presión debería subir. Si en el prototipo sigue sin aparecer, subir los costos fijos de la Sede 2.
4. **El novato tarda 29 jornadas,** pero en la simulación no aprende: su acierto queda fijo en 45%. En el juego real mejora con la práctica, así que la cifra real debería ser menor.

## 7. Qué Medir en el Prototipo
* Minutos reales por jornada y por sesión.
* Acierto real de jugadores nuevos en sus primeras 5 jornadas.
* Cuántas preguntas hace un jugador por sesión.
* Frecuencia real de caída en el Usurero.
