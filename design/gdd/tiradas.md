# Tiradas

> **Status**: In Review
> **Creative Director Review (CD-GDD-ALIGN)**: `/design-review` full del 2026-10-25 (primera pasada), NEEDS REVISION; corregida el mismo día (D-55); re-revisión full del 2026-10-25, NEEDS REVISION, corregida el mismo día (D-57); tercera revisión full del 2026-10-26, NEEDS REVISION, corregida el mismo día (D-58); cuarta revisión full del 2026-10-26, NEEDS REVISION, corregida el mismo día (D-59: la hipótesis económica pasa al plan del prototipo); pendiente de re-revisión dirigida a States, AC y UI
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-26
> **Last Verified**: 2026-10-26
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

El jugador elige qué tirada usar con cada cliente, después de verlo y escuchar el motivo, entre las que tiene desbloqueadas. Más cartas significa más información, más posiciones donde acertar y un precio más alto, pero también más tiempo de vela y más cartas que explicar (§5.4). Una tirada cara no garantiza más dinero: el cliente paga según cómo quedó (satisfecho, emocionado, pasmado, enojado) y hasta lo que tiene (R8e, D-57). Elegir la tirada es medir al cliente antes de leerle: saber cuándo alcanza una carta y cuándo vale la pena desplegar el paño. En el MVP esto es una hipótesis del prototipo, con su modelo y su métrica en `prototypes/nucleo/plan-hipotesis-tiradas.md` (D-59).

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

5. El jugador elige la tirada **después** de ver al cliente y escuchar el motivo, y **antes** de que se repartan las cartas. Elegir es gratis y se puede cambiar hasta confirmar el reparto; solo se puede elegir una tirada que se ofrece (R6), y elegir una que no se ofrece se rechaza. Elegir no cierra nada: con una tirada elegida se puede seguir preguntando o negociar la vuelta (D-59). Si una pregunta deja la vela por debajo del costo de la tirada elegida, esa tirada deja de estar elegida y pasa a "falta vela". Al confirmar, se vuelve a verificar R6 con la vela de ese momento y se descuenta el costo de la tirada, una sola vez; si ya no alcanza, el reparto se rechaza y no se descuenta nada. Una vez repartida, no se cambia. Se usa una sola tirada por cliente. El orden completo de la atención está en States and Transitions.
6. **Qué tiradas se ofrecen:** una tirada se ofrece si cumple tres condiciones:
   - está disponible en la partida;
   - todos sus roles están habilitados;
   - la vela tiene al menos su costo en UT.

   Si no se ofrece ninguna, el cliente no se puede leer (E2).
7. **Reparto:** Mazo y Robo reparte una carta por posición, en el orden de la tabla de R2, cada una derecha o invertida al azar (D-09). Tiradas no decide qué cartas salen.
8. **Tirada esperada:** cada forma de pregunta tiene una tirada esperada (R1). Si el jugador usa la esperada para la forma del motivo, se activa el bono de tirada (`B_tirada`, §5.8). Si usa otra, no hay bono y baja la Credulidad, salvo que justifique la tirada con una buena lectura (GDD §5.4). Cuánto vale el bono, cuánto baja la Credulidad y qué cuenta como justificar lo define Resonancia (*provisorio*).
   - **Vela corta (D-57, D-58):** si la vela **al sentarse el cliente** (paso 1 de States) ya no alcanzaba para la tirada esperada y sí se ofrece otra, el jugador elige entre dos salidas. Se mide al sentarse, no al elegir: si el jugador gasta vela en preguntas o trucos y después no le alcanza para la esperada, la baja de Credulidad se aplica. Así no se puede forzar la exención gastando vela a propósito:
     - leer con una tirada que se ofrece: no hay bono y **no** baja la Credulidad;
     - **negociar que el cliente vuelva la próxima jornada** (R8f).

**Carta aclaratoria (D-52)**

8a. Después del reparto, el jugador puede pedir **una carta aclaratoria** para una posición de su elección, pagando **5 UT**, que se descuentan al pedirla. Pedirla son dos pasos: elegir la posición, que es gratis y se puede cancelar o cambiar, y confirmar el pedido, que cobra (como elegir y confirmar la tirada, R5). Mazo y Robo reparte una carta más, con orientación al azar, y la deja junto a la de esa posición. Al interpretar esa posición, el jugador elige la palabra clave de cualquiera de las dos cartas; la posición conserva su rol y da un solo resultado (Taxonomía R11). Es la palanca del Pilar 6 ante una carta muda que pidió Cartas (E7, D-50).
8b. **Es ciega.** Se ofrece igual en cualquier posición, con rol o libre, sin consultar la verdad ni `acierto_posible` de Cartas. Si se ofreciera solo ante una carta muda, le diría al jugador algo de la verdad (Pilar 1).
8c. **Límites:** hasta `n_acl` aclaratorias por tirada, en total (hoy 1, Tuning Knobs), y como máximo una por posición (D-59); se pide antes de confirmar la lectura de esa posición, y solo si la vela tiene las 5 UT. Confirmar la lectura de una posición es un paso explícito (States). En la Carta Única, la tirada más la aclaratoria cuestan 15 UT, menos que Tres Tiempos (20), y el validador lo exige (R12).
8d. La aclaratoria no cambia la vecindad: la Gramática no la cuenta (*provisorio hasta el GDD de la Gramática*). Prestidigitación puede actuar sobre ella como sobre cualquier carta repartida (E6). Si el cliente desconfía de un tarotista que saca más cartas, lo define Resonancia (Open Questions).

**Precio, pago y vuelta del cliente (D-57)**

8e. **Precio y pago (D-57).** Cada tirada tiene un precio `π` (R1) que multiplica la tarifa del cliente: las tiradas más complejas valen más. El pago real no es el precio: depende de cómo quedó el cliente (satisfecho, emocionado, pasmado, enojado) y nunca supera lo que el cliente tiene. Un cliente pobre paga lo que puede aunque la tirada valga más. Cómo se calcula lo definen Resonancia y la economía; Tiradas solo fija los invariantes de F3a. Lo que tiene el cliente se deduce en la mesa, no se muestra (Pilar 1).
   - **Requisitos a Resonancia (D-58, D-59):** preguntar tiene que poder mejorar el pago (si no, "no preguntar y leer con la Carta Única" domina); la mejora tiene retornos decrecientes, para que preguntar siga siendo provocar tells y no un multiplicador por cantidad; y vender bien una carta muda tiene que pagar (Pilar 6). Los valores son de Resonancia; el prototipo los mide con el modelo de su plan.
   - **Requisito a Arquetipos y al Generador (D-58):** lo que tiene el cliente (`B_cliente`) tiene que ser legible en la mesa, con al menos **2 señales observables** (ropa, arquetipo, tells), y la relación `B_cliente / T` tiene una distribución definida por sede y estatus. Al menos una de esas señales es independiente del estatus: si todas lo repiten, `B_cliente / T` queda fijo por estatus y no hay nada que apostar. Sin eso el jugador no puede apostar sobre algo que no lee, y la fantasía no se entrega. Para el prototipo, la distribución y las señales son datos del plan (D-59).
8f. **Negociar la vuelta (D-57).** Se puede con cualquier cliente, solo **antes de confirmar el reparto** (después ya no se ofrece, D-58), y solo si **al sentarse el cliente** (paso 1 de States) la vela no alcanzaba para alguna tirada que sea ofrecible por catálogo (disponible y con todos sus roles habilitados, E3), sea o no la esperada. Se mide al sentarse, como la vela corta de R8 (D-59): gastar vela en preguntas no habilita la negociación. Así cubre la vela corta de R8 y el cliente sin tirada de E1 sin delatar cuál es la esperada: en el MVP, si el cliente se sienta con menos de 20 UT se puede negociar con él. El cliente se va sin lectura y puede volver o no en la próxima jornada. Si vuelve, es una atención nueva: llega sin las preguntas que se le hicieron (D-59), aunque el jugador recuerde lo que observó (Pilar 3). Negociar son dos pasos, elegir y confirmar, como el reparto (UI Requirements). La negociación no es gratis ni igual para todos: cambia la Paciencia, el enojo y otras métricas según el arquetipo, a veces a favor, a veces en contra y a veces sin efecto. El juego no lo explica; el jugador lo aprende jugando (§3.3). La negociación y sus efectos son de Fila y Mirilla y de Métricas del Cliente (*provisorio*); Tiradas solo fija cuándo se ofrece.

**Pregunta de sí o no (D-51)**

9. Cada tema de la Taxonomía tiene una **valencia**: favorable, desfavorable o ambigua.

   | Valencia | Temas |
   |---|---|
   | Favorable | amor, alegría, fortuna, éxito |
   | Desfavorable | culpa, duelo, deuda, traición, violencia, engaño, muerte, locura, enfermedad |
   | Ambigua | deseo, hogar, trabajo, ley, secreto, poder, rivalidad, fama, riesgo, cambio |

   El campo es de la Taxonomía, que lo incorporó en R1 (D-51).
10. Si la forma del motivo es *sí o no*, el Generador primero sortea la respuesta verdadera (sí o no, con una proporción fija `ρ`, en un sorteo independiente por cliente: nunca una bolsa o cuota que el jugador pueda contar; convención: con un valor uniforme `u` en [0, 1), sí ⇔ `u` < `ρ`). Después sortea el tema del desenlace entre los temas de la valencia que corresponde. Cada motivo de sí o no lleva un campo **`polaridad`** (D-59): `directa` si "sí" es lo que el cliente desea ("¿me va a llamar?") e `inversa` si "sí" es lo que teme ("¿me va a dejar?"). Con `directa`, sí = favorable y no = desfavorable; con `inversa`, al revés. La polaridad es dato del motivo, no se muestra: se deduce de cómo pregunta el cliente. El sorteo es entre los temas de esa valencia que son sorteables en el mazo activo (`p_t` > 0), con los pesos del mazo (Cartas F1) renormalizados dentro de ese conjunto. Un tema que el mazo solo tiene como forzada no es candidato (Cartas F1, E9); un mazo sin temas sorteables de una valencia es error de datos (`MAZO_SIN_VALENCIA`, Cartas). Un tema ambiguo nunca es el desenlace de una pregunta de sí o no. Esto es un contrato con el Generador.
11. En una pregunta de sí o no, el jugador afirma sí o no, con cualquier tirada. La afirmación se puede cambiar hasta confirmar la lectura completa, y afirmar no cierra ninguna posición (D-59). Compararlo con la respuesta verdadera, y castigar la contradicción con la palabra clave elegida, le corresponde a Interpretación y Resonancia. Tiradas solo garantiza que toda tirada que se ofrece tiene al menos una posición de desenlace, y las 5 la tienen.
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
| Disponible | Se ofrece si cumple R6 | No vuelve atrás durante la partida: Fama no puede revertirla (D-56, D-58). Un pedido de revertirla es un error del contrato con Fama |

Durante la lectura de un cliente: **elegida → repartida → (aclarada, opcional, hasta `n_acl` veces) → leída**. Mientras está elegida se puede cambiar sin costo; el paso a repartida cobra la tirada (R5) y no tiene vuelta atrás (R5, R8c).

**Orden de la atención de un cliente** (*provisorio hasta Flujo de Jornada, Preguntas e Interpretación*):

1. El cliente se sienta y dice su motivo. El motivo se dice una vez y **no queda escrito en pantalla** (Pilar 3, D-58): reconocer qué forma tiene la pregunta es memoria del jugador, como los tells. Cómo se dice, con subtítulo y repetición, está en UI Requirements (D-59). Se registra la vela en este momento, para la vela corta (R8) y para negociar la vuelta (R8f).
2. Preguntas y tells, opcionales (5 UT cada pregunta, GDD §5.1).
3. Negociar que vuelva (R8f), si la vela registrada en el paso 1 lo permite. La atención termina acá.
4. Elegir la tirada, gratis y reversible (R5).

   Los pasos 2, 3 y 4 se intercalan en cualquier orden hasta confirmar el reparto (D-59): elegir es un cursor, no un compromiso. Si una pregunta deja la vela por debajo del costo de la tirada elegida, la tirada deja de estar elegida (R5).
5. Confirmar el reparto: se revalida R6 y se cobra la tirada. Es el camino normal de la revalidación, porque la vela puede bajar entre elegir y confirmar: si falla, el reparto se rechaza sin cobrar, la tirada pasa a "falta vela" y se vuelve a los pasos 2–4. Desde acá no hay más preguntas ni negociación.
6. Por cada posición, en cualquier orden:
   1. aclaratoria, opcional (R8a): elegir la posición, que es reversible, y confirmar el pedido, que cobra. Se puede pedir antes o después de elegir la palabra; si ya había una palabra elegida, se conserva;
   2. elegir la palabra clave;
   3. confirmar la lectura de la posición. Es irreversible: cierra la aclaratoria y los trucos para esa posición (R8c).
7. En un sí o no, afirmar sí o no (R11). Se puede hacer en cualquier momento después del reparto, intercalado con el paso 6, y cambiar hasta el paso 8; no cierra ninguna posición.
8. Confirmar la lectura completa y pasar a Resonancia. Las posiciones que no se confirmaron se confirman acá; una posición sin palabra da NINGUNO, sin castigo extra (Taxonomía E5).

Los trucos de Prestidigitación (2 UT) se pueden hacer después del reparto y antes del paso 8, sobre cartas ya repartidas de posiciones sin confirmar, antes o después de afirmar.

**Operaciones permitidas por momento** (todo lo que no figura se rechaza: rechazo observable, Acceptance Criteria):

| Operación | Permitida | Se rechaza |
|---|---|---|
| Preguntar | Antes de confirmar el reparto, con o sin tirada elegida | Después del reparto |
| Negociar la vuelta (R8f) | Antes de confirmar el reparto, con o sin tirada elegida, si la vela al sentarse cumple la condición de R8f | Después del reparto, o si la vela al sentarse no la cumple (aunque la vela actual sí) |
| Elegir o cambiar la tirada | Antes de confirmar el reparto, una tirada que se ofrece (R6) | Después del reparto, o una tirada que no se ofrece |
| Confirmar el reparto | Con una tirada elegida que cumple R6 | Sin tirada elegida, o ya repartida |
| Pedir aclaratoria (R8a) | Después del reparto, en una posición sin confirmar y sin aclaratoria, dentro de `n_acl` y con 5 UT | Antes del reparto, en una posición confirmada o que ya tiene aclaratoria, o fuera de esos límites |
| Elegir palabra clave | Después del reparto, en una posición sin confirmar | Antes del reparto, o en una posición confirmada |
| Confirmar una posición | Después del reparto, una vez por posición | Antes del reparto, o si ya está confirmada |
| Truco de Prestidigitación | Después del reparto, sobre una posición sin confirmar | Antes del reparto, o sobre una posición confirmada |
| Afirmar o cambiar sí o no (R11) | Después del reparto y antes de confirmar la lectura completa, en una pregunta de sí o no, con cualquier tirada | Antes del reparto, después de confirmar la lectura completa, o con otra forma |
| Confirmar la lectura completa | Después del reparto; en un sí o no, con la afirmación hecha | Antes del reparto, o en un sí o no sin afirmar |

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
| Fila y Mirilla | Cuándo se puede negociar que el cliente vuelva (R8f), medido al sentarse | La negociación y sus efectos; el cliente que vuelve, como atención nueva |
| Generador | Nada directo. Contrato de R10 para la pregunta de sí o no | La verdad por rol, y en sí o no también la respuesta verdadera y la `polaridad` del motivo |
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

**F3a. Invariantes del pago** (D-57, D-58, D-59; la fórmula del pago es de Resonancia y la economía)

Tiradas no define cuánto paga el cliente: define tres invariantes que cualquier fórmula del pago tiene que cumplir.

`Pago ≤ B_cliente` · `Pago` crece con `π` cuando el tope no está activo · `b` va dentro del tope

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `π` | float | ≥ 1 | R1 | Precio de la tirada: ×1 / ×1,5 / ×2 / ×2 / ×3, multiplicador sobre la tarifa del cliente (`T`, `economia-mvp.md` §1) |
| `b` | float | ≥ 1 | Resonancia (`B_tirada`, R8) | Bono de tirada esperada; 1 sin bono |
| `B_cliente` | float | ≥ 0 | Arquetipos, Generador | Lo que el cliente tiene para pagar (R8e: legible con al menos 2 señales) |
| `Pago` | float | 0 a `B_cliente` | Resonancia y economía | Lo que cobra el tarotista por la lectura |

1. **Tope absoluto.** Ningún término del pago de la lectura, ni el bono, supera `B_cliente`. Un cliente pobre paga lo que tiene aunque la tirada valga más. El Doble Fondo no es pago de la lectura: su relación con el tope la define la economía (Pilar 4).
2. **El precio cuenta.** Con el tope sin activar y todo lo demás igual, una tirada con más `π` paga más. Sin esto, desplegar el paño nunca paga más y elegir no es una decisión (revisión del 2026-10-25). Que además rinda más por UT no lo garantiza este invariante: es la hipótesis del prototipo.
3. **El bono dentro del tope.** `b` multiplica antes del tope, nunca después.

- **Por qué no hay fórmula acá:** las revisiones del 2026-10-25 y del 2026-10-26 mostraron que cada número provisorio puesto en este GDD para sostener la hipótesis abría huecos nuevos (stub sin tope, sin Match, sin la intención retórica, sin la cantidad de clientes por jornada). La hipótesis se mide en el prototipo con el instrumento correcto: el modelo, los cruces, los barridos y la métrica de descarte están en `prototypes/nucleo/plan-hipotesis-tiradas.md` (D-59).
- Reemplaza la tarifa plana de `economia-mvp.md` §1, que está en recalibración (D-57, D-59).

**F4. Acertar el sí o no**

`P_acierto_sn = max(ρ, 1 − ρ) + Δ_deducción`

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `ρ` | float | 0 a 1; vale 0,5 | data file (Generador) | Proporción de respuestas verdaderas "sí" (Tuning Knobs) |
| `Δ_deducción` | float | 0 a 1 − max(ρ, 1 − ρ) | Detección | Lo que suma deducir al cliente (tells, preguntas) |
| `P_acierto_sn` | float | max(ρ, 1 − ρ) a 1 | calculated | Probabilidad de que el jugador afirme la respuesta verdadera. `max(ρ, 1 − ρ)` es contestar siempre lo más frecuente; con ρ = 0,5 da `0,5 + Δ_deducción` |

- **La carta no informa:** como el reparto es independiente de la verdad (R7, D-37), P(sí | carta favorable) = `ρ`. Toda la información del sí o no sale del cliente (Pilar 1).
- **Por qué `ρ` = 0,5:** con cualquier otro valor, contestar siempre lo mismo da más del 50 %.
- **La carta restringe:** si el jugador cree "sí" y la Respuesta solo tiene palabras de la valencia del "no" (desfavorables con polaridad directa, favorables con inversa, R10), puede elegir una palabra ambigua (Match 0 seguro, porque una ambigua nunca es desenlace de un sí o no) o contradecirse. Cómo se castiga la contradicción lo define Resonancia.
- **El lado favorable tiene menos cobertura:** su verdad sale de 4 temas, que la tradición usa poco; es el "sí" con polaridad directa y el "no" con inversa (R10). `P_pos` del desenlace en un sí o no se calcula con los pesos renormalizados dentro de la valencia. Está en el informe de Cartas (`P_pos⁺_v`, Cartas F3; `P_cero_v(k)`, Cartas F4; D-53), y un mazo sin temas sorteables de una valencia es error de datos (`MAZO_SIN_VALENCIA`). La probabilidad de que la Carta Única de un sí o no quede sin acierto posible es `ρ·(1 − P_pos⁺_favorable) + (1 − ρ)·(1 − P_pos⁺_desfavorable)` con polaridad directa, y con los dos términos de valencia intercambiados con inversa; con `ρ` = 0,5 da lo mismo en las dos. No mide si la afirmación es correcta.

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
   **Advertencia:** si una pregunta va a dejar la vela por debajo del costo de la tirada más barata que se ofrece en ese momento, el juego avisa antes. Los trucos no avisan: solo se hacen después del reparto, cuando la tirada ya está pagada. Las tiradas que una pregunta dejaría sin vela, sin ser la última, se muestran con una vista previa pasiva en el selector, todas con el mismo trato (UI Requirements), para no marcar la esperada. La acción igual se puede hacer. El umbral es siempre la más barata, no la esperada, para no marcar la tirada esperada (UI Requirements). Si ya no se ofrece ninguna tirada, no hay advertencia. Una acción que cuesta más de lo que queda en la vela no se puede hacer (contrato con Reloj de Vela).
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
| Generador de Situaciones | Blanda | Qué tiradas están disponibles, para emitir solo formas alcanzables (E3), y el contrato del sí o no (R10), con la `polaridad` de cada motivo |
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
| Precio por tirada (`π`) | Carta Única ×1 · Tres Tiempos ×1,5 · Dos Caminos ×2 · El Vínculo ×2 · Cruz Celta ×3 (D-57, *provisorio*) | ×1 a ×4, creciente con la complejidad de la tirada y cumpliendo los invariantes de F3a. Lo calibra el prototipo (`prototypes/nucleo/plan-hipotesis-tiradas.md`) | Cuánto vale desplegar el paño con un cliente que puede pagarlo (F3a) |
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
- **Orden y foco fijos (Pilar 1, D-58):** las tiradas van siempre en el mismo orden, por costo de menor a mayor, y el foco inicial está siempre en la primera que se muestra. El foco nunca arranca en la tirada esperada ni en la última usada, y no hay marca de "recomendada" ni de "última usada": cualquiera de esas cosas le diría al jugador cuál es la esperada.
- **Estado de cada tirada en el selector:**

  | Estado lógico | Se muestra | Motivo visible |
  |---|---|---|
  | No disponible (States) | No | — (el anuncio del desbloqueo es de Fama, D-56) |
  | Disponible, con algún rol deshabilitado (R6, condición 2) | No | — (en el MVP no ocurre) |
  | Disponible y con roles, sin vela suficiente (R6, condición 3) | Deshabilitada; puede recibir el foco | "falta vela", con texto o ícono además del color |
  | Ofrecida | Activa | — |
  | Elegida (R5) | Activa y marcada como elegida, distinta del foco, con forma o texto además del color | — |

  Si no se ofrece ninguna tirada, el selector se muestra igual, con todo deshabilitado, y siempre hay una salida: negociar la vuelta (R8f) o dejar ir al cliente. Si una pregunta deja la vela por debajo de la tirada elegida (R5) o la revalidación de R6 rechaza el reparto (States, paso 5), la tirada pasa a "falta vela", deja de estar elegida, el foco queda sobre ella y el selector sigue abierto.
- **Vista previa de la vela:** antes de confirmar una pregunta, el selector marca todas las tiradas que dejarían de alcanzar, con el mismo trato para todas, nunca solo la esperada (E1).
- **Elegir no es confirmar (D-59):** ningún botón elige y confirma a la vez. Con gamepad, el botón de acción sobre una tirada la elige (reversible); el reparto se confirma con un control aparte, "Repartir", que muestra el costo y la vela que queda, está deshabilitado con motivo mientras no hay tirada elegida, nunca recibe el foco inicial y no recibe el foco solo al elegir: el jugador lo mueve. Después de confirmar, la entrada se ignora hasta que termina el reparto, para que un toque doble no haga nada más. Al tacto rige lo mismo: tocar elige, no confirma.
- **Negociar la vuelta (R8f):** dos pasos, elegir y confirmar, como el reparto. Nunca recibe el foco inicial ni queda al lado de "Repartir". La opción aparece por la vela al sentarse, nunca por la forma del motivo, así que no delata cuál es la tirada esperada; su texto no nombra ninguna tirada.
- **Aclaratoria:** el botón muestra su costo y se ve igual en todas las posiciones (con rol o libres) y con cualquier carta (R8b). Si no se puede pedir, se ve deshabilitado con el motivo ("falta vela", "ya la usaste", "esta posición ya tiene una", "posición ya leída"; si se cumplen varios, se muestra el primero de esta lista). Elegir la posición y confirmar el pedido son dos acciones distintas (R8a).
- **Confirmar una posición es irreversible** (States, paso 6.3). Mientras la aclaratoria todavía se puede pedir en esa posición, el botón lo dice ("cerrar sin aclaratoria"), con el mismo texto en todas las posiciones.
- **Nada en la presentación depende del rol** de la posición, ni de si una carta tiene acierto posible: ni marco, ni color, ni orden, ni sonido.
- **La tirada esperada no se marca.** El motivo del cliente se dice en su texto ("¿me va a llamar, sí o no?"), y reconocer qué tirada pide es parte de leerlo (§3.3: lo aprendido no lo explica el juego). La exención de la vela corta (R8) tampoco se muestra nunca, ni en el selector ni en el resumen: diría cuál era la esperada.
- **El motivo (Pilar 3, D-58, D-59):** se dice una vez y no queda escrito después de dicho.
  - Mientras el cliente habla hay un subtítulo ligado a la línea, sin historial ni registro: se va cuando termina la línea.
  - La línea avanza al ritmo del jugador (botón para seguir), no con un temporizador.
  - Si la partida se interrumpe mientras el cliente dice el motivo (pausa, suspensión de la consola), al volver la línea empieza de nuevo y no cuenta como repetición.
  - **Pedir que repita** es una acción de la mesa con costo en UT, como una pregunta: repetir es provocar de nuevo al cliente, no guardar lo que dijo. El costo y si tiene un tell de fastidio los definen Preguntas y Métricas del Cliente (*provisorio*).
  - Una **opción de accesibilidad**, apagada por defecto, deja el motivo visible durante la atención. No cambia el puntaje. La define el GDD de Tutorial, Accesibilidad y Localización, con `design/accessibility-requirements.md`, que todavía no existe.
- La advertencia de E1 aparece antes de confirmar la acción que deja la vela sin tirada posible.

> 📌 **UX Flag — Tiradas:** antes de las historias del selector y del tapete hay que hacer su spec con `/ux-design`. Incluye: la disposición de la Cruz Celta en Switch portátil; la advertencia de la vela (alcance y frecuencia); la aclaratoria junto a su posición y la elección de palabra entre dos cartas; el control de sí o no; la asignación de botones para elegir, confirmar y negociar con gamepad; el selector sin tiradas ofrecidas; la vista previa de la vela; y el subtítulo, el ritmo y la repetición del motivo (Pilar 3). Los AC de UI (AC-20b, el selector y el tapete) se escriben ahí.

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
| D-56, D-57, D-58 | Desbloqueo en Fama y sí o no sobre temas sorteables; precio por tirada, pago limitado por el cliente, vela corta, negociar la vuelta y requisito del sí o no a Resonancia; pago con bono dentro del tope, preguntas que mejoran el pago, métrica de descarte en dos sentidos, vela corta al sentarse, negociar solo antes del reparto, operaciones por momento, motivo sin quedar escrito |
| D-59 | Hipótesis económica al plan del prototipo e invariantes del pago en F3a; pasos 2–4 intercalables y tirada elegida que se deselecciona; R8f medido al sentarse, cliente que vuelve sin preguntas y negociación en dos pasos; polaridad del sí o no; motivo con subtítulo efímero, repetición con costo y opción de accesibilidad; elegir ≠ confirmar con gamepad |
| Taxonomía R8–R13, E3, E4 | Roles, posiciones libres, formas, validador; rol ausente; roles repetidos |
| Cartas F1, F3, R11 | Pesos de la verdad; `P_pos`; informe de cobertura |

## Acceptance Criteria

Convenciones de prueba:
- Todo AC parte de `fixture_tiradas_valido` y lo muta en un solo punto. AC-01 prueba que el fixture sin mutar pasa limpio. Contenido mínimo del fixture: las 5 tiradas de R1 con las posiciones, roles y vecindades de R2 y R4; costos 10/20/30/30/45 UT; aclaratoria a 5 UT con `n_acl` = 1; Carta Única y Tres Tiempos disponibles y las otras tres no disponibles; roles origen, conflicto y desenlace habilitados y el otro, camino A y camino B deshabilitados (el estado del MVP). Los AC que necesitan otra tirada disponible o un rol habilitado lo mutan en ese punto. El archivo y los fixtures derivados (`tirada_vecina`, `tirada_sin_desenlace`, `tirada_con_libre`: una tirada de prueba de 2 posiciones, `p1` con rol desenlace y `p2` libre) los fija la historia.
- **Rechazo observable:** cuando un AC dice "se rechaza", significa: la operación devuelve error, la vela no cambia, no se piden cartas al mazo y el estado de la tirada no cambia.
- Cada error se verifica por la regla de la que es (con el código que fije la historia) y por su sujeto en formato R13 de la Taxonomía. Los controles dicen "no contiene error de la regla X con sujeto S", nunca "no hay errores".
- El RNG y el reparto se simulan; ningún test depende del azar.
- `ROL_INEXISTENTE`, `FORMA_INEXISTENTE`, `POSICION_AMBIGUA` y `TIRADA_SIN_COMPARABLES` ya los prueban AC-31, AC-33, AC-37a/b y AC-38 de la Taxonomía, y SIN_COMPARACION su E3. No se repiten acá.
- **Evidencia:** todos son Logic (test unitario en `[test root]/tiradas/`), salvo los marcados Integration, UI o Config/Data. Un AC *provisorio* depende de un GDD que todavía no existe: no se convierte en historia hasta que ese GDD exista y confirme el AC; desde ahí bloquea como cualquier otro.
- **Dependencias provisorias:** los AC que usan la vela (AC-06, 19, 20a, 24, 26, 29, 30, 31, 33, 36, 38) son *provisorios hasta Reloj de Vela*; los que reparten (AC-12, 13, 24) *hasta Mazo y Robo*; el bono, el pago y el resultado único (AC-14, 24, 31, 32) *hasta Resonancia*; el estado "leída" y la afirmación (AC-11, 26, 33, 35, 36) *hasta Interpretación*; la negociación (AC-30) *hasta Fila y Mirilla*; los trucos (AC-21, 33, 36) *hasta Prestidigitación*; la vecindad (AC-34) *hasta la Gramática*; la polaridad (AC-17d) *hasta el Generador*.
- **Sin AC, a propósito:** F2, F3 y F5 son de calibración y ningún código del juego las calcula. F3a son invariantes que cumple la fórmula de Resonancia: los prueba AC-32 sobre esa función. El modelo de la hipótesis es del prototipo (`prototypes/nucleo/plan-hipotesis-tiradas.md`) y no tiene AC. Los requisitos de R8e (preguntas que valen, señales de lo que tiene el cliente) y R11a son requisitos a Resonancia y a Arquetipos: se trazan en Open Questions y se vuelven AC en esos GDD. Cuánto baja la Credulidad y qué es justificar otra tirada (R8) es de Resonancia. La suma de deducción de F4 es de Detección. E5 lo cubre la Taxonomía (E3) y AC-08. La combinación de E7 es de Resonancia. E8 es una hipótesis del prototipo. R8f (negociar la vuelta) es de Fila y Mirilla; acá solo se prueba cuándo se ofrece (AC-30). El subtítulo, el ritmo y la repetición del motivo (UI Requirements) se prueban en `/ux-design`.

**Catálogo**
- **AC-01** (R1–R12) — GIVEN `fixture_tiradas_valido`, WHEN se valida, THEN, para cada regla de R12 y del validador de la Taxonomía (R13), no contiene error de esa regla con ningún sujeto del fixture.
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
- **AC-10a** (States; *provisorio hasta el GDD de Fama, Reputación y Ascenso*) — GIVEN una tirada Disponible, WHEN cambia la jornada, THEN sigue Disponible.
- **AC-10b** (States; *idem*) — GIVEN una tirada Disponible, WHEN cambia la sede, THEN sigue Disponible.
- **AC-10c** (States, D-56; *idem*) — GIVEN una tirada Disponible, WHEN Fama pide pasarla a No disponible, THEN se rechaza con error de contrato y la tirada sigue Disponible. Control: una tirada No disponible pasa a Disponible cuando Fama lo pide.

**Lectura**
- **AC-11a** (R5, States) — GIVEN una tirada elegida y 30 UT, WHEN se elige otra antes de repartir, THEN queda la nueva y la vela sigue en 30.
- **AC-11b** (R5, States) — GIVEN una tirada repartida, y en otro caso leída, WHEN se elige otra, THEN se rechaza (rechazo observable).
- **AC-11c** (R5) — GIVEN una tirada repartida, WHEN se pide un segundo reparto para el mismo cliente, con la misma tirada o con otra, THEN se rechaza (rechazo observable). Control: el cliente siguiente puede elegir cualquier tirada que se ofrezca.
- **AC-12** (R7) — GIVEN Tres Tiempos y un reparto simulado que devuelve (A, derecha), (B, invertida) y (C, derecha), WHEN se reparte, THEN se piden exactamente 3 cartas y quedan Pasado = A derecha, Presente = B invertida, Futuro = C derecha.
- **AC-13** (R7, D-37, F4) — GIVEN una situación con un doble de la verdad que falla si se lo lee, y la misma secuencia del RNG, WHEN se reparte cada una de las 5 tiradas, THEN el reparto termina sin leer la verdad. Control: con la verdad "sí" en una corrida y "no" en otra, las cartas y orientaciones de cada tirada son idénticas.
- **AC-14** (R8, E4) — GIVEN cada una de las 5 formas, WHEN se elige cada tirada, THEN solo la tirada esperada de R1 activa el bono. Con `forma.si_o_no` y Tres Tiempos no hay bono, y las 3 posiciones se comparan igual.

**Sí o no**
- **AC-15** (R9) — La valencia de cada tema la prueban AC-35d y AC-35e de la Taxonomía; no se repite acá.
- **AC-16a** (R10; *provisorio hasta el Generador*) — GIVEN `ρ` = 0,5 y un RNG simulado que devuelve siempre `u` = 0,1, WHEN se sortea la respuesta de 10 clientes seguidos, THEN los 10 son sí; con `u` = 0,7 siempre, los 10 son no (una bolsa o cuota no pasa). Con `u` = 0,5 da no (sí ⇔ `u` < `ρ`).
- **AC-16b** (R10, Tuning Knobs; Config/Data) — GIVEN los datos reales del Generador, WHEN se cargan, THEN `ρ` = 0,5.
- **AC-17a** (R10; *provisorio hasta el Generador*) — GIVEN una pregunta de sí o no con polaridad `directa` y un mazo de fixture donde `tema.culpa` y `tema.amor` aparecen solo como forzadas (`p_t` = 0), los otros 11 temas con valencia tienen `p_t` > 0 y `tema.trabajo` y `tema.secreto` (ambiguos) también, WHEN se arman los candidatos al desenlace, THEN para sí son exactamente alegría, fortuna y éxito, y para no los 8 desfavorables sin `tema.culpa`; ni `tema.trabajo` ni `tema.secreto` están entre los candidatos. Control: con `tema.culpa` y `tema.amor` como claras, están entre los candidatos de no y de sí.
- **AC-17b** (R10; *provisorio hasta el Generador*) — GIVEN los favorables con `p_t` crudos 0,05 / 0,10 / 0,15 / 0,20 (amor, alegría, fortuna, éxito), WHEN se renormalizan para sí, THEN quedan 0,10 / 0,20 / 0,30 / 0,40, con tolerancia 1e-9.
- **AC-17c** (R10, Cartas `MAZO_SIN_VALENCIA`) — Lo prueba AC-18n de Cartas, con el mazo y la valencia como sujeto; no se repite acá.
- **AC-17d** (R10, polaridad; *provisorio hasta el Generador*) — GIVEN la situación de AC-17a con polaridad `inversa`, WHEN se arman los candidatos, THEN para sí son los 8 desfavorables sin `tema.culpa` y para no alegría, fortuna y éxito. Control: con polaridad `directa`, los de AC-17a.
- **AC-18** (E3; *provisorio hasta el Generador*) — GIVEN Dos Caminos no disponible, WHEN se arman las formas que el Generador puede emitir, THEN no incluyen `forma.dilema`. Lo mismo con Dos Caminos disponible y `rol.camino_a` deshabilitado. Control: con Dos Caminos disponible, `forma.dilema`, `rol.camino_a` y `rol.camino_b` habilitados y 0 UT en la vela, la incluyen (la vela no cuenta).

**Advertencia de la vela**
- **AC-19** (E1) — GIVEN Carta Única y Tres Tiempos ofrecidas, 14 UT y una pregunta de 5 UT, WHEN se evalúa la pregunta, THEN corresponde avisar; con 15 UT, no. Después del aviso, la pregunta se ejecuta igual. Con la Carta Única no disponible (la más barata pasa a ser Tres Tiempos), con 24 UT corresponde avisar y con 25 no: el umbral sale de la tirada más barata que se ofrece, no es un valor fijo.
- **AC-20a** (E1) — GIVEN la vela en 14 UT y un espía que registra eventos, WHEN el jugador elige una pregunta de 5 UT, THEN el evento de advertencia se registra antes que el de descuento. Con 15 UT, no hay evento de advertencia. Con 9 UT y ninguna tirada ofrecida, tampoco.
- **AC-20b** (E1; UI) — Se escribe en `/ux-design` (UX Flag): captura retenida en `production/qa/evidence/` con la advertencia a 14 UT, y otra sin advertencia a 15 UT.

**Otros sistemas**
- **AC-21** (E6; Integration, *provisorio hasta Prestidigitación*) — GIVEN un truco que cambia la carta del Presente, WHEN se compara, THEN la posición sigue con rol conflicto y se compara la carta nueva. Si el truco la invierte, se compara la orientación nueva.
- **AC-22** (F1) — GIVEN todos los roles habilitados y presentes, WHEN se calcula `k`, THEN da 1/3/5/4/6 para Carta Única, Tres Tiempos, Dos Caminos, El Vínculo y Cruz Celta (en Cruz Celta, posiciones 1, 2, 4, 5, 6 y 10). Con los roles del MVP, Dos Caminos da 3 (Situación, Resultado A y Resultado B) y El Vínculo 3 (prueban la fórmula: en el MVP esas tiradas no se ofrecen). Con una situación de prueba construida a mano sin `rol.origen` (el Generador no la produce: es el caso de una partida guardada, Taxonomía E9), Tres Tiempos da 2.
- **AC-23** (R12, Tuning Knobs) — GIVEN `fixture_tiradas_valido` con la Carta Única a 15 UT (aclaratoria a 5, 1 por tirada, Tres Tiempos a 20), WHEN se valida, THEN contiene error de costos con sujeto `tirada.carta_unica` (15 + 5 = 20, no menor que 20, aunque 15 < 20). Control: con la Carta Única a 14, no lo contiene.
- **AC-24** (R8a) — GIVEN Tres Tiempos repartida y 10 UT, WHEN se pide una aclaratoria para Presente, THEN se reparte 1 carta más junto a Presente y se descuentan 5 UT; las palabras clave elegibles para Presente son las de las dos cartas, y Presente da un solo resultado.
- **AC-25** (R8b) — GIVEN Tres Tiempos repartida con una carta sin acierto posible en Presente y cartas con acierto posible en Pasado y Futuro, en dos situaciones con verdades distintas, WHEN se piden las posiciones donde se ofrece la aclaratoria, THEN en las dos son exactamente [Pasado, Presente, Futuro]. Lo mismo en la Carta Única, con la Respuesta con y sin acierto posible.
- **AC-25c** (R8b, E9) — GIVEN `tirada_con_libre`, repartida, con `p1` de rol desenlace y `p2` libre, y 100 UT, WHEN se piden las posiciones donde se ofrece la aclaratoria, THEN son exactamente [`p1`, `p2`], con la carta de `p1` con y sin acierto posible. Control contra la implementación que filtra: una oferta solo de posiciones con rol da [`p1`] y falla.
- **AC-26a** (R8c) — GIVEN Tres Tiempos repartida y ninguna aclaratoria pedida, WHEN se piden las posiciones donde se ofrece, THEN con 5 UT se ofrece y con 4 no.
- **AC-26b** (R8c) — GIVEN `n_acl` = 1 y una aclaratoria ya pedida en Presente, WHEN se pide otra en Pasado, THEN se rechaza (rechazo observable). Con `n_acl` = 2: la segunda en Pasado se acepta; una segunda en Presente se rechaza (una por posición); y con dos ya pedidas, una tercera en Futuro se rechaza.
- **AC-26c** (R8c, States) — GIVEN Tres Tiempos repartida, ninguna aclaratoria pedida y la lectura de Presente confirmada, WHEN se piden las posiciones donde se ofrece, THEN son exactamente [Pasado, Futuro].
- **AC-26d** (R8a) — GIVEN Tres Tiempos repartida y 10 UT, WHEN se elige Presente para la aclaratoria y se cancela antes de confirmar, THEN la vela sigue en 10, no se pidió carta y la aclaratoria sigue disponible.
- **AC-27** (R12, Tuning Knobs) — GIVEN la aclaratoria a 10 UT, 1 aclaratoria por tirada, con Carta Única a 10 y Tres Tiempos a 20, WHEN se valida, THEN contiene error de costos con sujeto `tirada.carta_unica`. Con 9, no lo contiene. Con la aclaratoria a 5 y 2 aclaratorias por tirada (10 + 2 · 5 = 20), lo contiene; con Tres Tiempos a 21, no.
- **AC-28** (R8b, D-50) — GIVEN cartas cuyo `acierto_posible` falla al leerse, por cualquier vía, y un acceso a la verdad que falla si se lo lee, WHEN se arma la oferta de aclaratoria de Tres Tiempos, THEN se arma sin fallar y es exactamente [Pasado, Presente, Futuro].
- **AC-29a** (R5) — GIVEN 30 UT, WHEN se elige la Carta Única, se cambia a Tres Tiempos y se confirma el reparto, THEN la vela queda en 10 (se descontaron 20, una vez).
- **AC-29b** (R5) — GIVEN 30 UT, WHEN se elige una tirada y no se confirma, THEN la vela sigue en 30.
- **AC-29c** (R5, States paso 4; D-59) — GIVEN 22 UT y Tres Tiempos elegida, WHEN se hace una pregunta de 5 UT, THEN la vela queda en 17, Tres Tiempos deja de estar elegida y está en "falta vela", y confirmar el reparto sin elegir otra se rechaza (rechazo observable). Control: con 25 UT, después de la pregunta Tres Tiempos sigue elegida y el reparto se confirma.
- **AC-29d** (R6, States paso 5; guarda) — GIVEN Tres Tiempos elegida y un doble de Reloj de Vela que informa 15 UT al confirmar, WHEN se confirma el reparto, THEN se rechaza (rechazo observable), la vela sigue en 15 y Tres Tiempos queda en "falta vela", sin elegir.
- **AC-30** (R8, R8f, E1; *provisorio hasta Reloj de Vela y Fila y Mirilla*) — GIVEN un cliente con `forma.situacion_general` y la tirada sin repartir, WHEN se pregunta si se puede negociar la vuelta, THEN con 19 y con 15 UT al sentarse sí (Tres Tiempos no se ofrecía), con 9 UT al sentarse sí (no se ofrecía ninguna) y con 20 UT al sentarse no. Con `forma.si_o_no` da lo mismo en los cuatro casos: la opción no depende de la forma. Controles: con 25 UT al sentarse y 2 preguntas (15 UT ahora), no; con 15 UT al sentarse y Tres Tiempos no disponible, no; con 25 UT y Dos Caminos disponible pero `rol.camino_b` deshabilitado, no (no es ofrecible por catálogo); con la tirada ya repartida, no.
- **AC-31** (R8, vela corta; *provisorio hasta Reloj de Vela y Resonancia*) — GIVEN `forma.situacion_general` y 15 UT al sentarse el cliente, WHEN se lee con la Carta Única, THEN la lectura no lleva bono de tirada ni marca de baja de Credulidad. Controles: con 19 UT al sentarse, tampoco la lleva; con 20 UT al sentarse, la lleva; con 25 UT al sentarse y 2 preguntas (15 UT al elegir), también la lleva.
- **AC-32** (F3a; *provisorio hasta Resonancia*) — GIVEN la función de pago de Resonancia, con todo igual salvo lo que dice cada caso, WHEN se calcula el pago, THEN: con un pago sin tope de 6,6 y `B_cliente` = 5, da 5 (con bono y sin bono); con `B_cliente` = 0, da 0; con el tope sin activar, Tres Tiempos (`π` = 1,5) paga más que la Carta Única (`π` = 1); y con `b` = 1,1 el pago nunca supera el de `b` = 1 con el tope activo. Tolerancia 1e-9.
- **AC-33** (States, operaciones permitidas; *provisorio hasta Reloj de Vela, Interpretación y Prestidigitación*) — Parametrizado: un caso por fila de la tabla de operaciones permitidas y por cada momento de su columna "Se rechaza". GIVEN ese momento, WHEN se intenta la operación, THEN se rechaza (rechazo observable). Casos mínimos, además de los de la tabla: confirmar el reparto sin tirada elegida; elegir palabra, pedir aclaratoria, hacer un truco, afirmar, confirmar una posición o confirmar la lectura completa antes del reparto; preguntar o negociar después del reparto; negociar con la vela al sentarse en 20 UT y la actual en 15; pedir aclaratoria con 4 UT o en una posición que ya tiene una; pedir aclaratoria, elegir palabra o hacer un truco sobre una posición confirmada; confirmar dos veces una posición; afirmar con `forma.situacion_general`; afirmar después de confirmar la lectura completa; confirmar la lectura completa de un sí o no sin afirmar. Control: cada operación, en un momento de su columna "Permitida", se acepta; en particular, preguntar y negociar con una tirada elegida.
- **AC-34** (R8d; *provisorio hasta la Gramática*) — GIVEN Tres Tiempos repartida con una aclaratoria en Presente, WHEN se piden las vecindades que usa la Gramática, THEN son exactamente Pasado–Presente y Presente–Futuro, y ninguna nombra la carta aclaratoria.
- **AC-35** (States paso 6; *provisorio hasta Interpretación*) — GIVEN Tres Tiempos repartida con una palabra elegida en Presente, WHEN se pide la aclaratoria para Presente, THEN la palabra elegida se conserva. Y con Pasado sin palabra ni confirmación, al confirmar la lectura completa, Pasado queda confirmada con resultado NINGUNO.
- **AC-36** (R11, States paso 7; *provisorio hasta Interpretación*) — GIVEN una pregunta de sí o no y Tres Tiempos repartida, WHEN se afirma sí, THEN se acepta. Y si después se afirma no, al confirmar la lectura completa la afirmación registrada es no. Con sí afirmado, pedir la aclaratoria y hacer un truco en una posición sin confirmar se aceptan.
- **AC-37** (UI Requirements, orden y foco; Pilar 1) — GIVEN el modelo del selector, para cada combinación de forma del motivo (sí o no, situación general) y última tirada usada (Carta Única, Tres Tiempos, ninguna), con 30 UT, WHEN se arma el selector, THEN el orden es [Carta Única, Tres Tiempos], el foco inicial está en la Carta Única, ninguna entrada lleva marca de recomendada ni de última usada, y "Repartir" no tiene el foco. Las capturas se escriben en `/ux-design`.
- **AC-38** (R5, R6) — GIVEN 15 UT y ninguna tirada elegida, WHEN se elige Tres Tiempos, THEN se rechaza (rechazo observable). Control: elegir la Carta Única se acepta.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| **Requisito de F2:** Resonancia mide en proporción a las posiciones comparables (`k`), no con un umbral fijo; si no, la Carta Única queda casi imposible de aprobar (72,6 % sin acierto posible). ¿El sí o no del jugador cuenta como un acierto propio? | GDD de Resonancia | Al diseñar Resonancia |
| Cuánto vale `B_tirada` y cómo pesa justificar otra tirada (§5.4). ¿Las posiciones libres pueden contradecir? | GDD de Resonancia | Al diseñar Resonancia |
| Contratos de R10 y E3: el sorteo del sí o no (`ρ` = 0,5, desenlace dentro de la valencia) y las formas solo con tirada disponible | GDD del Generador | Al diseñar el Generador |
| Qué desbloquea Dos Caminos y El Vínculo, y desde qué sede aparece la Cruz Celta | GDD de Fama, Reputación y Ascenso de Sede (D-56) | Antes del Vertical Slice |
| Negociar la vuelta (R8f): si el cliente vuelve, cuánto cambian Paciencia, enojo y otras métricas por arquetipo, y qué pasa con el cliente que se deja ir sin negociar (E1) | GDD de Fila y Mirilla, Métricas del Cliente | Al diseñar Fila y Mirilla |
| ¿El estatus del cliente (§5.4, "lo que puede pagar") limita qué tiradas se le ofrecen? | GDD de Arquetipos, economía | Al diseñar Arquetipos |
| **Hipótesis del prototipo (D-57, D-58, D-59):** con precio por tirada (`π`), pago limitado por el cliente (F3a) y preguntas que mejoran el pago, elegir tirada deja de ser solo reconocer la forma. El modelo de pago, los barridos, la cantidad de clientes por jornada, los bots de estrategia fija y la métrica de descarte en los dos sentidos están en `prototypes/nucleo/plan-hipotesis-tiradas.md`. Tiradas solo exige que ese modelo cumpla F3a y R8e | Diseñador | Prototipo del núcleo |
| **Datos del prototipo (D-58, D-59):** distribución de `B_cliente / T` por sede y estatus, y al menos 2 señales observables de lo que tiene el cliente, una de ellas independiente del estatus (R8e). Están en el plan del prototipo; Arquetipos y el Generador los heredan | Diseñador | Antes del prototipo del núcleo |
| **R8f en el prototipo (D-58, D-59):** stub de costo, condición medida al sentarse y métrica para detectar si se usa para diferir a los clientes que pagan más: en el plan del prototipo | Diseñador | Prototipo del núcleo |
| Recalibrar `economia-mvp.md` (en recalibración, D-59) y `tools/balance/economia_mvp.py` con el precio por tirada y el pago limitado: hoy suponen tarifa plana, cola ilimitada (la vela decide cuántos clientes hay), no modelan aclaratoria, trucos ni elección según la forma, descartan las UT entre 10 y 19 y no bajan a Carta Única cuando no alcanza para Tres Tiempos. Falta definir si el tope `B_cliente` va antes o después del Doble Fondo | Diseñador, economía | Antes de cerrar la economía del MVP |
| Cómo se deduce lo que tiene el cliente (`B_cliente`, F3a): ropa, arquetipo, tells. Requisito de R8e: al menos 2 señales observables | GDD de Arquetipos, Detección | Al diseñar Arquetipos |
| ¿"Fila Base" (GDD maestro §7.5: 2–3 clientes en la Sede 1 con Fama 0) es el total de clientes de la jornada o el largo de la fila en un momento, con reposición? La elección de tirada depende de cuántos clientes hay por jornada (plan del prototipo) | GDD de Fila y Mirilla, Flujo de Jornada | Al diseñar Fila y Mirilla |
| `design/accessibility-requirements.md` no existe: la opción de accesibilidad del motivo (UI Requirements) y los estados del selector sin color no se pueden auditar contra un nivel fijado | `/ux-design accessibility` | Antes del spec de UX de Tiradas |
| Costo de "pedir que repita" el motivo y si tiene tell de fastidio | GDD de Preguntas Capciosas, Métricas del Cliente | Al diseñar Preguntas |
| E8 y R11a: proporción de Cartas Únicas de sí o no resueltas con una palabra ambigua. Si pasa del 50 %, el refugio en la ambigua es la jugada por defecto y Resonancia no cumple R11a | Diseñador | Prototipo del núcleo |
| Con 10 a 14 UT, elegir la Carta Única deja sin aclaratoria justo cuando la carta puede salir muda. Medirlo con el umbral de impuesto de la aclaratoria (D-53) | Diseñador | Prototipo del núcleo |
| ¿Carta Única + *invertir* (12 UT) desplaza a Tres Tiempos (20 UT)? Medir | Diseñador | Prototipo del núcleo |
| ¿Las posiciones libres de la Cruz Celta y El Vínculo se sienten como una falsa elección? | Diseñador | Playtest |
| La tirada final del Mapa B (Cruz Celta del Lunes Negro) | `design/mapas/mapa-b-new-carthage.md` | Fuera del MVP |
| **Condición para habilitar la Cruz Celta:** no se habilita sin spec aprobado de `/ux-design` y una prueba en Switch portátil (10 cartas, aclaratoria y dos listas de palabras en pantalla chica). Si no entra, se revisa D-14 | `/ux-design`, Diseñador | Antes de habilitar la Cruz Celta |
| ¿El cliente desconfía de un tarotista que saca una carta aclaratoria (Credulidad)? | GDD de Resonancia, Métricas del Cliente | Al diseñar Resonancia |
| ¿La aclaratoria participa de la Gramática (dignidades con la carta de su posición)? | GDD de Gramática | Al diseñar la Gramática |
| Medir en el prototipo si la aclaratoria ciega rescata lo suficiente o si el Pilar 6 necesita otra palanca | Diseñador | Prototipo del núcleo |
