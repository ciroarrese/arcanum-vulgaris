# Review Log — Base de Datos de Cartas

## Review — 2026-10-24 — Verdict: NEEDS REVISION
Review mode: lean · Workflow: standard
Scope signal: L
Specialists: ninguno (lean)
Blocking items: 4 | Recommended: 9
Summary: La estructura y las cuentas de F2 a F4 verifican contra el conteo de Waite (`P_pos` ≈ 0,274, `P_cero` ≈ 0,38). El catálogo no se podía cargar de forma consistente: E2 contradecía a R6 y a la Taxonomía (`KW_SIN_TEMA`), y la cifra "14 de 72" no coincidía con el conteo (11 a 18 según el mazo). El riesgo de fondo, `P_cero` ≈ 0,38 contra el Pilar 6, es un costo aceptado en D-48 y no se relitigó, pero no tenía umbral falsable. Pasada lean: no sustituye una full.
Prior verdict resolved: First review
Findings:
- [BLOCKING] E2/R6: "elegir el tema más cercano" contradecía "nunca forzar" y el esquema no admitía orientación sin tema — corregido (campo `forzada`, orden de 4 pasos en E2, F2 solo sobre claras).
- [BLOCKING] E2/Open Questions: "14 de 72" falso; el conteo da 11 a 18, y 17 en Mayores + Copas — corregido.
- [BLOCKING] R3: `atribucion` sin definir para las 56 menores — corregido (decanato del *Book T* en 2 a 10, vacía en As y figuras; AC-04d).
- [BLOCKING] R4: ids `<1–3>` contra una perilla de máximo 4 — corregido (`<n>`, límites de la perilla, `orientaciones_con_una`, AC-05b/c).
- [RECOMMENDED] F3/F4: *invertir* citado como palanca sin número y sin umbral para el Pilar 6 — corregido (`P_pos_inv` ≈ 0,355 como cota, `P_cero_max` provisorio 0,30, AC-18e/f).
- [RECOMMENDED] F1: contrato de sorteo con un Generador sin diseñar — corregido (marcado como interfaz provisoria).
- [RECOMMENDED] R8: el 10 % repetido a mano — corregido (`Q_min`).
- [RECOMMENDED] AC-10: etiquetas de reglas equivocadas — corregido (R4; R6 lo cubre AC-11).
- [RECOMMENDED] AC-11: verificaba solo 78 de unas 400 palabras clave — corregido (MVP completo, todas las forzadas y muestra del 25 %).
- [RECOMMENDED] AC-09a ilegible, AC-15b sin receta, faltaban AC de `P_exacto` y de R7 con tema deprecado — corregido (AC-09a/c, AC-15b/d, AC-18b).
- [RECOMMENDED] Índice: línea de orden de diseño del Generador sin Cartas — corregido.
- [ADVISORY] Player Fantasy ausente — sin cambio.
- [NICE] Registro: Cartas no figura en `referenced_by` de los 23 temas — sin cambio.
Abierto tras las correcciones: el Dos de Copas invertida no tiene significado en Waite y E2 paso 4 no le da salida; `P_cero_max` es una propuesta a confirmar; falta rehacer la tabla por carta con los 23 temas.
Receipt: sin sello a propósito. El GDD se corrigió después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.

## Review — 2026-10-24 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, qa-lead, creative-director (senior)
Blocking items: 8 | Recommended: 7
Summary: La arquitectura de D-48 es correcta, pero fallaban piezas puntuales. F3 usaba un `p_f` que no era el de F1 y un `u_f` anterior a D-48, incompatible con los `q_f` actuales; la cota con *invertir* estaba al revés. Las forzadas generaban verdades. La alarma de 0,30 no distinguía ningún mazo, y `P_cero` empeora al sumar palos. La mitad de los AC no se podía aislar con la firma del validador. Dos de esos errores (`P_pos_inv` y la dirección de la cota) los había introducido la corrección de la pasada lean.
Prior verdict resolved: Partially — los 4 bloqueantes de la pasada lean se corrigieron, pero dos de las correcciones eran erróneas.
Findings:
- [BLOCKING] Formulas F3: `p_f` como parte de `c_f` en vez de Σ p_t de F1; `u_f` viejo incompatible; "a lo sumo 0,27" al revés — corregido.
- [BLOCKING] R6/F1: semántica de `forzada` — corregido (P1: `w_forz` 0,5, sorteable solo con 1 clara, R7 y `u_f` solo claras).
- [BLOCKING] F4: `P_cero_max` sin capacidad de discriminar y progresión invertida — corregido (P2/P4: `P_fallo_f` por familia, marca de progresión).
- [BLOCKING] F1: memorizar frecuencias como estrategia degenerada — corregido (F5 `V_prior`).
- [BLOCKING] AC/R13: firma del validador sin config ni informe — corregido (R12; R13 de la Taxonomía ajustada).
- [BLOCKING] AC-11: R6 sin gate bloqueante — corregido (Integration, regla de aprobación, revisor independiente, traducción).
- [BLOCKING] AC-04c/d, AC-18a, F2: oráculos y borde en coma flotante — corregido.
- [BLOCKING] AC-15b: cláusula de escape — corregido (4 recetas).
- [RECOMMENDED] E7: palanca de la carta muda — corregido (P3: relectura pagando UT en Tiradas/Resonancia; `acierto_posible`).
- [RECOMMENDED] E2: invertida sin fuente — corregido (P5: derecha debilitada, sujeta a citar la práctica).
- [RECOMMENDED] R5/R11: orientaciones sin elección, temas frágiles — corregido.
- [RECOMMENDED] Tuning Knobs: `Q_min` sin margen en 0,12 — corregido (hasta 0,11).
- [RECOMMENDED] Restos de "2 o 3" y UX Flag — corregido.
- [RECOMMENDED] Higiene de AC (controles vacuos, F2 por familia, ids, AC-20, AC-21, AC-18d) — corregido.
- [RECOMMENDED] Registro: `w_forz` y excepción de 1 — derivado a /consistency-check.
- [ADVISORY] Player Fantasy ausente — sin cambio.
Disputas: G3 (palanca del Pilar 6 como bloqueante de Cartas) — creative-director la asignó a Tiradas/Resonancia; Cartas solo expone `acierto_posible`.
Receipt: sin sello a propósito. El GDD se corrigió después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.

## Review — 2026-10-24 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, qa-lead, creative-director (senior)
Blocking items: 6 | Recommended: 25
Summary: Re-revisión full. Dato nuevo, verificado contra Project Gutenberg #43548: el conteo de D-48 omitió Waite III §4, que da significados adicionales a las 56 menores; el Dos de Copas invertida tiene "Passion", así que el caso `debilitada` era falso y las cifras de D-48 son pesimistas. El esqueleto (sorteo proporcional, R6, piso F2) se mantiene; fallaban la política de fuente, una definición de acierto que mezclaba claras y forzadas, el peso sin tope de las forzadas y una palanca del Pilar 6 que podía filtrar la verdad.
Prior verdict resolved: Yes — los 8 bloqueantes de la revisión full anterior siguen corregidos; esta revisión encontró problemas nuevos.
Findings:
- [BLOCKING] R4/E2/Formulas: Waite III §4 no contado — corregido (D-50: cuenta con prioridad de §2/§3; cifras rotuladas previas a §4; reconteo como bloqueante de datos).
- [BLOCKING] R4/E2: `debilitada` es un significado inventado y sin caso real — corregido (eliminada; orientación sin fuente = error de R4; AC-24 reescrito).
- [BLOCKING] Formulas F3/F4: acierto sobre claras contra `p_f` con forzadas — corregido (`P_pos⁺`, `P_fallo_f`, `P_cero` sobre `c_f⁺`; marca de progresión por par con `ε_prog`).
- [BLOCKING] Formulas F1: una clara habilitaba todo el peso forzado — corregido (tope `k_forz`, AC-18k).
- [BLOCKING] R12/E7: `acierto_posible` podía filtrar la verdad en juego — corregido (solo diseño y calibración; relectura ciega; dependencia Dura; pendiente en systems-index).
- [BLOCKING] AC: sin AC de comparación contra el oráculo y sin config fija del fixture — corregido (AC-04f, `config_prueba`, `atribuciones_gd_prueba`, reparto del fixture).
- [RECOMMENDED] F4: "sin reponer < 0,01" falso (0,013) — corregido.
- [RECOMMENDED] F4: independencia optimista y Destino oculto en el promedio — corregido (`P_cero_corr`, `P_cero_f`; Destino 0,58–0,67).
- [RECOMMENDED] F5: `V_prior` no comparable entre mazos — corregido (`max p_t`, `T_ef`).
- [RECOMMENDED] F2: doble fuente `Q_min`/`q_mil` — corregido (solo `q_mil` entero).
- [RECOMMENDED] E5/E9/R11: `P_fallo_f` con `p_f` = 0, temas trampa — corregido.
- [RECOMMENDED] Generador: contrato sin regla para temas con `p_t` = 0 — corregido.
- [RECOMMENDED] AC-03, 04e, 05e, 06/12, 09d, 10, 11, 11b, 13, 15a/c/e, 17, 18a–l, 20, 21, 22, 23 — aislamiento, sujetos, tolerancias, procedimiento de AC-11 para una persona — corregido.
- [ADVISORY] Player Fantasy ausente — sin cambio.
Disputas: (i) fijar ya `P_fallo_max` o un umbral de `P_cero` — el creative-director lo rechazó (el reconteo mueve las cifras; D-49 lo deja al prototipo). (ii) AC de gate del Pilar 6 en Cartas — rechazado; la dependencia pasa a Dura y el requisito va a Tiradas/Resonancia. (iii) §4 no invalida la decisión D-48, solo sus números. (iv) `debilitada` eliminada, sin oposición.
Receipt: sin sello a propósito. El GDD se corrigió después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.

## Review — 2026-10-25 — Verdict: NEEDS REVISION
Review mode: lean · Workflow: standard
Scope signal: L
Specialists: ninguno (lean)
Blocking items: 1 | Recommended: 5
Summary: Cuarta pasada. Las cuentas verifican: se recalcularon a mano AC-15a/b/c/e, AC-17 y AC-18a1 a AC-18k sin diferencias. El hueco es de alcance: F4 fija el exponente 3 (Tres Tiempos), pero el MVP incluye Carta Única (GDD maestro §5.4 y MVP), con `P_cero` ≈ 0,72 de una posición. D-48 aceptó el costo del Pilar 6 midiendo solo una de las dos tiradas del MVP. Pasada lean: no sustituye una full.
Prior verdict resolved: Yes — los 6 bloqueantes de la re-revisión full siguen corregidos; esta pasada encontró un problema nuevo.
Findings:
- [BLOCKING] Formulas F4/E7/Open Questions: `P_cero` solo para 3 posiciones; Carta Única (MVP, 1 posición) sin cifra ni palanca definida.
- [RECOMMENDED] F4: `P_cero` mide acierto posible, no alcanzado; "jugada útil" del Pilar 6 sin definir.
- [RECOMMENDED] R12: `acierto_posible` sin AC que impida su uso en el código de juego (Pilar 1).
- [RECOMMENDED] AC-11/Open Questions: "build del MVP" y "36 cartas del MVP" no fijan el conjunto; el MVP llega a 50 cartas en la Sede 3.
- [RECOMMENDED] Registro: `piso_familia_q_min` decimal contra `q_mil`; faltan `w_forz`, `k_forz` y `ε_prog`, y la excepción de 1.
- [RECOMMENDED] Formulas/Tuning Knobs: cifras de F3 a F5 y rango seguro de `q_mil` sin verificar hasta el reconteo.
- [ADVISORY] Player Fantasy ausente — sin cambio.
- [NICE] Tuning Knobs: "en 120 pasa sin ningún margen" es inexacto; Cartas sigue fuera de `referenced_by` de los 23 temas.
Receipt: sellado antes de las correcciones; describe la versión revisada, así que la versión corregida da CHANGED y pide re-revisión.
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md 90adb72567d630b9de82c57e938375dd179c5c61
Reviewed-Content-Hash: design/registry/entities.yaml 878b0e1995978e64f764eadcdb004407ad36e93b
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 3a31f95439cf6c6362d10b730c01a02d49d04f3b
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/ARCANUM_VULGARIS_GDD.md c5059d53f17055a59c460c9d4f734b3264c606f4
Reviewed-Content-Hash: design/gdd/systems-index.md 2770c597920c756e8d1b26331f8dd67e68428ba0

## Review — 2026-10-25 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, qa-lead, creative-director (senior)
Blocking items: 4 | Recommended: 8
Summary: Quinta pasada. Dentro del dominio las cuentas verifican, pero la configuración aceptaba valores que rompen F1 (`w_forz` < 0 da `p_t` < 0), las salidas con `T_m` = 0 u `O` = 0 eran números falsos, F4 afirmaba dos cotas falsas ("basta un k" para `P_cero_corr`, "el real queda entre los dos") y R11 y E9 definían distinto el tema trampa. El creative-director dejó Carta Única, AC-11, `V_prior`/`V_menú` y el scope del prototipo como no bloqueantes; queda escrita la cota `P_cero(1)` ≥ ~0,45 aun con III §4.
Prior verdict resolved: Yes — el bloqueante de la lean (F4 solo Tres Tiempos) sigue corregido; esta pasada encontró problemas nuevos.
Findings:
- [BLOCKING] Tuning Knobs/F1: sin dominio para `w_forz`, `k_forz`, `k_tiradas`, `ε_prog`, umbrales y mínimo/máximo de palabras clave — corregido (error de configuración, el validador no sigue; AC-27).
- [BLOCKING] Formulas/AC-22: salidas con `T_m` = 0 u `O` = 0 sin guarda — corregido ("Salidas vacías"; AC-22 ampliado).
- [BLOCKING] F4: "basta un k" y "el real queda entre los dos" falsos — corregido (progresión sobre `P_pos⁺` con tolerancia 1e-9; contraejemplo A/B; `P_cero_corr` es máximo con marginales iguales; AC-18f reescrito).
- [BLOCKING] R11/E9: dos definiciones de tema trampa — corregido (solo forzadas; "deprecados presentes" aparte; AC-18l).
- [RECOMMENDED] F4/Open Questions: el reconteo no resuelve Carta Única — corregido (cota ≥ ~0,45; k = 1 criterio de salida del prototipo; tasa de relectura).
- [RECOMMENDED] AC-11: sin pass/fail de artefactos — corregido (AC-11c; (a) provisorio; `orientaciones_con_una` refutable es falla).
- [RECOMMENDED] F4/Tuning Knobs: marca del mazo de 4 palos dentro del ruido — corregido (no concluyente hasta el reconteo).
- [RECOMMENDED] Scope: oráculo, AC-04c, 04f, 20 y 26 fuera del prototipo — corregido; `V_menú` a Open Questions de Resonancia.
- [RECOMMENDED] Informe: distribución de familias generada y tope de forzadas por mazo — sin cambio.
- [RECOMMENDED] AC: evidencia de AC-04c/19/20/26, AC de `chequear_informe` y de pureza, mutaciones múltiples sin declarar (09a, 05b, 05c, 15d, 18j), l.315 contra l.320 — sin cambio.
- [RECOMMENDED] Player Fantasy corta atada a "no hay carta mala" — sin cambio.
- [NICE] UI l.294 "3 a 6" — corregido (4 a 6). Pendientes: progresión solo contra el Aprendiz, igualdades/`T_m` = 1 en AC-18h, E6, casos de R3, tolerancias de AC-18b, numeración AC-11/11b.
Disputas: (i) Carta Única bloqueante (game-designer) — no, va a Tiradas/Resonancia con la cota escrita. (ii) AC-11 bloqueante (qa-lead) — recomendado, se aplicó la parte de artefactos. (iii) Normalizar `V_prior` (systems-designer) — no; se mantiene la tasa absoluta (cuarta revisión). (iv) Catálogo de prototipo separado (game-designer) — no; se etiquetan los AC no requeridos. (v) Re-revisión lean solo del delta (creative-director) — rechazada: la skill exige revisión completa, y esta pasada halló afirmaciones falsas en F4 tras cuatro revisiones.
Receipt: sellado antes de las correcciones (y antes de pasar systems-index a In Review); describe la versión revisada, así que la versión corregida da CHANGED y pide re-revisión.
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md 4a65f3b5c2a9bd44eca4eb0e73cb6b2061c46bd2
Reviewed-Content-Hash: design/registry/entities.yaml 878b0e1995978e64f764eadcdb004407ad36e93b
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 3a31f95439cf6c6362d10b730c01a02d49d04f3b
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/ARCANUM_VULGARIS_GDD.md c5059d53f17055a59c460c9d4f734b3264c606f4
Reviewed-Content-Hash: design/gdd/systems-index.md e921556719bf9fd342c6f05c566f0df1d1fcd3d3
Reviewed-Content-Hash: design/balance/cobertura-cartas-waite.md 455ea670272e48b1985e9d57cb2f410dfe6a253c
Reviewed-Content-Hash: design/decision-log.md a361d1b6720a59ae08e3dce9b3098a01f7492997

## Review — 2026-10-25 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, qa-lead, creative-director (senior)
Blocking items: 8 | Recommended: 8
Summary: Sexta pasada. La aritmética de los AC cierra (verificada por tres lados), pero `k_tiradas` tenía tres definiciones y armaba un ciclo de código con Tiradas, Tiradas pedía `P_cero_v` sin contraparte, F4 rotulaba al revés el error de la reposición y no valía para `k` grandes, y el fixture no podía construir los AC de Ambición, *culpa* y valencia. El creative-director recomendó congelar el alcance hasta el prototipo (D-53); el diseñador aplicó además todos los recomendados.
Prior verdict resolved: Yes — los 4 bloqueantes de la quinta pasada siguen corregidos; esta pasada encontró problemas nuevos.
Findings:
- [BLOCKING] Dependencies: la línea de `k_tiradas` cortaba la tabla y dejaba huérfanas 3 filas — corregido.
- [BLOCKING] R12/Tuning Knobs: `k_tiradas` sin dueño y ciclo con Tiradas — corregido (argumento del informe; `pesos_sorteo` como única función de juego; AC-27b).
- [BLOCKING] F4: "con reposición" sobreestima `P_cero` (pesimista, no optimista) y falla con `k` = 10 — corregido (válido para `k` ≤ 3; Open Question para `k` > 3).
- [BLOCKING] F3/F4: contrato de valencia — corregido (`P_cero_v(k)`, `V_prior_v`, `MAZO_SIN_VALENCIA`, marca de valencia deducible; AC-18m, AC-18n).
- [BLOCKING] AC: `taxonomia_prueba` sin Ambición, *culpa* ni valencias; `orientaciones_con_una` inicial sin definir — corregido (fixture completo).
- [BLOCKING] AC-11/11c: no reproducible tras corregir, THEN contradictorio, muestra (c) vacía, semilla sin algoritmo — corregido (SHA del commit de datos, hash de entrada, algoritmo SHA-256, "última pasada").
- [BLOCKING] AC: excepción de prototipo incoherente con AC-01/04b/04d/04e — corregido.
- [BLOCKING] AC: convención de un solo punto falsa (18j, 09a, 15d, 05b, 05c, 03, 05e) — corregido (excepciones declaradas, secundarios nombrados, 18j partido).
- [RECOMMENDED] F4: cota de Carta Única sin R4 (≥ 0,45 → ≥ 0,58; con aclaratoria ≥ 0,20 → ≥ 0,34) — corregido.
- [RECOMMENDED] F4/E7: supuesto de 1 aclaratoria contra el rango 1–2 de Tiradas — corregido (`a` declarado).
- [RECOMMENDED] Formulas: guardas explícitas y tolerancias de las marcas — corregido ("Comparaciones").
- [RECOMMENDED] R12: progresión sin función, `T_m` = 0 en runtime, `validar_mazo` con mazo chico, AC-09d subespecificado — corregido.
- [RECOMMENDED] AC: trazabilidad (pureza, invariantes, F4 con 3–4 palos, `P_cero_f(3)`, `T_m` = 1, R9) — corregido (AC-28, 18e, 18f2, 18c, 18h, 04g).
- [RECOMMENDED] AC: controles sin sujeto, dominios, AC-22/18f/18a3 partidos, AC-26 por módulos, AC-20, desvío Config/Data, doble transcripción, AC-21 — corregido.
- [RECOMMENDED] Plan de prototipo: separación de habilidad y umbral de impuesto — anotado en Open Questions y D-53.
- [RECOMMENDED] Etiqueta "producción" en la excepción de prototipo — corregido.
- [NICE] `q_mil` > 600 solo con máximo 3; `q_mil` = 0 apagaba R8; rango de `N` — corregido (`q_mil` de 1 a 1000).
Disputas: (i) B1–B3 del game-designer (criterio PROCEED/KILL, reconteo, aclaratoria como impuesto) como bloqueantes de Cartas — no: van al plan de prototipo, a Tiradas y Resonancia, y D-50. (ii) `V_menú` y prior por familia en Cartas — no, Resonancia (disputa ya resuelta). (iii) Recortar (game-designer) contra agregar AC (qa-lead) — por etapa: etiqueta "producción". (iv) Re-revisión acotada a los bloqueantes y F4 (creative-director) — rechazada por la revisión principal: la skill exige revisión completa, y esta pasada volvió a hallar un error en F4 fuera de lo marcado. Lo decide el diseñador.
Receipt: sellado antes de las correcciones; describe la versión revisada, así que la versión corregida da CHANGED y pide re-revisión.
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md 3d75325511e3541cf43f314603bed2b0005347f0
Reviewed-Content-Hash: design/registry/entities.yaml 57baf5849122b8e7da5e197f10ee09b9b1f7b428
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 194338d159df1c729fbd990fbcb4a6f285e5485d
Reviewed-Content-Hash: design/gdd/tiradas.md 6605e6c6e191ffa3a37c7e3c3ed4c838b64908b1
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/gdd/systems-index.md 0c7c2d0fd4b9e7c7fb13beaf897b734e4c6f0cf9
Reviewed-Content-Hash: design/decision-log.md d6c9213ca008d2c2bc263a632d48327fc3a06c8e
Reviewed-Content-Hash: design/balance/cobertura-cartas-waite.md 455ea670272e48b1985e9d57cb2f410dfe6a253c

## Review — 2026-10-25 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, qa-lead, creative-director (senior)
Blocking items: 4 | Recommended: 24
Summary: Séptima pasada. La aritmética de los AC cierra (script) y F1, F2, la convexidad de F4 y E1–E9 se sostienen. Los cuatro bloqueantes son locales: R12 decía que `pesos_sorteo` era la única función de juego mientras R10 valida al arrancar; AC-27b `[1,5]` ambiguo por la coma decimal; AC-11 sin clave de unión entre la asignación ciega y el catálogo; y las cifras de Carta Única calculadas sin valencia para la posición del desenlace, con una cota que ignoraba *Book T* y Mathers y no valía para 78 cartas. El creative-director atribuye el ciclo de revisiones al tamaño del documento (análisis probabilístico de sistemas que no existen) y pide diff mínimo y cifras derivadas fuera de la prosa.
Prior verdict resolved: Yes — los 8 bloqueantes de la sexta pasada siguen corregidos; esta pasada encontró problemas nuevos.
Findings:
- [BLOCKING] R10/R12/AC-26: `pesos_sorteo` "única" función de juego contra validación al arrancar — decisión del diseñador: la validación corre en el juego.
- [BLOCKING] AC-27b: caso `[1,5]` legible como lista válida.
- [BLOCKING] AC-11: pasos 1–2 sin clave de unión (`ubicacion` no identifica la palabra clave); "la traducción cambia el tema" no juzgable a ciegas — decisión: entrada por `kw_id` sin `texto_es`, traducción en un paso aparte.
- [BLOCKING] F4/E7: titulares de Carta Única sin valencia; cota de l.222 solo Waite y solo Mayores + Copas (con 78 cartas `P_cero(1)` ≳ 0,44).
- [RECOMMENDED] F4: brecha sin reposición es cota (≤ 0,013; con u = 2q, 0,004); dirección solo con roles iid.
- [RECOMMENDED] F4: aclaratoria con la misma verdad es `P_cero_corr(1+a)` (diferencia ~0,002).
- [RECOMMENDED] R12: determinismo (float64, multiplicación en vez de pow, `w_mil` entero) y firma de `pesos_sorteo`.
- [RECOMMENDED] F3/F5: valencia casi deducible con `T_m^v` > 1; `P_exacto_catálogo` (política de mayor `p_t` por carta); garantía inversa del Generador; `k` efectivo; UT por acierto rescatado (~18 UT).
- [RECOMMENDED] AC: AC-28 casi no falla; AC-22b vacuo con umbrales sin fijar; sujetos de mazo de prueba y de valencia sin formato R13; AC-05c/18j3/24 sin el id quitado; perilla mínimo y R2 sin AC; semilla de AC-11 elegible a posteriori; AC-18f2 sin valores para 4 palos; AC-18e sin control de u ≤ 2q; MAZO_SIN_* solo en fixture limpio; AC-08 y AC-09c fuera de las excepciones; etiquetas de prototipo; AC-21 prueba su stub.
- [NICE] Guardas k > N y Aprendiz vacío; `n_t^a` choca con `a`; signo neto del sesgo de F4; mazo rebarajado por cliente; contrato de desconfianza con Resonancia; ancestro del oráculo; fixture de AC-23; O y N en AC-18a1; controles "sin fijar" en AC-27.
Disputas: (i) validación en CI (creative-director) contra en el juego — el diseñador eligió en el juego, coherente con AC-25a/b de la Taxonomía. (ii) Ceguera de AC-11 — ceguera estricta, traducción en paso aparte. (iii) Criterio de impuesto en UT por acierto rescatado — va a Tiradas/D-53, no a Cartas. (iv) "Aprendiz = 1 palo" — lo decide Mazo y Robo. (v) Octava pasada lean y por delta (creative-director) — rechazada por la revisión principal: la skill exige revisión completa; las pasadas quinta y sexta hallaron errores fuera de lo marcado. Se acepta el fondo: menos prosa con números.
Receipt: sellado antes de las correcciones; describe la versión revisada, así que la versión corregida da CHANGED y pide re-revisión.
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md 5b551f54c8d41d594dfd79800acc885f8a158398
Reviewed-Content-Hash: design/registry/entities.yaml 57baf5849122b8e7da5e197f10ee09b9b1f7b428
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 194338d159df1c729fbd990fbcb4a6f285e5485d
Reviewed-Content-Hash: design/gdd/tiradas.md c21828d3c57bf88b848a97c599137ecbe94e8b8d
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/gdd/systems-index.md cf596b0543f1329bf372cd349f6db0757de43178
Reviewed-Content-Hash: design/decision-log.md 6803f41e81aa8629f50b8506a23b09abeb01b818
Reviewed-Content-Hash: design/balance/cobertura-cartas-waite.md 455ea670272e48b1985e9d57cb2f410dfe6a253c
