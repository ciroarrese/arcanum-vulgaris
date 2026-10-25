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
