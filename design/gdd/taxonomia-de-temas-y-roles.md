# Taxonomía de Temas y Roles

> **Status**: In Review
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-24
> **Last Verified**: 2026-10-23
> **Implements Pillar**: Regla Cero, Pilar 3 (Memoria Pura), Pilar 6 (No hay Carta Mala)
> **Creative Director Review (CD-GDD-ALIGN)**: `/design-review` full del 2026-10-23 (tercera pasada), NEEDS REVISION; revisado el mismo día (D-44); `/design-review` lean del 2026-10-23 (cuarta pasada), NEEDS REVISION, corregida (D-45); `/design-review` lean del 2026-10-23 (quinta pasada), APPROVED con 8 recomendados, 7 aplicados (D-46); R13 ampliado por el GDD de Cartas (D-47) y 3 temas de resultado agregados (D-48); valencia por tema (D-51); pendiente de re-revisión

## Summary

La Taxonomía es el diccionario común de la lectura. Tiene 23 temas agrupados en 5 familias, que siguen a los palos del tarot más los Arcanos Mayores, y tiene roles narrativos (origen, conflicto, desenlace). Con ese diccionario, las cartas, el cliente generado, las tiradas y los textos hablan el mismo idioma. Define también cuándo una lectura acierta exacto (mismo tema), a medias (misma familia) o no acierta. El jugador la ve en el tooltip de cada carta, como tema y familia.

> **Quick reference** — Layer: `Foundation` · Priority: `MVP` · Key deps: `None`

## Overview

La Taxonomía de Temas y Roles es el vocabulario cerrado que comparten todos los sistemas de la lectura. Tiene dos listas:

- **Temas:** etiquetas mecánicas como *traición*, *deuda*, *culpa* o *poder*, que dicen **de qué** habla algo.
- **Roles narrativos:** *origen*, *conflicto*, *desenlace*, *el otro*, *caminos*, que dicen **qué lugar ocupa** ese algo en la historia del cliente.

Cada sistema usa ese vocabulario a su manera:

- Cada carta declara sus temas, derivados de sus palabras clave (GDD §3.2).
- El Generador de Situaciones produce la verdad oculta del cliente como temas por rol.
- Cada tirada traduce sus posiciones a roles.
- Las preguntas y los textos se arman con las mismas palabras.

La Resonancia compara la lectura con la verdad usando las reglas de comparación entre temas que define este documento.

El jugador no maneja la taxonomía como sistema: la percibe a través de lo que habilita. Ve los temas de cada carta en el tooltip, que es conocimiento público (Pilar 3, GDD §3.3). Lee las posiciones de la tirada como preguntas ("¿de dónde viene esto?", "¿qué lo traba?"). Y descubre que lo que dice el cliente, lo que sale en las cartas y lo que paga la sentencia hablan el mismo idioma.

Sin este vocabulario, cada sistema tendría su propio lenguaje. El Generador tendría que conocer cada tirada, porque la tirada se elige después de generar al cliente (D-37). Y no habría forma de decir si una lectura "acertó".

## Detailed Design

### Core Rules

> Revisado en `/design-review` full con `game-designer`, `systems-designer`, `qa-lead`, `narrative-director` y `creative-director` (2026-10-22 y 2026-10-23). Las decisiones que salieron de esas revisiones están en D-43 y D-44.

**Temas y familias**

1. Hay **5 familias fijas**: una por palo y una para los Arcanos Mayores. No se agregan familias nuevas, porque salen de la estructura del tarot (GDD §3.5).

   | Familia | Palo / elemento | Campo | Temas del MVP |
   |---|---|---|---|
   | Emoción | Copas / Agua | lo que se siente | amor, culpa, duelo, deseo, alegría |
   | Bienes | Oros / Tierra | lo que se tiene o se pierde | deuda, fortuna, hogar, trabajo |
   | Conflicto | Espadas / Aire | lo que se enfrenta | traición, ley, violencia, engaño, secreto |
   | Ambición | Bastos / Fuego | lo que se busca | poder, rivalidad, fama, riesgo, éxito |
   | Destino | Arcanos Mayores | lo que le pasa al cliente y no controla | muerte, locura, enfermedad, cambio |

   Son 23 temas e incluyen los diez de ejemplo del GDD §3.2. La frontera entre Conflicto y Destino es una sola, y es el criterio de D-42: lo que el cliente controla o hace va en Conflicto, y lo que le pasa va en Destino. Por eso *secreto* va en Conflicto (el cliente lo esconde, el Doble Fondo) y *enfermedad* va en Destino (D-43). *Trabajo* (empleo, despido, cierre de fábrica) completa Bienes.

   **Temas de resultado (D-48).** La tradición de 1909 describe tanto el problema como su resolución, y contadas las 78 cartas, muchas orientaciones hablan de resultados que no tenían tema. Por eso se suman *alegría* (contento, felicidad, festejo), *éxito* (triunfo, victoria, logro; *fama* queda para la reputación) y *cambio* (noticias, mudanza, viaje, renovación). *Cambio* va en Destino por D-42: es lo que le llega al cliente. *Culpa* abarca también la vergüenza y la confesión, porque la tradición casi no usa *guilt* (D-48).

   **Valencia (D-51).** Cada tema base tiene una valencia, que usa la pregunta de sí o no (Tiradas R9–R11). Los temas de mapa toman la de su equivalente, igual que la familia.

   | Valencia | Temas |
   |---|---|
   | Favorable | amor, alegría, fortuna, éxito |
   | Desfavorable | culpa, duelo, deuda, traición, violencia, engaño, muerte, locura, enfermedad |
   | Ambigua | deseo, hogar, trabajo, ley, secreto, poder, rivalidad, fama, riesgo, cambio |

   **Regla Cero aplicada a los temas:** un tema describe **la situación del cliente, nunca una fuerza** que actúa sobre él. *Muerte* es que alguien murió o va a morir, no la Muerte; Destino es lo que le pasa al cliente sin que lo controle, no un orden cósmico. Todo nombre visible, glosario y texto que use un tema respeta esta regla.
2. Cada tema pertenece a **exactamente una familia**: en los datos, la familia es un campo único del tema. Una carta puede llevar temas de cualquier familia: un Cinco de Copas puede hablar de *deuda*.
3. **Mínimo por familia:** cada familia tiene al menos **2 temas base activos** (el valor sale de la perilla de Tuning Knobs), porque con uno solo el resultado parcial no puede darse. Los temas de mapa no cuentan: se comparan como su equivalente y no agregan un tema distinto. El objetivo de diseño es 3 o más. El validador rechaza un catálogo por debajo del mínimo, también cuando la causa es haber deprecado un tema.

**Identificadores**

4. Todo lo que define este catálogo tiene un **identificador estable**, separado del nombre que se muestra (que sale de la tabla de idioma y se traduce). El identificador lleva el prefijo de su tipo, de modo que dos tipos distintos nunca chocan:

   | Tipo | Prefijo | Formato completo | Ejemplo |
   |---|---|---|---|
   | Familia | `familia.` | `^familia\.[a-z0-9_]+$` | `familia.conflicto` |
   | Tema base | `tema.` | `^tema\.[a-z0-9_]+$` | `tema.traicion` |
   | Rol | `rol.` | `^rol\.[a-z0-9_]+$` | `rol.conflicto` |
   | Forma de pregunta | `forma.` | `^forma\.[a-z0-9_]+$` | `forma.si_o_no` |
   | Tema de mapa | `mapa_<mapa>.` | `^mapa_[a-z0-9]+\.[a-z0-9_]+$` | `mapa_a.hiperinflacion` |

   El tipo de una entrada lo da la lista donde está cargada (familias, temas, roles, formas, temas de un mapa), y su prefijo tiene que coincidir. El nombre del mapa (`<mapa>`) no lleva guion bajo, así que el identificador se parte sin ambigüedad en el primer punto. Un identificador que no cumple el formato de su tipo (mayúsculas, tildes, nada después del prefijo, o el prefijo de otro tipo, como un tema cargado como `rol.x`) da `ID_FORMATO`. Los archivos de mapa tienen su propia precedencia (R5). Cada identificador es único en todo el catálogo. Ningún identificador se renombra ni se borra, sea del tipo que sea: un tema que deja de usarse se marca como deprecado, y un rol o una forma se deshabilita (ver States).
5. Los mapas pueden **agregar temas**, y solo eso: el archivo de un mapa declara únicamente identificadores con su propio prefijo (`mapa_a.` en el archivo del Mapa A). Si declara un tema base, es `MAPA_SOBREESCRIBE_BASE`, cambie o no algún campo; ese caso **no** da además `ID_DUPLICADO` (la unicidad de R4 se comprueba sin contar las entradas de los archivos de mapa que repiten un identificador base). Cualquier otro identificador ajeno es `MAPA_ID_AJENO`. En el archivo de un mapa, cada identificador da **un solo** error, según este orden: (a) prefijo `tema.` → `MAPA_SOBREESCRIBE_BASE`; (b) bien formado como tema de mapa pero con el prefijo de otro mapa, o con el prefijo de otro tipo (`rol.`, `forma.`, `familia.`) → `MAPA_ID_AJENO`; (c) cualquier otro → `ID_FORMATO`. Cada tema de mapa declara un **tema base equivalente**, que tiene que existir y ser un tema base (no otro tema de mapa). Si el tema de mapa está activo, su equivalente también tiene que estarlo; un tema de mapa deprecado puede apuntar a un equivalente deprecado (ver States). El tema de mapa **no declara familia**: toma la de su equivalente. Varios temas de mapa pueden compartir el mismo equivalente. Los temas de mapa tienen el mismo ciclo de vida que los temas base.

**Comparación (la regla que usa la Resonancia)**

6. La comparación es una función pura:

   `comparar(leído: tema base, verdadero: tema base o de mapa) → EXACTO | PARCIAL | NINGUNO`

   Que el jugador no haya elegido palabra clave no llega a esta función: lo resuelve R11, paso 3. Primero, si el verdadero es un tema de mapa, se reemplaza por su equivalente base. Después:
   - **EXACTO:** el leído y el verdadero son el mismo tema base;
   - **PARCIAL:** son temas distintos de la misma familia;
   - **NINGUNO:** son de familias distintas.

   La función supone un catálogo que pasó el validador, pero igual comprueba sus entradas, en este orden, y falla con un error tipado; nunca devuelve NINGUNO en silencio:
   1. `ID_INEXISTENTE`: el leído o el verdadero no existe en el catálogo;
   2. `LEIDO_ES_DE_MAPA`: el leído es un tema de mapa.

   Los resultados no tienen puntaje en este documento: el puntaje (por ejemplo, el 2/1/0 del GDD §5.8) lo define Resonancia.
7. El tema leído es el de **la palabra clave que el jugador elige** para la carta. Cada palabra clave derecha o invertida se asocia a **exactamente un tema base**: ni a ninguno (`KW_SIN_TEMA`) ni a más de uno (`KW_TEMAS_MULTIPLES`).

**Roles**

8. Roles del MVP, habilitados: **origen**, **conflicto** y **desenlace**. Roles planificados para después del MVP *(provisorios hasta el GDD de Tiradas)*, que existen como identificadores deshabilitados: **el otro**, **camino A** y **camino B**.
9. Cada posición de una tirada se traduce a **un rol o a "libre"**. Una posición libre no se compara contra la verdad, pero sus cartas cuentan para la gramática de combinación. Esto permite agregar tiradas grandes, como la Cruz Celta, sin inventar un rol por casillero. En los datos de una tirada, una posición libre se declara con el campo `libre` = sí y **sin rol**; nunca lleva un identificador ni una palabra reservada, así que no puede chocar con un rol. Una posición con rol **y** `libre`, o sin ninguno de los dos (un rol que se olvidó de cargar), da `POSICION_AMBIGUA`: no se toma por libre en silencio. Una tirada sin ninguna posición con rol habilitado da `TIRADA_SIN_COMPARABLES` *(provisorio hasta el GDD de Tiradas)*.
10. El Generador asigna **un tema a cada rol habilitado**, porque todavía no sabe qué tirada se va a usar. Un rol está **habilitado** si el catálogo lo marca como producido por el Generador en la build actual (campo `habilitado`). *Habilitado* no es lo mismo que *activo*: activo/deprecado es el estado de un tema (States), y habilitado sí/no es un interruptor de roles y formas. En el MVP están habilitados origen, conflicto y desenlace. El catálogo tiene al menos un rol habilitado.

    La Taxonomía **no restringe qué temas van juntos** en una situación: si dos roles pueden repetir tema o si los temas deben ser coherentes entre sí lo define el Generador. El esquema reserva el campo `afinidad_por_rol` para eso (ver Open Questions).

**Resolución de una posición**

11. Cada posición de la tirada produce **un resultado propio**, siguiendo estos pasos en orden:
    1. Se toma el rol de la posición, o "libre".
    2. Si la posición es libre, o si la situación no contiene ese rol, el resultado es **SIN_COMPARACION** y se termina acá.
    3. Si el jugador no eligió palabra clave, el resultado es **NINGUNO**.
    4. Si eligió, el tema leído es el de esa palabra clave (R7), y el resultado es `comparar(leído, tema verdadero del rol)` (R6).

    La resolución devuelve una lista con una entrada por posición, en el orden de la tirada: (id de posición, rol o libre, resultado). SIN_COMPARACION no es lo mismo que NINGUNO: la primera no entra en ninguna cuenta y la segunda vale cero. Cómo se agregan los resultados (por ejemplo, dos posiciones con el mismo rol) lo define Resonancia.

**Motivo de consulta**

12. El motivo tiene dos partes:
    - un **tema**, tomado de esta lista, que es de qué dice venir a hablar el cliente;
    - una **forma de pregunta**: *sí o no*, *situación general*, *dilema*, *vínculo* o *asunto grave*. La forma sugiere la tirada esperada (GDD §5.4). Las cinco existen como identificadores; en el MVP solo están habilitadas *sí o no* y *situación general*. El catálogo tiene al menos una forma habilitada.

    El tema del motivo puede no coincidir con la verdad: eso es el Doble Fondo, que lo decide el Generador (ver Open Questions).

**Validador del catálogo**

13. Los errores de datos los detecta el **validador del catálogo**, una función pura:

    `validar_catalogo(catálogo, cartas, tiradas, mapas, tablas de idioma, catálogo anterior opcional) → lista de errores`

    Cartas amplía las entradas con `config`, `orientaciones_con_una` y el oráculo `atribuciones_gd` (R12 de Cartas).

    Cada error es `{código, sujeto, detalle}`: el código identifica la regla rota y el sujeto dice qué está mal cargado. Los tests verifican el código y el sujeto, nunca el texto del detalle. Formato del sujeto:
    - un identificador del catálogo, tal cual (`tema.deuda`);
    - una palabra clave: su id de Cartas R4, `<id de carta>/<derecha|invertida>/<n>`;
    - una orientación de carta: `<id de carta>/<derecha|invertida>`;
    - un mazo y una familia (Cartas, F2 y F3): `<palos del mazo en el orden copas, oros, espadas, bastos, unidos por +>/<familia>`, con los Mayores implícitos (`copas+espadas/familia.destino`); un mazo sin familia (Cartas, `MAZO_SIN_VERDADES`), solo la parte de los palos (`copas+espadas`);
    - una tirada: su id; una posición de tirada: `<id de tirada>/<id de posición>`;
    - un error de todo el catálogo, sin una entrada concreta (`SIN_ROLES_HABILITADOS`, `SIN_FORMAS_HABILITADAS`): el sujeto fijo `catalogo`;
    - una entrada sin identificador utilizable (por ejemplo, vacío): `<archivo>#<índice de la entrada>`, con el índice numerado **desde 1**;
    - un nombre faltante en una tabla de idioma: `<identificador>@<id de la tabla>` (`tema.deuda@es_prueba`).

    Con el catálogo anterior, el validador revisa también lo que no puede cambiar entre versiones. Si no se pasa catálogo anterior, o está vacío (primera build), esas reglas no se revisan y no dan errores. Códigos:

    | Código | Regla |
    |---|---|
    | `ID_VACIO`, `ID_DUPLICADO`, `ID_FORMATO` | R4 |
    | `FAMILIA_EXTRA` | R1: el catálogo declara una familia que no es una de las 5 |
    | `TEMA_SIN_FAMILIA`, `FAMILIA_INEXISTENTE` | R2 |
    | `FAMILIA_BAJO_MINIMO` | R3 |
    | `CAMPO_INVALIDO` | Esquema: `estado` fuera de {activo, deprecado}, `valencia` fuera de {favorable, desfavorable, ambigua}, `habilitado` / `habilitada` que no es sí / no, o `afinidad_por_rol` no vacío (reservado). Sujeto: el identificador |
    | `NOMBRE_FALTANTE` | R4: falta el nombre visible de un identificador (familia, tema, tema de mapa, rol o forma) en una tabla de idioma. Se revisa en cada tabla cargada |
    | `KW_SIN_TEMA`, `KW_TEMAS_MULTIPLES`, `KW_TEMA_INEXISTENTE`, `KW_TEMA_DE_MAPA` | R7, E7 |
    | `MAPA_SIN_EQUIVALENTE`, `MAPA_EQUIV_INEXISTENTE`, `MAPA_EQUIV_ES_DE_MAPA`, `MAPA_EQUIV_DEPRECADO`, `MAPA_DECLARA_FAMILIA`, `MAPA_SOBREESCRIBE_BASE`, `MAPA_ID_AJENO` | R5, States |
    | `SIN_ROLES_HABILITADOS` | R10 |
    | `SIN_FORMAS_HABILITADAS` | R12 |
    | `ROL_INEXISTENTE` | E3: una posición de tirada nombra un rol que no está en el catálogo |
    | `FORMA_INEXISTENTE` | R12: una tirada declara como esperada una forma de pregunta que no está en el catálogo |
    | `POSICION_AMBIGUA`, `TIRADA_SIN_COMPARABLES` | R9: posición con rol y `libre`, o sin ninguno; tirada sin posición con rol habilitado. Sujeto: la posición, o la tirada |
    | `ID_ELIMINADO`, `ID_REACTIVADO`, `DEPRECAR_CON_DEPENDIENTES`, `FAMILIA_CAMBIADA`, `EQUIV_CAMBIADO` | States |

    Si la lista no está vacía, el juego no pasa del arranque y muestra los errores (E1).

**Esquema mínimo**

| Entrada | Campos |
|---|---|
| Familia | `id`, `marca` (símbolo; ver Visual/Audio), `palo` (Copas / Oros / Espadas / Bastos / Arcanos Mayores, la correspondencia de R1; la usa la Gramática) |
| Tema base | `id`, `familia`, `estado` (activo / deprecado), `valencia` (favorable / desfavorable / ambigua, D-51), `afinidad_por_rol` (reservado: vacío hasta que lo defina el GDD del Generador) |
| Tema de mapa | `id`, `equivalente`, `estado` (activo / deprecado) |
| Rol | `id`, `habilitado` (sí / no) |
| Forma de pregunta | `id`, `habilitada` (sí / no) |
| Palabra clave *(dato de Cartas)* | carta, orientación, `tema` |
| Posición *(dato de Tiradas)* | `id`, `rol` o `libre` (exactamente uno de los dos; ver R9) |

Los nombres visibles no están en estas entradas: salen de las tablas de idioma, por identificador. De las dos últimas filas, este documento fija solo los campos que lee.

### States and Transitions

**Temas (base y de mapa)**

| Estado | Significa | Transición |
|---|---|---|
| Activo | Lo pueden usar cartas, situaciones y textos | → Deprecado, si se deja de usar. Un tema base, además, solo si ningún tema de mapa **activo** lo tiene como equivalente y si su familia sigue con el mínimo de R3 |
| Deprecado | No se generan situaciones nuevas con él. Las partidas guardadas que lo tengan siguen funcionando, y las cartas pueden seguir ofreciéndolo como palabra clave | Fin: nunca vuelve a Activo y su identificador nunca se borra ni se reutiliza |

**La familia de un tema base y el equivalente de un tema de mapa no cambian entre versiones** (D-45): cambiarlos altera el resultado de EXACTO / PARCIAL / NINGUNO de las partidas guardadas. Con catálogo anterior, el validador da `FAMILIA_CAMBIADA` (sujeto: el tema base) o `EQUIV_CAMBIADO` (sujeto: el tema de mapa) si el valor difiere. Si una asignación está mal, se depreca el tema y se crea uno nuevo con otro identificador. Sin catálogo anterior, o vacío, estas reglas no se revisan: mientras no haya build publicada, las asignaciones se pueden corregir directamente.

Para deprecar un tema base que es equivalente de temas de mapa, primero se deprecan esos temas de mapa. Un tema de mapa deprecado puede seguir apuntando a un equivalente deprecado, porque las partidas guardadas lo siguen usando; el equivalente nunca se elimina (`ID_ELIMINADO`).

Un tema base deprecado con un tema de mapa **activo** que lo tiene como equivalente da exactamente un error:
- `DEPRECAR_CON_DEPENDIENTES` (sujeto: el tema base), si el catálogo anterior lo tenía activo: el error es deprecarlo en esta versión;
- `MAPA_EQUIV_DEPRECADO` (sujeto: el tema de mapa), en cualquier otro caso (sin catálogo anterior, o el tema base ya estaba deprecado): el error es apuntar un tema de mapa activo a un deprecado.

**Roles y formas de pregunta:** `habilitado` puede pasar de no a sí y de sí a no en cualquier build. No es una reactivación y no da `ID_REACTIVADO`. Nunca se borran.

**Familias:** fijas (R1); nunca se borran.

Fuera de este ciclo de vida, la taxonomía no cambia durante la partida: es un catálogo fijo de datos que se carga una vez.

### Interactions with Other Systems

| Sistema | Qué recibe de la Taxonomía | Qué le devuelve o aporta |
|---|---|---|
| Base de Datos de Cartas | Lista de temas | Cada palabra clave, asociada a un tema; pasa por el validador (R13) |
| Interpretación y Sentencia | Tema de cada palabra clave | La palabra clave elegida por posición, que define el tema leído (R7) |
| Tapete y Tooltips de Cartas | Nombre visible y familia de cada tema, y su marca | Nada; los muestra en el tooltip |
| Generador de Situaciones | Temas activos, familias, roles habilitados y formas habilitadas | Un tema por rol habilitado, más el motivo (tema y forma) |
| Tiradas | Roles y formas | La traducción de cada posición a un rol o a "libre", y la forma que espera cada tirada; pasan por el validador (R13) |
| Resonancia y Resolución | `comparar` y la lista de resultados por posición (R6, R11) | Nada; la consume |
| Gramática de Combinación | Familia de cada palo | Nada; la usa para el bono por palo dominante |
| Arquetipos y Pieles de Mapa | Temas | Los temas típicos de cada arquetipo y de sus secretos; los temas de mapa |
| Textos por Plantillas | Nombre visible de cada tema y rol | Nada; los usa para armar preguntas y sentencias |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD todavía.

## Formulas

La comparación (R6) es categórica y no tiene fórmulas. Lo que sigue es la **línea base de azar** que se deriva del reparto de familias y que usan E8, la meta de Open Questions y el AC-09. No es una regla de juego: la usa el diseño para calibrar.

**Variables**

| Variable | Significado | Valor actual |
|---|---|---|
| `T` | Cantidad de temas base activos | 23 (rango: ≥ 2 × cantidad de familias) |
| `n_f` | Cantidad de temas base activos de la familia `f` | 5 / 4 / 5 / 5 / 4 (Emoción / Bienes / Conflicto / Ambición / Destino) |
| `n` | `n_f` de la familia del tema **leído** | 4 a 5 |
| `P_exacto`, `P_parcial(n)` | Probabilidad de EXACTO / PARCIAL si leído y verdadero se eligen al azar, uniformes e independientes | ver abajo |
| `V(n)` | Valor esperado por posición al azar con el puntaje ilustrativo 2/1/0 (el real lo define Resonancia) | ver abajo |

**Fórmulas**

- `P_exacto = 1 / T`
- `P_parcial(n) = (n − 1) / T`
- `V(n) = 2 · P_exacto + 1 · P_parcial(n) = (n + 1) / T`
- Pares ordenados (leído, verdadero): `T²` en total; `T` EXACTO; `Σ n_f · (n_f − 1)` PARCIAL; el resto NINGUNO.

**Ejemplo con el catálogo base (`T` = 23)**

| Cuenta | Valor |
|---|---|
| Pares ordenados | 529 |
| EXACTO | 23 (4,3 %) |
| PARCIAL | 84 (15,9 %) |
| NINGUNO | 422 |
| `P_parcial` por familia del leído | 0,174 Emoción, Conflicto y Ambición; 0,130 Bienes y Destino |
| `V` por familia del leído | 0,261 Emoción, Conflicto y Ambición; 0,217 Bienes y Destino. Promedio: 0,246 |
| Desvío respecto del promedio | Familias de 5 temas +6,2 %; de 4 temas −11,5 % |

**Rango y degeneración:** `P_parcial` es 0 si `n` = 1, caso que R3 impide. Con el mínimo de R3 (2), `P_parcial` ≥ 1 / T. Si `T` o el reparto cambian, hay que recalcular la tabla y el AC-09 (sus totales son provisorios).

## Edge Cases

1. **Datos mal cargados** (una palabra clave sin tema o con un tema que no existe, un tema sin familia, un identificador vacío o repetido). Es un error de datos: el validador lo devuelve con su código (R13), el juego no arranca y nombra lo que está mal cargado. Nunca se resuelve en silencio.
2. **La situación tiene un rol que la tirada no cubre** (por ejemplo, Carta Única frente a un cliente con origen, conflicto y desenlace). Solo se comparan los roles que la tirada cubre; los demás no suman ni restan. Qué rol cubre cada posición lo define el GDD de Tiradas.
3. **Una posición pide un rol que la situación no contiene** (un rol deshabilitado, como "el otro" en el MVP). La posición da **SIN_COMPARACION** (R11, paso 2), aunque el jugador no haya elegido palabra clave: no se compara, pero sus cartas cuentan para la gramática. Un rol que **no existe** en el catálogo (por ejemplo, un error de tipeo como `rol.orijen`) no es este caso: es un error de datos (`ROL_INEXISTENTE`).
4. **Dos posiciones con el mismo rol** (por ejemplo, en la Cruz Celta). Cada una produce su propio resultado contra el mismo tema verdadero. Está permitido. Cómo se combinan esos resultados lo define Resonancia.
5. **El jugador no elige palabra clave en una posición comparable.** El resultado es **NINGUNO**. No hay castigo extra.
6. **Una partida guardada con un tema deprecado.** Se carga y resuelve normal: las cartas pueden seguir ofreciéndolo, así que el exacto sigue siendo posible. El tema deja de aparecer solo en situaciones nuevas.
7. **Temas propios de un mapa.** Las cartas se comparten entre mapas, así que usan solo temas base. Para comparar, un tema de mapa se reemplaza por su equivalente (R6). Por ejemplo, con `mapa_a.hiperinflacion` → `tema.deuda` (familia Bienes): leer `deuda` da **EXACTO**, leer otro tema de Bienes da **PARCIAL** y leer uno de otra familia da **NINGUNO**. Los textos muestran el nombre del tema de mapa. Mecánicamente, un tema de mapa se comporta igual que su equivalente; lo que agrega es texto. Hoy el Mapa B no declara temas de mapa, así que esta lógica se prueba con datos de prueba (*hiperinflación* es del Mapa A). Si el Mapa B debería declarar algunos es una pregunta abierta.
8. **Las familias no tienen el mismo tamaño** (5/4/5/5/4). Eso da una ventaja **estructural** a las familias grandes: la probabilidad de PARCIAL y el valor esperado al azar cambian con el tamaño de la familia del tema leído (cifras en Formulas). La meta de sesgo de Open Questions se mide contra la línea base de cada familia, no contra el promedio. El sesgo real depende también de cómo reparten las familias las Cartas y el Generador, así que se vuelve a medir en el prototipo con los datos reales. Mientras no haya build publicada, revisar la asignación es barato, porque las cartas y las situaciones referencian temas por identificador; después, cambiar la familia de un tema está prohibido (States, D-45).
9. **Una partida guardada cuya situación contiene un rol que ahora está deshabilitado.** La situación ya generada se respeta: contiene ese rol, así que una posición con ese rol se compara normal (R11, paso 2, mira la situación, no el catálogo). Deshabilitar un rol solo cambia lo que genera el Generador de ahí en adelante.

## Dependencies

**Depende de:** ninguno (capa Foundation).

**Dependen de la Taxonomía:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Base de Datos de Cartas | Dura | Asocia cada palabra clave a un tema |
| Interpretación y Sentencia | Dura | El tema de la palabra clave elegida es el tema leído |
| Tapete y Tooltips de Cartas | Blanda | Nombre visible, familia y marca de cada tema |
| Generador de Situaciones | Dura | Temas por rol, motivo (tema y forma de pregunta) |
| Tiradas | Dura | Traduce cada posición a un rol o a "libre"; declara la forma esperada |
| Resonancia y Resolución | Dura | `comparar` y la lista de resultados por posición |
| Arquetipos y Pieles de Mapa | Dura | Temas típicos de cada arquetipo y sus secretos; temas de mapa |
| Textos por Plantillas | Dura | Nombres visibles de temas y roles |
| Gramática de Combinación | Blanda | Familia de cada palo, para el palo dominante |
| Preguntas Capciosas | Blanda, indirecta | Pregunta por temas a través del Generador y de Textos |
| Inspección y Tells | Blanda, indirecta | Los tells apuntan a los temas de la verdad, a través del Generador |

**Bidireccionalidad:** ninguno de estos sistemas tiene GDD todavía. La sección Dependencies de cada uno tiene que nombrar a la Taxonomía cuando se escriba. En `systems-index.md` figuran como dependientes directos todos los de tipo dura o blanda; los indirectos llegan por el Generador.

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Asignación de tema a familia | Tabla de R1 (5/4/5/5/4) | Toda familia con el mínimo de temas activos. **Solo se toca antes de la primera build publicada**; después, `FAMILIA_CAMBIADA` (D-45) | Probabilidad de parcial por familia y línea base de Formulas |
| Mínimo de temas activos por familia | 2 (objetivo de diseño: 3) | 2 a 4 con el catálogo actual (con 1 no hay parcial posible; con 5 o más Bienes y Destino, que tienen 4 temas, quedan bajo el mínimo y falla AC-01a) | Lo que acepta el validador, que lee el valor de acá y no lo tiene fijo en el código |
| Roles habilitados | origen, conflicto, desenlace | Al menos 1 | Cuántos temas genera el Generador por situación |
| Formas de pregunta habilitadas | sí o no, situación general | Al menos 1 | Tiradas esperadas disponibles |

## Visual/Audio Requirements

- Cada familia tiene una marca visual propia, la misma en el tooltip, el tapete y cualquier texto: el símbolo de su palo (copa, oro, espada, basto) o, para Destino, el de los Arcanos Mayores.
- La marca no depende solo del color, por accesibilidad.
- El color de cada familia sale de la paleta de las cartas de 1909 (D-39). El detalle se define en `/art-bible`.
- No hay sonido propio de este sistema.

## Game Feel

No aplica: la Taxonomía no se opera directamente. El feel del acierto exacto o parcial le corresponde a Resonancia.

## UI Requirements

- El tooltip de cada carta muestra, para la palabra clave derecha y la invertida, **el tema y su familia**: por ejemplo, "*engaño* · Conflicto" con la marca de la familia.
- El nombre del tema que se ve sale de la tabla de idioma, nunca del identificador interno.
- Los roles no se muestran con su nombre técnico. El jugador ve el nombre de la posición de la tirada ("Pasado", "Presente"); el rol queda detrás.

> 📌 **UX Flag — Taxonomía de Temas y Roles:** antes de escribir las historias de implementación hay que hacer el spec del tooltip con `/ux-design`. Los criterios de aceptación del tooltip y de la marca (con captura retenida, incluida una en escala de grises) se escriben ahí, y las historias del tooltip no cierran sin ellos.

## Cross-References

| Fuente | Qué se toma |
|---|---|
| GDD §3.2, §3.3 | Temas derivados de las palabras clave; temas públicos |
| GDD §3.5 | Palos y elementos → familias |
| GDD §5.3 | Motivo de consulta, separado en tema y forma de pregunta |
| GDD §5.4 | Tirada esperada según la forma de pregunta |
| GDD §5.8 | Match 0/1/2 → exacto / parcial / ninguno |
| D-08, D-37, D-39 | Significado público; desacople entre Generador y Tiradas; paleta de 1909 |
| D-42, D-43, D-44, D-45, D-46, D-47, D-48 | Criterio Conflicto/Destino; decisiones de las revisiones full y lean |

## Acceptance Criteria

Las cifras de Formulas se derivan del reparto y las prueba AC-09. Los criterios salen de Core Rules, States, Formulas y Edge Cases.

Convenciones de prueba:
- Los errores de datos se prueban contra el validador (R13): cada AC verifica que la lista **contiene** un error con ese código y ese sujeto (formato de R13), nunca el texto. Que el juego no arranque se prueba una sola vez (AC-25a y AC-25b).
- Los errores de `comparar` se prueban por su código (`ID_INEXISTENTE`, `LEIDO_ES_DE_MAPA`): no alcanza con que falle.
- Cada AC arma su propio fixture con nombre; ninguno depende de otro AC ni del orden de ejecución.
- Los AC de nombres visibles usan **tablas de idioma de prueba con nombres centinela** (por ejemplo `«A:amor»`), nunca la tabla real, para que mostrar un identificador se pueda detectar.
- **Evidencia:** todos son Logic (test unitario en el test root del motor, `[test root]/taxonomia/`), salvo los marcados Integration o UI.
- **Provisorios:** dependen de un GDD que todavía no existe. No bloquean el cierre de una historia hasta que ese GDD exista y los revise.
- Los AC-16 a AC-18 se retiraron: probaban al Generador y pasan a su GDD (ver Open Questions). Sus números no se reutilizan.

**Datos del catálogo**
- **AC-01a** (R1, R2, R3) — GIVEN el catálogo base, WHEN se carga, THEN tiene exactamente las 5 familias de R1, cada tema base tiene exactamente una familia y cada familia tiene al menos el mínimo de temas activos de la perilla.
- **AC-01b** (R1; snapshot) — GIVEN el catálogo base, WHEN se carga, THEN sus temas base activos son exactamente: `familia.emocion` `amor`, `culpa`, `duelo`, `deseo`, `alegria`; `familia.bienes` `deuda`, `fortuna`, `hogar`, `trabajo`; `familia.conflicto` `traicion`, `ley`, `violencia`, `engano`, `secreto`; `familia.ambicion` `poder`, `rivalidad`, `fama`, `riesgo`, `exito`; `familia.destino` `muerte`, `locura`, `enfermedad`, `cambio` (todos con prefijo `tema.`). Este snapshot se actualiza a propósito, junto con la decisión que cambie el catálogo.
- **AC-01c** (R13; Integration, *provisorio hasta Cartas y Tiradas*) — GIVEN el catálogo base, las cartas, las tiradas, los mapas y la tabla de idioma reales, WHEN se valida, THEN la lista de errores está vacía.
- **AC-02a** (R4) — GIVEN las tablas de idioma de prueba A y B, con nombres centinela distintos entre sí y distintos del identificador, WHEN se pide el nombre visible de cada tema con cada tabla, THEN devuelve el de esa tabla, nunca el identificador, y el conjunto de identificadores del catálogo es el mismo con las dos.
- **AC-02b** (R13) — GIVEN la tabla de idioma `es_prueba` a la que le falta el nombre de `tema.deuda`, WHEN se valida, THEN la lista contiene `NOMBRE_FALTANTE` con sujeto `tema.deuda@es_prueba`.
- **AC-02c** (R13; un caso por identificador) — GIVEN la tabla de idioma `es_prueba` a la que le falta el nombre de uno de `familia.bienes`, `rol.origen`, `forma.si_o_no` o `mapa_a.hiperinflacion`, WHEN se valida, THEN la lista contiene `NOMBRE_FALTANTE` con sujeto `<ese identificador>@es_prueba`.
- **AC-03a** (R7, E1) — GIVEN la carta de prueba `carta.copas_05` con la palabra clave derecha sin tema, WHEN se valida, THEN la lista contiene `KW_SIN_TEMA` con sujeto `carta.copas_05/derecha/1`.
- **AC-03b** (R7, E1) — GIVEN `carta.copas_05` con la palabra clave invertida apuntando a `tema.inexistente`, WHEN se valida, THEN la lista contiene `KW_TEMA_INEXISTENTE` con sujeto `carta.copas_05/invertida/1`.
- **AC-03c** (R7) — GIVEN `carta.copas_05` con la palabra clave derecha asociada a `tema.deuda` y `tema.fortuna`, WHEN se valida, THEN la lista contiene `KW_TEMAS_MULTIPLES` con sujeto `carta.copas_05/derecha/1`.
- **AC-04a** (R2, E1) — GIVEN un tema `tema.prueba` sin familia, WHEN se valida, THEN la lista contiene `TEMA_SIN_FAMILIA` con sujeto `tema.prueba`.
- **AC-04b** (R2, E1) — GIVEN un tema `tema.prueba` con familia `familia.sombra`, que no está declarada, WHEN se valida, THEN la lista contiene `FAMILIA_INEXISTENTE` con sujeto `tema.prueba`.
- **AC-04c** (R1) — GIVEN un catálogo que declara la familia `familia.sombra` además de las 5, WHEN se valida, THEN la lista contiene `FAMILIA_EXTRA` con sujeto `familia.sombra`.
- **AC-05a** (R4) — GIVEN un catálogo con dos temas activos de identificador `tema.deuda`, WHEN se valida, THEN la lista contiene `ID_DUPLICADO` con sujeto `tema.deuda`.
- **AC-05d** (R4) — GIVEN un catálogo con dos temas `tema.deuda`, uno activo y otro deprecado, WHEN se valida, THEN la lista contiene `ID_DUPLICADO` con sujeto `tema.deuda`.
- **AC-05b** (R4, States) — GIVEN un catálogo anterior con `tema.deuda` deprecado y uno nuevo donde `tema.deuda` no está, WHEN se valida, THEN la lista contiene `ID_ELIMINADO` con sujeto `tema.deuda`.
- **AC-05e** (R4, States) — GIVEN un catálogo anterior con `tema.deuda` activo y uno nuevo donde no está, WHEN se valida, THEN la lista contiene `ID_ELIMINADO` con sujeto `tema.deuda`.
- **AC-05f** (R4, States) — GIVEN un catálogo anterior con `rol.el_otro` y uno nuevo donde no está, WHEN se valida, THEN la lista contiene `ID_ELIMINADO` con sujeto `rol.el_otro`.
- **AC-05c** (States) — GIVEN un catálogo anterior con `tema.deuda` deprecado y uno nuevo con `tema.deuda` activo, WHEN se valida, THEN la lista contiene `ID_REACTIVADO` con sujeto `tema.deuda`.
- **AC-05g** (R13) — GIVEN un catálogo anterior vacío y el catálogo base, WHEN se valida, THEN la lista no contiene `ID_ELIMINADO`, `ID_REACTIVADO` ni `DEPRECAR_CON_DEPENDIENTES`.
- **AC-05h** (States) — GIVEN un catálogo anterior con `rol.el_otro` deshabilitado y uno nuevo con `rol.el_otro` habilitado, WHEN se valida, THEN la lista no contiene `ID_REACTIVADO`.
- **AC-25a** (E1, R13; Integration) — GIVEN el catálogo de prueba `fixture_invalido_arranque`, WHEN corre la secuencia de arranque sin pantalla, THEN devuelve "no arrancó", el menú principal nunca se alcanza y los errores que devuelve son los mismos que da `validar_catalogo`. Control: con el catálogo base, arranca y se llega al menú principal.
- **AC-25b** (E1; UI) — GIVEN `fixture_invalido_arranque`, WHEN se lanza el juego real, THEN la pantalla de error lista el código y el sujeto de cada error. Evidencia: captura retenida en `production/qa/evidence/`.
- **AC-26a** (R8, R10) — GIVEN el catálogo base, WHEN se carga, THEN los roles habilitados son `rol.origen`, `rol.conflicto` y `rol.desenlace`, y `rol.el_otro`, `rol.camino_a` y `rol.camino_b` existen y están deshabilitados.
- **AC-26b** (R12) — GIVEN el catálogo base, WHEN se carga, THEN las formas habilitadas son `forma.si_o_no` y `forma.situacion_general`, y `forma.dilema`, `forma.vinculo` y `forma.asunto_grave` existen y están deshabilitadas.
- **AC-27a** (R4) — GIVEN la entrada 3 de la lista de temas del archivo `temas_prueba` con identificador vacío, WHEN se valida, THEN la lista contiene `ID_VACIO` con sujeto `temas_prueba#3`.
- **AC-27b** (R4) — GIVEN un tema `tema.Traición`, WHEN se valida, THEN la lista contiene `ID_FORMATO` con sujeto `tema.Traición`.
- **AC-27c** (R4) — GIVEN un tema `tema.`, WHEN se valida, THEN la lista contiene `ID_FORMATO` con sujeto `tema.`.
- **AC-27d** (R4) — GIVEN una entrada de la lista de temas con identificador `rol.prueba`, WHEN se valida, THEN la lista contiene `ID_FORMATO` con sujeto `rol.prueba`.
- **AC-27e** (R4) — GIVEN un tema de mapa `mapa_a_b.prueba`, WHEN se valida, THEN la lista contiene `ID_FORMATO` con sujeto `mapa_a_b.prueba`.
- **AC-28a** (R3) — GIVEN un catálogo de prueba donde `familia.destino` tiene un solo tema activo, WHEN se valida, THEN la lista contiene `FAMILIA_BAJO_MINIMO` con sujeto `familia.destino`.
- **AC-28b** (R3; borde) — GIVEN un catálogo de prueba donde `familia.destino` tiene exactamente 2 temas activos, WHEN se valida, THEN la lista no contiene `FAMILIA_BAJO_MINIMO`.
- **AC-28c** (R3, States) — GIVEN un catálogo de prueba donde `familia.destino` tiene 3 temas, 2 de ellos deprecados, WHEN se valida, THEN la lista contiene `FAMILIA_BAJO_MINIMO` con sujeto `familia.destino`.
- **AC-28d** (R3) — GIVEN un catálogo de prueba donde `familia.destino` tiene un solo tema base activo y un tema de mapa activo que lo tiene como equivalente, WHEN se valida, THEN la lista contiene `FAMILIA_BAJO_MINIMO` con sujeto `familia.destino`.
- **AC-02d** (R13) — GIVEN las tablas de idioma `es_prueba` (completa) y `en_prueba` (sin el nombre de `tema.deuda`), WHEN se valida, THEN la lista contiene `NOMBRE_FALTANTE` con sujeto `tema.deuda@en_prueba` y no contiene `tema.deuda@es_prueba`.
- **AC-35a** (Esquema) — GIVEN un tema `tema.prueba` con `estado` = `pausado`, WHEN se valida, THEN la lista contiene `CAMPO_INVALIDO` con sujeto `tema.prueba`.
- **AC-35b** (Esquema) — GIVEN un rol `rol.origen` con `habilitado` = `quizás`, WHEN se valida, THEN la lista contiene `CAMPO_INVALIDO` con sujeto `rol.origen`.
- **AC-35c** (Esquema) — GIVEN un tema `tema.deuda` con `afinidad_por_rol` no vacío, WHEN se valida, THEN la lista contiene `CAMPO_INVALIDO` con sujeto `tema.deuda`. Control: con `afinidad_por_rol` vacío, no lo contiene.
- **AC-35d** (Esquema, D-51) — GIVEN un tema `tema.prueba` con `valencia` = `neutra`, WHEN se valida, THEN la lista contiene `CAMPO_INVALIDO` con sujeto `tema.prueba`. Control: con `favorable`, no lo contiene.
- **AC-35e** (R1, D-51; snapshot) — GIVEN el catálogo base, WHEN se carga, THEN cada tema tiene la valencia de la tabla de R1, y `mapa_a.hiperinflacion` toma la de su equivalente (`tema.deuda`, desfavorable).
- **AC-29a** (R10) — GIVEN un catálogo de prueba sin roles habilitados, WHEN se valida, THEN la lista contiene `SIN_ROLES_HABILITADOS` con sujeto `catalogo`.
- **AC-29b** (R12) — GIVEN un catálogo de prueba sin formas habilitadas, WHEN se valida, THEN la lista contiene `SIN_FORMAS_HABILITADAS` con sujeto `catalogo`.

**Comparación**
- **AC-06** (R6) — GIVEN leído `tema.traicion` y verdadero `tema.traicion`, WHEN se comparan, THEN el resultado es EXACTO.
- **AC-07** (R6) — GIVEN leído `tema.engano` y verdadero `tema.traicion`, y también al revés, WHEN se comparan, THEN los dos resultados son PARCIAL.
- **AC-08** (R6) — GIVEN leído `tema.amor` y verdadero `tema.deuda`, WHEN se comparan, THEN el resultado es NINGUNO.
- **AC-09** (R6, Formulas; exhaustivo) — GIVEN el catálogo base, WHEN se compara cada par ordenado (leído, verdadero) de temas base activos, THEN cada resultado es EXACTO si son el mismo tema, PARCIAL si son distintos de la misma familia y NINGUNO si son de familias distintas; y los totales son 23 EXACTO, 84 PARCIAL y 422 NINGUNO. *Los totales son provisorios: cambian si cambia el reparto.*
- **AC-10** (R7) — GIVEN una carta con palabra clave derecha de tema `tema.traicion` e invertida de tema `tema.amor`, WHEN se selecciona la derecha y después la invertida, THEN el tema leído es `tema.traicion` y después `tema.amor`.
- **AC-11** (R11, E5) — GIVEN una posición `p1` con rol `rol.origen`, una situación que contiene `rol.origen` y ninguna palabra clave elegida, WHEN se resuelve, THEN la lista es [(`p1`, `rol.origen`, NINGUNO)].
- **AC-30a** (R6) — GIVEN leído `tema.inexistente` y verdadero `tema.traicion`, WHEN se llama a `comparar`, THEN falla con `ID_INEXISTENTE` y no devuelve resultado.
- **AC-30b** (R6) — GIVEN leído `tema.traicion` y verdadero `tema.inexistente`, WHEN se llama a `comparar`, THEN falla con `ID_INEXISTENTE` y no devuelve resultado.
- **AC-30c** (R6) — GIVEN leído `mapa_a.hiperinflacion` y verdadero `tema.deuda`, WHEN se llama a `comparar`, THEN falla con `LEIDO_ES_DE_MAPA` y no devuelve resultado.
- **AC-30d** (R6; orden) — GIVEN leído `mapa_a.inexistente` y verdadero `tema.deuda`, WHEN se llama a `comparar`, THEN falla con `ID_INEXISTENTE`, no con `LEIDO_ES_DE_MAPA`.

**Roles y posiciones** *(provisorios hasta el GDD de Tiradas; usan tiradas de prueba)*
- **AC-12** (R9, R11) — GIVEN la tirada de prueba con la posición `p1` de rol `rol.origen` y la posición `p2` libre, una situación con origen `tema.traicion`, leído `tema.traicion` en `p1` y una palabra clave elegida en `p2`, WHEN se resuelve, THEN la lista es [(`p1`, `rol.origen`, EXACTO), (`p2`, libre, SIN_COMPARACION)], en ese orden.
- **AC-13a** (E3, R11) — GIVEN la posición `p1` con rol `rol.el_otro`, una situación sin ese rol y una palabra clave elegida, WHEN se resuelve, THEN la lista es [(`p1`, `rol.el_otro`, SIN_COMPARACION)].
- **AC-13b** (E3, R11) — GIVEN la posición `p1` con rol `rol.el_otro`, una situación sin ese rol y ninguna palabra clave elegida, WHEN se resuelve, THEN la lista es [(`p1`, `rol.el_otro`, SIN_COMPARACION)].
- **AC-14** (E2) — GIVEN una tirada de prueba de una sola posición `p1` con rol `rol.conflicto`, una situación con origen `tema.amor`, conflicto `tema.traicion` y desenlace `tema.muerte`, y leído `tema.engano`, WHEN se resuelve, THEN la lista tiene largo 1 y es [(`p1`, `rol.conflicto`, PARCIAL)].
- **AC-15** (E4) — GIVEN una tirada de prueba con las posiciones `p1` y `p2`, las dos de rol `rol.origen`, verdadero `tema.traicion` y leídos `tema.engano` en `p1` y `tema.amor` en `p2`, WHEN se resuelve, THEN la lista es [(`p1`, `rol.origen`, PARCIAL), (`p2`, `rol.origen`, NINGUNO)].
- **AC-31** (E3, R13) — GIVEN la tirada de prueba `tirada_typo` con la posición `p1` de rol `rol.orijen`, WHEN se valida, THEN la lista contiene `ROL_INEXISTENTE` con sujeto `tirada_typo/p1`.
- **AC-37a** (R9, R13) — GIVEN la tirada de prueba `tirada_ambigua` con la posición `p1` sin rol y sin `libre`, WHEN se valida, THEN la lista contiene `POSICION_AMBIGUA` con sujeto `tirada_ambigua/p1`.
- **AC-37b** (R9, R13) — GIVEN `tirada_ambigua` con la posición `p1` de rol `rol.origen` y `libre` = sí, WHEN se valida, THEN la lista contiene `POSICION_AMBIGUA` con sujeto `tirada_ambigua/p1`. Control: con `p1` solo de rol `rol.origen`, o solo `libre` = sí, no la contiene.
- **AC-38** (R9, R13) — GIVEN la tirada de prueba `tirada_libre` con dos posiciones, las dos `libre` = sí, WHEN se valida, THEN la lista contiene `TIRADA_SIN_COMPARABLES` con sujeto `tirada_libre`. Control: con una posición de rol `rol.origen`, no la contiene.
- **AC-33** (R12, R13) — GIVEN la tirada de prueba `tirada_forma` que declara como esperada `forma.inexistente`, WHEN se valida, THEN la lista contiene `FORMA_INEXISTENTE` con sujeto `tirada_forma`.
- **AC-34** (E9) — GIVEN un catálogo con `rol.el_otro` deshabilitado, una situación que contiene `rol.el_otro` con verdadero `tema.traicion`, y la posición `p1` de rol `rol.el_otro` con leído `tema.traicion`, WHEN se resuelve, THEN la lista es [(`p1`, `rol.el_otro`, EXACTO)].

**Ciclo de vida y mapas**
- **AC-19a** (E6, States) — GIVEN el fixture `catalogo_traicion_deprecada` (catálogo base con `tema.traicion` deprecado), WHEN se compara leído `tema.traicion` contra verdadero `tema.traicion`, THEN da EXACTO.
- **AC-19b** (E6, States) — GIVEN `catalogo_traicion_deprecada`, WHEN se compara leído `tema.engano` contra verdadero `tema.traicion`, THEN da PARCIAL.
- **AC-19c** (States) — GIVEN `catalogo_traicion_deprecada` y una carta con una palabra clave de tema `tema.traicion`, WHEN se valida, THEN la lista no contiene ningún error.
- **AC-19d** (E6; Integration, *provisorio hasta Guardado*) — GIVEN una partida guardada con el catálogo base, con verdadero de origen `tema.traicion`, en la que leer `tema.traicion` da EXACTO y leer `tema.engano` da PARCIAL, WHEN se carga con `catalogo_traicion_deprecada`, THEN las mismas lecturas dan EXACTO y PARCIAL.
- **AC-20a** (R5) — GIVEN el tema de mapa de prueba `mapa_a.hiperinflacion` con equivalente `tema.deuda`, WHEN se valida, THEN no hay errores y su familia es `familia.bienes`.
- **AC-20b** (R5) — GIVEN un tema de mapa `mapa_a.prueba` sin equivalente, WHEN se valida, THEN la lista contiene `MAPA_SIN_EQUIVALENTE` con sujeto `mapa_a.prueba`.
- **AC-20c** (R5) — GIVEN un tema de mapa `mapa_a.prueba` con equivalente `tema.inexistente`, WHEN se valida, THEN la lista contiene `MAPA_EQUIV_INEXISTENTE` con sujeto `mapa_a.prueba`.
- **AC-20d** (R5) — GIVEN un tema de mapa `mapa_a.prueba` con equivalente `mapa_a.hiperinflacion`, WHEN se valida, THEN la lista contiene `MAPA_EQUIV_ES_DE_MAPA` con sujeto `mapa_a.prueba`.
- **AC-20e** (R5, States) — GIVEN, sin catálogo anterior, un tema de mapa activo `mapa_a.prueba` con equivalente `tema.deuda` deprecado, WHEN se valida, THEN la lista contiene `MAPA_EQUIV_DEPRECADO` con sujeto `mapa_a.prueba` y no contiene `DEPRECAR_CON_DEPENDIENTES`.
- **AC-20f1** (R5) — GIVEN un tema de mapa `mapa_a.prueba` con equivalente `tema.deuda` que declara familia `familia.emocion`, WHEN se valida, THEN la lista contiene `MAPA_DECLARA_FAMILIA` con sujeto `mapa_a.prueba`.
- **AC-20f2** (R5) — GIVEN un tema de mapa `mapa_a.prueba` con equivalente `tema.deuda` que declara familia `familia.bienes` (la misma que la del equivalente), WHEN se valida, THEN la lista contiene `MAPA_DECLARA_FAMILIA` con sujeto `mapa_a.prueba`.
- **AC-20g** (R5, States) — GIVEN un catálogo anterior con `mapa_a.hiperinflacion` activo → `tema.deuda` activo, y uno nuevo con los dos deprecados (y `familia.bienes` sigue con el mínimo), WHEN se valida, THEN la lista no contiene `MAPA_EQUIV_DEPRECADO` ni `DEPRECAR_CON_DEPENDIENTES`.
- **AC-20h** (R5) — GIVEN los temas de mapa `mapa_a.hiperinflacion` y `mapa_a.usura`, los dos con equivalente `tema.deuda`, WHEN se valida, THEN la lista no contiene errores.
- **AC-21a** (R5) — GIVEN el archivo del Mapa A con una entrada `tema.deuda` idéntica a la del catálogo base, WHEN se valida, THEN la lista contiene `MAPA_SOBREESCRIBE_BASE` con sujeto `tema.deuda` y no contiene `ID_DUPLICADO` ni `ID_FORMATO`.
- **AC-21b** (R5) — GIVEN el archivo del Mapa A con una entrada `mapa_b.prueba`, WHEN se valida, THEN la lista contiene `MAPA_ID_AJENO` con sujeto `mapa_b.prueba` y no contiene `ID_FORMATO`.
- **AC-21c** (R5) — GIVEN el archivo del Mapa A con una entrada `rol.prueba`, WHEN se valida, THEN la lista contiene `MAPA_ID_AJENO` con sujeto `rol.prueba` y no contiene `ID_FORMATO`.
- **AC-21d** (R5) — GIVEN el archivo del Mapa A con una entrada `mapa_a_b.prueba`, WHEN se valida, THEN la lista contiene `ID_FORMATO` con sujeto `mapa_a_b.prueba` y no contiene `MAPA_ID_AJENO`.
- **AC-22** (E7, R6) — GIVEN verdadero `mapa_a.hiperinflacion` (equivalente `tema.deuda`), WHEN se compara contra leído `tema.deuda`, `tema.fortuna` y `tema.amor`, THEN los resultados son EXACTO, PARCIAL y NINGUNO.
- **AC-23** (E7) — GIVEN `carta.copas_05` con la palabra clave derecha asociada a `mapa_a.hiperinflacion`, WHEN se valida, THEN la lista contiene `KW_TEMA_DE_MAPA` con sujeto `carta.copas_05/derecha/1`.
- **AC-24a** (E7) — GIVEN una tabla de idioma de prueba con `«MAPA:Hiperinflación»` y `«BASE:Deuda»`, WHEN se pide el nombre visible de `mapa_a.hiperinflacion`, THEN es `«MAPA:Hiperinflación»`.
- **AC-24b** (E7; Integration, *provisorio hasta Textos por Plantillas*) — GIVEN una plantilla de sentencia con el tema verdadero `mapa_a.hiperinflacion` y la tabla de prueba de AC-24a, WHEN se arma el texto, THEN contiene `«MAPA:Hiperinflación»` y no contiene `«BASE:Deuda»`.
- **AC-36a** (States, D-45) — GIVEN un catálogo anterior con `tema.hogar` en `familia.bienes` y uno nuevo con `tema.hogar` en `familia.emocion`, WHEN se valida, THEN la lista contiene `FAMILIA_CAMBIADA` con sujeto `tema.hogar`.
- **AC-36b** (States, D-45) — GIVEN un catálogo anterior con `mapa_a.hiperinflacion` → `tema.deuda` y uno nuevo con `mapa_a.hiperinflacion` → `tema.fortuna`, WHEN se valida, THEN la lista contiene `EQUIV_CAMBIADO` con sujeto `mapa_a.hiperinflacion`.
- **AC-36c** (States, D-45) — GIVEN un catálogo anterior vacío y el catálogo base, o un catálogo anterior igual al nuevo, WHEN se valida, THEN la lista no contiene `FAMILIA_CAMBIADA` ni `EQUIV_CAMBIADO`.
- **AC-32** (States) — GIVEN un catálogo anterior con `mapa_a.hiperinflacion` activo → `tema.deuda` activo, y uno nuevo donde `tema.deuda` pasa a deprecado y el tema de mapa sigue activo, WHEN se valida, THEN la lista contiene `DEPRECAR_CON_DEPENDIENTES` con sujeto `tema.deuda` y no contiene `MAPA_EQUIV_DEPRECADO`.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| ¿El reparto de familias produce un sesgo que se note, además del estructural de Formulas? Medir en el prototipo, con las cartas y el Generador reales, el puntaje esperado al azar por familia y la frecuencia de "tirada sin jugada útil" por familia verdadera. Meta: ninguna familia se aparta más de ±15 % de **su propio valor de línea base en Formulas**; el desvío estructural del reparto (+6,2 % y −11,5 % sobre el promedio) no cuenta. Con el sorteo de la verdad según el mazo (Cartas F1, D-48), el sesgo real lo decide sobre todo la tradición de las cartas, no el reparto. Si Conflicto domina, la primera palanca es *secreto* (dato nuevo para revisar D-42) | Diseñador | Prototipo del núcleo |
| **Doble Fondo:** ¿contra qué rol se compara el tema del motivo? ¿La fachada puede ser de la misma familia que la verdad? (Daría parcial, y el Pilar 4 pide que la fachada rinda poco y seguro.) ¿Todos los clientes tienen Doble Fondo? ¿*Secreto* puede ser la verdad de un rol, o es una tautología con el Doble Fondo? Si no puede, la regla vive en el Generador | GDD del Generador | Al diseñar el Generador |
| **Coherencia entre roles (obligatoria antes del prototipo):** con 23 temas y 3 roles hay 12.167 tríos y muchos no cuentan una historia. Sin observables que reduzcan los candidatos por rol, el exacto es azar. El Generador tiene que dar una garantía mínima de coherencia; la afinidad de cada tema con cada rol (alta / posible / evitar) va en el campo reservado `afinidad_por_rol` | GDD del Generador | Antes del prototipo |
| **AC del Generador (ex AC-16 a AC-18):** cada situación tiene un tema por rol habilitado y ningún otro rol; el motivo tiene un tema activo y una forma habilitada; un tema deprecado nunca entra a los candidatos. Escribirlos como contrato sobre la lista de candidatos con un RNG simulado, sin semilla fija. Definir también cómo reparte las familias. Sumar un AC de playtest: los testers justifican sus elecciones por algo observado del cliente, no por azar | GDD del Generador | Al diseñar el Generador |
| **Agregación y umbral:** cómo se combinan varias posiciones del mismo rol (suma, máximo o promedio); qué pasa si la lista no tiene ningún resultado comparable (0/0); el umbral se calibra contra la línea base de Formulas, porque sin castigo por error adivinar siempre conviene; ¿el feedback distingue "deduje mal" de "no tenía la carta", y "no elegí" de "elegí mal"? ¿El feedback de un PARCIAL dice que fue por la familia? | GDD de Resonancia | Al diseñar Resonancia |
| Carta Única cubre un solo rol de tres. ¿Qué rol cubre "Respuesta"? ¿Qué es la verdad de una pregunta *sí o no*, si la verdad se expresa en temas? Toda tirada tiene que tener al menos una posición con rol habilitado. ¿Las posiciones libres son una falsa elección para el jugador? ¿Dónde vive el vínculo forma → tirada esperada (`FORMA_INEXISTENTE`)? | GDD de Tiradas | Al diseñar Tiradas |
| Roles posteriores al MVP (el otro, camino A y B) y su mapeo a posiciones | GDD de Tiradas | Al diseñar Tiradas |
| La exigencia "cada tema aparece en al menos una carta del nivel Aprendiz". **Invariante del Pilar 6:** toda tirada repartida puede llegar al menos a PARCIAL con alguna elección (por ejemplo, que las dos palabras clave de cada carta sean de familias distintas). ¿"Una palabra clave = un tema" deja poca palanca de lector? ¿Hace falta un tema secundario que puntúe como máximo parcial? Destino representa a los 22 Arcanos Mayores pero tiene 3 temas: ¿cuántas cartas la llevan? **Resuelta en D-47 y revisada en D-48:** sin tema secundario. El invariante absoluto se reemplaza por la cobertura que da la tradición (piso por familia, Cartas F2). Cada tema aparece en alguna de las 78 cartas, y el Generador sortea la verdad según lo que el mazo activo puede decir (Cartas F1). El riesgo que queda (`P_cero` ≈ 0,38 en Tres Tiempos) está en Open Questions de Cartas | GDD de Cartas | Resuelta (D-48) |
| ¿Qué señal observable distingue a cada tema de los de su familia? Si los tells no separan temas dentro de una familia, el exacto es azar | GDD de Inspección y Tells | Al diseñar Tells |
| Guardar la versión del catálogo en la partida. Ya no hace falta para detectar cambios de familia (D-45 los prohíbe entre builds publicadas y el validador los detecta); queda solo si Guardado la quiere para migraciones | GDD de Guardado | Al diseñar Guardado |
| La marca de la familia es el símbolo de un palo: en una carta de otro palo (Cinco de Copas con *deuda*) puede leerse como el palo de la carta. Resolverlo en el spec del tooltip | `/ux-design`, `/art-bible` | Antes de las historias del tooltip |
| Vocabulario: <br>- Glosario de una línea por tema, con la frontera entre vecinos (deseo/amor, poder/rivalidad, engaño/traición, engaño/secreto) y la frontera Conflicto/Destino en los casos ambiguos (violencia sufrida / muerte, traición sufrida, ley / enfermedad): D-42 dice quién controla, pero *traición*, *violencia* y *ley* suelen pasarle al cliente. Sin esto, quien asigne temas a las palabras clave de las 78 cartas decide a ojo.<br>- Nombre visible de Destino. <br>- *Locura*: renombrarla por sensibilidad (estigma de la enfermedad mental), no solo por tono, y pasar el glosario por una lectura de sensibilidad (ESRB/PEGI). <br>- Colisión visible entre la familia "Conflicto" y el rol "conflicto" en el tooltip (D-43 resolvió los ids, no lo que lee el jugador); preferencia: renombrar la familia. <br>- *Fortuna* (¿suerte o dinero?) y *hogar* (¿casa o familia?). <br>- Renombrar *riesgo*, que es una actitud y no un asunto (*apuesta* y *juego* chocan con el "apostar" del Pilar 4). <br>- ¿El equivalente de *hiperinflación* es *deuda* o *fortuna*? | Diseñador | Antes de escribir los datos del catálogo |
| **Mapa B:** ¿declara temas de mapa para su clientela (juego clandestino, adicción, familia, fe, papeles migratorios)? E7 permite ampliar sin tocar los 23 temas base. **Esta respuesta decide si las historias de temas de mapa entran al MVP:** son 7 códigos del validador (`MAPA_*`, `EQUIV_CAMBIADO`, `KW_TEMA_DE_MAPA`) y unos 20 AC (AC-20*, 21*, 22, 23, 24*, 28d, 32, 36b). Si el Mapa B no declara temas de mapa, esas historias van después del MVP; el GDD no cambia | GDD de Arquetipos y Pieles, `design/mapas/mapa-b-new-carthage.md` | Antes de `/create-epics` |
| El GDD maestro está desfasado con esta Taxonomía en cinco puntos:<br>- El motivo de consulta (§5.3) sigue escrito como lista única y mezcla temas con cosas que no lo son: *dinero* (¿`fortuna` o `deuda`?), *salud* (`enfermedad`), *peligro* (¿`riesgo` o `violencia`?) y *decisión*, que es una forma de pregunta.<br>- §5.3, §5.8 y D-15 hablan de "temas por posición", y desde D-37 son temas por rol.<br>- §3.5 llama "la sentencia" al Futuro, y el rol es `desenlace`; "sentencia" ya es la intención retórica.<br>- *Enfermedad* pasó a Destino y se sumó *trabajo* (D-43). | Diseñador | Próxima versión del GDD maestro |
