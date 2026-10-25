# Base de Datos de Cartas — Anexo de producción

> **Status**: Diferido (D-53, D-54). **No se revisa hasta después del prototipo del núcleo.** Lo que está acá no lo necesita el prototipo: bloquea las historias de producción, no el prototipo.
> **GDD principal**: [`../base-de-datos-de-cartas.md`](../base-de-datos-de-cartas.md). Las reglas (R), fórmulas (F), casos (E), convenciones de prueba y fixtures son las de ese documento.
> **Cifras**: las que salen del conteo están en `design/balance/cifras-cartas.md`, generado por `tools/balance/cobertura_cartas.py`.

## Funciones (amplían R12)

Viven en el módulo de herramientas y pruebas (R12, Módulos):

- `marcas_progresion(informes por mazo) → lista de pares (mazo, Aprendiz)`: la marca de progresión (abajo, Cifras), que compara mazos y por eso no cabe en `informe_mazo`;
- `chequear_informe(informe) → lista de violaciones`: comprueba los invariantes del informe: `q_f ≤ u_f ≤ 2·q_f` (en enteros, con los conteos de R11), `|Σ p_t − 1|` ≤ 1e-9 o todos los `p_t` en 0, y `c_f ≤ c_f⁺`. Es una herramienta de prueba, no de datos. `q_f ≤ u_f ≤ 2·q_f` vale por construcción (cada carta aporta 0, 1 o 2 orientaciones a `c_f`): no es una regla de datos sino un invariante que prueba la implementación del informe.

## Cifras del informe (amplían R11)

Para cada mazo alcanzable, el informe agrega `P_pos_inv`, `P_cero_corr(k)` para cada `k` de `k_tiradas`, `T_ef`, `V_prior_v` por valencia con la marca de **valencia deducible**, y las marcas de progresión. Siguen las Salidas vacías y las Comparaciones de Formulas: con `T_m` = 0 quedan vacíos `P_pos_inv`, `P_cero_corr(k)` y `T_ef`; con `T_m^v` = 0, `V_prior_v` de esa valencia.

**Con *invertir*** (F3): `P_pos_inv = Σ_f p_f · u_f⁺`. Es una cota **teórica**: supone que *invertir* es gratis, ilimitado y que el jugador sabe cuándo conviene, o sea que conoce la verdad. Ninguna de las tres cosas es cierta, así que solo acota por arriba, y `(1 − P_pos_inv)³` acota `P_cero` por abajo. No hay cifra: el único detalle por carta del conteo es anterior a D-48, y su `u_f` no es compatible con los `q_f` de ahora. Se calcula con el reconteo.

**Roles en la misma familia** (F4): `P_cero_corr(k) = Σ_f p_f · (1 − q_f⁺)^k` supone que el Generador pone todos los roles en la misma familia. Por convexidad, `P_cero(k) ≤ P_cero_corr(k)`, y con las mismas marginales en todos los roles `P_cero_corr(k)` es el **máximo**. La independencia no es el mínimo: un Generador que reparte los roles en familias distintas puede quedar por debajo, y cuánto depende de cómo acople los roles, que lo define el Generador. Si el Generador cambia las marginales por rol (`afinidad_por_rol`), ninguna de las dos fórmulas es cota. Las dos son aproximaciones del caso real, no un intervalo que lo contenga. Con `k` = 1 coinciden. La carta aclaratoria se compara con la misma verdad que la carta de su posición, así que su modelo es `P_cero_corr(1 + a)` y no `(1 − P_pos⁺)^(1 + a)`; las dos cifras están en `cifras-cartas.md`.

**Número efectivo de verdades** (F5): `T_ef = 1 / Σ_t p_t²`, de 1 a `T_m`. Comparable entre mazos con distinto `T_m`. Concentrar el sorteo (`n_t^γ`, γ > 1) sube `V_prior` y baja `T_ef`.

**Por valencia** (F3, F5): `V_prior_v = max_t p_t^v`, con los pesos renormalizados de F3: la probabilidad de acertar el desenlace de un sí o no apostando al tema más frecuente de esa valencia, una vez deducida la respuesta. Con `T_m^v` = 1 vale 1: el desenlace de esa respuesta sale siempre del mismo tema, y como el catálogo es público, el jugador que deduce la respuesta conoce el desenlace exacto sin mirar las cartas (contra el Pilar 1). El informe lo marca como **valencia deducible**, sin impedir el arranque. No se compara con `V_prior_max`: hasta que el prototipo fije un umbral propio, solo se muestra.

**La progresión** (F4): `marcas_progresion` compara cada mazo de 2 o más palos con **cada** mazo Aprendiz de 1 palo que contiene, y marca el par (mazo, Aprendiz) cuando `P_pos⁺` del mazo < `P_pos⁺` del Aprendiz − `ε_prog` − 1e-9 (la tolerancia evita que una diferencia igual a `ε_prog` marque por la coma flotante). Compara `P_pos⁺` y no `P_cero`, así que no depende de `k` ni de `k_tiradas`: `P_cero(k) = (1 − P_pos⁺)^k` es monótona en `P_pos⁺`, y el orden entre mazos es el mismo para todo `k` **con independencia**. No vale para `P_cero_corr` ni `P_cero_f`: con el mazo A con `1 − q_f⁺` = 0,7 en todas las familias, y el B con 0,5 (`p_f` 0,6) y 0,95 (`p_f` 0,4), `P_cero_corr(1)` da 0,70 contra 0,68 y `P_cero_corr(3)` 0,343 contra 0,418: el orden se invierte. Una marca dice que un jugador que empezó con ese Aprendiz empeora el Pilar 6 al sumar palos. Las marcas del conteo están en `cifras-cartas.md` (§ Marca de progresión) y **no son concluyentes**: la diferencia es del tamaño del error de la aproximación de `p_f`, y `ε_prog` queda por debajo del ruido de un conteo de una sola lectura. Se reevalúan con el reconteo. Cómo se compensa es una pregunta de Prestidigitación (Open Questions del GDD).

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| `ε_prog` (margen de la marca de progresión, en `P_pos⁺`) | 0,005 | 0 a 0,02. Con el conteo actual, de una sola lectura, cualquier valor de este rango queda por debajo del ruido; recalibrar con el reconteo | Solo la marca de progresión del informe |

Dominio: de 0 a 0,05 (`float`, data file). Fuera de él es un error de configuración con sujeto `ε_prog`, como las perillas del GDD.

## Acceptance Criteria

Mismas convenciones que el GDD. Todos son Logic salvo AC-26 (Integration).

- **AC-18e** (R11, R12; invariantes) — GIVEN el informe de los 15 mazos del fixture, WHEN se le pasa a `chequear_informe`, THEN no devuelve ninguna violación. Controles, cada uno con un informe armado a mano: (1) `c_Destino` = 12 de `O` = 72 y 3 cartas con Destino de `N` = 36 (`q` 0,17, `u` 0,08) devuelve la violación de `q_f ≤ u_f`; (2) `c_f` = 12 con 6 cartas con `f` de `N` = 36 (`q_f` = `u_f` exacto) no devuelve ninguna violación, aunque en coma flotante `12/72` y `6/36` se calculen por caminos distintos; (3) `p_t` que suman 0,9 devuelven la violación de `Σ p_t`; (4) `c_f` = 5 con `c_f⁺` = 4 devuelve la violación de `c_f ≤ c_f⁺`.
- **AC-18f2** (F4; marca de progresión) — GIVEN `marcas_progresion` con un mazo de 2 palos de `P_pos⁺` 0,28 y sus dos Aprendiz con 0,29 y 0,27, THEN marca el par con el de 0,29 y no el de 0,27; con `P_pos⁺` 0,287, no marca ningún par (dentro de `ε_prog`); con exactamente 0,285 (diferencia igual a `ε_prog`), no marca. GIVEN un mazo de 3 palos de 0,28 con sus Aprendiz en 0,29, 0,27 y 0,30, THEN marca los pares con 0,29 y 0,30; GIVEN el de 4 palos, THEN lo compara con sus 4 Aprendiz. Ningún mazo de 1 palo aparece en un par. Las marcas son las mismas con informes calculados con `k_tiradas` = [1, 3] y = [2].
- **AC-P1** (F3; `P_pos_inv`; de AC-18a3) — GIVEN `fixture_informe_chico`, WHEN se pide el informe, THEN `P_pos_inv` = 0,667.
- **AC-P2** (F4; `P_cero_corr`; de AC-18a4 y AC-18c) — GIVEN `fixture_informe_chico`, WHEN se pide el informe, THEN `P_cero_corr(3)` = 0,125 y `P_cero_corr(1)` = `P_cero(1)` = 0,5. GIVEN los `q⁺` y `p_f` de AC-18c, WHEN se calcula, THEN `P_cero_corr(3)` = 0,3849 y `P_cero_corr(1)` = `P_cero(1)` = 0,7245.
- **AC-P3** (F5; `T_ef`; de AC-18a5 y AC-18h) — GIVEN `fixture_informe_chico`, WHEN se pide el informe, THEN `T_ef` = 2,793. GIVEN un mazo de prueba con `p` = 0,5 / 0,25 / 0,25, THEN `T_ef` = 2,667; con `p` uniforme sobre 3 temas, 3; con `T_m` = 1, 1.
- **AC-P4** (F3, F5; `V_prior_v` y valencia deducible; de AC-18m) — GIVEN `fixture_informe_chico` con las valencias de AC-18m, WHEN se pide el informe, THEN `T_m^favorable` = 1, `V_prior_favorable` = 1 y el informe marca la valencia favorable como deducible; `V_prior_desfavorable` = 0,6 y esa valencia no se marca. Control: el fixture completo no marca ninguna valencia deducible.
- **AC-P5** (Tuning Knobs; `ε_prog`; de AC-27) — GIVEN `config_prueba` con `ε_prog` = −0,001 o 0,06 (un caso cada uno), WHEN se valida, THEN contiene un error de configuración con sujeto `ε_prog`, ningún error de datos, y no se calcula el informe. Control: con 0 y con 0,05, ningún error de configuración con sujeto `ε_prog`.
- **AC-P6** (Salidas vacías; de AC-22b) — GIVEN el mazo de AC-22a, WHEN se llama `informe_mazo`, THEN `P_pos_inv`, `P_cero_corr(k)` para cada `k` de `k_tiradas_prueba`, `T_ef` y los dos `V_prior_v` están vacíos, sin excepción, y no hay marca de valencia deducible.
- **AC-26** (R12, Pilar 1; Integration, *provisorio hasta `/create-architecture`*) — GIVEN la build, WHEN se compila, THEN el módulo de juego no depende del módulo de herramientas y pruebas que fije la arquitectura, donde viven `acierto_posible`, `informe_cobertura`, `informe_mazo`, `marcas_progresion` y `chequear_informe` (R12): la regla de dependencias del build lo impide. Control positivo: una referencia agregada a propósito desde un sistema de juego hace fallar el build. Control negativo: `validar_catalogo`, `validar_mazo` y `pesos_sorteo` están en el módulo de juego y el build pasa. Una búsqueda de texto de `acierto_posible` en el código de juego queda como respaldo, no como prueba (no ve alias ni llamadas indirectas). La evidencia es la salida de CI.
- **AC-28** (R12; pureza) — GIVEN el fixture y una copia profunda de las cartas, el catálogo y la configuración, WHEN se llama `informe_cobertura` dos veces, y una tercera con las cartas en otro orden, THEN los tres informes son iguales y las entradas siguen iguales a la copia. Además, para cada mazo alcanzable, `validar_mazo` da los mismos errores de F2, `MAZO_SIN_VERDADES` y `MAZO_SIN_VALENCIA` que `validar_catalogo` con ese mazo como sujeto, y `pesos_sorteo` da los mismos `p_t` que el informe.
