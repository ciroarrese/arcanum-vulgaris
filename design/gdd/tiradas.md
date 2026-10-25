# Tiradas

> **Status**: Designed
> **Creative Director Review (CD-GDD-ALIGN)**: NOT ASSESSED 2026-10-25 — omitida en modo lean
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-25
> **Last Verified**: 2026-10-24
> **Implements Pillar**: Pilar 5 (Tiranía del Tiempo), Pilar 6 (No hay Carta Mala), D-05 (tarot real)

## Summary

Una tirada es la forma en que se reparten las cartas: cuántas, en qué posiciones y qué pregunta cada una. Este sistema define las 5 tiradas del juego (2 en el MVP: Carta Única y Tres Tiempos), qué rol de la Taxonomía pregunta cada posición, qué cartas son vecinas, cuánta vela cuesta cada una y para qué motivo es la esperada. El jugador elige la tirada después de escuchar al cliente y antes de repartir; elegir es medir cuánto vale la pena invertir en él. También define cómo funciona la pregunta de sí o no, con la valencia de cada tema.

> **Quick reference** — Layer: `Core` · Priority: `MVP` · Key deps: `Taxonomía de Temas y Roles, Mazo y Robo, Reloj de Vela`

## Overview

Una tirada es la forma en que se reparten las cartas sobre la mesa: cuántas son, en qué posiciones caen y qué pregunta hace cada posición. El sistema de Tiradas es el catálogo de esas formas. Para cada tirada define:

- sus **posiciones**, con el nombre que ve el jugador ("Pasado", "Respuesta") y el **rol** de la Taxonomía que cada una pregunta (origen, conflicto, desenlace), o "libre";
- qué posiciones son **vecinas**, que es lo que la Gramática usa para las dignidades elementales;
- su **costo en UT** y su **disponibilidad** (desde el inicio, desbloqueable, sedes altas);
- la **forma de pregunta** para la que es la tirada esperada (GDD §5.4).

El jugador elige qué tirada usar con cada cliente, después de verlo y escuchar el motivo. Más cartas significa más información y más posiciones donde acertar, pero también más tiempo de vela y más cartas que explicar (§5.4). Elegir la tirada es medir al cliente antes de leerle: saber cuándo alcanza una carta y cuándo hace falta desplegar el paño.

Las tiradas existen para desacoplar la lectura del cliente. El Generador produce la verdad por rol sin saber qué tirada se va a usar (D-37), y la tirada traduce sus posiciones a esos roles. Sin este catálogo no habría forma de saber qué compara cada carta, ni de que una tirada nueva funcione sin tocar al Generador.

## Detailed Design

### Core Rules

> Redactado en modo lean, sin consultar a `game-designer` ni a `systems-designer`. Hay que revisarlo a mano antes de producción.

**Las tiradas**

1. Hay **5 tiradas** (D-14). Cada una tiene un identificador estable con prefijo `tirada.`, un nombre visible que sale de la tabla de idioma, posiciones, vecindades, costo, disponibilidad y forma esperada:

   | Tirada | Cartas | Costo | Disponibilidad | Forma esperada | MVP |
   |---|---|---|---|---|---|
   | `tirada.carta_unica` | 1 | 10 UT | desde el inicio | `forma.si_o_no` | sí |
   | `tirada.tres_tiempos` | 3 | 20 UT | desde el inicio | `forma.situacion_general` | sí |
   | `tirada.dos_caminos` | 5 | 30 UT | desbloqueable | `forma.dilema` | no |
   | `tirada.vinculo` | 5 | 30 UT | desbloqueable | `forma.vinculo` | no |
   | `tirada.cruz_celta` | 10 | 45 UT | sedes altas | `forma.asunto_grave` | no |

2. **Posiciones y roles.** Cada posición tiene un id, un nombre visible y exactamente uno de dos datos: un rol o `libre` = sí (R9 de la Taxonomía).

   | Tirada | Posición → rol |
   |---|---|
   | Carta Única | Respuesta → desenlace |
   | Tres Tiempos | Pasado → origen · Presente → conflicto · Futuro → desenlace |
   | Dos Caminos | Situación → conflicto · Camino A → camino A · Camino B → camino B · Resultado A → camino A · Resultado B → camino B |
   | El Vínculo | Consultante → libre · El Otro → el otro · Lo que une → origen · Lo que separa → conflicto · Desenlace → desenlace |
   | Cruz Celta | 1 Lo que cubre → conflicto · 2 Lo que cruza → conflicto · 3 Corona → libre · 4 Base → origen · 5 Lo que queda atrás → origen · 6 Lo que viene → desenlace · 7 El consultante → libre · 8 El entorno → libre · 9 Esperanzas y temores → libre · 10 Resultado → desenlace |

   Los nombres de las posiciones salen de la tradición: Waite (1910) describe la Cruz Celta en la Parte III, §7. Las libres son las que hablan del propio cliente o de su ánimo, que el jugador ya observa en la mesa. Sus cartas cuentan para la Gramática y sirven para armar la Sentencia, pero no se comparan (R9 de la Taxonomía).
3. **Roles posteriores al MVP.** El otro, camino A y camino B están deshabilitados en el MVP (R8 de la Taxonomía). Si una posición pregunta un rol que la situación no tiene, da SIN_COMPARACION (E3 de la Taxonomía). Por eso Dos Caminos y El Vínculo no se ofrecen hasta que sus roles estén habilitados (R6).
4. **Vecindad.** Dos cartas son vecinas si sus posiciones lo son; la Gramática usa esto para las dignidades (§3.5).
   - Carta Única: sin vecinas.
   - Tres Tiempos: en línea, Pasado–Presente–Futuro.
   - Dos Caminos: Situación con Camino A y con Camino B; cada Camino con su Resultado.
   - El Vínculo: Desenlace en el centro, vecino de las otras 4; Consultante y El Otro son vecinos de Lo que une y de Lo que separa.
   - Cruz Celta: 1 y 2 son vecinas entre sí y de 3, 4, 5 y 6; la columna 7–8–9–10 va en línea y no toca la cruz.

**Elegir y repartir**

5. El jugador elige la tirada **después** de ver al cliente y escuchar el motivo, y **antes** de que se repartan las cartas. Una vez repartida, no se cambia. Se usa una sola tirada por cliente.
6. **Qué tiradas se ofrecen:** una tirada se ofrece si cumple tres condiciones:
   - está disponible en la partida;
   - todos sus roles están habilitados;
   - la vela tiene al menos su costo en UT.

   Si no se ofrece ninguna, el cliente no se puede leer (E2).
7. **Reparto:** Mazo y Robo reparte una carta por posición, en el orden de la tabla de R2, cada una derecha o invertida al azar (D-09). Tiradas no decide qué cartas salen.
8. **Tirada esperada:** cada forma de pregunta tiene una tirada esperada (R1). Si el jugador usa la esperada para la forma del motivo, se activa el bono de tirada (`B_tirada`, §5.8). Cuánto vale ese bono y cómo pesa justificar otra tirada lo define Resonancia.

**Carta aclaratoria (D-52)**

8a. Después del reparto, el jugador puede pedir **una carta aclaratoria** para una posición de su elección, pagando **5 UT**. Mazo y Robo reparte una carta más, con orientación al azar, y la deja junto a la de esa posición. Al interpretar esa posición, el jugador elige la palabra clave de cualquiera de las dos cartas; la posición conserva su rol y da un solo resultado (Taxonomía R11). Es la palanca del Pilar 6 ante una carta muda que pidió Cartas (E7, D-50).
8b. **Es ciega.** Se ofrece igual en cualquier posición, con rol o libre, sin consultar la verdad ni `acierto_posible` de Cartas. Si se ofreciera solo ante una carta muda, le diría al jugador algo de la verdad (Pilar 1).
8c. **Límites:** una aclaratoria por tirada, en total; se pide antes de confirmar la lectura de esa posición, y solo si la vela tiene las 5 UT. En la Carta Única, la tirada más la aclaratoria cuestan 15 UT, menos que Tres Tiempos (20), y el validador lo exige (R12).
8d. La aclaratoria no cambia la vecindad: la Gramática no la cuenta (*provisorio hasta el GDD de la Gramática*). Prestidigitación puede actuar sobre ella como sobre cualquier carta repartida (E6). Si el cliente desconfía de un tarotista que saca más cartas, lo define Resonancia (Open Questions).

**Pregunta de sí o no (D-51)**

9. Cada tema de la Taxonomía tiene una **valencia**: favorable, desfavorable o ambigua.

   | Valencia | Temas |
   |---|---|
   | Favorable | amor, alegría, fortuna, éxito |
   | Desfavorable | culpa, duelo, deuda, traición, violencia, engaño, muerte, locura, enfermedad |
   | Ambigua | deseo, hogar, trabajo, ley, secreto, poder, rivalidad, fama, riesgo, cambio |

   El campo es de la Taxonomía, que lo incorporó en R1 (D-51).
10. Si la forma del motivo es *sí o no*, el Generador primero sortea la respuesta verdadera (sí o no, con una proporción fija). Después sortea el tema del desenlace entre los temas de esa valencia (sí = favorable, no = desfavorable), con los pesos del mazo (Cartas F1). Un tema ambiguo nunca es el desenlace de una pregunta de sí o no. Esto es un contrato con el Generador.
11. En una pregunta de sí o no, el jugador afirma sí o no, con cualquier tirada. Compararlo con la respuesta verdadera, y castigar la contradicción con la palabra clave elegida, le corresponde a Interpretación y Resonancia. Tiradas solo garantiza que toda tirada que se ofrece tiene al menos una posición de desenlace, y las 5 la tienen.

**Validación**

12. Las tiradas pasan por el validador del catálogo (R13 de la Taxonomía): `ROL_INEXISTENTE`, `FORMA_INEXISTENTE`, `POSICION_AMBIGUA` y `TIRADA_SIN_COMPARABLES`. Este GDD agrega dos reglas:
    - una vecindad nombra solo posiciones de su tirada;
    - toda tirada tiene al menos una posición de desenlace (R11);
    - la Carta Única cuesta menos que Tres Tiempos, y la Carta Única más la aclaratoria también (Tuning Knobs).

    Los códigos se fijan en las historias.

### States and Transitions

| Estado de una tirada en la partida | Significa | Pasa a |
|---|---|---|
| No disponible | Todavía no se desbloqueó (Dos Caminos, El Vínculo) o no se llegó a la sede (Cruz Celta) | Disponible, cuando se cumple su condición. Lo define el sistema de desbloqueo (Open Questions) |
| Disponible | Se ofrece si cumple R6 | No vuelve atrás durante la partida |

Durante la lectura de un cliente: **elegida → repartida → (aclarada, opcional y una sola vez) → leída**. No hay vuelta atrás (R5, R8c).

### Interactions with Other Systems

| Sistema | Qué recibe de Tiradas | Qué aporta o devuelve |
|---|---|---|
| Taxonomía | Las posiciones con su rol o `libre`; la forma esperada | Roles, formas, validador y la valencia de cada tema (R9) |
| Mazo y Robo | Cuántas cartas repartir y en qué orden, y la carta aclaratoria (R8a) | Las cartas, con su orientación |
| Reloj de Vela | El costo en UT de la tirada elegida | Las UT que quedan (R6) |
| Gramática | La vecindad de cada tirada | Nada; la usa para las dignidades |
| Interpretación y Sentencia | Las posiciones con su rol o libre y su nombre visible | La palabra clave elegida por posición; el sí o no del jugador |
| Resonancia | Si la tirada fue la esperada (R8) | Nada; aplica `B_tirada` |
| Generador | Nada directo. Contrato de R10 para la pregunta de sí o no | La verdad por rol, y en sí o no también la respuesta verdadera |
| Prestidigitación | Las posiciones repartidas | Altera cartas ya repartidas; no cambia la tirada (R5) |
| Tapete y Tooltips | La forma visual, los nombres de las posiciones y el costo | Nada; los muestra |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD salvo la Taxonomía.

## Formulas

Las cuentas usan los datos de cobertura de Cartas (F3: `P_pos` ≈ 0,274 en Mayores + Copas). Son de calibración: el puntaje real y el umbral los define Resonancia. Ese `P_pos` sale del conteo de D-48, que no incluyó Waite III §4: las cifras son **pesimistas** hasta el reconteo (D-50). El reconteo no cambia los Mayores, que aportan la mayor parte de `P_pos`.

**F1. Posiciones comparables**

`k = cantidad de posiciones con rol (no libres) cuyo rol está habilitado y presente en la situación`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `k` | int | 1 a 6 | calculated (R2, R3) | Posiciones de la tirada que se comparan contra la verdad |

| Tirada | Carta Única | Tres Tiempos | Dos Caminos | El Vínculo | Cruz Celta |
|---|---|---|---|---|---|
| `k` | 1 | 3 | 5 | 4 | 6 (posiciones 1, 2, 4, 5, 6 y 10) |

**F2. Al menos un acierto posible en la tirada**

`P_alguno(k) = 1 − (1 − P_pos)^k`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `P_pos` | float | 0 a 1 | Cartas F3 | Probabilidad de acierto de familia posible en una posición |
| `P_alguno` | float | 0 a 1 | calculated | Probabilidad de que al menos una posición tenga acierto posible |

- **Valores:** con k = 1, 3, 4, 5 y 6 da **0,274 / 0,617 / 0,722 / 0,798 / 0,854**.
- **La Carta Única queda sin ningún acierto posible el 72,6 % de las veces.** Por eso Resonancia no puede usar un umbral fijo: tiene que medir en proporción a `k` (Open Questions).
- **Independencia:** es razonable aunque se repitan roles (Cruz Celta). Contando que dos posiciones del mismo rol comparten la verdad, la probabilidad de fallar en las dos da 0,527, contra 0,525 si fueran independientes. Repetir un rol sí aumenta la varianza: acertar el conflicto paga dos veces y errarlo cuesta dos veces.

**F3. Rendimiento por UT** (calibración)

`E_Match = k · s · (P_pos + P_exacto)` · `η = E_Match / C`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `P_exacto` | float | 0 a 1 | Cartas F3 (hipótesis: 0,09) | Probabilidad de acierto exacto posible en una posición |
| `s` | float | 0 a 1 | prototipo | Qué tan seguido el jugador elige la palabra correcta cuando hay acierto posible (1 = juego perfecto) |
| `C` | int | 10 a 45 | R1 | Costo de la tirada en UT |
| `η` | float | ≥ 0 | calculated | Match esperado (2/1/0, ilustrativo) por UT |

- **Con s = 1:** Carta Única 0,036 · Tres Tiempos 0,055 · Dos Caminos 0,061 · El Vínculo 0,049 · Cruz Celta 0,049. No incluye dignidades ni el bono de tirada.
- **Lectura:** la Carta Única es la más cara por punto, y la Cruz Celta rinde menos por UT que Tres Tiempos. Las tiradas grandes se justifican por la tarifa del cliente, no por eficiencia.
- `P_exacto` es una hipótesis; se reemplaza por el informe del validador (Cartas R11).

**F4. Acertar el sí o no**

`P_acierto_sn = 0,5 + Δ_deducción`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `ρ` | float | 0,5 | data file (Generador) | Proporción de respuestas verdaderas "sí" (Tuning Knobs) |
| `Δ_deducción` | float | 0 a 0,5 | Detección | Lo que suma deducir al cliente (tells, preguntas) |

- **La carta no informa:** como el reparto es independiente de la verdad (R7, D-37), P(sí | carta favorable) = `ρ`. Toda la información del sí o no sale del cliente (Pilar 1).
- **Por qué `ρ` = 0,5:** con cualquier otro valor, contestar siempre lo mismo da más del 50 %.
- **La carta restringe:** si el jugador cree "sí" y la Respuesta solo tiene palabras desfavorables, puede elegir una palabra ambigua (Match 0 seguro, porque una ambigua nunca es desenlace de un sí o no) o contradecirse. Cómo se castiga la contradicción lo define Resonancia.
- **El lado "sí" tiene menos cobertura:** su verdad sale de 4 temas, que la tradición usa poco. `P_pos` del desenlace en un sí o no se calcula con los pesos renormalizados dentro de la valencia, y tiene que agregarse al informe de Cartas R11.

**F5. Acierto posible con carta aclaratoria**

`P_alguno_acl(k) = 1 − (1 − P_pos)^(k + 1)`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `k` | int | 1 a 6 | F1 | Posiciones comparables |
| `P_alguno_acl` | float | 0 a 1 | calculated | Probabilidad de al menos un acierto posible con una aclaratoria en una posición comparable |

- Como es ciega, una aclaratoria equivale a una carta más en una posición: la Carta Única pasa de 0,274 a **0,473** por 15 UT, y Tres Tiempos de 0,617 a **0,722** por 25 UT.
- Si el jugador la pide en una posición libre, no suma acierto: la fórmula es una cota superior.

## Edge Cases

1. **A la vela no le alcanza para ninguna tirada.** No se ofrece ninguna (R6) y el cliente no se puede leer. Qué pasa con ese cliente (si se va o si abre una Deuda) lo define Fila y Mirilla. **Advertencia:** si una acción (una pregunta, un truco) va a dejar la vela por debajo del costo de la tirada más barata que se ofrece, el juego avisa antes. La acción igual se puede hacer.
2. **No se ofrece ninguna tirada por otra causa.** En el MVP no puede pasar: la Carta Única está disponible desde el inicio y su rol (desenlace) siempre está habilitado. Si pasara, se trata igual que el caso 1.
3. **Una forma de pregunta cuya tirada esperada no está disponible.** El Generador solo emite formas habilitadas cuya tirada esperada esté disponible en la partida, para que el bono de tirada siempre se pueda alcanzar. Esto es un contrato con el Generador (D-51). En el MVP no cambia nada, porque *sí o no* y *situación general* tienen sus tiradas desde el inicio.
4. **El jugador usa otra tirada que la esperada.** Está permitido, sin bono de tirada (R8). Si el motivo es de sí o no y usa Tres Tiempos, igual afirma sí o no (R11) y se comparan las 3 posiciones.
5. **Una posición pregunta un rol que la situación no tiene.** Da SIN_COMPARACION (E3 de la Taxonomía). En el MVP no se ofrecen las tiradas con roles deshabilitados (R3).
6. **Prestidigitación cambia o invierte una carta ya repartida.** La posición y su rol no cambian: se compara la carta nueva, en su orientación nueva.
7. **Dos posiciones con el mismo rol** (Cruz Celta, Dos Caminos). Cada una da su propio resultado contra la misma verdad. Cómo se combinan lo define Resonancia (E4 de la Taxonomía).
8. **En un sí o no, la Respuesta solo tiene palabras ambiguas o de la valencia contraria a lo que cree el jugador.** No hay forma de afirmar sin contradecirse o sin aceptar un Match 0 (F4). Es intencional: la carta condiciona y el estafador tiene que venderla igual.
9. **El jugador pide la aclaratoria en una posición libre.** Está permitido (R8b): si se prohibiera, la oferta diría qué posiciones cuentan, cosa que el nombre de la posición ya deja ver. No suma acierto (F5).

## Dependencies

**Depende de:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Taxonomía de Temas y Roles | Dura | Roles, formas de pregunta, posiciones libres, el validador (R8–R13) y la valencia de cada tema (R9) |
| Mazo y Robo | Dura, *provisoria* | Reparte una carta por posición con orientación al azar (R7) |
| Base de Datos de Cartas | Dura | `acierto_posible` (Cartas R12), solo para diseñar y calibrar la aclaratoria, nunca en juego (D-50). Cartas lee de este catálogo los `k` de las tiradas habilitadas (`k_tiradas`) |
| Reloj de Vela | Dura, *provisoria* | Las UT que quedan, para saber qué tiradas se ofrecen (R6) y para la advertencia de E1 |
| Sistema de desbloqueo | Blanda, *provisoria* | Cuándo pasan a disponibles Dos Caminos, El Vínculo y Cruz Celta (States). Todavía no se sabe qué sistema es (Open Questions) |

**Dependen de Tiradas:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Gramática de Combinación | Dura | La vecindad de cada tirada (R4) |
| Interpretación y Sentencia | Dura | Las posiciones, con su rol o libre y su nombre visible |
| Resonancia y Resolución | Dura | El rol de cada posición, `k` (F1) y si la tirada fue la esperada (R8) |
| Prestidigitación | Dura | Las posiciones repartidas sobre las que actúa un truco |
| Tapete y Tooltips de Cartas | Dura | La forma visual, los nombres de las posiciones y el costo |
| Generador de Situaciones | Blanda | Qué tiradas están disponibles, para emitir solo formas alcanzables (E3), y el contrato del sí o no (R10) |

**Bidireccionalidad:**

- La Taxonomía ya nombra a Tiradas entre sus dependientes e incorporó la valencia (R9).
- Los demás no tienen GDD; cada uno tiene que nombrar a Tiradas cuando se escriba.
- `systems-index.md` ya lista Reloj de Vela entre las dependencias de Tiradas, y Tiradas entre las del Generador.

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Costo en UT por tirada | Carta Única 10 · Tres Tiempos 20 · Dos Caminos 30 · El Vínculo 30 · Cruz Celta 45 (D-14) | Carta Única de 5 a 15 y Tres Tiempos de 15 a 30. La Carta Única tiene que costar menos que Tres Tiempos: es regla del validador (R12). Con la vela de 100 UT y 2 preguntas por cliente, son entre 3 y 5 clientes por jornada | Clientes por jornada y rendimiento por UT (F3) |
| Disponibilidad de Dos Caminos y El Vínculo | desbloqueables, condición a definir | La define el sistema de desbloqueo (Open Questions) | Cuándo se amplía el repertorio |
| Sede mínima de la Cruz Celta | "sedes altas", a definir | Sede 4 a 8 en el Mapa B (fuera del MVP, que va de la Sede 1 a la 3) | Cuándo aparecen los asuntos graves |
| Proporción de "sí" (`ρ`) | 0,5 | Solo 0,5: con cualquier otro valor, contestar siempre lo mismo conviene (F4). Es del Generador; está acá como referencia | Que el sí o no se deduzca del cliente y no se adivine |
| Costo de la carta aclaratoria | 5 UT | 3 a 9, siempre con Carta Única + aclaratoria < Tres Tiempos (regla del validador, R12) | Cuánto cuesta rescatar una carta muda (F5) |
| Aclaratorias por tirada | 1 | 1 a 2 | Cuánta palanca del Pilar 6 hay por cliente |

El bono por tirada esperada no está acá: lo define Resonancia (R8). El umbral de la advertencia de E1 tampoco es perilla, porque sale del costo de la tirada más barata que se ofrece.

## Visual/Audio Requirements

- Cada tirada se dibuja en el tapete con su disposición tradicional: Tres Tiempos en línea, Dos Caminos como una horquilla, El Vínculo como un rombo con el Desenlace al centro, y la Cruz Celta con la cruz y la columna de Waite (1910, Parte III §7).
- Las posiciones vecinas (R4) se ven juntas. Ninguna disposición pone pegadas dos posiciones que no son vecinas, para que la Gramática no contradiga lo que el jugador ve.
- El nombre de cada posición se ve en el tapete; el rol, nunca (UI Requirements de la Taxonomía).
- No hay sonido propio de este sistema; el sonido de repartir es de Mazo y Robo y del Tapete.

## Game Feel

Elegir la tirada es un compromiso: una vez repartida no se cambia (R5). El momento de elegir tiene que sentirse como una decisión sobre el cliente, no como un menú. El reparto en sí (animación, ritmo) es del Tapete. Tiene que ser breve, porque la vela ya pagó la tirada y el tiempo real solo corre en los tells (D-28).

## UI Requirements

- El selector de tiradas muestra, para cada tirada: nombre, cantidad de cartas, forma en el tapete y costo en UT.
- Las tiradas que no se ofrecen (R6) se ven deshabilitadas, con el motivo: "falta vela" o "todavía no la conocés". Las que no existen en la partida (no disponibles) no se muestran.
- **La tirada esperada no se marca.** El motivo del cliente se dice en su texto ("¿me va a llamar, sí o no?"), y reconocer qué tirada pide es parte de leerlo (§3.3: lo aprendido no lo explica el juego).
- La advertencia de E1 aparece antes de confirmar la acción que deja la vela sin tirada posible.

> 📌 **UX Flag — Tiradas:** antes de las historias del selector y del tapete hay que hacer su spec con `/ux-design`, con la disposición de la Cruz Celta en Switch portátil y la advertencia de la vela. Los AC visuales (AC-20 y los del tapete) se escriben ahí.

## Cross-References

| Fuente | Qué se toma |
|---|---|
| GDD §3.5 | Posición como pregunta; dignidades entre vecinas |
| GDD §5.1 | Vela de 100 UT; costo por acción |
| GDD §5.4 | Las 5 tiradas, sus posiciones y la tirada esperada |
| GDD §5.5 | Robo al azar; interpretación por posición |
| GDD §5.8 | `B_tirada`; Match por posición |
| Waite (1910), Parte III §7 | Posiciones de la Cruz Celta |
| D-09, D-14, D-23, D-28, D-37 | Robo al azar; tiradas y costos; MVP; vela por acción; Generador sin conocer la tirada |
| D-48, D-50, D-51, D-52 | Sorteo de la verdad según el mazo; Carta Única → desenlace y pregunta de sí o no |
| Taxonomía R8–R13, E3, E4 | Roles, posiciones libres, formas, validador; rol ausente; roles repetidos |
| Cartas F1, F3, R11 | Pesos de la verdad; `P_pos`; informe de cobertura |

## Acceptance Criteria

Convenciones de prueba:
- Todo AC parte de `fixture_tiradas_valido` y lo muta en un solo punto. AC-01 prueba que el fixture sin mutar pasa limpio.
- Cada error se verifica por la regla de la que es (con el código que fije la historia) y por su sujeto en formato R13 de la Taxonomía. Los controles dicen "no contiene error de la regla X con sujeto S", nunca "no hay errores".
- El RNG y el reparto se simulan; ningún test depende del azar.
- `ROL_INEXISTENTE`, `FORMA_INEXISTENTE`, `POSICION_AMBIGUA` y `TIRADA_SIN_COMPARABLES` ya los prueban AC-31, AC-33, AC-37a/b y AC-38 de la Taxonomía, y SIN_COMPARACION su E3. No se repiten acá.
- **Evidencia:** todos son Logic (test unitario en `[test root]/tiradas/`), salvo los marcados Integration, UI o Config/Data. Los *provisorios* dependen de un GDD que no existe y no bloquean hasta que exista.
- **Sin AC, a propósito:** F2 y F3 son de calibración y ningún código del juego las calcula. La suma de deducción de F4 es de Detección. E5 lo cubre la Taxonomía (E3) y AC-08. La combinación de E7 es de Resonancia. E8 es una consecuencia intencional de R10 y va al playtest.

**Catálogo**
- **AC-01** (R1–R12) — GIVEN `fixture_tiradas_valido`, WHEN se valida, THEN la lista está vacía.
- **AC-02** (R1, R2) — GIVEN el catálogo real, WHEN se carga, THEN hay 5 tiradas con los ids de R1, con 1/3/5/5/10 posiciones, costos 10/20/30/30/45 y la forma esperada de R1, y cada posición tiene exactamente el rol o `libre` de la tabla de R2.
- **AC-03** (R4) — GIVEN el catálogo real, WHEN se cargan las vecindades, THEN son exactamente estas, y simétricas:
  - Carta Única: ninguna.
  - Tres Tiempos: Pasado–Presente y Presente–Futuro (Pasado y Futuro no son vecinas).
  - Dos Caminos: Situación–Camino A, Situación–Camino B, Camino A–Resultado A y Camino B–Resultado B.
  - El Vínculo: Desenlace con las otras 4; Consultante y El Otro, cada uno con Lo que une y con Lo que separa.
  - Cruz Celta: 1–2, 1 y 2 con cada una de 3 a 6, 7–8, 8–9 y 9–10.
- **AC-04** (R12) — GIVEN `tirada_vecina` con la vecindad `p1–p9`, donde `p9` no es una posición suya, WHEN se valida, THEN contiene error de vecindad con sujeto `tirada_vecina/p9`. Control: con `p1–p2`, no lo contiene.
- **AC-05** (R11, R12) — GIVEN `tirada_sin_desenlace`, sin ninguna posición de rol desenlace, WHEN se valida, THEN contiene error de desenlace con sujeto `tirada_sin_desenlace`. Control: con una posición de desenlace, no lo contiene.

**Oferta**
- **AC-06** (R6, E1) — GIVEN Carta Única y Tres Tiempos disponibles, WHEN se piden las tiradas ofrecidas, THEN: con 20 UT, las dos; con 19, solo Carta Única; con 10, solo Carta Única; con 9, ninguna, y el cliente queda marcado como "no se puede leer".
- **AC-07** (E2) — GIVEN Carta Única no disponible y 100 UT, WHEN se piden las tiradas ofrecidas, THEN no se ofrece ninguna y el cliente lleva la misma marca que en AC-06.
- **AC-08** (R3, R6) — GIVEN Dos Caminos disponible, `rol.camino_b` deshabilitado y 100 UT, WHEN se piden las tiradas ofrecidas, THEN Dos Caminos no está. Lo mismo con El Vínculo y `rol.el_otro`. Control: con el rol habilitado, se ofrece.
- **AC-09** (R6, States) — GIVEN Cruz Celta no disponible y 100 UT, WHEN se piden las tiradas ofrecidas, THEN no está. Control: disponible, se ofrece.
- **AC-10** (States; *provisorio hasta el sistema de desbloqueo*) — GIVEN una tirada Disponible, WHEN cambia la jornada y cambia la sede, THEN sigue Disponible.

**Lectura**
- **AC-11** (R5, States) — GIVEN una tirada elegida, WHEN se elige otra antes de repartir, THEN se cambia. GIVEN una tirada repartida o leída, WHEN se elige otra, THEN se rechaza y la tirada no cambia. Un segundo reparto para el mismo cliente también se rechaza.
- **AC-12** (R7) — GIVEN Tres Tiempos y un reparto simulado que devuelve (A, derecha), (B, invertida) y (C, derecha), WHEN se reparte, THEN se piden exactamente 3 cartas y quedan Pasado = A derecha, Presente = B invertida, Futuro = C derecha.
- **AC-13** (R7, D-37, F4) — GIVEN la misma secuencia del RNG y la verdad "sí" en una corrida y "no" en otra, WHEN se reparte, THEN los dos repartos son idénticos.
- **AC-14** (R8, E4) — GIVEN cada una de las 5 formas, WHEN se elige cada tirada, THEN solo la tirada esperada de R1 activa el bono. Con `forma.si_o_no` y Tres Tiempos no hay bono, y las 3 posiciones se comparan igual.

**Sí o no**
- **AC-15** (R9) — La valencia de cada tema la prueban AC-35d y AC-35e de la Taxonomía; no se repite acá.
- **AC-16** (R10, Tuning Knobs; *provisorio hasta el Generador*) — GIVEN un fixture con `ρ` = 1, WHEN se sortea la respuesta, THEN siempre sale sí; con `ρ` = 0, siempre no. En los datos reales, `ρ` = 0,5 (Config/Data).
- **AC-17** (R10; *provisorio hasta el Generador*) — GIVEN una pregunta de sí o no, WHEN se arman los candidatos al desenlace, THEN son exactamente los 4 temas favorables para sí y los 9 desfavorables para no, con los pesos de Cartas F1 renormalizados dentro de la valencia; ningún tema ambiguo está entre los candidatos.
- **AC-18** (E3; *provisorio hasta el Generador*) — GIVEN Dos Caminos no disponible, WHEN se arman las formas que el Generador puede emitir, THEN no incluyen `forma.dilema`. Control: con Dos Caminos disponible, la incluyen.

**Advertencia de la vela**
- **AC-19** (E1) — GIVEN 14 UT, una acción de 5 UT y 10 UT como costo de la tirada más barata que se ofrece, WHEN se evalúa la acción, THEN corresponde avisar; con 15 UT, no. Después del aviso, la acción se ejecuta igual.
- **AC-20** (E1; UI) — GIVEN la vela en 14 UT, WHEN el jugador elige una pregunta de 5 UT, THEN la advertencia aparece antes de descontar las UT. Evidencia: captura retenida en `production/qa/evidence/`.

**Otros sistemas**
- **AC-21** (E6; Integration, *provisorio hasta Prestidigitación*) — GIVEN un truco que cambia la carta del Presente, WHEN se compara, THEN la posición sigue con rol conflicto y se compara la carta nueva. Si el truco la invierte, se compara la orientación nueva.
- **AC-22** (F1) — GIVEN todos los roles habilitados y presentes, WHEN se calcula `k`, THEN da 1/3/5/4/6 para Carta Única, Tres Tiempos, Dos Caminos, El Vínculo y Cruz Celta (en Cruz Celta, posiciones 1, 2, 4, 5, 6 y 10). Con los roles del MVP, Dos Caminos da 1 y El Vínculo 3. En una situación sin el rol origen, Tres Tiempos da 2.
- **AC-23** (R12, Tuning Knobs) — GIVEN `fixture_tiradas_valido` con la Carta Única a 20 UT y Tres Tiempos a 20 UT, WHEN se valida, THEN contiene error de costos con sujeto `tirada.carta_unica`. Lo mismo con la Carta Única a 25. Control: con 19, no lo contiene.
- **AC-24** (R8a) — GIVEN Tres Tiempos repartida y 10 UT, WHEN se pide una aclaratoria para Presente, THEN se reparte 1 carta más junto a Presente y se descuentan 5 UT; las palabras clave elegibles para Presente son las de las dos cartas, y Presente da un solo resultado.
- **AC-25** (R8b) — GIVEN dos situaciones con verdades distintas y el mismo reparto, WHEN se piden las posiciones donde se ofrece la aclaratoria, THEN en las dos son todas las posiciones de la tirada.
- **AC-26** (R8c) — GIVEN una aclaratoria ya pedida en la tirada, WHEN se pide otra, THEN se rechaza. Con 4 UT, no se ofrece. Después de confirmar la lectura de una posición, no se ofrece para esa posición.
- **AC-27** (R12, Tuning Knobs) — GIVEN la aclaratoria a 10 UT, con Carta Única a 10 y Tres Tiempos a 20, WHEN se valida, THEN contiene error de costos con sujeto `tirada.carta_unica`. Con 9, no lo contiene.
- **AC-28** (R8b, D-50) — GIVEN un doble de `acierto_posible` y del acceso a la verdad que fallan si se los llama, WHEN se arma la oferta de aclaratoria, THEN la oferta se arma sin llamarlos.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| **Requisito de F2:** Resonancia mide en proporción a las posiciones comparables (`k`), no con un umbral fijo; si no, la Carta Única queda casi imposible de aprobar (72,6 % sin acierto posible). ¿El sí o no del jugador cuenta como un acierto propio? | GDD de Resonancia | Al diseñar Resonancia |
| Cuánto vale `B_tirada` y cómo pesa justificar otra tirada (§5.4). ¿Las posiciones libres pueden contradecir? | GDD de Resonancia | Al diseñar Resonancia |
| Contratos de R10 y E3: el sorteo del sí o no (`ρ` = 0,5, desenlace dentro de la valencia) y las formas solo con tirada disponible | GDD del Generador | Al diseñar el Generador |
| `P_pos` del desenlace en un sí o no, con pesos renormalizados dentro de la valencia: sumarlo al informe de Cartas R11 | GDD de Cartas | Revisión de Cartas |
| Qué desbloquea Dos Caminos y El Vínculo, y desde qué sede aparece la Cruz Celta | GDD del sistema de desbloqueo (Fama o Trastienda) | Antes del Vertical Slice |
| Qué pasa con un cliente al que no se le puede ofrecer ninguna tirada (E1) | GDD de Fila y Mirilla | Al diseñar Fila y Mirilla |
| ¿El estatus del cliente (§5.4, "lo que puede pagar") limita qué tiradas se le ofrecen? | GDD de Arquetipos, economía | Al diseñar Arquetipos |
| ¿Carta Única + *invertir* (12 UT) desplaza a Tres Tiempos (20 UT)? Medir | Diseñador | Prototipo del núcleo |
| ¿Las posiciones libres de la Cruz Celta y El Vínculo se sienten como una falsa elección? | Diseñador | Playtest |
| La tirada final del Mapa B (Cruz Celta del Lunes Negro) | `design/mapas/mapa-b-new-carthage.md` | Fuera del MVP |
| ¿El cliente desconfía de un tarotista que saca una carta aclaratoria (Credulidad)? | GDD de Resonancia, Métricas del Cliente | Al diseñar Resonancia |
| ¿La aclaratoria participa de la Gramática (dignidades con la carta de su posición)? | GDD de Gramática | Al diseñar la Gramática |
| Medir en el prototipo si la aclaratoria ciega rescata lo suficiente o si el Pilar 6 necesita otra palanca | Diseñador | Prototipo del núcleo |
