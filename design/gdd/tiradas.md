# Tiradas

> **Status**: In Review
> **Creative Director Review (CD-GDD-ALIGN)**: `/design-review` full del 2026-10-25 (primera pasada), NEEDS REVISION; corregida el mismo día (D-55); re-revisión full del 2026-10-25, NEEDS REVISION, corregida el mismo día (D-57); pendiente de re-revisión
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-25
> **Last Verified**: 2026-10-25
> **Implements Pillar**: Pilar 5 (Tiranía del Tiempo), Pilar 6 (No hay Carta Mala), D-05 (tarot real)

## Summary

Una tirada es la forma en que se reparten las cartas: cuántas, en qué posiciones y qué pregunta cada una. Este sistema define las 5 tiradas del juego (2 en el MVP: Carta Única y Tres Tiempos), qué rol de la Taxonomía pregunta cada posición, qué cartas son vecinas, cuánta vela cuesta y cuánto vale cada una, y para qué motivo es la esperada. El jugador elige la tirada después de escuchar al cliente y antes de repartir; elegir es medir cuánto vale la pena invertir en él y cuánto puede pagar (D-57). También define cómo funciona la pregunta de sí o no, con la valencia de cada tema.

> **Quick reference** — Layer: `Core` · Priority: `MVP` · Key deps: `Taxonomía de Temas y Roles, Mazo y Robo, Reloj de Vela`

## Overview

Una tirada es la forma en que se reparten las cartas sobre la mesa: cuántas son, en qué posiciones caen y qué pregunta hace cada posición. El sistema de Tiradas es el catálogo de esas formas. Para cada tirada define:

- sus **posiciones**, con el nombre que ve el jugador ("Pasado", "Respuesta") y el **rol** de la Taxonomía que cada una pregunta (origen, conflicto, desenlace), o "libre";
- qué posiciones son **vecinas**, que es lo que la Gramática usa para las dignidades elementales;
- su **costo en UT**, su **precio** (cuánto vale para el cliente; D-57) y su **disponibilidad** (desde el inicio, desbloqueable, sedes altas);
- la **forma de pregunta** para la que es la tirada esperada (GDD §5.4).

El jugador elige qué tirada usar con cada cliente, después de verlo y escuchar el motivo, entre las que tiene desbloqueadas. Más cartas significa más información, más posiciones donde acertar y un precio más alto, pero también más tiempo de vela y más cartas que explicar (§5.4). Una tirada cara no garantiza más dinero: el cliente paga según cómo quedó (satisfecho, emocionado, pasmado, enojado) y hasta lo que tiene (R8e, D-57). Elegir la tirada es medir al cliente antes de leerle: saber cuándo alcanza una carta y cuándo vale la pena desplegar el paño. En el MVP esto es una hipótesis del prototipo (Open Questions).

Las tiradas existen para desacoplar la lectura del cliente. El Generador produce la verdad por rol sin saber qué tirada se va a usar (D-37), y la tirada traduce sus posiciones a esos roles. Sin este catálogo no habría forma de saber qué compara cada carta, ni de que una tirada nueva funcione sin tocar al Generador.

## Player Fantasy

Elegir la tirada es apostar cuánto vale este cliente. El tarotista mira la ropa, escucha la pregunta y decide si le alcanza una carta o si hay que desplegar el paño. Una tirada grande impresiona y cuesta más, pero un cliente pobre paga lo que tiene y uno enojado no paga nada (R8e). La carta que sale es una excusa para la venta, no una respuesta: la verdad está en el cliente (Pilar 1), y cualquier carta se puede vender (Pilar 6).

## Detailed Design

### Core Rules

**Las tiradas**

1. Hay **5 tiradas** (D-14). Cada una tiene un identificador estable con prefijo `tirada.`, un nombre visible que sale de la tabla de idioma, posiciones, vecindades, costo, precio, disponibilidad y forma esperada:

   | Tirada | Cartas | Costo | Precio (`π`) | Disponibilidad | Forma esperada | MVP |
   |---|---|---|---|---|---|---|
   | `tirada.carta_unica` | 1 | 10 UT | ×1 | desde el inicio | `forma.si_o_no` | sí |
   | `tirada.tres_tiempos` | 3 | 20 UT | ×1,5 | desde el inicio | `forma.situacion_general` | sí |
   | `tirada.dos_caminos` | 5 | 30 UT | ×2 | desbloqueable | `forma.dilema` | no — pendiente |
   | `tirada.vinculo` | 5 | 30 UT | ×2 | desbloqueable | `forma.vinculo` | no — pendiente |
   | `tirada.cruz_celta` | 10 | 45 UT | ×3 | sedes altas | `forma.asunto_grave` | no — pendiente |

   El precio es un multiplicador sobre la tarifa del cliente (R8e). Los valores son *provisorios* hasta el prototipo (D-57). Las tres tiradas fuera del MVP tienen pendientes de diseño (R3a).

2. **Posiciones y roles.** Cada posición tiene un id, un nombre visible y exactamente uno de dos datos: un rol o `libre` = sí (R9 de la Taxonomía).

   | Tirada | Posición → rol |
   |---|---|
   | Carta Única | Respuesta → desenlace |
   | Tres Tiempos | Pasado → origen · Presente → conflicto · Futuro → desenlace |
   | Dos Caminos | Situación → conflicto · Camino A → camino A · Camino B → camino B · Resultado A → desenlace · Resultado B → desenlace |
   | El Vínculo | Consultante → libre · El Otro → el otro · Lo que une → origen · Lo que separa → conflicto · Desenlace → desenlace |
   | Cruz Celta | 1 Lo que cubre → conflicto · 2 Lo que cruza → conflicto · 3 Corona → libre · 4 Base → origen · 5 Lo que queda atrás → origen · 6 Lo que viene → desenlace · 7 El consultante → libre · 8 El entorno → libre · 9 Esperanzas y temores → libre · 10 Resultado → desenlace |

   Los nombres de las posiciones salen de la tradición: Waite (1910) describe la Cruz Celta en la Parte III, §7. Las libres son las que hablan del propio cliente o de su ánimo, que el jugador ya observa en la mesa. Sus cartas cuentan para la Gramática y sirven para armar la Sentencia, pero no se comparan (R9 de la Taxonomía).
3. **Roles posteriores al MVP.** El otro, camino A y camino B están deshabilitados en el MVP (R8 de la Taxonomía). Si una posición pregunta un rol que la situación no tiene, da SIN_COMPARACION (E3 de la Taxonomía). Por eso Dos Caminos y El Vínculo no se ofrecen hasta que sus roles estén habilitados (R6).
3a. **Fuera del MVP — pendiente.** Estas tres tiradas no se ofrecen en el MVP y tienen huecos conocidos, que se resuelven antes de habilitarlas:
   - **Dos Caminos:** Resultado A y Resultado B comparan contra el mismo desenlace (D-55), así que no distinguen los caminos. Se rediseña al habilitar `rol.camino_a` y `rol.camino_b` (Generador, Taxonomía).
   - **Cruz Celta:** rinde menos Match por UT que Tres Tiempos (F3). Su precio (R1) es la compensación provisoria; se recalibra con la economía.
   - **Desbloqueo:** si Dos Caminos y El Vínculo se desbloquean por partida o por perfil (metaprogresión) lo decide Fama (D-56). States supone por partida; si es por perfil, la tabla cambia.
4. **Vecindad.** Dos cartas son vecinas si sus posiciones lo son; la Gramática usa esto para las dignidades (§3.5).
   - Carta Única: sin vecinas.
   - Tres Tiempos: en línea, Pasado–Presente–Futuro.
   - Dos Caminos: Situación con Camino A y con Camino B; cada Camino con su Resultado.
   - El Vínculo: Desenlace en el centro, vecino de las otras 4; Consultante y El Otro son vecinos de Lo que une y de Lo que separa.
   - Cruz Celta: 1 y 2 son vecinas entre sí y de 3, 4, 5 y 6; la columna 7–8–9–10 va en línea y no toca la cruz.

**Elegir y repartir**

5. El jugador elige la tirada **después** de ver al cliente y escuchar el motivo, y **antes** de que se repartan las cartas. Elegir es gratis y se puede cambiar hasta confirmar el reparto. Al confirmar, se vuelve a verificar R6 con la vela de ese momento y se descuenta el costo de la tirada, una sola vez; si ya no alcanza, el reparto se rechaza y no se descuenta nada. Una vez repartida, no se cambia. Se usa una sola tirada por cliente. El orden completo de la atención está en States and Transitions.
6. **Qué tiradas se ofrecen:** una tirada se ofrece si cumple tres condiciones:
   - está disponible en la partida;
   - todos sus roles están habilitados;
   - la vela tiene al menos su costo en UT.

   Si no se ofrece ninguna, el cliente no se puede leer (E2).
7. **Reparto:** Mazo y Robo reparte una carta por posición, en el orden de la tabla de R2, cada una derecha o invertida al azar (D-09). Tiradas no decide qué cartas salen.
8. **Tirada esperada:** cada forma de pregunta tiene una tirada esperada (R1). Si el jugador usa la esperada para la forma del motivo, se activa el bono de tirada (`B_tirada`, §5.8). Si usa otra, no hay bono y baja la Credulidad, salvo que justifique la tirada con una buena lectura (GDD §5.4). Cuánto vale el bono, cuánto baja la Credulidad y qué cuenta como justificar lo define Resonancia (*provisorio*).
   - **Vela corta (D-57):** si la tirada esperada no se ofrece porque la vela no alcanza (R6, tercera condición) y sí se ofrece otra, el jugador elige entre dos salidas:
     - leer con una tirada que se ofrece: no hay bono y **no** baja la Credulidad;
     - **negociar que el cliente vuelva la próxima jornada** (R8f).

**Carta aclaratoria (D-52)**

8a. Después del reparto, el jugador puede pedir **una carta aclaratoria** para una posición de su elección, pagando **5 UT**, que se descuentan al pedirla. Pedirla son dos pasos: elegir la posición, que es gratis y se puede cancelar o cambiar, y confirmar el pedido, que cobra (como elegir y confirmar la tirada, R5). Mazo y Robo reparte una carta más, con orientación al azar, y la deja junto a la de esa posición. Al interpretar esa posición, el jugador elige la palabra clave de cualquiera de las dos cartas; la posición conserva su rol y da un solo resultado (Taxonomía R11). Es la palanca del Pilar 6 ante una carta muda que pidió Cartas (E7, D-50).
8b. **Es ciega.** Se ofrece igual en cualquier posición, con rol o libre, sin consultar la verdad ni `acierto_posible` de Cartas. Si se ofreciera solo ante una carta muda, le diría al jugador algo de la verdad (Pilar 1).
8c. **Límites:** hasta `n_acl` aclaratorias por tirada, en total (hoy 1, Tuning Knobs); se pide antes de confirmar la lectura de esa posición, y solo si la vela tiene las 5 UT. Confirmar la lectura de una posición es un paso explícito (States). En la Carta Única, la tirada más la aclaratoria cuestan 15 UT, menos que Tres Tiempos (20), y el validador lo exige (R12).
8d. La aclaratoria no cambia la vecindad: la Gramática no la cuenta (*provisorio hasta el GDD de la Gramática*). Prestidigitación puede actuar sobre ella como sobre cualquier carta repartida (E6). Si el cliente desconfía de un tarotista que saca más cartas, lo define Resonancia (Open Questions).

**Precio, pago y vuelta del cliente (D-57)**

8e. **Precio y pago (D-57).** Cada tirada tiene un precio `π` (R1) que multiplica la tarifa del cliente: las tiradas más complejas valen más. El pago real no es el precio: depende de cómo quedó el cliente (satisfecho, emocionado, pasmado, enojado) y nunca supera lo que el cliente tiene. Un cliente pobre paga lo que puede aunque la tirada valga más. Cómo se calcula lo definen Resonancia y la economía (F3a, *provisorio*). Lo que tiene el cliente se deduce en la mesa, no se muestra (Pilar 1, Open Questions).
8f. **Negociar la vuelta (D-57).** Se puede con cualquier cliente, pero solo cuando la vela no alcanza para su tirada esperada (R8) o para ninguna (E1). El cliente se va sin lectura y puede volver o no en la próxima jornada. La negociación no es gratis ni igual para todos: cambia la Paciencia, el enojo y otras métricas según el arquetipo, a veces a favor, a veces en contra y a veces sin efecto. El juego no lo explica; el jugador lo aprende jugando (§3.3). La negociación y sus efectos son de Fila y Mirilla y de Métricas del Cliente (*provisorio*); Tiradas solo fija cuándo se ofrece.

**Pregunta de sí o no (D-51)**

9. Cada tema de la Taxonomía tiene una **valencia**: favorable, desfavorable o ambigua.

   | Valencia | Temas |
   |---|---|
   | Favorable | amor, alegría, fortuna, éxito |
   | Desfavorable | culpa, duelo, deuda, traición, violencia, engaño, muerte, locura, enfermedad |
   | Ambigua | deseo, hogar, trabajo, ley, secreto, poder, rivalidad, fama, riesgo, cambio |

   El campo es de la Taxonomía, que lo incorporó en R1 (D-51).
10. Si la forma del motivo es *sí o no*, el Generador primero sortea la respuesta verdadera (sí o no, con una proporción fija `ρ`, en un sorteo independiente por cliente: nunca una bolsa o cuota que el jugador pueda contar). Después sortea el tema del desenlace entre los temas de esa valencia (sí = favorable, no = desfavorable) que son sorteables en el mazo activo (`p_t` > 0), con los pesos del mazo (Cartas F1) renormalizados dentro de ese conjunto. Un tema que el mazo solo tiene como forzada no es candidato (Cartas F1, E9); un mazo sin temas sorteables de una valencia es error de datos (`MAZO_SIN_VALENCIA`, Cartas). Un tema ambiguo nunca es el desenlace de una pregunta de sí o no. Esto es un contrato con el Generador.
11. En una pregunta de sí o no, el jugador afirma sí o no, con cualquier tirada. Compararlo con la respuesta verdadera, y castigar la contradicción con la palabra clave elegida, le corresponde a Interpretación y Resonancia. Tiradas solo garantiza que toda tirada que se ofrece tiene al menos una posición de desenlace, y las 5 la tienen.
11a. **Requisito a Resonancia (D-57).** Una palabra ambigua nunca es el desenlace de un sí o no (R10), así que elegirla da Match 0 seguro y nunca contradice. Para que no sea la jugada por defecto, Resonancia tiene que cumplir dos condiciones:
   - contradecirse cuesta al menos lo mismo que perder el Match por elegir una ambigua;
   - en la posición de desenlace de un sí o no, la ambigua nunca rinde más, en esperanza, que una palabra coherente con la afirmación del jugador.

   Los valores son de Resonancia. El prototipo mide la hipótesis de E8.

**Validación**

12. Las tiradas pasan por el validador del catálogo (R13 de la Taxonomía): `ROL_INEXISTENTE`, `FORMA_INEXISTENTE`, `POSICION_AMBIGUA` y `TIRADA_SIN_COMPARABLES`. Este GDD agrega tres reglas:
    - una vecindad nombra solo posiciones de su tirada;
    - toda tirada tiene al menos una posición de desenlace (R11);
    - la Carta Única cuesta menos que Tres Tiempos, y también la Carta Única más todas sus aclaratorias: `C_CU + n_acl · C_acl < C_TT`, con `n_acl` las aclaratorias por tirada (Tuning Knobs).

    Los códigos se fijan en las historias.

### States and Transitions

| Estado de una tirada en la partida | Significa | Pasa a |
|---|---|---|
| No disponible | Todavía no se desbloqueó (Dos Caminos, El Vínculo) o no se llegó a la sede (Cruz Celta) | Disponible, cuando se cumple su condición. Lo decide Fama, Reputación y Ascenso de Sede (D-56) |
| Disponible | Se ofrece si cumple R6 | No vuelve atrás durante la partida |

Durante la lectura de un cliente: **elegida → repartida → (aclarada, opcional, hasta `n_acl` veces) → leída**. Mientras está elegida se puede cambiar sin costo; el paso a repartida cobra la tirada (R5) y no tiene vuelta atrás (R5, R8c).

**Orden de la atención de un cliente** (*provisorio hasta Flujo de Jornada, Preguntas e Interpretación*):

1. El cliente se sienta y dice su motivo. El motivo queda visible hasta el final de la lectura.
2. Preguntas y tells, opcionales (5 UT cada pregunta, GDD §5.1). No hay preguntas después del reparto.
3. Si la vela no alcanza para la tirada esperada, se puede negociar que vuelva (R8f) y la atención termina acá.
4. Elegir la tirada, gratis y reversible (R5).
5. Confirmar el reparto: se revalida R6 y se cobra la tirada.
6. Por cada posición, en cualquier orden:
   1. aclaratoria, opcional (R8a): elegir la posición, que es reversible, y confirmar el pedido, que cobra;
   2. elegir la palabra clave;
   3. confirmar la lectura de la posición, que cierra la aclaratoria para esa posición (R8c).
7. En un sí o no, afirmar sí o no (R11).
8. Confirmar la lectura completa y pasar a Resonancia.

Los trucos de Prestidigitación (2 UT) se pueden hacer entre los pasos 5 y 7, sobre cartas ya repartidas.

### Interactions with Other Systems

| Sistema | Qué recibe de Tiradas | Qué aporta o devuelve |
|---|---|---|
| Taxonomía | Las posiciones con su rol o `libre`; la forma esperada | Roles, formas, validador y la valencia de cada tema (R1 de la Taxonomía) |
| Base de Datos de Cartas | Los `k` de las tiradas habilitadas, que la composición de la build pasa como `k_tiradas` (Cartas R12) | `acierto_posible`, solo para diseñar y calibrar (D-50), y las cifras de cobertura `P_pos⁺`, `P_pos⁺_v`, `P_cero_v(k)` (Cartas F3, F4) |
| Mazo y Robo | Cuántas cartas repartir y en qué orden, y la carta aclaratoria (R8a) | Las cartas, con su orientación |
| Reloj de Vela | El costo en UT de la tirada, al confirmar el reparto (R5), y el de la aclaratoria, al pedirla (R8a) | Las UT que quedan (R6) |
| Gramática | La vecindad de cada tirada | Nada; la usa para las dignidades |
| Interpretación y Sentencia | Las posiciones con su rol o libre y su nombre visible | La palabra clave elegida por posición; el sí o no del jugador |
| Resonancia | Si la tirada fue la esperada (R8), si no se ofreció por vela corta, y el precio `π` (R8e) | Nada; aplica `B_tirada` y el pago (R8e) |
| Fila y Mirilla | Cuándo se puede negociar que el cliente vuelva (R8f) | La negociación y sus efectos |
| Generador | Nada directo. Contrato de R10 para la pregunta de sí o no | La verdad por rol, y en sí o no también la respuesta verdadera |
| Prestidigitación | Las posiciones repartidas | Altera cartas ya repartidas; no cambia la tirada (R5) |
| Tapete y Tooltips | La forma visual, los nombres de las posiciones y el costo | Nada; los muestra |

**Interfaces provisorias:** de estos sistemas solo tienen GDD la Taxonomía y la Base de Datos de Cartas.

## Formulas

Las cuentas usan los datos de cobertura de Cartas (F3: `P_pos` ≈ 0,274 en Mayores + Copas). Son de calibración: el puntaje real y el umbral los define Resonancia. Ese `P_pos` sale del conteo de D-48, que no incluyó Waite III §4: las cifras son **pesimistas** hasta el reconteo (D-50). El reconteo no cambia los Mayores, que aportan la mayor parte de `P_pos`.

**Sin valencia.** Las cifras de F2, F3 y F5 usan el `P_pos` de todo el mazo. En la forma esperada de la Carta Única (sí o no) el desenlace sale solo de los temas de una valencia (R10, F4), así que para la Carta Única son referencias, no la cifra del juego. Las cifras con valencia (`P_pos⁺_v`, `P_cero_v`, Cartas F4) las necesita el prototipo y salen del reconteo (D-50, D-54), en `design/balance/cifras-cartas.md`; hasta tenerlas, ninguna conclusión de diseño se apoya en las cifras de la Carta Única de esta sección.

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
- **Con `k` = 1 la mayoría de las tiradas no tiene ningún acierto posible** (sin valencia, 72,6 %). Por eso Resonancia no puede usar un umbral fijo: tiene que medir en proporción a `k` (Open Questions).
- **Independencia:** es razonable aunque se repitan roles (Cruz Celta, Dos Caminos). Contando que dos posiciones del mismo rol comparten la verdad, la probabilidad de fallar en las dos da 0,529, contra 0,527 si fueran independientes (`P_cero_corr(2)`, Copas, `design/balance/cifras-cartas.md`). Repetir un rol sí aumenta la varianza: acertar el conflicto paga dos veces y errarlo cuesta dos veces.

**F3. Rendimiento por UT** (calibración)

`E_Match = k · s · (P_pos⁺ + P_exacto)` · `η = E_Match / C`

**Inclusión:** todo acierto exacto posible es también acierto de familia posible, así que `P_exacto ≤ P_pos⁺`, y Match 2/1/0 da `2·P_exacto + 1·(P_pos⁺ − P_exacto) = P_pos⁺ + P_exacto`. Las dos cifras se miden sobre la misma base, claras y forzadas (`n_t⁺`, Cartas F3). Con los datos contados solo existe `P_pos` (solo claras, 0,274), que se usa como cota inferior de `P_pos⁺`.

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `P_pos⁺` | float | 0 a 1 | Cartas F3 (hoy aproximada por `P_pos` = 0,274) | Probabilidad de acierto de familia posible en una posición, claras y forzadas |
| `P_exacto` | float | 0 a `P_pos⁺` | Cartas F3 (hipótesis: 0,09) | Probabilidad de acierto exacto posible en una posición, sobre la misma base |
| `s` | float | 0 a 1 | prototipo | Qué tan seguido el jugador elige la palabra correcta cuando hay acierto posible (1 = juego perfecto) |
| `C` | int | 5 a 45 | R1, Tuning Knobs | Costo de la tirada en UT (el validador exige `C ≥ 1`) |
| `η` | float | ≥ 0 | calculated | Match esperado (2/1/0, ilustrativo) por UT |

- **Con s = 1:** Carta Única 0,036 · Tres Tiempos 0,055 · Dos Caminos 0,061 · El Vínculo 0,049 · Cruz Celta 0,049. No incluye dignidades ni el bono de tirada. Dos Caminos y El Vínculo usan el `k` con todos los roles, que no existe en el MVP (F1).
- **Lectura:** mide Match por UT, no dinero por UT; el dinero es F3a. Solo cuenta el costo de la tirada; con las preguntas del cliente (unos 10 UT con 2 preguntas) el orden cambia, porque ese costo fijo pesa más en la Carta Única. La Cruz Celta rinde menos Match por UT que Tres Tiempos; lo compensa su precio (R1, R8e), *provisorio* (R3a).
- `P_exacto` es una hipótesis; se reemplaza por el informe del validador (Cartas R11).

**F3a. Pago de la lectura** (*provisorio*, D-57; la fórmula final es de Resonancia y la economía)

`Pago = min(T · π · R_cliente, B_cliente)`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `T` | float | > 0 | `economia-mvp.md` | Tarifa del cliente (sede × estatus) |
| `π` | float | ≥ 1 | R1 | Precio de la tirada: ×1 / ×1,5 / ×2 / ×2 / ×3 |
| `R_cliente` | float | ≥ 0 | Resonancia | Cómo quedó el cliente: 0 si se enojó, alrededor de 1 si quedó satisfecho, más si quedó emocionado |
| `B_cliente` | float | ≥ 0 | Arquetipos, Generador | Lo que el cliente tiene para pagar |
| `Pago` | float | 0 a `B_cliente` | calculated | Lo que cobra el tarotista |

- **Ejemplo:** con `T` = 4 y el cliente satisfecho (`R_cliente` = 1), Tres Tiempos vale 6 y la Carta Única 4. Si el cliente solo tiene 5, Tres Tiempos cobra 5. Si se enojó, ninguna cobra.
- **Por qué:** con tarifa plana, la Carta Única rinde más dinero por UT que Tres Tiempos, y elegir tirada no sería una decisión (revisión del 2026-10-25). Con `π`, una tirada grande vale la pena con un cliente que puede pagarla y no con uno pobre.
- **Hipótesis del prototipo:** con motivo de situación general y el perfil medio, Tres Tiempos rinde al menos lo mismo que la Carta Única en `Pago / (C + preguntas)`. Métrica de descarte en Open Questions.
- Reemplaza la tarifa plana de `economia-mvp.md` §1; la economía y su script se recalibran (D-57, pendiente).

**F4. Acertar el sí o no**

`P_acierto_sn = max(ρ, 1 − ρ) + Δ_deducción`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `ρ` | float | 0 a 1; vale 0,5 | data file (Generador) | Proporción de respuestas verdaderas "sí" (Tuning Knobs) |
| `Δ_deducción` | float | 0 a 1 − max(ρ, 1 − ρ) | Detección | Lo que suma deducir al cliente (tells, preguntas) |
| `P_acierto_sn` | float | max(ρ, 1 − ρ) a 1 | calculated | Probabilidad de que el jugador afirme la respuesta verdadera. `max(ρ, 1 − ρ)` es contestar siempre lo más frecuente; con ρ = 0,5 da `0,5 + Δ_deducción` |

- **La carta no informa:** como el reparto es independiente de la verdad (R7, D-37), P(sí | carta favorable) = `ρ`. Toda la información del sí o no sale del cliente (Pilar 1).
- **Por qué `ρ` = 0,5:** con cualquier otro valor, contestar siempre lo mismo da más del 50 %.
- **La carta restringe:** si el jugador cree "sí" y la Respuesta solo tiene palabras desfavorables, puede elegir una palabra ambigua (Match 0 seguro, porque una ambigua nunca es desenlace de un sí o no) o contradecirse. Cómo se castiga la contradicción lo define Resonancia.
- **El lado "sí" tiene menos cobertura:** su verdad sale de 4 temas, que la tradición usa poco. `P_pos` del desenlace en un sí o no se calcula con los pesos renormalizados dentro de la valencia. Está en el informe de Cartas (`P_pos⁺_v`, Cartas F3; `P_cero_v(k)`, Cartas F4; D-53), y un mazo sin temas sorteables de una valencia es error de datos (`MAZO_SIN_VALENCIA`). La mezcla con `ρ` es `ρ·(1 − P_pos⁺_favorable) + (1 − ρ)·(1 − P_pos⁺_desfavorable)` en la Carta Única.

**F5. Acierto posible con carta aclaratoria**

`P_alguno_acl(k) = 1 − (1 − P_pos)^(k + 1)`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `k` | int | 1 a 6 | F1 | Posiciones comparables |
| `P_alguno_acl` | float | 0 a 1 | calculated | Probabilidad de al menos un acierto posible con una aclaratoria en una posición comparable |

- Como es ciega, una aclaratoria equivale a una carta más en una posición: sin valencia y con el conteo de Cartas previo a §4 (`design/balance/cifras-cartas.md`), la Carta Única pasa de 0,274 a **0,473** por 15 UT, y Tres Tiempos de 0,617 a **0,722** por 25 UT.
- Si el jugador la pide en una posición libre, no suma acierto: la fórmula es una cota superior.

## Edge Cases

1. **A la vela no le alcanza para ninguna tirada.** No se ofrece ninguna (R6) y el cliente no se puede leer. El jugador puede negociar que vuelva la próxima jornada (R8f) o dejarlo ir; qué le pasa a ese cliente en cada caso lo define Fila y Mirilla (*provisorio*). Las UT que sobran al final de la jornada se pierden: no pasan a la siguiente, y es intencional (Pilar 5).
   **Advertencia:** si una acción (una pregunta, un truco) va a dejar la vela por debajo del costo de la tirada más barata que se ofrece en ese momento, el juego avisa antes. La acción igual se puede hacer. El umbral es siempre la más barata, no la esperada, para no marcar la tirada esperada (UI Requirements). Si ya no se ofrece ninguna tirada, no hay advertencia. Una acción que cuesta más de lo que queda en la vela no se puede hacer (contrato con Reloj de Vela).
2. **No se ofrece ninguna tirada por otra causa.** En el MVP no puede pasar: la Carta Única está disponible desde el inicio y su rol (desenlace) siempre está habilitado. Si pasara, se trata igual que el caso 1.
3. **Una forma de pregunta cuya tirada esperada no es ofrecible.** El Generador solo emite formas habilitadas cuya tirada esperada sea **ofrecible por catálogo**: disponible en la partida y con todos sus roles habilitados (R6, primeras dos condiciones). No mira la vela, que el Generador no conoce; la vela corta la trata R8. Así el bono de tirada siempre se puede alcanzar con vela suficiente. Esto es un contrato con el Generador (D-51). En el MVP no cambia nada, porque *sí o no* y *situación general* tienen sus tiradas desde el inicio.
4. **El jugador usa otra tirada que la esperada.** Está permitido, sin bono de tirada y con la baja de Credulidad de R8, salvo que la justifique o que la esperada no se ofrezca por vela corta (R8: entonces no baja la Credulidad). Si el motivo es de sí o no y usa Tres Tiempos, igual afirma sí o no (R11) y se comparan las 3 posiciones.
5. **Una posición pregunta un rol que la situación no tiene.** Da SIN_COMPARACION (E3 de la Taxonomía). En el MVP no se ofrecen las tiradas con roles deshabilitados (R3).
6. **Prestidigitación cambia o invierte una carta ya repartida.** La posición y su rol no cambian: se compara la carta nueva, en su orientación nueva.
7. **Dos posiciones con el mismo rol** (Cruz Celta, Dos Caminos). Cada una da su propio resultado contra la misma verdad. Cómo se combinan lo define Resonancia (E4 de la Taxonomía).
8. **En un sí o no, la Respuesta solo tiene palabras ambiguas o de la valencia contraria a lo que cree el jugador.** No hay forma de afirmar sin contradecirse o sin aceptar un Match 0 (F4). Es intencional: la carta condiciona y el estafador tiene que venderla igual. **Hipótesis del prototipo:** el refugio en la ambigua no es la jugada por defecto si Resonancia cumple R11a. Se mide la proporción de Cartas Únicas de sí o no resueltas con una palabra ambigua (Open Questions).
9. **El jugador pide la aclaratoria en una posición libre.** Está permitido (R8b): si se prohibiera, la oferta diría qué posiciones cuentan, cosa que el nombre de la posición ya deja ver. Es intencional: el nombre tradicional de la posición revela si es libre o comparable, y el rol nunca se muestra. No suma acierto (F5).

## Dependencies

**Depende de:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Taxonomía de Temas y Roles | Dura | Roles, formas de pregunta, posiciones libres, el validador (R8–R13) y la valencia de cada tema (R1) |
| Mazo y Robo | Dura, *provisoria* | Reparte una carta por posición con orientación al azar (R7) |
| Base de Datos de Cartas | Dura | `acierto_posible` (Cartas R12), solo para diseñar y calibrar la aclaratoria, nunca en juego (D-50); `P_pos⁺_v` y `P_cero_v(k)` para el sí o no (Cartas F3, F4). La composición de la build pasa los `k` de las tiradas habilitadas al informe de Cartas como argumento (`k_tiradas`, Cartas R12, D-53); Cartas no lee este catálogo |
| Reloj de Vela | Dura, *provisoria* | Las UT que quedan, para saber qué tiradas se ofrecen (R6) y para la advertencia de E1 |

**Dependen de Tiradas:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Gramática de Combinación | Dura | La vecindad de cada tirada (R4) |
| Interpretación y Sentencia | Dura | Las posiciones, con su rol o libre y su nombre visible |
| Resonancia y Resolución | Dura | El rol de cada posición, `k` (F1) y si la tirada fue la esperada (R8) |
| Prestidigitación | Dura | Las posiciones repartidas sobre las que actúa un truco |
| Tapete y Tooltips de Cartas | Dura | La forma visual, los nombres de las posiciones y el costo |
| Generador de Situaciones | Blanda | Qué tiradas están disponibles, para emitir solo formas alcanzables (E3), y el contrato del sí o no (R10) |
| Fila y Mirilla | Blanda, *provisoria* | Cuándo se puede negociar que el cliente vuelva (R8f) y el cliente sin tirada (E1) |
| Fama, Reputación y Ascenso de Sede | Blanda, *provisoria* | Decide cuándo pasan a disponibles Dos Caminos, El Vínculo y Cruz Celta (States, D-56). Tiradas solo guarda el estado de disponibilidad que Fama le fija |

**Bidireccionalidad:**

- La Taxonomía ya nombra a Tiradas entre sus dependientes e incorporó la valencia (su R1).
- Los demás no tienen GDD; cada uno tiene que nombrar a Tiradas cuando se escriba.
- `systems-index.md` ya lista Reloj de Vela entre las dependencias de Tiradas, y Tiradas entre las del Generador.

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Costo en UT por tirada | Carta Única 10 · Tres Tiempos 20 · Dos Caminos 30 · El Vínculo 30 · Cruz Celta 45 (D-14) | Carta Única de 5 a 15 y Tres Tiempos de 15 a 30, siempre con `C_CU + n_acl · C_acl < C_TT`. La condición es regla del validador (R12) y manda sobre los rangos. Dos Caminos, El Vínculo y Cruz Celta, a recalibrar con el precio (R3a). Con 2 preguntas por cliente (5 UT cada una, GDD §5.1; las 2 son un supuesto de `tools/balance/economia_mvp.py` PERFILES, donde el experto hace 3), un cliente cuesta como mínimo 20 UT con Carta Única y 30 con Tres Tiempos: 5 clientes, o 3 con 10 UT sobrantes, por vela de 100 UT; 4 y 2 con una aclaratoria | Clientes por jornada y rendimiento por UT (F3) |
| Precio por tirada (`π`) | Carta Única ×1 · Tres Tiempos ×1,5 · Dos Caminos ×2 · El Vínculo ×2 · Cruz Celta ×3 (D-57, *provisorio*) | ×1 a ×4, creciente con la complejidad de la tirada. Lo calibra el prototipo con la hipótesis de F3a | Cuánto vale desplegar el paño con un cliente que puede pagarlo (F3a) |
| Disponibilidad de Dos Caminos y El Vínculo | desbloqueables, condición a definir | La define Fama, Reputación y Ascenso de Sede (D-56) | Cuándo se amplía el repertorio |
| Sede mínima de la Cruz Celta | "sedes altas", a definir | Sede 4 a 8 en el Mapa B (fuera del MVP, que va de la Sede 1 a la 3) | Cuándo aparecen los asuntos graves |
| Proporción de "sí" (`ρ`) | 0,5 | Solo 0,5: con cualquier otro valor, contestar siempre lo mismo conviene (F4). Es del Generador; está acá como referencia | Que el sí o no se deduzca del cliente y no se adivine |
| Costo de la carta aclaratoria | 5 UT | 3 a 9, siempre con `C_CU + n_acl · C_acl < C_TT` (regla del validador, R12) | Cuánto cuesta rescatar una carta muda (F5) |
| Aclaratorias por tirada | 1 | 1 a 2, siempre con `C_CU + n_acl · C_acl < C_TT` (con 2 y 5 UT, Tres Tiempos tiene que costar más de 20). Las cifras de Cartas F4 suponen 1; con 2 se recalculan | Cuánta palanca del Pilar 6 hay por cliente |

El bono por tirada esperada no está acá: lo define Resonancia (R8). El umbral de la advertencia de E1 tampoco es perilla, porque sale del costo de la tirada más barata que se ofrece.

## Visual/Audio Requirements

- Cada tirada se dibuja en el tapete con su disposición tradicional: Tres Tiempos en línea, Dos Caminos como una horquilla, El Vínculo como un rombo con el Desenlace al centro, y la Cruz Celta con la cruz y la columna de Waite (1910, Parte III §7).
- Las posiciones vecinas (R4) se ven juntas. Ninguna disposición pone pegadas dos posiciones que no son vecinas, para que la Gramática no contradiga lo que el jugador ve.
- El nombre de cada posición se ve en el tapete; el rol, nunca (UI Requirements de la Taxonomía).
- No hay sonido propio de este sistema; el sonido de repartir es de Mazo y Robo y del Tapete.

## Game Feel

Elegir la tirada es un compromiso: una vez repartida no se cambia (R5). El momento de elegir tiene que sentirse como una decisión sobre el cliente, no como un menú. El reparto en sí (animación, ritmo) es del Tapete. Tiene que ser breve, porque la vela ya pagó la tirada y el tiempo real solo corre en los tells (D-28).

## UI Requirements

- El selector de tiradas muestra, para cada tirada: nombre, cantidad de cartas, forma en el tapete, costo en UT y precio (`π`).
- **Estado de cada tirada en el selector:**

  | Estado lógico | Se muestra | Motivo visible |
  |---|---|---|
  | No disponible (States) | No | — |
  | Disponible, con algún rol deshabilitado (R6, condición 2) | No | — (en el MVP no ocurre) |
  | Disponible y con roles, sin vela suficiente (R6, condición 3) | Deshabilitada | "falta vela", con texto o ícono además del color |
  | Ofrecida | Activa | — |

  Si no se ofrece ninguna tirada, el selector se muestra igual, con todo deshabilitado, y siempre hay una salida: negociar la vuelta (R8f) o dejar ir al cliente.
- **Aclaratoria:** el botón muestra su costo y se ve igual en todas las posiciones (con rol o libres) y con cualquier carta (R8b). Si no se puede pedir, se ve deshabilitado con el motivo ("falta vela", "ya la usaste", "posición ya leída"). Elegir la posición y confirmar el pedido son dos acciones distintas (R8a).
- **Nada en la presentación depende del rol** de la posición, ni de si una carta tiene acierto posible: ni marco, ni color, ni orden, ni sonido.
- **Negociar la vuelta (R8f):** la opción no puede delatar cuál es la tirada esperada (Open Questions).
- **La tirada esperada no se marca.** El motivo del cliente se dice en su texto ("¿me va a llamar, sí o no?"), y reconocer qué tirada pide es parte de leerlo (§3.3: lo aprendido no lo explica el juego).
- La advertencia de E1 aparece antes de confirmar la acción que deja la vela sin tirada posible.

> 📌 **UX Flag — Tiradas:** antes de las historias del selector y del tapete hay que hacer su spec con `/ux-design`. Incluye: la disposición de la Cruz Celta en Switch portátil; la advertencia de la vela (alcance y frecuencia); la aclaratoria junto a su posición y la elección de palabra entre dos cartas; el control de sí o no; la diferencia entre elegir y confirmar con gamepad; el selector sin tiradas ofrecidas; y que el motivo del cliente quede visible al elegir. Los AC de UI (AC-20b, el selector y el tapete) se escriben ahí.

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
| D-53, D-54, D-55 | Interfaz `k_tiradas` y umbral de impuesto de la aclaratoria; cifras con valencia para el prototipo; cobro al confirmar, Dos Caminos con desenlace, Credulidad y costos |
| D-56, D-57 | Desbloqueo en Fama y sí o no sobre temas sorteables; precio por tirada, pago limitado por el cliente, vela corta, negociar la vuelta y requisito del sí o no a Resonancia |
| Taxonomía R8–R13, E3, E4 | Roles, posiciones libres, formas, validador; rol ausente; roles repetidos |
| Cartas F1, F3, R11 | Pesos de la verdad; `P_pos`; informe de cobertura |

## Acceptance Criteria

Convenciones de prueba:
- Todo AC parte de `fixture_tiradas_valido` y lo muta en un solo punto. AC-01 prueba que el fixture sin mutar pasa limpio. Contenido mínimo del fixture: Carta Única y Tres Tiempos con las posiciones, roles y vecindades de R2 y R4; costos 10 y 20 UT; aclaratoria a 5 UT con `n_acl` = 1; las dos disponibles; roles origen, conflicto y desenlace habilitados. El archivo y los fixtures derivados (`tirada_vecina`, `tirada_sin_desenlace`) los fija la historia.
- **Rechazo observable:** cuando un AC dice "se rechaza", significa: la operación devuelve error, la vela no cambia, no se piden cartas al mazo y el estado de la tirada no cambia.
- Cada error se verifica por la regla de la que es (con el código que fije la historia) y por su sujeto en formato R13 de la Taxonomía. Los controles dicen "no contiene error de la regla X con sujeto S", nunca "no hay errores".
- El RNG y el reparto se simulan; ningún test depende del azar.
- `ROL_INEXISTENTE`, `FORMA_INEXISTENTE`, `POSICION_AMBIGUA` y `TIRADA_SIN_COMPARABLES` ya los prueban AC-31, AC-33, AC-37a/b y AC-38 de la Taxonomía, y SIN_COMPARACION su E3. No se repiten acá.
- **Evidencia:** todos son Logic (test unitario en `[test root]/tiradas/`), salvo los marcados Integration, UI o Config/Data. Un AC *provisorio* depende de un GDD que todavía no existe: no se convierte en historia hasta que ese GDD exista y confirme el AC; desde ahí bloquea como cualquier otro.
- **Dependencias provisorias:** los AC que usan la vela (AC-06, 19, 20a, 24, 26, 29) son *provisorios hasta Reloj de Vela*; los que reparten (AC-12, 13, 24) *hasta Mazo y Robo*; el bono y el resultado único (AC-14, 24) *hasta Resonancia*; el estado "leída" (AC-11, 26) *hasta Interpretación*.
- **Sin AC, a propósito:** F2, F3, F3a y F5 son de calibración y ningún código del juego las calcula. La suma de deducción de F4 es de Detección. E5 lo cubre la Taxonomía (E3) y AC-08. La combinación de E7 es de Resonancia. E8 es una hipótesis del prototipo (Open Questions): se registra en el informe del prototipo con su métrica. R8f (negociar la vuelta) es de Fila y Mirilla; acá solo se prueba cuándo se ofrece (AC-30).

**Catálogo**
- **AC-01** (R1–R12) — GIVEN `fixture_tiradas_valido`, WHEN se valida, THEN la lista está vacía.
- **AC-02** (R1, R2) — GIVEN el catálogo real, WHEN se carga, THEN hay 5 tiradas con los ids de R1, con 1/3/5/5/10 posiciones, costos 10/20/30/30/45, precios ×1/×1,5/×2/×2/×3 y la forma esperada de R1, y cada posición tiene exactamente el rol o `libre` de la tabla de R2.
- **AC-03** (R4) — GIVEN el catálogo real, WHEN se cargan las vecindades, THEN son exactamente estas, y simétricas:
  - Carta Única: ninguna.
  - Tres Tiempos: Pasado–Presente y Presente–Futuro (Pasado y Futuro no son vecinas).
  - Dos Caminos: Situación–Camino A, Situación–Camino B, Camino A–Resultado A y Camino B–Resultado B.
  - El Vínculo: Desenlace con las otras 4; Consultante y El Otro, cada uno con Lo que une y con Lo que separa.
  - Cruz Celta: 1–2, 1 y 2 con cada una de 3 a 6, 7–8, 8–9 y 9–10.
- **AC-04** (R12) — GIVEN `tirada_vecina` con la vecindad `p1–p9`, donde `p9` no es una posición suya, WHEN se valida, THEN contiene error de vecindad con sujeto `tirada_vecina/p9`. Control: con `p1–p2`, no lo contiene.
- **AC-05** (R11, R12) — GIVEN `tirada_sin_desenlace`, con una posición de rol `rol.origen` y ninguna de rol desenlace (para que no salte `TIRADA_SIN_COMPARABLES`), WHEN se valida, THEN contiene error de desenlace con sujeto `tirada_sin_desenlace`. Control: con una posición de desenlace, no lo contiene.

**Oferta**
- **AC-06** (R6, E1) — GIVEN Carta Única y Tres Tiempos disponibles, WHEN se piden las tiradas ofrecidas, THEN: con 20 UT, las dos; con 19, solo Carta Única; con 10, solo Carta Única; con 9, ninguna, y el cliente queda marcado como "no se puede leer".
- **AC-07** (E2) — GIVEN un catálogo de prueba donde ninguna tirada está disponible y 100 UT, WHEN se piden las tiradas ofrecidas, THEN no se ofrece ninguna y el cliente lleva la misma marca que en AC-06. Control: con solo la Carta Única disponible, se ofrece la Carta Única.
- **AC-08** (R3, R6) — GIVEN Dos Caminos disponible, `rol.camino_b` deshabilitado y 100 UT, WHEN se piden las tiradas ofrecidas, THEN Dos Caminos no está. Lo mismo con El Vínculo y `rol.el_otro`. Control: con el rol habilitado, se ofrece.
- **AC-09** (R6, States) — GIVEN Cruz Celta no disponible y 100 UT, WHEN se piden las tiradas ofrecidas, THEN no está. Control: disponible, se ofrece.
- **AC-10** (States; *provisorio hasta el GDD de Fama, Reputación y Ascenso*) — GIVEN una tirada Disponible, WHEN cambia la jornada y cambia la sede, THEN sigue Disponible.

**Lectura**
- **AC-11a** (R5, States) — GIVEN una tirada elegida y 30 UT, WHEN se elige otra antes de repartir, THEN queda la nueva y la vela sigue en 30.
- **AC-11b** (R5, States) — GIVEN una tirada repartida, y en otro caso leída, WHEN se elige otra, THEN se rechaza (rechazo observable).
- **AC-11c** (R5) — GIVEN una tirada repartida, WHEN se pide un segundo reparto para el mismo cliente, con la misma tirada o con otra, THEN se rechaza (rechazo observable). Control: el cliente siguiente puede elegir cualquier tirada que se ofrezca.
- **AC-12** (R7) — GIVEN Tres Tiempos y un reparto simulado que devuelve (A, derecha), (B, invertida) y (C, derecha), WHEN se reparte, THEN se piden exactamente 3 cartas y quedan Pasado = A derecha, Presente = B invertida, Futuro = C derecha.
- **AC-13** (R7, D-37, F4) — GIVEN una situación con un doble de la verdad que falla si se lo lee, y la misma secuencia del RNG, WHEN se reparte cada una de las 5 tiradas, THEN el reparto termina sin leer la verdad. Control: con la verdad "sí" en una corrida y "no" en otra, las cartas y orientaciones de cada tirada son idénticas.
- **AC-14** (R8, E4) — GIVEN cada una de las 5 formas, WHEN se elige cada tirada, THEN solo la tirada esperada de R1 activa el bono. Con `forma.si_o_no` y Tres Tiempos no hay bono, y las 3 posiciones se comparan igual.

**Sí o no**
- **AC-15** (R9) — La valencia de cada tema la prueban AC-35d y AC-35e de la Taxonomía; no se repite acá.
- **AC-16** (R10, Tuning Knobs; *provisorio hasta el Generador*) — GIVEN un fixture con `ρ` = 1, WHEN se sortea la respuesta, THEN siempre sale sí; con `ρ` = 0, siempre no. En los datos reales, `ρ` = 0,5 (Config/Data).
- **AC-17a** (R10; *provisorio hasta el Generador*) — GIVEN una pregunta de sí o no y un mazo de fixture donde `tema.culpa` aparece solo como forzada (`p_t` = 0), los otros 12 temas con valencia tienen `p_t` > 0 y algunos ambiguos también, WHEN se arman los candidatos al desenlace, THEN para sí son exactamente los 4 favorables y para no los 8 desfavorables sin `tema.culpa`; ningún tema ambiguo está entre los candidatos. Control: con `tema.culpa` como clara, está entre los 9 de no.
- **AC-17b** (R10; *provisorio hasta el Generador*) — GIVEN los favorables con `p_t` crudos 0,05 / 0,10 / 0,15 / 0,20 (amor, alegría, fortuna, éxito), WHEN se renormalizan para sí, THEN quedan 0,10 / 0,20 / 0,30 / 0,40, con tolerancia 1e-9.
- **AC-17c** (R10, Cartas `MAZO_SIN_VALENCIA`) — GIVEN un mazo de fixture sin ningún tema favorable sorteable, WHEN se valida, THEN contiene `MAZO_SIN_VALENCIA` con el mazo como sujeto. Control: con un favorable sorteable, no lo contiene.
- **AC-18** (E3; *provisorio hasta el Generador*) — GIVEN Dos Caminos no disponible, WHEN se arman las formas que el Generador puede emitir, THEN no incluyen `forma.dilema`. Lo mismo con Dos Caminos disponible y `rol.camino_a` deshabilitado. Control: con Dos Caminos disponible, `forma.dilema`, `rol.camino_a` y `rol.camino_b` habilitados y 0 UT en la vela, la incluyen (la vela no cuenta).

**Advertencia de la vela**
- **AC-19** (E1) — GIVEN 14 UT, una acción de 5 UT y 10 UT como costo de la tirada más barata que se ofrece, WHEN se evalúa la acción, THEN corresponde avisar; con 15 UT, no. Después del aviso, la acción se ejecuta igual.
- **AC-20a** (E1) — GIVEN la vela en 14 UT y un espía que registra eventos, WHEN el jugador elige una pregunta de 5 UT, THEN el evento de advertencia se registra antes que el de descuento. Con 15 UT, no hay evento de advertencia. Con 9 UT y ninguna tirada ofrecida, tampoco.
- **AC-20b** (E1; UI) — Se escribe en `/ux-design` (UX Flag): captura retenida en `production/qa/evidence/` con la advertencia a 14 UT, y otra sin advertencia a 15 UT.

**Otros sistemas**
- **AC-21** (E6; Integration, *provisorio hasta Prestidigitación*) — GIVEN un truco que cambia la carta del Presente, WHEN se compara, THEN la posición sigue con rol conflicto y se compara la carta nueva. Si el truco la invierte, se compara la orientación nueva.
- **AC-22** (F1) — GIVEN todos los roles habilitados y presentes, WHEN se calcula `k`, THEN da 1/3/5/4/6 para Carta Única, Tres Tiempos, Dos Caminos, El Vínculo y Cruz Celta (en Cruz Celta, posiciones 1, 2, 4, 5, 6 y 10). Con los roles del MVP, Dos Caminos da 3 (Situación, Resultado A y Resultado B) y El Vínculo 3 (prueban la fórmula: en el MVP esas tiradas no se ofrecen). Con una situación de prueba construida a mano sin `rol.origen` (el Generador no la produce: es el caso de una partida guardada, Taxonomía E9), Tres Tiempos da 2.
- **AC-23** (R12, Tuning Knobs) — GIVEN `fixture_tiradas_valido` con la aclaratoria a 1 UT, 1 aclaratoria por tirada, la Carta Única a 20 UT y Tres Tiempos a 20 UT, WHEN se valida, THEN contiene error de costos con sujeto `tirada.carta_unica`. Lo mismo con la Carta Única a 25. Control: con 18 (18 + 1 = 19 < 20), no lo contiene.
- **AC-24** (R8a) — GIVEN Tres Tiempos repartida y 10 UT, WHEN se pide una aclaratoria para Presente, THEN se reparte 1 carta más junto a Presente y se descuentan 5 UT; las palabras clave elegibles para Presente son las de las dos cartas, y Presente da un solo resultado.
- **AC-25** (R8b) — GIVEN Tres Tiempos repartida con una carta sin acierto posible en Presente y cartas con acierto posible en Pasado y Futuro, en dos situaciones con verdades distintas, WHEN se piden las posiciones donde se ofrece la aclaratoria, THEN en las dos son exactamente [Pasado, Presente, Futuro]. Lo mismo en la Carta Única, con la Respuesta con y sin acierto posible.
- **AC-26a** (R8c) — GIVEN Tres Tiempos repartida y ninguna aclaratoria pedida, WHEN se piden las posiciones donde se ofrece, THEN con 5 UT se ofrece y con 4 no.
- **AC-26b** (R8c) — GIVEN `n_acl` = 1 y una aclaratoria ya pedida en la tirada, WHEN se pide otra, THEN se rechaza (rechazo observable). Con `n_acl` = 2, la segunda se acepta y la tercera se rechaza.
- **AC-26c** (R8c, States) — GIVEN Tres Tiempos repartida, ninguna aclaratoria pedida y la lectura de Presente confirmada, WHEN se piden las posiciones donde se ofrece, THEN son exactamente [Pasado, Futuro].
- **AC-26d** (R8a) — GIVEN Tres Tiempos repartida y 10 UT, WHEN se elige Presente para la aclaratoria y se cancela antes de confirmar, THEN la vela sigue en 10, no se pidió carta y la aclaratoria sigue disponible.
- **AC-27** (R12, Tuning Knobs) — GIVEN la aclaratoria a 10 UT, 1 aclaratoria por tirada, con Carta Única a 10 y Tres Tiempos a 20, WHEN se valida, THEN contiene error de costos con sujeto `tirada.carta_unica`. Con 9, no lo contiene. Con la aclaratoria a 5 y 2 aclaratorias por tirada (10 + 2 · 5 = 20), lo contiene; con Tres Tiempos a 21, no.
- **AC-28** (R8b, D-50) — GIVEN cartas cuyo `acierto_posible` falla al leerse, por cualquier vía, y un acceso a la verdad que falla si se lo lee, WHEN se arma la oferta de aclaratoria de Tres Tiempos, THEN se arma sin fallar y es exactamente [Pasado, Presente, Futuro].
- **AC-29** (R5, R6) — GIVEN 30 UT, WHEN se elige la Carta Única, se cambia a Tres Tiempos y se confirma el reparto, THEN la vela queda en 10 (se descontaron 20, una vez). Elegir sin confirmar no descuenta nada. Si la vela baja a 15 entre la elección de Tres Tiempos y la confirmación, el reparto se rechaza y la vela sigue en 15.
- **AC-30** (R8, R8f, E1; *provisorio hasta Reloj de Vela y Fila y Mirilla*) — GIVEN un cliente con `forma.situacion_general`, WHEN se pregunta si se puede negociar la vuelta, THEN con 15 UT sí (Tres Tiempos no se ofrece), con 9 UT sí (no se ofrece ninguna) y con 20 UT no. Con `forma.si_o_no`, a 15 UT no (la Carta Única se ofrece).
- **AC-31** (R8; *provisorio hasta Resonancia*) — GIVEN `forma.situacion_general` y 15 UT, WHEN se lee con la Carta Única, THEN la lectura no lleva bono de tirada ni marca de baja de Credulidad. Control: con 30 UT y la Carta Única, lleva la marca de baja.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| **Requisito de F2:** Resonancia mide en proporción a las posiciones comparables (`k`), no con un umbral fijo; si no, la Carta Única queda casi imposible de aprobar (72,6 % sin acierto posible). ¿El sí o no del jugador cuenta como un acierto propio? | GDD de Resonancia | Al diseñar Resonancia |
| Cuánto vale `B_tirada` y cómo pesa justificar otra tirada (§5.4). ¿Las posiciones libres pueden contradecir? | GDD de Resonancia | Al diseñar Resonancia |
| Contratos de R10 y E3: el sorteo del sí o no (`ρ` = 0,5, desenlace dentro de la valencia) y las formas solo con tirada disponible | GDD del Generador | Al diseñar el Generador |
| Qué desbloquea Dos Caminos y El Vínculo, y desde qué sede aparece la Cruz Celta | GDD de Fama, Reputación y Ascenso de Sede (D-56) | Antes del Vertical Slice |
| Negociar la vuelta (R8f): si el cliente vuelve, cuánto cambian Paciencia, enojo y otras métricas por arquetipo, y qué pasa con el cliente que se deja ir sin negociar (E1) | GDD de Fila y Mirilla, Métricas del Cliente | Al diseñar Fila y Mirilla |
| **Fuga de información de R8f:** como la negociación se habilita cuando la vela no alcanza para la tirada esperada, que aparezca la opción delata cuál es la esperada (con 15 UT aparece en situación general y no en sí o no). ¿Se acepta, se habilita siempre que alguna tirada disponible no alcance, o se esconde de otra forma? | Diseñador, `/ux-design` | Antes de las historias del selector |
| ¿El estatus del cliente (§5.4, "lo que puede pagar") limita qué tiradas se le ofrecen? | GDD de Arquetipos, economía | Al diseñar Arquetipos |
| **Hipótesis del prototipo (D-57):** con precio por tirada (`π`) y pago limitado por el cliente (F3a), elegir tirada deja de ser solo reconocer la forma. Valores iniciales: `π` de R1, `B_tirada` ×1,1 sobre el pago, baja de Credulidad de 10 puntos. **Métrica de descarte:** si más del 80 % de los clientes de situación general con vela suficiente se leen con la Carta Única, o más del 95 % de todos los clientes con su tirada esperada sin mirar al cliente, la hipótesis cae | Diseñador | Prototipo del núcleo |
| Recalibrar `economia-mvp.md` y `tools/balance/economia_mvp.py` con el precio por tirada y el pago limitado (F3a): hoy suponen tarifa plana, no modelan aclaratoria, trucos ni elección según la forma, descartan las UT entre 10 y 19 y no bajan a Carta Única cuando no alcanza para Tres Tiempos | Diseñador, economía | Antes de cerrar la economía del MVP |
| Cómo se deduce lo que tiene el cliente (`B_cliente`, F3a): ropa, arquetipo, tells | GDD de Arquetipos, Detección | Al diseñar Arquetipos |
| E8 y R11a: proporción de Cartas Únicas de sí o no resueltas con una palabra ambigua. Si pasa del 50 %, el refugio en la ambigua es la jugada por defecto y Resonancia no cumple R11a | Diseñador | Prototipo del núcleo |
| Con 10 a 14 UT, elegir la Carta Única deja sin aclaratoria justo cuando la carta puede salir muda. Medirlo con el umbral de impuesto de la aclaratoria (D-53) | Diseñador | Prototipo del núcleo |
| ¿Carta Única + *invertir* (12 UT) desplaza a Tres Tiempos (20 UT)? Medir | Diseñador | Prototipo del núcleo |
| ¿Las posiciones libres de la Cruz Celta y El Vínculo se sienten como una falsa elección? | Diseñador | Playtest |
| La tirada final del Mapa B (Cruz Celta del Lunes Negro) | `design/mapas/mapa-b-new-carthage.md` | Fuera del MVP |
| ¿El cliente desconfía de un tarotista que saca una carta aclaratoria (Credulidad)? | GDD de Resonancia, Métricas del Cliente | Al diseñar Resonancia |
| ¿La aclaratoria participa de la Gramática (dignidades con la carta de su posición)? | GDD de Gramática | Al diseñar la Gramática |
| Medir en el prototipo si la aclaratoria ciega rescata lo suficiente o si el Pilar 6 necesita otra palanca | Diseñador | Prototipo del núcleo |
