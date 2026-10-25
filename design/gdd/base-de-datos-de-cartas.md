# Base de Datos de Cartas

> **Status**: In Review — reescrito el 2026-10-24 (D-48); `/design-review` lean, full y re-revisión full del 2026-10-24, las tres NEEDS REVISION y corregidas el mismo día (D-49, D-50); `/design-review` lean del 2026-10-25, NEEDS REVISION (F4 solo medía Tres Tiempos), corregida; `/design-review` full del 2026-10-25, NEEDS REVISION (dominio de la configuración, salidas vacías, F4, tema trampa), corregida; pendiente de re-revisión full
> **Creative Director Review (CD-GDD-ALIGN)**: NEEDS REVISION 2026-10-24 (re-revisión full: Waite III §4), corregida
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-25
> **Last Verified**: 2026-10-24
> **Implements Pillar**: Pilar 3 (Memoria Pura: significado público), Pilar 6 (No hay Carta Mala), D-05 (tarot real)

## Summary

La Base de Datos de Cartas es el catálogo de las 78 cartas del mazo Smith 1909. Guarda los datos públicos de cada carta y de 2 a 3 palabras clave por orientación (1 en unas pocas excepciones), cada una con un tema de la Taxonomía y una fuente tradicional citada. Los temas salen de la tradición de 1909 y no se fuerzan: el mazo garantiza solo que cada tema exista en alguna carta y que ninguna familia desaparezca de un mazo. La verdad del cliente se sortea según lo que el mazo activo puede decir (D-48). El jugador ve este catálogo en el tooltip de cada carta.

> **Quick reference** — Layer: `Foundation` · Priority: `MVP` · Key deps: `Taxonomía de Temas y Roles`

## Overview

La Base de Datos de Cartas es el catálogo de las 78 cartas del mazo Smith 1909 (tradición Rider-Waite-Smith, arte de 1909 de dominio público). Guarda los datos públicos de cada carta:

- nombre;
- número;
- palo, o Arcano Mayor;
- elemento;
- palabras clave derechas e invertidas, cada una asociada a exactamente un tema de la Taxonomía (R7).

Es un catálogo fijo: se carga una vez y no cambia durante la partida.

Este sistema solo dice qué es cada carta y qué puede decir. Los otros sistemas toman de él lo que necesitan:

- **Mazo y Robo** baraja y reparte. De acá toma qué cartas forman cada Nivel de Mazo.
- **La Gramática** combina las cartas de la tirada. De acá lee el palo, el elemento y el número.
- **Interpretación** ofrece al jugador las palabras clave de la orientación que salió.
- **El Tapete** las muestra en el tooltip.
- **Resonancia** compara la lectura con la verdad. No toca este catálogo directamente: recibe los temas a través de Interpretación.

Además, el catálogo define qué cobertura de temas tiene que tener el mazo. De esa cobertura depende que una tirada le dé al jugador algo con qué trabajar (Pilar 6).

Sin este catálogo, la promesa de D-05 (tarot real, significados tradicionales) no tendría dónde vivir. Tampoco habría forma de conectar lo que sale en la mesa con la verdad del cliente, que la Taxonomía expresa en temas.

## Detailed Design

### Core Rules

> Revisado en modo full el 2026-10-24 (`game-designer`, `systems-designer`, `qa-lead`, `creative-director`). Sin consultar a `writer`: los textos de las palabras clave se revisan con AC-11.

**El mazo**

1. El catálogo tiene exactamente las **78 cartas** del Smith 1909:
   - 22 Arcanos Mayores, numerados 0 a 21 en el orden de 1909 (la Fuerza es el 8 y la Justicia el 11);
   - 4 palos de 14 cartas: As a 10, más Sota (11), Caballero (12), Reina (13) y Rey (14).
2. Cada carta tiene un **identificador estable** con prefijo `carta.`: `carta.mayor_00` a `carta.mayor_21`, y `carta.<palo>_01` a `carta.<palo>_14`. Igual que en la Taxonomía (R4), un identificador nunca se renombra ni se borra, y el nombre visible sale de la tabla de idioma.
3. Campos de cada carta:

   | Campo | Valores | Nota |
   |---|---|---|
   | `id` | ver R2 | |
   | `arcano` | mayor / menor | |
   | `palo` | copas / oros / espadas / bastos; vacío en los Mayores | |
   | `numero` | 0–21 (Mayores), 1–14 (Menores) | Lo usa la Gramática para los números repetidos (§3.5.6) |
   | `elemento` | fuego / agua / aire / tierra / ninguno | Menores: Copas = agua, Oros = tierra, Espadas = aire, Bastos = fuego (coincide con R1 de la Taxonomía). Mayores: según la atribución de la Golden Dawn (§3.2); `ninguno` para las 7 planetarias hasta que se decida (Open Questions) |
   | `atribucion` | Mayores: signo, planeta o elemento de la Golden Dawn. Menores 2 a 10: signo y planeta del decanato según el *Book T*. As y figuras (Sota, Caballero, Reina, Rey): vacía | Dato público del tooltip. En los Mayores de acá sale `elemento`; en los Menores `elemento` sale siempre del palo, nunca del decanato. La tabla de decanatos se verifica contra el *Book T* al cargar los datos (Open Questions) |
   | `arte` | referencia a la imagen de 1909 | Nunca la recoloración de 1971 (§3.1) |
   | `derecha`, `invertida` | de 2 a 3 palabras clave cada una (1 en las excepciones de R4) | R4 a R6 |

**Palabras clave**

4. Cada orientación tiene **de 2 a 3 palabras clave** (GDD §3.2). Los límites salen de la perilla de Tuning Knobs, no del código. **Excepción:** las orientaciones de una lista cerrada `orientaciones_con_una` (un archivo de datos) pueden tener **1 sola**. Entran ahí solo cuando ninguna fuente de la lista da más de un significado para esa orientación (E2). Cada entrada nombra una orientación que existe, aparece una sola vez y anota las fuentes que se buscaron; si no, es un error de R4 con la entrada como sujeto. Cada palabra clave tiene:
   - un identificador `<id de carta>/<derecha|invertida>/<n>`, con `n` de 1 hasta el máximo de la perilla;
   - un texto, que sale de la tabla de idioma;
   - **exactamente un tema base** (R7 de la Taxonomía);
   - una `fuente`, de la lista cerrada `waite_1910`, `book_t` o `mathers_1888`, y una `ubicacion` (página o sección, nunca vacía), para que R6 se pueda verificar. Con `waite_1910`, la `ubicacion` empieza por la sección: `III§2` (Menores), `III§3` (Mayores) o `III§4` (*Some Additional Meanings of the Lesser Arcana*, solo Menores);
   - `forzada` (sí / no, por defecto no): sí cuando el tema es el más cercano disponible porque la tradición no da uno claro (R6, E2).

   **Waite III §4 (D-50).** Cuenta como `waite_1910`, con dos límites. Al elegir las palabras clave de una orientación, primero van los significados de §2 y §3, y §4 entra solo para completar lugares o familias. Además, no se toma de §4 un significado que contradiga de frente a uno principal de la misma orientación: el mismo Waite avisa que los adicionales "very often" no coinciden con los principales. Una orientación sin ningún significado en ninguna fuente de la lista es un error de R4 con la orientación como sujeto: no se inventa una lectura (R6).
5. **Sin cobertura forzada por carta.** Las palabras clave de una orientación pueden repetir familia y hasta tema: la variedad la da la tradición, no una regla (D-48). Cuando una orientación tiene más significados tradicionales que lugares, se eligen los que cubren familias distintas y, a igual familia, temas distintos: cada tema más es una elección más para el jugador (Pilar 6). Contadas las 78 cartas contra Waite (1910), una orientación tiene en promedio ~1,3 familias claras (Formulas; conteo previo a III §4, pesimista para los Menores).
6. **El texto manda sobre el tema.** Cada palabra clave es un significado tradicional de la carta (D-05), tomado de la tradición de 1909 (por ejemplo, *The Pictorial Key to the Tarot* de Waite, 1910, de dominio público). El tema se deriva del texto (§3.2). Nunca se inventa un significado para cumplir la cobertura (F2). Cuando el significado es real pero ningún tema encaja con claridad, se asigna el tema más cercano y la palabra clave se marca `forzada` (E2). Marcar como clara una que no lo es incumple esta regla, y lo revisa AC-11. Una palabra clave `forzada` se puede leer y da EXACTO o PARCIAL como cualquier otra, pero en el sorteo (F1) pesa `w_forz`, no hace sorteable a un tema por sí sola, y no cuenta para el piso F2 ni para R7.

**Cobertura del mazo**

7. **Cada tema base activo aparece en al menos una palabra clave clara de las 78 cartas.** Un mazo concreto puede no tener algún tema (por ejemplo, *riesgo* no está en Mayores + Copas). Eso no rompe nada, porque el Generador solo sortea temas que el mazo activo dice con claridad (F1, D-48). Un tema con una sola orientación clara en las 78 cartas (hoy, *culpa*) es frágil: si una relectura de los datos la reclasifica, R7 falla. El informe lo marca (R11).
8. **Los Mayores apuntan a cualquier familia.** La familia es del tema, no de la carta: los Mayores no van atados a Destino. Las "fuerzas fuera de tu control" de los Mayores las cubre la regla de peso de la Gramática (§3.5.5), no este catálogo. En cada mazo alcanzable (los 22 Mayores más cualquier combinación de palos, E1), cada familia aparece en al menos `q_mil` milésimos de las orientaciones (`q_f`, F2; hoy 10 %), contando solo palabras clave claras: ninguna familia puede desaparecer de un mazo.
9. Todos los datos de una carta son **públicos** (D-08, Pilar 3): nada de este catálogo es secreto ni se desbloquea.

**Validación**

10. Las reglas R1 a R8 (incluidas la lista de excepciones de R4, el campo `forzada` y la orientación sin fuente), F2 y `MAZO_SIN_VERDADES` (F1) se agregan al validador del catálogo (R13 de la Taxonomía). Un incumplimiento es un error de datos y el juego no arranca. Los sujetos de los errores siguen el formato de R13 de la Taxonomía: carta, orientación, palabra clave o mazo. Los códigos de error y sus casos se definen en las historias de implementación, no en este GDD.
11. **Informe de cobertura.** Para cada mazo alcanzable (E1), el validador produce un informe con:
    - por tema: `n_t^clara`, `n_t^forz`, `n_t`, `n_t⁺` y `p_t` (F1), con los temas frágiles (R7) marcados;
    - por familia: `c_f`, `c_f⁺`, `q_f`, `q_f⁺`, `u_f`, `p_f`, `P_fallo_f` y `P_cero_f` (F3, F4), con la marca de `P_fallo_max`. Con `p_f` = 0 (la familia nunca sale como verdad, E5), `P_fallo_f` y `P_cero_f` se muestran vacíos y no marcan;
    - por mazo: la cantidad de palabras clave `forzada`, las orientaciones sin elección (todas sus palabras clave del mismo tema, o una sola), los **temas trampa** (temas activos que en el mazo aparecen solo en palabras clave forzadas: se pueden leer y nunca son la verdad, E9), los **deprecados presentes** (temas deprecados con alguna palabra clave en el mazo; tampoco son nunca la verdad, E5, pero no son trampa), `P_exacto`, `P_pos`, `P_pos⁺`, `P_pos_inv`, `P_cero` y `P_cero_corr` para cada `k` de `k_tiradas` (F3, F4) y `V_prior` (F5), con las marcas de F4 (progresión, una por cada mazo Aprendiz que contiene) y F5. Una cifra vacía (Formulas, Salidas vacías) no dispara ninguna marca.

    El informe no es una lista de errores, y ninguna marca impide arrancar el juego. Sirve para calibrar, y de él lee el Generador los pesos `p_t` del mazo activo (D-48). `q_f ≤ u_f ≤ 2·q_f` vale por construcción (cada carta aporta 0, 1 o 2 orientaciones a `c_f`): no es una regla de datos sino un invariante que prueba la implementación del informe (AC-18e).
12. **Interfaz** (amplía R13 de la Taxonomía). Todas son funciones puras, sin estado:
    - `validar_catalogo` recibe además, de Cartas: `config` (las perillas de Tuning Knobs), `orientaciones_con_una` y el oráculo `atribuciones_gd`, un archivo de datos con una fila por Mayor y por decanato. El oráculo se transcribe a mano desde un escaneo de dominio público del *Book T*, con la página en cada fila, en un commit anterior a los datos de las cartas; nunca se deriva del catálogo. El validador compara contra él la `atribucion` de cada Mayor y de cada Menor 2 a 10, y el `elemento` de cada Mayor;
    - `informe_cobertura(cartas, catálogo, config) → informe por mazo alcanzable` (R11);
    - `informe_mazo(mazo, cartas, catálogo, config) → informe` y `validar_mazo(mazo, cartas, catálogo, config) → lista de errores` (F2 y `MAZO_SIN_VERDADES` de un mazo): las mismas cuentas para un mazo cualquiera, alcanzable o no, para probar F1 a F5. `informe_cobertura` y `validar_catalogo` las llaman con cada mazo alcanzable;
    - `chequear_informe(informe) → lista de violaciones`: comprueba los invariantes del informe (`q_f ≤ u_f ≤ 2·q_f`, `Σ p_t` = 1 o 0, `c_f ≤ c_f⁺`). Es una herramienta de prueba, no de datos;
    - `acierto_posible(carta, orientación, tema verdadero, catálogo) → EXACTO | PARCIAL | NINGUNO`: el mejor resultado que permite alguna palabra clave de esa orientación, claras y forzadas. **Necesita la verdad, así que nunca alimenta nada que el jugador vea o pueda inferir durante la partida** (Pilar 1): la usan el informe, las pruebas, la telemetría y el diseño de la palanca de Tiradas y Resonancia (E7). No basta con la convención: la función vive fuera del código de juego, en el módulo de herramientas y pruebas, y ningún sistema de juego la llama (AC-26);
    - `MAZO_SIN_VERDADES`: el mazo no tiene ningún tema sorteable (F1). Sujeto: el mazo, en el formato de R13 sin familia (`copas+oros`).

### States and Transitions

El catálogo no tiene estados: se carga una vez y no cambia durante la partida.

Entre versiones:

- Una carta nunca se borra ni cambia de identificador.
- El texto y el tema de una palabra clave **pueden** cambiar entre versiones. La partida guardada guarda la verdad del cliente, no las palabras clave, así que el cambio solo afecta a las lecturas que se hagan después.
- Una palabra clave puede seguir apuntando a un tema deprecado (Taxonomía, States).

### Interactions with Other Systems

| Sistema | Qué recibe de Cartas | Qué aporta o devuelve |
|---|---|---|
| Taxonomía de Temas y Roles | — | Los temas y familias que validan las palabras clave (R7) |
| Mazo y Robo | La lista de cartas por arcano y palo | Arma el mazo de cada Nivel de Mazo y reparte |
| Gramática de Combinación | `palo`, `elemento` y `numero` | Nada; los usa para dignidades, palo dominante y números repetidos |
| Interpretación y Sentencia | Las palabras clave de la orientación que salió (de 1 a 3) y su tema | La palabra clave elegida por posición |
| Tiradas y Resonancia | `acierto_posible` (R12), solo para diseñar y calibrar | Definen la palanca del Pilar 6 ante una carta muda, sin consultar la verdad en juego (E7) |
| Generador de Situaciones | Los pesos `p_t` del mazo activo (R11, F1) | Sortea el tema verdadero de cada rol con esos pesos (D-48) |
| Tapete y Tooltips | Nombre, número, palo, `atribucion`, elemento, arte, y las palabras clave con su tema y familia | Nada; los muestra |
| Prestidigitación (indirecta, a través de Mazo y Robo) | La invertida de cada carta (para *invertir*) | Nada |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD salvo la Taxonomía. En particular, el sorteo de F1 es un contrato provisorio con el Generador: este puede filtrar o reescalar `p_t` (por arquetipo, por coherencia entre roles, por `afinidad_por_rol`, ver Open Questions de la Taxonomía). Lo único que Cartas garantiza es que la verdad sorteada sea decible por el mazo activo, y eso es parte del contrato: el Generador puede bajar o subir pesos, pero **ningún arquetipo ni restricción puede sortear un tema con `p_t` = 0 en el mazo activo**. Si un arquetipo exige un tema que el mazo no dice, el Generador elige otro arquetipo o otro tema; nunca la verdad.

## Formulas

Contadas las 78 cartas contra Waite (1910) —asignaciones claras, sin forzar; detalle en `design/balance/cobertura-cartas-waite.md`—, la tradición da en promedio **~1,3 familias por orientación**, y entre 11 y 18 de las 72 orientaciones de un mazo Aprendiz no tienen ningún tema claro (17 en Mayores + Copas). Por eso el mazo no puede garantizar cobertura alta por posición, y la cobertura se resuelve del lado de la verdad: el Generador sortea lo que el mazo puede decir (F1). F2 la comprueba el validador; F1 es el contrato con el Generador; F3 a F5 son calibración y salen en el informe (R11).

> **Cifras previas a III §4 (D-50).** El conteo usó solo Waite III §2 y §3, y no los significados adicionales de III §4, que dan una derecha y una invertida más a cada una de las 56 menores. Todas las cifras de esta sección son, por eso, **pesimistas** para los Menores: menos familias por orientación y más `P_cero` que con §4. Se rehacen con el reconteo (Open Questions), que es condición antes de cargar los datos y antes del prototipo. Además cuentan solo claras, así que están del lado pesimista también por las forzadas (F3).

Un **acierto de familia** es que la carta, en la orientación que salió, tenga una palabra clave **clara o forzada** de la familia de la verdad de su rol: es la condición para PARCIAL o EXACTO (R6). Un **acierto exacto posible** pide una palabra clave del mismo tema. `acierto_posible` (R12) da el mejor de los dos para una orientación y una verdad. Esta es la única definición de acierto de F3 y F4. F2 es otra cosa: un piso de datos, y cuenta solo claras (R6).

**Variables**

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `N` | int | 36 (Aprendiz) a 78 | Mazo y Robo | Cartas del mazo activo |
| `O` | int | `2·N` | calculated | Orientaciones del mazo |
| `n_t^clara` | int | 0 a `O` | calculated (catálogo) | Orientaciones con al menos una palabra clave **clara** del tema `t` |
| `n_t^forz` | int | 0 a `O` | calculated (catálogo) | Orientaciones con una palabra clave forzada del tema `t` y ninguna clara de `t` |
| `n_t` | float | 0 a `(1 + w_forz·k_forz)·n_t^clara` | calculated (F1) | Peso de sorteo: `n_t^clara + w_forz · min(n_t^forz, k_forz · n_t^clara)` |
| `n_t⁺` | int | 0 a `O` | calculated | `n_t^clara + n_t^forz`: orientaciones donde el exacto es posible |
| `c_f`, `c_f⁺` | int | 0 a `O` | calculated (catálogo) | Orientaciones con al menos una palabra clave clara de la familia `f`; `c_f⁺`, clara o forzada |
| `q_f`, `q_f⁺` | float | 0 a 1 | calculated | `c_f / O` y `c_f⁺ / O`: probabilidad de que una carta al azar, en una orientación al azar, tenga la familia `f` (solo claras, o claras y forzadas) |
| `u_f`, `u_f⁺` | float | 0 a 1 | calculated (catálogo) | Proporción de cartas cuya derecha o cuya invertida tiene una palabra clave de `f` (clara; clara o forzada). Por construcción, `q_f ≤ u_f ≤ 2·q_f`, y lo mismo con ⁺ |
| `p_t` | float | 0 a 1, suman 1 (o 0 si `T_m` = 0) | calculated (F1) | Probabilidad de que la verdad de un rol sea el tema `t` |
| `p_f` | float | 0 a 1 | calculated (F1) | `Σ p_t` de los temas de la familia `f`. Es el único `p_f` que usan F3 a F5 |
| `T_m` | int | 0 a 23 | calculated | Temas sorteables del mazo (F1). Con 0, `MAZO_SIN_VERDADES` |
| `w_forz` | float | 0 a 1 | data file | Peso de una forzada en el sorteo (Tuning Knobs) |
| `k_forz` | int | 0 a 3 | data file | Tope de forzadas que suman peso, por cada orientación clara del tema (Tuning Knobs) |
| `q_mil` | int | 0 a 1000 | data file | Piso de `q_f` en milésimos (hoy 100, o sea 10 %). Es el único valor guardado: no existe un `Q_min` decimal |
| `k` | int | 1 a 10 | Tiradas | Posiciones **comparables** de una tirada: con rol habilitado y no libres (Taxonomía R9, R11). Carta Única 1, Tres Tiempos 3 |
| `k_tiradas` | lista de int | valores de `k` | data file | Los `k` de las tiradas habilitadas en la build, para los que el informe calcula F4 (hoy 1 y 3). Sale del catálogo de Tiradas (Tiradas F1): las tiradas que se ofrecen en la build, con sus posiciones comparables |
| `ε_prog` | float | 0 a 0,05 | data file | Margen de la marca de progresión, en `P_pos⁺` (F4); hoy 0,005 |
| `P_fallo_max`, `V_prior_max` | float | 0 a 1 | data file | Umbrales de las marcas del informe (F3, F5); sin fijar hasta el prototipo |

Supuestos: la orientación sale 50/50 y la carta es uniforme dentro del mazo.

**Salidas vacías.** Cada fórmula de F3 a F5 se evalúa solo si sus entradas existen; si no, la cifra es **vacía** (no un número) y no dispara ninguna marca:
- con `T_m` = 0 (`MAZO_SIN_VERDADES`, F1) quedan vacíos `P_exacto`, `P_pos`, `P_pos⁺`, `P_pos_inv`, todos los `P_fallo_f`, `P_cero(k)`, `P_cero_corr(k)`, `P_cero_f(k)`, `V_prior` y `T_ef`. La fórmula literal daría `P_cero` = 1 y `P_cero_corr` = 0, dos números falsos;
- con `O` = 0 (mazo de prueba sin cartas) quedan además vacíos `q_f`, `q_f⁺`, `u_f` y `u_f⁺`, y el mazo da `MAZO_SIN_VERDADES`: no tiene temas sorteables. Ningún mazo alcanzable tiene `O` = 0;
- con `p_f` = 0, `P_fallo_f` y `P_cero_f` de esa familia (E5, R11).

**F1. Sorteo de la verdad según el mazo** (contrato con el Generador, D-48)

`n_t = n_t^clara + w_forz · min(n_t^forz, k_forz · n_t^clara)` · `p_t = n_t / Σ_s n_s`, sobre los temas **sorteables** del mazo activo: activos y con `n_t^clara` ≥ 1

- **Rango:** `p_t` = 0 para un tema que el mazo no tiene o que solo tiene como forzada. La verdad siempre es algo que el mazo dice con al menos un significado claro.
- **Degeneración:** si `Σ_s n_s` = 0 (ningún tema sorteable, por ejemplo un mazo cuyas claras apuntan todas a temas deprecados), el validador da `MAZO_SIN_VERDADES` con el mazo como sujeto (R12), todos los `p_t` valen 0 y F3 a F5 quedan vacíos. F1 nunca divide por cero.
- **Por qué las forzadas pesan menos:** el jugador puede leerlas y dan EXACTO, así que cuentan. Pero un tema que la tradición no dice con claridad no tiene que decidir qué verdad le toca al cliente (R6, D-48). Con `w_forz` = 0,5, cuentan la mitad.
- **Por qué el tope (D-50):** sin `k_forz`, una sola clara habilitaría todo el peso de las forzadas. Con `n_t^clara` = 1, `n_t^forz` = 30 y `w_forz` = 0,5, `n_t` daría 16: un tema casi todo forzado dominaría el sorteo. Con `k_forz` = 1 da 1,5. Con `k_forz` = 0 las forzadas no pesan, igual que con `w_forz` = 0.
- **Ejemplo:** *culpa* tiene 1 sola orientación clara en las 78 cartas (Ocho de Bastos invertida; conteo previo a §4). En Mayores + Bastos es sorteable, con `n_t` = 1, y sale como verdad muy rara vez. En Mayores + Espadas solo aparece como forzada (vergüenza y confesión), así que ahí `p` = 0: es un **tema trampa** (R11, E9). En Mayores + Copas no aparece.
- **Lo que no cambia:** el Generador sigue sin conocer la tirada (D-37). El mazo activo se fija con el Nivel de Mazo al empezar la partida y cambia solo al sumar un palo en una Sede.
- **Interfaz provisoria:** el Generador puede componer `p_t` con otras restricciones (Interactions), pero nunca darle peso a un tema con `p_t` = 0. La forma proporcional tiene un costo, que mide F5: cuanto más concentra `p_t`, más rinde apostar al tema más frecuente en vez de deducir.

**F2. Piso por familia** (lo comprueba el validador, en enteros)

`c_f · 1000 ≥ q_mil · O` para cada familia `f` y cada mazo alcanzable (E1)

- **Por qué en enteros:** `⌈0,07 · 100⌉` en coma flotante da 8 y no 7. Por eso el piso se guarda solo como `q_mil` entero: un valor con más de 3 decimales no se puede escribir, y no hay redondeo. Un `q_mil` que no es entero o está fuera de 0 a 1000 es un error de configuración y el juego no arranca. Dentro de ese intervalo, un valor fuera del rango seguro de Tuning Knobs no es un error.
- **Rango:** con `q_mil` = 100, `c_f` ≥ 8 con `O` = 72, ≥ 10 con 100, ≥ 13 con 128 y ≥ 16 con 156. Con `q_mil` = 1000 haría falta `c_f` = `O`.
- **Con los datos contados:** los 15 mazos lo cumplen. El mínimo es Destino en Mayores + Oros (9 de 72, `q` = 0,125). `c_f` cuenta solo palabras clave claras, que es lo que se contó: las forzadas no ayudan a cumplir el piso (R6). Las claras de temas deprecados sí cuentan (E5); si dejan una familia con `p_f` = 0, el informe lo muestra.
- **Por qué solo un piso:** una banda con techo obligaría a forzar significados (R6). El piso evita que una familia desaparezca, y con eso que el PARCIAL deje de existir para esa familia.

**F3. Acierto posible por posición** (calibración)

`P_exacto = Σ_t p_t · n_t⁺ / O` · `P_pos⁺ = Σ_f p_f · q_f⁺` · `P_pos = Σ_f p_f · q_f` · `P_fallo_f = 1 − q_f⁺` · `P_pos_inv = Σ_f p_f · u_f⁺`

- **Rango:** de 0 a 1. **`P_pos⁺` es la cifra principal**: cuenta lo que el jugador puede alcanzar, claras y forzadas. `P_pos`, con solo claras, es una cota inferior informativa (`P_pos ≤ P_pos⁺`).
- **Con los datos contados** (Mayores + Copas; previo a §4 y solo claras, así que es `P_pos`, no `P_pos⁺`): `q` = 0,31 / 0,26 / 0,31 / 0,28 / 0,17 (Emoción, Bienes, Conflicto, Ambición, Destino). El conteo todavía no tiene `n_t` por tema, así que el `p_f` de F1 no se puede calcular. Con la aproximación `p_f` ≈ parte de cada familia en `Σ c_f` (22/95, 19/95…), **`P_pos` ≈ 0,274**: acierto de familia posible algo más de 1 vez de cada 4. La aproximación no es el `p_f` de F1: una orientación con dos temas de la misma familia pesa doble en F1 y una vez en `c_f`, y las forzadas suman peso. Por eso la cifra no se usa para fijar umbrales; se recalcula con el reconteo (Open Questions).
- **Por familia:** `P_fallo_f` es la probabilidad de que una posición no tenga acierto posible cuando la verdad es de `f`. En Mayores + Copas (solo claras), Destino da **0,83**, contra 0,69 a 0,74 en las otras familias: el riesgo se concentra en los clientes de Destino. El informe marca la familia con `P_fallo_f` > `P_fallo_max`. Hasta que el prototipo fije el umbral, muestra el valor y no marca. Con `p_f` = 0 no se muestra (R11).
- **Con *invertir*:** `P_pos_inv` es una cota **teórica**: supone que *invertir* es gratis, ilimitado y que el jugador sabe cuándo conviene, o sea que conoce la verdad. Ninguna de las tres cosas es cierta, así que solo acota por arriba, y `(1 − P_pos_inv)³` acota `P_cero` por abajo. No hay cifra: el único detalle por carta del conteo es anterior a D-48, y su `u_f` no es compatible con los `q_f` de ahora (Destino: `u` 0,08 < `q` 0,17). Se calcula con el reconteo.
- "Posible" es una cota superior: el jugador no conoce la verdad.

**F4. Una tirada sin ningún acierto de familia** (calibración)

`P_cero(k) = (1 − P_pos⁺)^k` · `P_cero_f(k) = (1 − q_f⁺)^k` · `P_cero_corr(k) = Σ_f p_f · (1 − q_f⁺)^k`

- **`k`:** las posiciones comparables de la tirada. Las dos tiradas del MVP son Carta Única (`k` = 1) y Tres Tiempos (`k` = 3) (GDD §5.4 y MVP); el informe calcula F4 para cada `k` de `k_tiradas`. Una posición libre, o con un rol que la situación no contiene, da SIN_COMPARACION (Taxonomía R11) y no cuenta en `k`.
- **Rango:** de 0 a 1. `P_cero(k)` supone que los `k` roles sortean su verdad por separado; `P_cero_corr(k)`, que el Generador pone todos los roles en la misma familia. Por convexidad, `P_cero(k) ≤ P_cero_corr(k)`, y con las mismas marginales en todos los roles `P_cero_corr(k)` es el **máximo**. La independencia no es el mínimo: un Generador que reparte los roles en familias distintas queda por debajo (hoy, ~0,003 menos), y si el Generador cambia las marginales por rol (`afinidad_por_rol`), ninguna de las dos fórmulas es cota. Las dos son aproximaciones del caso real, no un intervalo que lo contenga. Con `k` = 1 los dos coinciden: `P_cero(1)` = `P_cero_corr(1)` = `1 − P_pos⁺`. `P_cero_f(k)` es el de un cliente con todas sus verdades en la familia `f`; con `k` = 1 es `P_fallo_f`.
- **Unidad:** cada posición de la tirada se compara con la verdad del rol que le asigna Tiradas, y solo con esa (Taxonomía R9). `P_cero(k)` es la probabilidad de que ninguna de las `k` posiciones tenga acierto de familia posible con su propio rol. Sin otro calificativo, `P_cero` en este GDD es `P_cero(3)`.
- **Con los datos contados, Tres Tiempos** (aproximación de F3; previo a §4 y solo claras): `P_cero(3)` ≈ 0,38 en Mayores + Copas y Mayores + Oros, 0,378 en Mayores + Espadas, 0,392 en Mayores + Bastos, y **0,403 en el mazo de 4 palos**. En Mayores + Copas, `P_cero_corr(3)` ≈ 0,387. Para un cliente de Destino, `P_cero_f(3)` ≈ **0,58** en Mayores + Copas y **0,67** en Mayores + Oros: el promedio esconde a esa familia. D-48 acepta el costo promedio; el de Destino se mide en el prototipo con clientes de Destino (Open Questions).
- **Con los datos contados, Carta Única:** `P_cero(1)` ≈ **0,73** en Mayores + Copas (`1 − 0,274`): unas 3 de cada 4 Cartas Únicas no pueden llegar ni a PARCIAL. Para un cliente de Destino, 0,83 en Mayores + Copas y 0,875 en Mayores + Oros. Es la tirada más expuesta del MVP y D-48 no la midió: la cifra que aceptó (0,38) es de Tres Tiempos.
- **El reconteo no resuelve Carta Única.** III §4 solo agrega significados a los Menores. En Mayores + Copas, 10 de las 17 orientaciones sin tema claro son de Mayores, y los Mayores aportan ~0,162 de los 0,274 de `P_pos` (Copas, ~0,111). Aunque cada orientación de Copas tuviera las 5 familias, `P_pos` ≤ 0,162 + 28/72 ≈ 0,55: `P_cero(1)` ≥ ~0,45 con claras. Con un aporte realista de §4, ~0,6–0,65. Las forzadas lo bajan algo más, pero no cambian el orden de magnitud. La solución, si hace falta, es estructural (otro rol para "Respuesta", una regla de Resonancia propia o una palanca propia) y es de Tiradas y Resonancia; Cartas solo deja la cota escrita. Qué rol cubre la posición "Respuesta" está abierto en la Taxonomía (Open Questions), y la palanca ante una Carta Única muda en Tiradas (E7).
- **Posible no es alcanzado:** `P_cero(k)` cuenta las tiradas donde **ninguna** elección da acierto de familia. Es una cota inferior del fallo real, porque el jugador elige sin conocer la verdad (F3). Además el Pilar 6 habla de "jugada útil", y este GDD no la define: no dice si un PARCIAL alcanza, ni si una lectura sin acierto puede ser útil por la Sentencia (Pilar 2). Tiradas y Resonancia la definen antes de que el prototipo fije `P_fallo_max` (Open Questions); hasta entonces, el acierto de familia posible es el sustituto.
- **La progresión:** el informe compara cada mazo de 2 o más palos con **cada** mazo Aprendiz que contiene, y marca el par (mazo, Aprendiz) cuando `P_pos⁺` del mazo < `P_pos⁺` del Aprendiz − `ε_prog` − 1e-9 (la tolerancia evita que una diferencia igual a `ε_prog` marque por la coma flotante). Compara `P_pos⁺` y no `P_cero`, así que no depende de `k` ni de `k_tiradas`: `P_cero(k) = (1 − P_pos⁺)^k` es monótona en `P_pos⁺`, y el orden entre mazos es el mismo para todo `k` **con independencia**. No vale para `P_cero_corr` ni `P_cero_f`: con el mazo A con `1 − q_f⁺` = 0,7 en todas las familias, y el B con 0,5 (`p_f` 0,6) y 0,95 (`p_f` 0,4), `P_cero_corr(1)` da 0,70 contra 0,68 y `P_cero_corr(3)` 0,343 contra 0,418: el orden se invierte. Una marca dice que un jugador que empezó con ese Aprendiz empeora el Pilar 6 al sumar palos. Con el conteo previo a §4, el mazo de 4 palos tiene `P_pos` ≈ 0,261 contra 0,268 a 0,277 de los 4 Aprendiz (`P_cero(3)` 0,403 contra 0,378 a 0,392) y marcaría contra los 4, pero **no es concluyente**: la diferencia es del tamaño del error de la aproximación de `p_f` (~0,025 en `P_cero(3)`, F3), y `ε_prog` = 0,005 queda por debajo del ruido de un conteo de una sola lectura. Se reevalúa con el reconteo. Cómo se compensa es una pregunta de Prestidigitación (Open Questions).
- **Palancas:** *invertir*, la relectura de una carta muda (E7, en Tiradas y Resonancia), la Sentencia (Pilar 2) y la forma del sorteo del Generador. Se miden en el prototipo.
- **Supuestos:** carta con reposición. Sacar sin reponer baja `P_cero` hasta ~0,013 con 36 cartas (0,364 contra 0,377 cuando las 3 verdades son de la misma familia) y menos con mazos más grandes. No se corrige porque es menor que la incertidumbre del conteo, y va hacia el lado optimista del error.

**F5. Ventaja del prior** (calibración)

`V_prior = max_t p_t` · `T_ef = 1 / Σ_t p_t²`

- **Rango:** `V_prior` va de `1/T_m` (todas las verdades igual de probables) a 1 (una sola verdad posible). `T_ef` va de 1 a `T_m`. Con `T_m` = 0 los dos quedan vacíos.
- **Qué mide:** `V_prior` es la probabilidad de acertar el tema exacto de un rol apostando siempre al tema más frecuente del mazo, sin mirar al cliente ni las cartas. `T_ef` es el número efectivo de verdades. El catálogo es público (Pilar 3), así que un jugador puede deducir esas frecuencias y apostar al tema más común en vez de deducir del cliente. Eso choca con el Pilar 1. Las dos son comparables entre mazos con distinto `T_m`.
- **El trade-off:** subir `P_pos⁺` concentrando el sorteo (`n_t^a`, a > 1) sube `V_prior` y baja `T_ef`. Toda forma de sorteo del Generador se mide contra `P_cero` y contra `V_prior` a la vez. El informe marca el mazo con `V_prior` > `V_prior_max`; el umbral lo fija el prototipo. Con `T_m` = 1, `V_prior` = 1 y marca con cualquier umbral menor que 1.
- **Con los datos contados:** no se puede calcular hasta tener `n_t` por tema.

## Edge Cases

1. **Mazos de otro tamaño.** El nivel Aprendiz suma un palo en las Sedes 3, 5 y 7 (§3.4), así que en el MVP también hay mazos de 50 cartas. El piso F2 vale para **todo mazo alcanzable**: los 22 Mayores más cualquier combinación de 1 a 4 palos, que son 15 mazos. Al sumar un palo, el Generador recalcula `p_t` con el mazo nuevo para los clientes siguientes; los ya generados no cambian.
2. **Una orientación no tiene en Waite ningún significado con tema claro** (entre 11 y 18 de 72 en un mazo Aprendiz y 17 en Mayores + Copas, según el conteo previo a III §4; con §4 serán menos en los Menores). En este orden:
   1. se busca primero en Waite III §4 si la carta es un Menor (con los límites de R4), y después en otras fuentes de dominio público de la misma tradición: el *Book T* de la Golden Dawn y Mathers (1888);
   2. si hay un significado real pero ningún tema encaja con claridad, se asigna el tema más cercano y la palabra clave se marca `forzada` = sí (R6). Cuenta para el sorteo (F1) y no para el piso (F2), y AC-11 las revisa todas;
   3. si ninguna fuente da más de un significado para la orientación, entra en `orientaciones_con_una` con 1 palabra clave (R4);
   4. si ninguna fuente da siquiera un significado, es un **error de datos** de R4 con la orientación como sujeto, y la carta no pasa AC-19. No hay lectura sintética (sale la "derecha debilitada", D-50): nunca se inventa un significado (R6). Hoy no se conoce ningún caso. El único que se creía, el Dos de Copas invertida, tiene significado en Waite III §4 (*"Passion"*).
3. **La misma palabra, el mismo tema o la misma familia en varias palabras clave de una carta.** Está permitido, en la misma orientación o entre derecha e invertida (R5).
4. **El mismo texto de palabra clave en varias cartas** (por ejemplo, *pérdida*). Está permitido: cada palabra clave tiene su propio identificador y su propio tema.
5. **Una palabra clave apunta a un tema deprecado.** Es válida (Taxonomía, States). Cuenta para `c_f`, `c_f⁺`, `u_f` y `u_f⁺`, porque su familia sigue dando acierto de familia contra verdades activas de esa familia. No cuenta para `n_t` de F1 ni para R7, que miran temas **activos**. Si una familia de un mazo queda cubierta solo por temas deprecados, cumple F2 pero tiene `p_f` = 0: nunca sale como verdad, y el informe deja vacíos su `P_fallo_f` y su `P_cero_f` (R11). Si el mazo entero queda sin temas sorteables, es `MAZO_SIN_VERDADES` (R12).
6. **Un Mayor con atribución planetaria.** Su `elemento` es `ninguno` hasta que se decida (Open Questions). Mientras tanto, la Gramática lo trata como neutro con cualquier vecina.
7. **La orientación que salió no tiene la familia de la verdad.** No hay acierto de familia posible en esa posición (una **carta muda**): el mejor resultado es NINGUNO. Cartas no lo compensa, pero lo informa: `acierto_posible` (R12) dice si la orientación es muda para una verdad. La palanca acordada es **releer esa carta pagando UT** (D-49); la regla vive en Tiradas y Resonancia, con dos condiciones que pone Cartas (D-50):
   - **La relectura es ciega.** Se ofrece por igual en cualquier posición, sin consultar `acierto_posible` ni la verdad: si solo se ofreciera ante una carta muda, le diría al jugador algo de la verdad, contra el Pilar 1. El jugador relee según su hipótesis, y eso es deducir.
   - **No choca con D-28.** La vela se consume por acción; releer es una acción con costo en UT, no tiempo real, así que no castiga la interpretación.
   - **Carta Única.** Con una sola posición, releer la carta es rehacer la tirada entera, y la muda es el caso más común (`P_cero(1)` ≈ 0,73, F4). Tiradas define si ahí la relectura cuesta lo mismo, si tiene otro tope y si sigue siendo más barata que la tirada (10 UT, GDD §5.4). Cartas solo exige que se mida con `k` = 1, no con el `P_cero` de Tres Tiempos.

   Las otras palancas son *invertir* (`P_pos_inv`, F3, cota teórica) y la Sentencia (Pilar 2), y la frecuencia se calibra con F3 (por familia) y F4.
8. **Falta el texto de una palabra clave en una tabla de idioma.** Es un error de datos del mismo tipo que `NOMBRE_FALTANTE` de la Taxonomía, con sujeto `<id de la palabra clave>@<tabla>`. El juego no arranca. Lo mismo con el nombre visible de una carta (sujeto `<id de carta>@<tabla>`).
9. **Un tema aparece en un mazo solo como forzada.** Se puede leer y da EXACTO, pero no es sorteable en ese mazo: `p_t` = 0 (F1), así que ese EXACTO nunca se alcanza en ese mazo. Es un **tema trampa**: el informe los lista por mazo (R11). Por ejemplo, *culpa* en Mayores + Espadas. Si el tooltip los distingue es decisión de `/ux-design` (UI Requirements).

## Dependencies

**Depende de:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Taxonomía de Temas y Roles | Dura | Temas base, familias y el validador del catálogo (R7 y R13 de la Taxonomía) |

**Dependen de Cartas:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Mazo y Robo | Dura | Lista de cartas por arcano y palo, para armar los mazos de cada Nivel |
| Gramática de Combinación | Dura | `palo`, `elemento` y `numero` |
| Interpretación y Sentencia | Dura | Las palabras clave de la orientación que salió (de 1 a 3) y su tema |
| Tiradas, Resonancia y Resolución | Dura | La palanca del Pilar 6 ante una carta muda (E7): el riesgo de F4 lo acepta D-48 contando con que esa palanca exista. Usan `acierto_posible` (R12) solo para diseñarla y calibrarla, nunca en juego |
| Tapete y Tooltips de Cartas | Dura | Todos los datos públicos de la carta y el arte |
| Prestidigitación | Blanda, indirecta | La invertida (*invertir*), a través de Mazo y Robo |
| Generador de Situaciones | Dura | Los pesos `p_t` del mazo activo, para sortear la verdad (F1, D-48) |

**Bidireccionalidad:**

- La Taxonomía ya nombra a Cartas en su tabla de dependientes.
- Los demás sistemas no tienen GDD todavía. La sección Dependencies de cada uno tiene que nombrar a Cartas cuando se escriba.
- El Generador depende de Cartas por F1: `systems-index.md` lo refleja (D-48).
- Tiradas y Resonancia dependen de Cartas por E7: `systems-index.md` lo refleja, con el pendiente de definir la palanca del Pilar 6 sin filtrar la verdad (D-50).

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Palabras clave por orientación | mínimo 2, máximo 3 | Mínimo 1 a 2, máximo 3 a 4. Con más no se gana cobertura si la tradición no la tiene, y el tooltip se recarga | Volumen de contenido, legibilidad del tooltip |
| `orientaciones_con_una` | lista cerrada (dato) | Solo orientaciones que ninguna fuente de la lista puede completar a 2 (E2). Cada entrada anota las fuentes que se buscaron | Volumen de contenido, cota de `P_pos` |
| `q_mil` (piso de `q_f` por familia, en milésimos) | 100 (10 %) | 50 a 110 con los datos contados. Destino en Mayores + Oros (9 de 72, 125 milésimos) pasa con 120 por 5 milésimos y falla desde 126, con un conteo de una sola lectura previo a III §4. Entero de 0 a 1000; fuera de eso es error de configuración (F2) | Que ninguna familia desaparezca de un mazo (F2) |
| `w_forz` (peso de una forzada en F1) | 0,5 | 0 a 1. Con 0 las forzadas no generan verdades; con 1 pesan como claras y el mazo "dice" temas que la tradición no dice con claridad. El prototipo compara `P_pos⁺`, `P_cero` y `V_prior` con 0, 0,5 y 1 | Distribución de verdades, `V_prior` |
| `k_forz` (tope de forzadas por clara en F1) | 1 | 0 a 3. Con 0 las forzadas no pesan; con más de 3, un tema casi todo forzado vuelve a dominar el sorteo | Distribución de verdades |
| `k_tiradas` (posiciones comparables para F4) | 1 y 3 | Los `k` de las tiradas habilitadas en la build. Se deriva del catálogo de Tiradas (Tiradas F1); la configuración solo lo fija en los fixtures | Qué cifras de F4 muestra el informe |
| `ε_prog` (margen de la marca de progresión, en `P_pos⁺`) | 0,005 | 0 a 0,02. Con el conteo actual, de una sola lectura, cualquier valor de este rango queda por debajo del ruido (F4); recalibrar con el reconteo | Solo la marca de progresión del informe (F4) |
| `P_fallo_max` | sin fijar | Lo fija el prototipo | Solo la marca por familia del informe (F3) |
| `V_prior_max` | sin fijar | Lo fija el prototipo | Solo la marca del informe (F5) |

El validador lee estos valores del archivo de configuración; no los tiene fijos en el código. Un valor fuera del rango seguro pero dentro de su **dominio** no es un error de configuración: el rango seguro es una guía de calibración. Un valor fuera del dominio sí es un error de configuración, con la clave como sujeto, y el juego no arranca (AC-17, AC-27). Con un error de configuración, el validador no valida los datos ni calcula el informe: devuelve solo los errores de configuración, para no listar cientos de errores de datos que salen de una perilla mal escrita. Dominios:

- `q_mil`: entero de 0 a 1000 (F2). Con más de 600 ningún mazo puede pasar F2 (5 familias, como máximo 3 palabras clave por orientación), pero no es un error de configuración;
- mínimo y máximo de palabras clave: enteros, con 1 ≤ mínimo ≤ máximo;
- `w_forz`: de 0 a 1. Con un valor negativo `n_t` puede dar negativo y `p_t` deja de ser una distribución; con más de 1, una forzada pesa más que una clara (contra R6);
- `k_forz`: entero de 0 a 3;
- `k_tiradas`: lista no vacía de enteros distintos de 1 a 10;
- `ε_prog`: de 0 a 0,05;
- `P_fallo_max` y `V_prior_max`: de 0 a 1, o sin fijar. La forma del sorteo de F1 (proporcional a `n_t`) es una perilla del Generador, no de este catálogo.

## Visual/Audio Requirements

- El arte de cada carta es el escaneo de la edición de 1909 (Pamela Colman Smith), nunca la recoloración de 1971 (§3.1). La fuente de referencia de los escaneos la fija `/art-bible`, con validación legal previa a la producción de arte (§3.1).
- Una carta invertida es la misma imagen rotada 180°; no hay arte propio para la invertida.
- No hay sonido propio de este sistema.

## Game Feel

No aplica: el catálogo no se opera directamente. El feel de robar y dar vuelta una carta le corresponde a Mazo y Robo y al Tapete.

## UI Requirements

- El tooltip de una carta muestra sus datos públicos: nombre, número, palo o Arcano Mayor, atribución y elemento.
- Muestra también las palabras clave de **las dos orientaciones** (Pilar 3, §3.3), con la orientación que salió destacada. Cada palabra clave lleva su tema y su familia, con la marca de la familia (Taxonomía, UI Requirements).
- La `fuente` y la `ubicacion` no se muestran en el MVP; mostrarlas como cita es decisión de `/ux-design`. También lo es si se marcan las palabras clave `forzada` y los temas trampa del mazo activo (E9): mostrar igual que una clara un significado que la tradición no respalda roza la Regla Cero.

> 📌 **UX Flag — Base de Datos de Cartas:** con las perillas actuales, el tooltip muestra de 4 a 6 palabras clave con tema y familia (3, o 2, si una o las dos orientaciones están en `orientaciones_con_una`; hasta 8 con el máximo de 4 por orientación). Antes de las historias del tooltip hay que hacer su spec con `/ux-design`, junto con el de la Taxonomía, incluida la legibilidad en Switch portátil.

## Cross-References

| Fuente | Qué se toma |
|---|---|
| GDD §3.1, §3.2, §3.3 | Smith 1909 y restricciones legales; anatomía de la carta; datos públicos |
| GDD §3.4 | Niveles de Mazo; los palos que se suman en las Sedes 3, 5 y 7 (E1) |
| GDD §3.5 | Elemento, palo y número para la Gramática; peso de los Mayores |
| GDD §5.5, §9.2 | Interpretación por palabra clave; el truco *invertir* |
| D-05, D-06, D-08, D-09, D-18, D-22 | Tarot real; escuelas; significado público; robo al azar; 78 cartas; Nivel de Mazo |
| D-47 | `fuente`, informe de cobertura y sujetos de R13 |
| D-48 | Conteo de las 78 cartas contra Waite (1910); cobertura según la tradición; piso por familia; sorteo de la verdad según el mazo; 3 temas de resultado en la Taxonomía |
| Revisión full del 2026-10-24 (`reviews/base-de-datos-de-cartas-review-log.md`) | Peso de las forzadas en F1, marcas por familia y de progresión, relectura de la carta muda |
| D-50 (re-revisión full del 2026-10-24) | Waite III §4 como fuente, salida de la derecha debilitada, tope `k_forz`, acierto sobre `c_f⁺`, relectura ciega |
| `/design-review` lean del 2026-10-25 | F4 con `k` posiciones comparables (Carta Única), "jugada útil" pendiente, `acierto_posible` fuera del código de juego (AC-26), cartas de la build del MVP en AC-11 |
| `/design-review` full del 2026-10-25 | Dominio de la configuración (AC-27), salidas vacías, progresión sobre `P_pos⁺`, cotas de F4 corregidas, tema trampa solo con forzadas, cota de Carta Única, AC-11c |
| Taxonomía R4, R7, R13, States | Identificadores; un tema por palabra clave; validador y formato de sujetos; temas deprecados |

## Acceptance Criteria

Convenciones de prueba:
- Todo AC parte de `fixture_catalogo_valido` (78 cartas sintéticas con ids reales, textos centinela y `taxonomia_prueba`) y lo **muta en un solo punto**. Las excepciones lo dicen: AC-15b y AC-15e redistribuyen una familia entera, y AC-17 cambia configuración y datos a la vez. AC-01 prueba que el fixture sin mutar pasa limpio.
- **Configuración y oráculo fijos.** Salvo que el AC diga otra cosa, todo AC usa `config_prueba` (mínimo 2 y máximo 3 palabras clave, `q_mil` = 100, `w_forz` = 0,5, `k_forz` = 1, `k_tiradas` = 1 y 3, `ε_prog` = 0,005, `P_fallo_max` y `V_prior_max` sin fijar) y `atribuciones_gd_prueba`, un oráculo de prueba escrito a mano con la forma de `atribuciones_gd` (R12) y separado del fixture. Ningún AC Logic lee la configuración ni el oráculo de producción.
- **Reparto del fixture.** Cada familia tiene en `fixture_catalogo_valido` 6 orientaciones con palabra clave clara en los Mayores y 3 en cada palo, así que `c_f` = 9, 12, 15 y 18 en los mazos de 1 a 4 palos: todos pasan F2 con margen. La tabla va con el fixture. *taxonomia_prueba* usa las familias reales: *amor* y *duelo* en Emoción, *deuda* y *fortuna* en Bienes, *traición* en Conflicto, *muerte* y *locura* en Destino.
- Cada error se verifica por la regla de la que es (con el código que fije la historia) y por su sujeto en formato R13 de la Taxonomía. Los controles dicen "ningún error de la regla X cuyo sujeto empiece por S", nunca "no hay errores". Si la mutación produce por fuerza un segundo error, el AC lo nombra.
- Que el juego no arranque lo prueban AC-25a/b de la Taxonomía; que cada palabra clave tenga exactamente un tema, AC-03a–c de la Taxonomía. No se repiten acá.
- Las funciones de R12 (`informe_mazo`, `validar_mazo`, F1 a F5 y las marcas) aceptan entradas arbitrarias: los AC del informe usan mazos de prueba que no son alcanzables.
- **Tolerancias:** ± 1e-9 en los valores exactos; ± 0,001 en los que se dan redondeados a 3 cifras, salvo que el AC diga otra.
- **Evidencia:** todos son Logic (test unitario en `[test root]/cartas/`), salvo los marcados Integration. Los *provisorios* dependen de un GDD que no existe y no bloquean hasta que exista.
- **Prototipo del núcleo:** AC-04c, AC-04f, AC-20 y AC-26, el oráculo `atribuciones_gd` y los campos `atribucion` y `arte` **no son requeridos** para el prototipo del núcleo de lectura (`/prototype`), que solo necesita cartas, palabras clave, temas y el informe. Bloquean las historias de producción, no el prototipo.

**Estructura**
- **AC-01** (R1–R8, R10, F2) — GIVEN `fixture_catalogo_valido`, `config_prueba` y `atribuciones_gd_prueba`, WHEN se valida, THEN la lista está vacía.
- **AC-02a** (R1) — GIVEN el fixture sin `carta.copas_05`, WHEN se valida, THEN contiene error de R1 con sujeto `carta.copas_05`.
- *AC-02b se retiró el 2026-10-24: era ambiguo entre R1 y R3; el caso pasó a AC-04e. Su número no se reutiliza.*
- **AC-03** (R2; parametrizado) — GIVEN el fixture con `carta.copas_05` renombrada a `carta.copas_15`, `carta.mayor_22`, `carta.copas_5` o `carta.copos_05` (un caso cada uno), WHEN se valida, THEN contiene error de R2 con el id nuevo como sujeto, y error de R1 con sujeto `carta.copas_05` (la carta que falta). Con una segunda carta de id `carta.copas_05` en lugar de `carta.copas_06`, contiene error de R2 con sujeto `carta.copas_05` y de R1 con sujeto `carta.copas_06`.
- **AC-04a** (R3) — GIVEN el fixture con `carta.copas_05` de elemento fuego, WHEN se valida, THEN contiene error de R3 con sujeto `carta.copas_05`.
- **AC-04b** (R3) — GIVEN el fixture con `carta.mayor_04` de elemento agua cuando `atribuciones_gd_prueba` dice fuego, WHEN se valida, THEN contiene error de R3 con sujeto `carta.mayor_04`. Control: un Mayor planetario con `ninguno` no da ningún error de R3 cuyo sujeto empiece por su id.
- **AC-04c** (R3, R12; Integration) — GIVEN los datos reales y el oráculo `atribuciones_gd` transcripto desde el escaneo del *Book T* (R12), WHEN se cargan, THEN las 22 atribuciones de los Mayores y los 36 decanatos de los Menores 2 a 10 coinciden con el oráculo; `carta.mayor_08` tiene Leo y `carta.mayor_11` Libra; los 7 planetarios tienen elemento `ninguno`, y cada palo el elemento de R3. La evidencia anota la página del escaneo de cada fila del oráculo.
- **AC-04d** (R3; parametrizado) — GIVEN el fixture con `carta.copas_05` sin decanato, o con `carta.copas_01`, `_11`, `_12`, `_13` o `_14` con decanato (un caso cada uno), WHEN se valida, THEN contiene error de R3 con sujeto esa carta.
- **AC-04e** (R3; parametrizado) — GIVEN el fixture con uno de estos 6 cambios: `carta.mayor_09` con número 8 (el id es válido, así que es R3 y no R2); `carta.mayor_04` con palo copas; `carta.copas_05` sin palo; `carta.copas_05` con elemento `metal`; `carta.copas_05` con arcano `medio`; `carta.copas_05` con `arte` vacío. WHEN se valida, THEN contiene error de R3 con sujeto la carta cambiada.
- **AC-04f** (R3, R12; parametrizado) — GIVEN el fixture con `carta.copas_05` con el decanato de `carta.copas_06` según `atribuciones_gd_prueba`, o con `carta.mayor_08` con atribución Libra (un caso cada uno), WHEN se valida, THEN contiene error de R3 con sujeto esa carta. Control: con la atribución del oráculo, ningún error de R3 cuyo sujeto empiece por esa carta.

**Palabras clave**
- **AC-05a** (R4) — GIVEN el fixture con 1 palabra clave en `carta.copas_05/derecha`, que no está en `orientaciones_con_una`, WHEN se valida, THEN contiene error de R4 con ese sujeto. Lo mismo con 4 (máximo 3 en `config_prueba`). Control: con 2 y con 3, no lo contiene.
- **AC-05b** (R4, Tuning Knobs) — GIVEN `config_prueba` con máximo 4 palabras clave por orientación y `carta.copas_05/derecha` con 4, la cuarta con id `carta.copas_05/derecha/4`, WHEN se valida, THEN no contiene error de R4 con ese sujeto ni de identificador.
- **AC-05c** (R4, E2) — GIVEN `carta.copas_02/invertida` en `orientaciones_con_una` con 1 palabra clave, WHEN se valida, THEN no contiene error de R4 con ese sujeto. Con 2, tampoco (la lista permite 1, no obliga). El caso con 0 lo cubre AC-24.
- **AC-05d** (R4; parametrizado) — GIVEN `orientaciones_con_una` con una entrada `carta.copas_15/derecha` (no existe), una entrada repetida, o una entrada sin las fuentes buscadas (un caso cada uno), WHEN se valida, THEN contiene error de R4 con sujeto la entrada en formato R13 de la Taxonomía.
- **AC-05e** (R4; parametrizado) — GIVEN el fixture con una palabra clave de id `carta.copas_05/derecha/0`, o con id `carta.copas_05/derechaa/1` (un caso cada uno), WHEN se valida, THEN contiene error de R4 con sujeto ese id. Con `carta.copas_05/derecha/1` y `/3` sin `/2`, contiene error de R4 con sujeto `carta.copas_05/derecha`.
- **AC-06** (R5, E3; parametrizado) — GIVEN `carta.copas_05/derecha` con sus 3 palabras clave de la misma familia, o `carta.copas_05` con el mismo tema en la derecha y en la invertida (un caso cada uno), WHEN se valida, THEN no contiene ningún error cuyo sujeto empiece por `carta.copas_05`. Control positivo: con una de esas palabras clave sin `fuente`, contiene error de R4 con su id (la prueba ve esa carta).
- *AC-07 se retiró el 2026-10-24 (D-48: no hay mínimo de familias por carta). Su número no se reutiliza.*
- **AC-08** (R7) — GIVEN el fixture donde `tema.locura` no aparece en ninguna palabra clave de las 78 cartas, WHEN se valida, THEN contiene error de R7 con sujeto `tema.locura`. Control: si aparece en una sola palabra clave clara, no lo contiene; si aparece solo en palabras clave forzadas, sí.
- **AC-09a** (E5) — GIVEN el fixture con `tema.traicion` deprecado y el mazo `copas` con `c_Conflicto` = 8, donde una de esas orientaciones tiene como única palabra clave de Conflicto una de `tema.traicion` (sin ella `c_Conflicto` sería 7), WHEN se valida, THEN no contiene error de F2 con sujeto `copas/familia.conflicto`. Es el par de AC-15a, donde 7 sí da error.
- **AC-09b** (E5, F1) — GIVEN un mazo de prueba con `n_t^clara` = 2 para `tema.amor`, 2 para `tema.deuda` y 4 para `tema.traicion` deprecado, WHEN se pide el informe, THEN `p_traicion` = 0 y `p_amor` = `p_deuda` = 0,5.
- **AC-09c** (E5, R7) — GIVEN `tema.locura` deprecado y sin ninguna palabra clave, WHEN se valida, THEN no contiene error de R7 con sujeto `tema.locura`.
- **AC-09d** (E5) — GIVEN un mazo de prueba de 2 cartas (`O` = 4) con una orientación cuya única palabra clave es clara y de `tema.traicion` deprecado, y otra con una clara de `tema.amor`, WHEN se pide el informe, THEN `c_Conflicto` = 1, `c_Conflicto⁺` = 1, `u_Conflicto` = 0,5, `p_traicion` = 0, `p_Conflicto` = 0, y `P_fallo_Conflicto` y `P_cero_Conflicto` vacíos.
- **AC-10** (R4; parametrizado) — GIVEN `carta.copas_05/derecha/1` sin `fuente`, con una `fuente` fuera de la lista, con `ubicacion` vacía, con `fuente` `waite_1910` y `ubicacion` que no empieza por `III§2`, `III§3` o `III§4`, o `carta.mayor_04/derecha/1` con `ubicacion` `III§4` (un caso cada uno), WHEN se valida, THEN contiene error de R4 con ese id como sujeto. Control: `carta.copas_05/derecha/1` con `waite_1910` y `III§4`, no. Que el texto salga de la fuente citada, y la prioridad de §2 y §3 sobre §4 (R6, R4), no los puede juzgar el validador: los cubre AC-11.
- **AC-11** (R4, R6; Integration, revisión documentada; bloquea la historia de contenido) — GIVEN los datos reales, WHEN se revisan: (a) todas las palabras clave de las cartas de cualquier mazo que pueda armar la build del MVP (Aprendiz en las Sedes 1 a 3: los 22 Mayores, el palo inicial y el que se suma en la Sede 3; si la build deja elegir los palos, las 78), según la lista de cartas que fije Mazo y Robo, (b) todas las `forzada` = sí y (c) una muestra de al menos el 25 % de las demás, sorteada con una semilla anotada. Procedimiento para un equipo de una persona:
  1. una sesión de IA nueva, sin acceso al catálogo, recibe solo el texto original inglés de cada `ubicacion` y asigna tema, clara o forzada, y si contradice a un significado principal de la misma orientación;
  2. un script compara esa asignación con el catálogo y lista las discrepancias;
  3. el diseñador revisa en frío, 48 horas o más después de cargar los datos, todas las discrepancias y el 100 % de las forzadas.

  THEN hay 0 fallas en (a) y (b), y una sola falla en (c) obliga a revisar el 100 %. Es falla: el significado no está en la `ubicacion`; la traducción cambia el tema asignado; una `forzada` tiene un tema claro en alguna fuente, o una clara no lo tiene; un significado de §4 contradice a uno principal o entra antes que uno de §2/§3 que cabía; una entrada de `orientaciones_con_una` tiene un segundo significado en alguna fuente de la lista. El conjunto (a) es *provisorio hasta el GDD de Mazo y Robo*; mientras no exista, (a) son las 78 cartas. Una falla en (a) o (b) se corrige y esa carta entera se revisa de nuevo. La evidencia va en `production/qa/evidence/ac-11-[fecha].md`: modelo y sesión de la revisión ciega, semilla, lista de discrepancias y fallas, y decisión sobre cada una. La correlación entre la IA que cargó y la que revisa es un sesgo conocido y queda anotado.
- **AC-11c** (AC-11; Integration, chequeo de artefactos) — GIVEN `production/qa/evidence/ac-11-[fecha].md`, WHEN se chequea, THEN: (1) tiene archivado el transcript de la sesión ciega del paso 1; (2) `git log` muestra 48 horas o más entre el commit que carga los datos y el de la evidencia; (3) la semilla y el script anotados regeneran la misma muestra (c); (4) el script del paso 2, corrido de nuevo, da la misma lista de discrepancias, y cada una tiene una decisión de la lista cerrada `corregir catálogo` o `ratificar con cita de la ubicación`; (5) el 100 % de las `forzada` aparece con decisión. Un punto que no se cumple es falla. El script del paso 2 tiene su propio test Logic: con una asignación igual al catálogo da 0 discrepancias, y con una distinta en una palabra clave da exactamente esa.
- **AC-11b** (R4) — GIVEN `carta.copas_05/derecha/1` con `forzada` fuera de {sí, no}, WHEN se valida, THEN contiene error de R4 con ese sujeto. Control: sin el campo (por defecto no), no lo contiene.
- *AC-12 se fusionó con AC-06 el 2026-10-24. Su número no se reutiliza.*
- **AC-13** (E4) — GIVEN el mismo texto en `carta.copas_05/derecha/1` y `carta.oros_05/derecha/1`, WHEN se valida, THEN no contiene error de identificador duplicado. Control positivo: con el id `carta.copas_05/derecha/1` repetido, sí.
- **AC-14** (E8) — GIVEN la tabla `es_prueba` sin el texto de `carta.copas_05/derecha/2`, WHEN se valida, THEN contiene el error de nombre faltante (el mismo tipo que `NOMBRE_FALTANTE` de la Taxonomía) con sujeto `carta.copas_05/derecha/2@es_prueba`.
- **AC-14b** (E8) — GIVEN las tablas `es_prueba` y `en_prueba`, y `en_prueba` sin el nombre visible de `carta.copas_05`, WHEN se valida, THEN contiene ese error con sujeto `carta.copas_05@en_prueba`, y ninguno con sujeto `carta.copas_05@es_prueba`.

**Cobertura**
- **AC-15a** (F2; parametrizado por familia) — GIVEN, para cada una de las 5 familias, el fixture con el bloque copas de esa familia bajado de 3 a 1, de modo que el mazo `copas` tenga `c_f` = 7, WHEN se valida, THEN contiene error de F2 con sujeto `copas/<familia>` y ningún otro error de F2. Con el bloque en 2 (`c_f` = 8), no lo contiene.
- **AC-15b** (F2, E1; parametrizado, redistribuye una familia) — GIVEN, para cada uno de los 15 mazos alcanzables, el fixture con `c_Destino` por bloque (Mayores / copas / oros / espadas / bastos) según la receta de su tamaño, WHEN se valida, THEN contiene exactamente un error de F2 de `familia.destino`, con el sujeto de ese mazo en el orden canónico de R13 (nunca `oros+copas/...`). Recetas, con el mazo objetivo formado por los palos del valor más bajo (se permutan los palos para los demás mazos del mismo tamaño):
  - 1 palo (objetivo `copas`): 7 / 0 / 3 / 3 / 3;
  - 2 palos (objetivo `copas+oros`): 7 / 1 / 1 / 4 / 4;
  - 3 palos (objetivo `copas+oros+espadas`): 6 / 2 / 2 / 2 / 4;
  - 4 palos: 7 / 2 / 2 / 2 / 2.
- **AC-15c** (F2; borde) — GIVEN el mazo `copas+oros+espadas+bastos` (`O` = 156), WHEN `c_Destino` vale 16, THEN no contiene error de F2 con sujeto `copas+oros+espadas+bastos/familia.destino`; con 15, sí.
- **AC-15d** (F2, R6) — GIVEN el mazo `copas` con 7 orientaciones con palabra clave clara de Destino y 1 palabra clave `forzada` de Destino en otra orientación, WHEN se valida, THEN contiene error de F2 con sujeto `copas/familia.destino`. Con 8 claras, no.
- **AC-15e** (F2; aritmética entera, redistribuye una familia) — GIVEN `q_mil` = 70 y el mazo `copas+oros` (`O` = 100), WHEN `c_Destino` vale 7, THEN no contiene error de F2 con sujeto `copas+oros/familia.destino`; con 6, sí. Con `q_mil` = 100: 10 no, 9 sí.
- *AC-16 se retiró el 2026-10-24 (D-48: sin piso de* invertir*). Su número no se reutiliza.*
- **AC-17** (Tuning Knobs, F2; configuración y datos) — GIVEN `config_prueba` con `q_mil` = 150 y el mazo `copas` con `c_Destino` = 10, WHEN se valida, THEN contiene error de F2 con sujeto `copas/familia.destino` (hace falta 11). Con 11, no lo contiene. Con `q_mil` = 150 no hay error de configuración aunque esté fuera del rango seguro; con `q_mil` = 1001 o 100,5, sí (F2).

**Informe de cobertura y funciones de R12**

`fixture_informe_chico` (2 cartas, `O` = 4): carta A con derecha [*amor* clara, *deuda* forzada] e invertida [*amor* clara, *duelo* clara]; carta B con derecha [*deuda* clara] e invertida [*muerte* forzada].
- **AC-18a1** (R11; conteos) — GIVEN `fixture_informe_chico`, WHEN se pide el informe, THEN `c` = Emoción 2, Bienes 1, Destino 0; `c⁺` = Emoción 2, Bienes 2, Destino 1; `u` = Emoción 0,5, Bienes 0,5, Destino 0; `u⁺` = Emoción 0,5, Bienes 1, Destino 0,5; forzadas = 2.
- **AC-18a2** (R11, F1; pesos) — GIVEN `fixture_informe_chico`, WHEN se pide el informe, THEN `n` = *amor* 2, *duelo* 1, *deuda* 1,5, *muerte* 0 (no sorteable: sin clara, el tope da 0); `n⁺` = *amor* 2, *duelo* 1, *deuda* 2, *muerte* 1; `p` = 0,444 / 0,222 / 0,333 / 0.
- **AC-18a3** (F3, F4, F5; cifras) — GIVEN `fixture_informe_chico`, WHEN se pide el informe, THEN `P_pos` = 0,417; `P_pos⁺` = 0,500; `P_exacto` = 0,444 (con `n` en vez de `n⁺` daría 0,403); `P_pos_inv` = 0,667; `P_fallo` = Emoción 0,5, Bienes 0,5, Destino vacío (`p_f` = 0); `P_cero(3)` = 0,125 y `P_cero_corr(3)` = 0,125; `P_cero(1)` = `P_cero_corr(1)` = 0,5; `V_prior` = 0,444 y `T_ef` = 2,793.
- **AC-18b** (R11, F1) — GIVEN un mazo de prueba de 10 cartas (`O` = 20), todas sus palabras clave claras, con `n_t` = 6, 3 y 1 para tres temas y 0 para el resto, WHEN se pide el informe, THEN `p_t` = 0,6 / 0,3 / 0,1 y 0 para los temas ausentes, y `P_exacto` = 0,23.
- **AC-18c** (F3, F4) — GIVEN `q⁺` = 0,31 / 0,26 / 0,31 / 0,28 / 0,17 y `p_f` = 0,23 / 0,20 / 0,23 / 0,21 / 0,13 (orden Emoción, Bienes, Conflicto, Ambición, Destino), WHEN se calcula, THEN `P_pos⁺` = 0,2755, `P_cero(3)` = 0,3803, `P_cero_corr(3)` = 0,3849, `P_cero(1)` = `P_cero_corr(1)` = 0,7245, `P_cero(2)` = 0,5249 (± 0,0005) y `P_fallo_Destino` = `P_cero_Destino(1)` = 0,83. Son datos redondeados: no tienen que coincidir con el 0,274 de F3.
- *AC-18d se retiró el 2026-10-24: sortear 1.000 verdades es una prueba del Generador; la parte de Cartas (`p_t` = 0 sin palabras clave) la cubren AC-18a2 y AC-18b. Su número no se reutiliza.*
- **AC-18e** (R11, R12; invariante) — GIVEN el informe de los 15 mazos del fixture, WHEN se le pasa a `chequear_informe`, THEN no devuelve ninguna violación; el chequeo compara en enteros (cartas y orientaciones), no en coma flotante. Control: con un informe armado a mano con `c_Destino` = 12 de `O` = 72 y 3 cartas con Destino de `N` = 36 (`q` 0,17, `u` 0,08), devuelve la violación de `q_f ≤ u_f`.
- **AC-18f** (F3, F4; marcas) — GIVEN `P_fallo_max` = 0,85 y un mazo de prueba de 5 cartas (`O` = 10), WHEN una familia con verdad posible tiene `c⁺` = 2 (`P_fallo` 0,8), THEN no se marca; con `c⁺` = 1 (0,9), sí. Con `P_fallo_max` sin fijar, ninguna se marca. GIVEN la función de marca de progresión con un mazo de 2 palos de `P_pos⁺` 0,28 y sus dos Aprendiz con 0,29 y 0,27, THEN marca el par con el de 0,29 y no el de 0,27; con `P_pos⁺` 0,287, no marca ningún par (dentro de `ε_prog`); con exactamente 0,285 (diferencia igual a `ε_prog`), no marca. La marca da lo mismo con `k_tiradas` = [1, 3] y = [2].
- **AC-18g** (F1, `w_forz`) — GIVEN `fixture_informe_chico`, WHEN `w_forz` vale 0 o 1, THEN `p` (*amor*, *duelo*, *deuda*) da 0,5 / 0,25 / 0,25 o 0,4 / 0,2 / 0,4, y en los dos casos *muerte* tiene `p` = 0.
- **AC-18g2** (F1) — GIVEN `fixture_informe_chico` con una palabra clave clara de *muerte* agregada a la invertida de B, WHEN se pide el informe, THEN `n_muerte` = 1 y `p_muerte` = 0,182.
- **AC-18h** (F5) — GIVEN un mazo de prueba con `p` = 0,5 / 0,25 / 0,25 (`T_m` = 3), WHEN se calcula, THEN `V_prior` = 0,5 y `T_ef` = 2,667; con `p` uniforme, 0,333 y 3. Con `V_prior_max` = 0,5 no se marca; con 0,45, sí.
- **AC-18i** (R11, E1) — GIVEN el fixture, WHEN se pide el informe, THEN tiene exactamente 15 entradas, con las claves `copas`, `oros`, `espadas`, `bastos`, `copas+oros`, `copas+espadas`, `copas+bastos`, `oros+espadas`, `oros+bastos`, `espadas+bastos`, `copas+oros+espadas`, `copas+oros+bastos`, `copas+espadas+bastos`, `oros+espadas+bastos` y `copas+oros+espadas+bastos`.
- **AC-18j** (R11) — GIVEN el fixture con `tema.culpa` en una sola orientación clara de las 78 cartas, `carta.copas_05/derecha` con sus palabras clave todas de un mismo tema y `carta.copas_06/derecha` en `orientaciones_con_una` con 1 palabra clave, WHEN se pide el informe, THEN marca `tema.culpa` como frágil y cuenta `carta.copas_05/derecha` y `carta.copas_06/derecha` entre las orientaciones sin elección.
- **AC-18k** (F1, `k_forz`) — GIVEN un mazo de prueba de 20 cartas (`O` = 40) con el tema X en 1 orientación clara y 30 forzadas, y el tema Y en 2 orientaciones claras, WHEN se pide el informe con `k_forz` = 1, 3 y 0, THEN `p_X` = 0,429, 0,556 y 0,333.
- **AC-18l** (R11, E9) — GIVEN un mazo de prueba donde `tema.muerte` aparece solo en palabras clave forzadas, WHEN se pide el informe, THEN `tema.muerte` está en la lista de temas trampa del mazo y `p_muerte` = 0. Control: con una clara de *muerte*, no está en la lista. Con `tema.traicion` deprecado y una palabra clave clara de *traición* en el mazo, *traición* está en la lista de deprecados presentes y no en la de temas trampa.
- **AC-22** (R12, F1) — GIVEN un mazo de prueba donde todas las palabras clave claras son de temas deprecados, WHEN se llaman `validar_mazo` e `informe_mazo`, THEN la lista contiene `MAZO_SIN_VERDADES` con el mazo como sujeto; en el informe, todos los `p_t` valen 0, y están vacíos (no son un número) `P_exacto`, `P_pos`, `P_pos⁺`, `P_pos_inv`, cada `P_fallo_f`, `P_cero(k)`, `P_cero_corr(k)` y `P_cero_f(k)` para cada `k` de `k_tiradas`, `V_prior` y `T_ef`, sin excepción, y el informe no tiene ninguna marca de F3 a F5. Con un mazo de prueba sin cartas (`O` = 0), lo mismo, y además `q_f`, `q_f⁺`, `u_f` y `u_f⁺` están vacíos; ninguna función lanza una excepción.
- **AC-23** (R12) — GIVEN una orientación con *amor* (clara) y *deuda* (forzada), WHEN se consulta `acierto_posible` con verdad *amor*, *deuda*, *duelo*, *fortuna* y *muerte*, THEN da EXACTO, EXACTO, PARCIAL, PARCIAL (por la forzada de Bienes) y NINGUNO.
- **AC-24** (R4, E2 paso 4; parametrizado) — GIVEN `carta.copas_02/invertida` sin ninguna palabra clave, en `orientaciones_con_una` o fuera de ella (un caso cada uno), WHEN se valida, THEN contiene error de R4 con sujeto `carta.copas_02/invertida`.
- **AC-26** (R12, Pilar 1; Integration, *provisorio hasta `/create-architecture`*) — GIVEN el código fuente de la build, WHEN se buscan las llamadas a `acierto_posible`, THEN todas están en el módulo de herramientas y pruebas que fije la arquitectura, y ninguna en el código de juego. Control positivo: una llamada agregada a propósito en un sistema de juego hace fallar el chequeo. La evidencia es la salida del chequeo en CI.
- **AC-27** (Tuning Knobs; parametrizado, configuración) — GIVEN `config_prueba` con uno de estos cambios: `w_forz` = −0,1 o 1,1; `k_forz` = −1, 1,5 o 4; `k_tiradas` = [], [0], [11] o [3, 3]; `ε_prog` = −0,001 o 0,06; `P_fallo_max` = 1,2; `V_prior_max` = −0,1; mínimo de palabras clave 0; mínimo 3 con máximo 2 (un caso cada uno), WHEN se valida, THEN contiene un error de configuración con sujeto la clave cambiada, ningún error de datos (R1 a R8, F2), y no se calcula el informe (Tuning Knobs). Control: con `w_forz` = 0 y 1, `k_forz` = 0 y 3, `k_tiradas` = [1, 3, 5], `ε_prog` = 0,05 y mínimo = máximo = 2 (dentro del dominio aunque algunos estén fuera del rango seguro), ningún error de configuración. Los casos de `q_mil` los cubre AC-17.

**Datos reales y otros**
- **AC-19** (R10; Integration) — GIVEN el catálogo, las cartas, las tablas de idioma y `atribuciones_gd` reales, WHEN se valida, THEN la lista está vacía. Bloquea la historia de contenido, no la del validador.
- **AC-20** (R3; Integration, *provisorio hasta `/art-bible`*) — GIVEN el manifiesto de la fuente de escaneos que fije `/art-bible`, con la URL y el SHA-256 que publica esa fuente para cada imagen, WHEN se hashea el archivo original de cada una de las 78 `arte` (el que está en la carpeta de fuentes de arte, antes de que el motor lo importe), THEN cada hash coincide con el de su carta en el manifiesto. Que esa fuente no sea la recoloración de 1971 lo decide `/art-bible` con su validación legal.
- **AC-21** (States) — GIVEN una partida simulada que serializa la verdad *traición* de un rol como su id de tema, WHEN se deserializa con una versión del catálogo que cambió el tema de una palabra clave de *traición* a *engaño*, THEN la verdad del cliente sigue siendo `tema.traicion`. Cuando exista el GDD de Guardado, el mismo caso se repite con el formato real (Integration).
- Lo que muestra el tooltip (R9) lo prueban los AC de Tapete y Tooltips (`/ux-design`). E6 y E7 los prueban la Gramática y Resonancia.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| **Reconteo con Waite III §4 (D-50; bloqueante de datos).** Rehacer `design/balance/cobertura-cartas-waite.md` por carta, con los 23 temas, `n_t` por tema, claras y forzadas, y las 56 menores con §2 y §4 (con los límites de R4). Publicar la tabla de `c_f` y `c_f⁺` de los 15 mazos. Sin eso no se pueden calcular el `p_f` de F1, `P_pos⁺`, `P_pos_inv` (F3), `P_cero` real (F4) ni `V_prior` (F5), y todas las cifras de este GDD siguen siendo previas a §4 y pesimistas | Diseñador | Antes de cargar los datos y antes del prototipo |
| El conteo de D-48 lo hizo una sola lectura (diseñador más IA), con criterio de "asignación clara", y se le pasó III §4. El reconteo usa el procedimiento de revisión ciega de AC-11 para las cartas de AC-11(a) | Diseñador | Con el reconteo |
| Elemento de los 7 Mayores con atribución planetaria (Mago, Sacerdotisa, Emperatriz, Rueda, Torre, Sol, Mundo): ¿neutro, el del planeta según otra tradición, o un elemento propio? | GDD de Gramática | Al diseñar la Gramática |
| Forma del sorteo de F1: ¿proporcional a `n_t`, o con sobrepeso (`n_t^a`, a > 1) para subir `P_pos⁺`? ¿Los roles de una situación se sortean independientes o con afinidad (`afinidad_por_rol` de la Taxonomía)? Con afinidad, `P_cero` se acerca a `P_cero_corr` (F4) | GDD del Generador | Al diseñar el Generador |
| **Riesgo del Pilar 6:** con el conteo previo a §4 (pesimista), `P_cero(3)` ≈ 0,38 en Tres Tiempos y 0,40 en 78 cartas, y 0,58 a 0,67 para un cliente de Destino; en Carta Única, `P_cero(1)` ≈ 0,73, y 0,83 a 0,875 para Destino (F4). Con el reconteo, medir en el prototipo si es jugable con *invertir*, la relectura ciega de una carta y la Sentencia, **incluidos clientes de Destino y las dos tiradas del MVP**, y recién ahí fijar `P_fallo_max` y `V_prior_max`. **Carta Única (`k` = 1) es criterio de salida explícito del prototipo**, y se mide la tasa de relectura: si casi toda Carta Única se relee, la palanca es un impuesto y no una elección. El criterio de aprobación se escribe antes de correr el prototipo. El prototipo compara además `w_forz` 0, 0,5 y 1. Si hace falta subir `P_pos⁺`, la palanca viene de trucos o de la forma del sorteo, siempre medida contra `V_prior` (F5) | Diseñador | Prototipo del núcleo |
| **Palanca del Pilar 6 ante una carta muda** (E7): relectura ciega pagando UT. Costo en UT, cuántas por tirada, si la carta nueva sale del mismo mazo, y cómo se ofrece sin consultar la verdad. Es pendiente de esos GDD en `systems-index.md` | GDD de Tiradas y de Resonancia | Al diseñarlos |
| **Carta Única** (F4, E7): ¿qué rol cubre "Respuesta" (Taxonomía, Open Questions)? ¿Cómo funciona la relectura cuando la tirada es una sola carta, y sigue siendo más barata que rehacerla? Con `P_cero(1)` ≈ 0,73, ¿Carta Única necesita una palanca propia o una regla de Resonancia distinta? El reconteo no alcanza: aun con III §4, `P_cero(1)` ≥ ~0,45 con claras y ~0,6–0,65 realista (F4), así que no hay que esperar al reconteo para decidir | GDD de Tiradas y de Resonancia | Al diseñarlos, antes del prototipo |
| **`V_menú`, métrica candidata del informe** (Pilar 1): F5 mide la apuesta global al tema más frecuente, pero el jugador elige entre las 2 o 3 palabras clave de la carta que salió. Elegir siempre la de mayor `p_t` es un exploit por carta: `V_menú = E_carta[max_{t∈menú} p_t / Σ_{t∈menú} p_t]`, comparado con el azar uniforme dentro del menú. Decidir si entra en el informe y con qué umbral | GDD de Resonancia | Al diseñar Resonancia, antes de fijar `V_prior_max` |
| **"Jugada útil" del Pilar 6** (F4): ¿alcanza un PARCIAL? ¿Una lectura sin acierto puede ser útil por la Sentencia? Hasta que se defina, F4 usa el acierto de familia posible como sustituto, que es una cota inferior del fallo real | GDD de Tiradas y de Resonancia | Antes de que el prototipo fije `P_fallo_max` |
| Lista de cartas de la build del MVP (AC-11(a)): ¿el palo inicial del Aprendiz y el de la Sede 3 los elige el jugador o son fijos? Si se eligen, la build del MVP carga las 78 | GDD de Mazo y Robo | Antes de la historia de contenido |
| **La progresión del mazo empeora `P_cero`** (F4): compensarlo con más trucos por Sede (preferido en la revisión) o con el multiplicador de recompensa de D-22 | GDD de Prestidigitación | Al diseñar Prestidigitación |
| Orientaciones sin tema claro (E2): de 11 a 18 por mazo Aprendiz según el conteo previo a §4. Buscarlas primero en III §4 (Menores) y después en el *Book T* y en Mathers; las que queden van `forzada`; una orientación sin ningún significado es error de datos | Diseñador | Con el reconteo |
| Oráculo `atribuciones_gd`: transcribir a mano desde un escaneo de dominio público del *Book T* los 22 Mayores y los 36 decanatos, con la página en cada fila, en un commit anterior a los datos. Decidir si las figuras llevan atribución propia (hoy no) | Diseñador | Antes de cargar los datos |
| Registro: agregar `w_forz`, `k_forz` y `ε_prog`, cambiar `piso_familia_q_min` a `q_mil` entero, y anotar la excepción de 1 en `palabras_clave_por_orientacion` | `/consistency-check` | Antes del GDD del Generador |
| Traducción de las palabras clave del inglés de Waite al español rioplatense: ¿la `ubicacion` cita el original, y quién valida que la traducción no cambie el tema? AC-11 ya compara contra el original | Diseñador, `/localize` | Al escribir los datos |
| Tooltip: ¿se marcan las palabras clave `forzada` y los temas trampa del mazo activo (E9)? | `/ux-design` | Antes de las historias del tooltip |
| Fuente de referencia de los escaneos de 1909, con URL y SHA-256 por imagen (AC-20), y validación legal | `/art-bible` | Antes de producir arte |
