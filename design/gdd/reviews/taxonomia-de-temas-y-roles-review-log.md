# Review Log — Taxonomía de Temas y Roles

## Review — 2026-10-22 — Verdict: NEEDS REVISION
Review mode: lean · Workflow: standard
Scope signal: M
Specialists: ninguno (lean)
Blocking items: 1 | Recommended: 9
Summary: El diseño es coherente con los pilares y con el GDD maestro, y la comparación exacto / parcial / ninguno es implementable. Lo frenaba una regla de datos ambigua (la familia de los temas de mapa podía contradecir a su equivalente) y varias referencias cruzadas sin cerrar. Las revisiones se aplicaron en la misma sesión (D-42); falta una re-revisión que decida si se aprueba.
Prior verdict resolved: First review
Findings:
- [BLOCKING] Core Rules R4 / Edge Cases E7: la familia declarada por un tema de mapa podía contradecir a su equivalente — corregido: la familia se deriva del equivalente.
- [RECOMMENDED] Core Rules R9: "rol activo" sin definir — corregido.
- [RECOMMENDED] Cross-References: GDD maestro §5.3, §5.8, D-15 y §3.5 desfasados — anotado en Open Questions.
- [RECOMMENDED] Dependencies: faltaban Interpretación y Sentencia, Tapete y Tooltips, Inspección y Tells — corregido.
- [RECOMMENDED] Acceptance Criteria: AC con "el juego no arranca" — pasados al validador del catálogo y sumado AC-25.
- [RECOMMENDED] Open Questions: Carta Única cubre 1 de 3 roles, y falta definir la verdad de "sí o no" — anotado.
- [RECOMMENDED] Registry: los 19 temas no estaban registrados — registrados en entities.yaml.
- [RECOMMENDED] Core Rules R9: no se decía qué combinaciones de temas por rol son válidas — corregido (las define el Generador).
- [RECOMMENDED] Core Rules R1 / E8: `secreto` mal ubicado en Destino — movido a Conflicto.
- [RECOMMENDED] Header: faltan las consultas a systems-designer, game-designer y narrative-director — sigue abierto.
Receipt: sin sello a propósito. El documento se revisó después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.

## Review — 2026-10-22 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: M
Specialists: game-designer, systems-designer, qa-lead, narrative-director, creative-director
Blocking items: 5 | Recommended: 8
Summary: La arquitectura (tema y rol separados, tiradas traducidas a roles, validador de datos) es correcta para una capa Foundation, así que el veredicto no es MAJOR. Fallaban cinco cosas locales que había que cerrar antes de cargar datos, porque R3 hace permanentes los ids y el esquema: Destino con 2 temas, un contrato de comparación ambiguo, un ciclo de vida que se contradecía, la colisión de namespaces y AC sin contrato de validador. Las revisiones se aplicaron el 2026-10-23 (D-43); falta una re-revisión que decida si se aprueba.
Prior verdict resolved: Yes — el bloqueante de la revisión lean (familia de los temas de mapa) estaba corregido.
Findings:
- [BLOCKING] Core Rules R1 / E8: Destino con 2 temas (parcial casi imposible; puntaje al azar 0,16 contra 0,32 en Conflicto) y umbral de "30 % de testers" sin base — corregido: enfermedad a Destino, trabajo a Bienes, mínimo 2 temas activos por familia, línea base calculada.
- [BLOCKING] Core Rules R5 / E3 / E4 / E7: "mismo tema" contradecía a E7, faltaban firma, orden de evaluación y SIN_COMPARACION — corregido (R6, R11).
- [BLOCKING] States / R4: deprecar un equivalente de mapa dejaba el juego sin arrancar; no se decía si las cartas podían ofrecer temas deprecados — corregido (DEPRECAR_CON_DEPENDIENTES, sin reactivación, válidos en cartas).
- [BLOCKING] Core Rules R3: colisión familia Conflicto / rol conflicto y esquema sin fijar con ids permanentes — corregido: prefijo por tipo.
- [BLOCKING] Acceptance Criteria: validador sin contrato, AC-05 y AC-25 mal formulados, AC-16..18 con semilla fija, R7 sin cubrir — corregido (R13, AC reescritos, AC-16..18 al Generador, AC-26..32 nuevos).
- [RECOMMENDED] Open Questions: Doble Fondo, coherencia entre roles, agregación y umbral de Resonancia, invariantes de Tiradas, palanca de Cartas, tells y catalog_version — anotados con dueño.
- [RECOMMENDED] Tuning Knobs: faltaba la sección — agregada.
- [RECOMMENDED] Vocabulario: glosario por tema, nota de Regla Cero, nombre visible de Destino y de locura, renombrar riesgo — anotado.
- [RECOMMENDED] E7: hiperinflación es del Mapa A y el MVP no tiene temas de mapa; ¿equivalente deuda o fortuna? — anotado.
- [RECOMMENDED] UI: la marca de familia confunde en cartas de otro palo; AC del tooltip — derivado a /ux-design.
- [RECOMMENDED] Header: nota "no consultados — modo Lean" desactualizada — corregido.
- [RECOMMENDED] Disputa sobre sacar secreto del catálogo: no se reabre D-42 sin un dato nuevo; queda como palanca si el prototipo muestra que Conflicto domina.
- [RECOMMENDED] AC-09 a provisorio, con un parcial por familia — corregido.
Receipt: sin sello a propósito. El documento se revisó después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.

## Review — 2026-10-23 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: M
Specialists: game-designer, systems-designer, qa-lead, narrative-director, creative-director
Blocking items: 6 | Recommended: 6
Summary: La taxonomía como diseño está sana: familias, temas, la frontera de D-42 y los prefijos de D-43 se sostienen. Fallaban el contrato del validador, la máquina de estados de deprecación, la gramática de ids, una meta que se contradecía con su propia línea base y los AC que heredaban esos defectos. Las revisiones se aplicaron el mismo día (D-44); falta una re-revisión completa que decida si se aprueba.
Prior verdict resolved: Yes — los 5 bloqueantes de la revisión full del 2026-10-22 estaban corregidos.
Findings:
- [BLOCKING] Core Rules R13: `validar_catalogo` no recibía tiradas y `ROL_INEXISTENTE` lo dispara una tirada; faltaba código de forma inexistente — corregido (tiradas en la firma, `FORMA_INEXISTENTE`, formato de sujeto).
- [BLOCKING] States / R5: deprecar mapa → base quedaba trabado por `MAPA_EQUIV_DEPRECADO` — corregido (solo cuentan temas de mapa activos; exactamente un error según el catálogo anterior).
- [BLOCKING] Core Rules R4: gramática de ids sin formato, sujeto de `ID_VACIO` indefinido, archivo de mapa ajeno — corregido (formato por tipo, `<archivo>#<índice>`, `MAPA_ID_AJENO`).
- [BLOCKING] Open Questions / E8: la meta de ±15 % la violaba la línea base uniforme (Conflicto +17,6 %, Destino −21,6 %) — corregido (desvío respecto de la línea base de cada familia; 2/1/0 ilustrativo).
- [BLOCKING] Acceptance Criteria: AC-09 incorrecto, AC-12/13 probaban a la Gramática, AC-27/30/20b..f mezclaban casos, R3 sin borde ni control positivo, E8 sin AC — corregido (AC de un caso, AC-09 exhaustivo, AC-01c, AC-28a..d, provisorios no bloqueantes).
- [BLOCKING] Core Rules R1: la Regla Cero estaba solo como pregunta de vocabulario — corregido (un tema describe la situación del cliente, nunca una fuerza).
- [RECOMMENDED] Core Rules R10 / States: "activo" significaba dos cosas — corregido ("habilitado" para roles y formas).
- [RECOMMENDED] Core Rules: esquema de campos, libre como rol vacío, `KW_TEMAS_MULTIPLES`, `FAMILIA_EXTRA`, catálogo anterior vacío, rol deshabilitado en partida guardada (E9) — corregido.
- [RECOMMENDED] Open Questions: afinidad tema-rol obligatoria antes del prototipo, con campo reservado — anotado (Generador).
- [RECOMMENDED] Open Questions: invariante "toda tirada puede llegar a PARCIAL" — anotado (Cartas).
- [RECOMMENDED] Open Questions: vocabulario (*locura* por sensibilidad, colisión visible Conflicto familia/rol, *fortuna*, *hogar*) y temas de mapa del Mapa B — anotado.
- [RECOMMENDED] UI: AC del tooltip y de la marca con captura retenida — derivado a /ux-design.
Disputas no resueltas a favor de un especialista: afinidad tema-rol como bloqueante (game-designer) y cobertura del Mapa B como bloqueante (narrative-director) — creative-director las derivó; *secreto* como tautología — no se reabre D-42, queda en el Generador.
Receipt: sin sello a propósito. El documento se revisó después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.

## Review — 2026-10-23 — Verdict: APPROVED
Review mode: lean · Workflow: standard
Scope signal: M
Specialists: ninguno (lean)
Blocking items: 0 | Recommended: 8
Summary: Sin contradicciones entre reglas, fórmulas, registro y AC; las cifras de Formulas y los 20 temas del registro coinciden. Quedaban huecos de borde del validador (precedencia de errores en archivos de mapa, sujeto de errores de todo el catálogo, rol olvidado tomado por libre). Es una pasada lean: no sustituye una full, y la pasada lean anterior (D-45) no había quedado en este log.
Prior verdict resolved: Yes — los 6 bloqueantes de la revisión full del 2026-10-23 y los de la pasada lean (D-45) estaban corregidos.
Findings:
- [RECOMMENDED] R4/R5: un id ajeno en un archivo de mapa daba dos errores posibles — corregido (precedencia a/b/c, AC-21a..d, D-46).
- [RECOMMENDED] R13: `SIN_ROLES_HABILITADOS` y `SIN_FORMAS_HABILITADAS` sin sujeto — corregido (`catalogo`).
- [RECOMMENDED] R9: un rol olvidado se tomaba por libre en silencio — corregido (`libre`, `POSICION_AMBIGUA`, `TIRADA_SIN_COMPARABLES`, AC-37a/b y AC-38; provisorios hasta Tiradas).
- [RECOMMENDED] Esquema: faltaba el palo de cada familia para la Gramática — corregido (`palo`).
- [RECOMMENDED] Tuning Knobs: la asignación a familia no aclaraba que D-45 la bloquea tras la primera build — corregido.
- [RECOMMENDED] Open Questions: guardar la versión del catálogo quedó parcialmente superada por D-45 — corregido.
- [RECOMMENDED] Log: faltaba la entrada de la pasada lean de D-45 — anotado acá; no se reconstruyó con detalles inventados.
- [RECOMMENDED] E6: una carta con palabra clave de un tema deprecado queda con techo PARCIAL en situaciones nuevas — sin cambio; decidir si algún día se depreca un tema.
- [NICE] Alcance: los temas de mapa pesan 7 de ~45 códigos y ~20 de ~85 AC y el Mapa B no declara ninguno — decisión del diseñador.
Receipt: sin sello a propósito. El GDD se editó después de este review (D-46), y un sello de la versión corregida haría pasar el documento nuevo por el que se revisó.

## Nota — 2026-10-23 — Cambio fuera de revisión (D-47)
No es una revisión. Al diseñar la Base de Datos de Cartas se amplió R13: el sujeto de una palabra clave pasa a ser su id de Cartas (`<carta>/<orientación>/<n>`) y se agregan los sujetos de orientación y de mazo; AC-03a–c y AC-23 cambian de fixture (`carta.copas_05`). El estado vuelve a In Review por decisión del diseñador: el APPROVED del 2026-10-23 no cubre este cambio.

## Nota — 2026-10-24 — Cambio fuera de revisión (D-48)
No es una revisión. Al contar las 78 cartas contra Waite (1910) para el GDD de Cartas se agregaron 3 temas de resultado: *alegría* (Emoción), *éxito* (Ambición) y *cambio* (Destino). Quedan 23 temas, reparto 5/4/5/5/4; se recalcularon la línea base de Formulas, AC-01b, AC-09 y las perillas. *Culpa* abarca vergüenza y confesión. Sigue en In Review.

## Nota — 2026-10-24 — Cambio fuera de revisión (D-49)
No es una revisión. La revisión full de Cartas amplió R13: `validar_catalogo` recibe además `config`, `orientaciones_con_una` y `atribuciones_gd` (R12 de Cartas), y se agrega el formato de sujeto de un mazo sin familia (`MAZO_SIN_VERDADES`). Sigue en In Review.

## Nota — 2026-10-25 — Cambio fuera de revisión (D-51)
No es una revisión. El GDD de Tiradas agregó la valencia de cada tema (favorable / desfavorable / ambigua) para la pregunta de sí o no: tabla en R1, campo en el esquema, `CAMPO_INVALIDO` y AC-35d/e. Se sacaron las marcas "provisorio hasta el GDD de Tiradas" de `FORMA_INEXISTENTE`, `POSICION_AMBIGUA` y `TIRADA_SIN_COMPARABLES`. Sigue en In Review.
