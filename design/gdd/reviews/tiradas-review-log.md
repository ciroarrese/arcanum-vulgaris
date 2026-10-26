# Review Log — Tiradas

## Review — 2026-10-25 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, economy-designer, qa-lead, ux-designer, creative-director (senior)
Blocking items: 9 | Recommended: 7
Summary: Primera revisión (el GDD se redactó en lean). Dos Caminos no tenía posición de desenlace contra R11 y el validador; el cobro de UT no tenía momento; los rangos seguros permitían costos que el validador rechaza; las cifras de la Carta Única ignoraban la valencia de su forma esperada, y F3 atribuía a la tarifa una justificación que la economía no tiene. El creative-director separó los bloqueantes del prototipo (cobro, cifras, economía, Credulidad, rangos) de los de APPROVED (Dos Caminos, AC-23, AC débiles, R12) según D-54; se corrigieron todos.
Prior verdict resolved: First review
Findings:
- [BLOCKING] R5/R6: cobro de UT sin momento — corregido: al confirmar el reparto (D-55), AC-29.
- [BLOCKING] Formulas: cifras de Carta Única sin valencia; F2 "0,527 contra 0,525" mal tomado (es 0,529 contra 0,527); F4 listaba ρ sin usarla — corregido (nota "Sin valencia", cifra citada, `max(ρ, 1−ρ) + Δ`).
- [BLOCKING] F3/Tuning Knobs: "se justifican por la tarifa" y "3 a 5 clientes" sin fuente — corregido (borrado; cuenta citada de §5.1; tarifa por tirada a Open Questions).
- [BLOCKING] R8/E4: desvío del GDD maestro §5.4 (Credulidad) sin registrar — corregido: se adopta el maestro, provisorio.
- [BLOCKING] Tuning Knobs: rangos que violan el validador — corregido: condición conjunta `C_CU + n_acl · C_acl < C_TT`.
- [BLOCKING] R2: Dos Caminos sin desenlace — corregido: Resultado A/B → desenlace (D-55).
- [BLOCKING] AC-23: control que falla con código correcto (19 + 5 ≥ 20) — corregido.
- [BLOCKING] AC-13/25/28/05: pasaban con el bug más probable o no aislaban la regla — corregidos.
- [BLOCKING] R12: "dos reglas" con tres viñetas — corregido.
- [RECOMMENDED] Overview: "medir al cliente" no existe en el MVP (elegir tirada = reconocer la forma); bajarlo tras el prototipo.
- [RECOMMENDED] Player Fantasy ausente (advisory en standard).
- [RECOMMENDED] R10: qué pasa con origen y conflicto en un sí o no.
- [RECOMMENDED] Posiciones libres: decidir que no contradicen; incoherencia "el rol, nunca" contra E9.
- [RECOMMENDED] AC-11 y AC-26: partir; AC-20 provisorio; rotular AC que dependen de Reloj de Vela o Mazo y Robo.
- [RECOMMENDED] UI: qué se oculta y qué va con candado en el selector (contradice AC-08/09); fatiga de la advertencia E1.
- [RECOMMENDED] Aclaratoria con 10–14 UT y Carta Única — a Open Questions como medición de D-53.
Disputas: (i) un solo acto en el sí o no y tarifa atada al cliente (game-designer, bloqueante) contra hipótesis del prototipo (creative-director) — se tomó la del CD. (ii) Cifras con valencia en `cifras-cartas.md` (creative-director) — de acuerdo con D-54 (el prototipo las necesita), pero salen del reconteo, que no está hecho; mientras tanto se rotularon como sin valencia. (En la revisión se atribuyó por error a D-53 que eran de producción; lo corrigió `/review-all-gdds` del mismo día.) (iii) ~13 AC bloqueantes (qa-lead) — solo AC-05/13/23/25/28 eran defectos; códigos y fixtures quedan en las historias. (iv) UX de Cruz Celta, confirmación y aclaratoria (ux-designer) — no bloquean: fuera del MVP o de `/ux-design`.
Receipt: sellado sobre la versión revisada (antes de las correcciones), así que la versión corregida da CHANGED y pide re-revisión.
Reviewed-Content-Hash: design/gdd/tiradas.md aa3348770e1c24c1287b569c43ba122aadb85d63
Reviewed-Content-Hash: design/registry/entities.yaml 57baf5849122b8e7da5e197f10ee09b9b1f7b428
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 194338d159df1c729fbd990fbcb4a6f285e5485d
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md ff03ef4801bcd5e16f02dfde3220f0923868269d
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/gdd/systems-index.md cf596b0543f1329bf372cd349f6db0757de43178
Reviewed-Content-Hash: design/decision-log.md bc9a2cfa5fd6da63245a8ad50346e01a3ec1bdb8
Reviewed-Content-Hash: design/balance/cifras-cartas.md a55d6717e2bd70757e764fc8aaaaf81b030401e6
Reviewed-Content-Hash: design/balance/economia-mvp.md 9d7032562c3c2d170b30213df756fdc90f791147
Reviewed-Content-Hash: design/ARCANUM_VULGARIS_GDD.md c5059d53f17055a59c460c9d4f734b3264c606f4

## Review — 2026-10-25 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, economy-designer, qa-lead, ux-designer, creative-director (senior)
Blocking items: 17 (4 para prototipar, 13 para APPROVED) | Recommended: 12
Summary: Re-revisión. Los 9 bloqueantes anteriores estaban corregidos. El hallazgo central (economy-designer, con `tools/balance/economia_mvp.py`) es que con tarifa plana la Carta Única rinde más dinero por UT que Tres Tiempos, así que la hipótesis de D-55 no se podía medir. El diseñador decidió precio por tirada con pago limitado por la reacción y el bolsillo del cliente, vela corta sin baja de Credulidad y negociar la vuelta del cliente (D-57). Se corrigieron todos los bloqueantes.
Prior verdict resolved: Yes
Findings:
- [BLOCKING-proto] R1/R8/F3: Carta Única domina por ingreso/UT con tarifa plana — corregido: precio `π`, R8e, F3a, hipótesis y métrica de descarte (D-57).
- [BLOCKING-proto] States: orden de la atención sin escribir — corregido: secuencia de 8 pasos; aclaratoria en dos pasos (R8a).
- [BLOCKING-proto] R8/E1: cola de jornada 10–19 UT — corregido: vela corta sin baja, R8f negociar la vuelta, UT sobrantes se pierden, E1 sin advertencia con conjunto vacío.
- [BLOCKING-proto] R11/E8: palabra ambigua como refugio — corregido: R11a requisito a Resonancia, ρ por cliente, E8 hipótesis con métrica.
- [BLOCKING] AC-07 fallaba con código correcto; AC-18 control contra R6 (E3 → "ofrecible por catálogo"); AC-22 situación imposible; AC-17 pasaba con pesos uniformes — corregidos.
- [BLOCKING] AC-11/AC-26 sin rechazo observable ni borde 5/4; AC-20 mezclaba Logic y UI — partidos.
- [BLOCKING] R8c contra `n_acl`; F3 sin `P_exacto ⊆ P_pos⁺`; cita falsa "2 preguntas (§5.1)" — corregidos.
- [BLOCKING] Convención de provisorios contra coding-standards; AC sin rótulo — corregidos.
- [BLOCKING] UI: "todavía no la conocés" falso para tirada disponible con roles deshabilitados — tabla de estados.
- [BLOCKING] Higiene (fila de Cartas, l.131, nota lean, Last Verified); Dos Caminos/Vínculo/Cruz Celta sin rótulo — R3a.
- [RECOMMENDED] Rangos de costos como derivados de R12 y monotonía de costos.
- [RECOMMENDED] Recalibrar `economia-mvp.md` y el script (tarifa plana, aclaratoria, trucos, l.90, l.92) — en Open Questions.
- [RECOMMENDED] Propina negativa con Credulidad < 0; Credulidad sin fuentes (H7).
- [RECOMMENDED] F2 pesimista por reposición; F4 sin restricción de la carta; `T_m^v` = 1; `η` con aclaratoria.
- [RECOMMENDED] Partir AC-02/06/14/16/21/24/27/29; validador sobre el catálogo real; AC de R8d, E9 y transiciones.
- [RECOMMENDED] UX a `/ux-design`: motivo visible, elegir ≠ confirmar en gamepad, forma + color, pista a posteriori, fatiga de E1, Cruz Celta en Switch.
- [OPEN] R8f delata la tirada esperada (la opción aparece solo cuando no alcanza la esperada) — en Open Questions, a decidir.
- [OPEN] Valores iniciales sin decidir por el diseñador: `B_tirada` ×1,1, baja de Credulidad 10, umbrales 80/95/50 %.
Disputas: (i) game-designer y economy pedían reabrir D-55 — el CD no la reabrió; lo resolvió D-57 por decisión del diseñador. (ii) Rangos de costos (systems, bloqueante) — el CD los dejó recomendados. (iii) UX: al GDD solo la confirmación de la aclaratoria y la tabla de estados; el resto a `/ux-design`. (iv) Tiradas fuera del MVP — rótulo de pendiente en vez de bloqueo. (v) Provisorios — razón al qa-lead en la forma.
Receipt: sellado sobre la versión revisada (antes de las correcciones); tiradas.md, decision-log.md y systems-index.md con su hash de HEAD, así que la versión corregida da CHANGED y pide re-revisión.
Reviewed-Content-Hash: design/gdd/tiradas.md 4d5d22464f14f36ed7f194af656a148bff06950a
Reviewed-Content-Hash: design/registry/entities.yaml 57baf5849122b8e7da5e197f10ee09b9b1f7b428
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 194338d159df1c729fbd990fbcb4a6f285e5485d
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md b37ffe1ed707d4760640a7e8f4326b8e22c51d47
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/gdd/systems-index.md 4303f55de6f7826bbc2bd9ee0cb08053a162e515
Reviewed-Content-Hash: design/decision-log.md 2aa92e8da22491ae1ec9c73a3b0589d877501a21
Reviewed-Content-Hash: design/balance/cifras-cartas.md a55d6717e2bd70757e764fc8aaaaf81b030401e6
Reviewed-Content-Hash: design/balance/economia-mvp.md 9d7032562c3c2d170b30213df756fdc90f791147
Reviewed-Content-Hash: design/ARCANUM_VULGARIS_GDD.md c5059d53f17055a59c460c9d4f734b3264c606f4
Reviewed-Content-Hash: tools/balance/economia_mvp.py 319c7d2b47321f84d97aabf8bbc8ddd39d588aef
Reviewed-Content-Hash: design/gdd/gdd-cross-review-2026-10-25.md e9634ded1a1500ba564587e6a9d3807e6bcb0520

## Review — 2026-10-26 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, economy-designer, qa-lead, ux-designer, creative-director (senior)
Blocking items: 12 (5 para prototipar, 7 para APPROVED) | Recommended: 8
Summary: Tercera pasada. Estructura completa, aritmética verificada y sin conflictos con el registro. El hallazgo central (economy, game-designer, systems) es que D-57 no cumple su propio objetivo: con 0 preguntas (son opcionales y hoy costo puro) o con B < T, la Carta Única domina en pago por UT, así que la hipótesis del prototipo vuelve a no poder fallar. El CD pide recalibrar sin rehacer: F3a ordenada, preguntas como variable medida con beneficio stub, métrica de descarte simétrica y por jornada, B/T legible en el fixture y R8f fuera del prototipo o acotada.
Prior verdict resolved: Yes (los 17 bloqueantes anteriores figuran corregidos; las correcciones trasladan validación a sistemas sin GDD)
Findings:
- [BLOCKING-proto] F3a: orden de bono, tope y R sin definir; cruce mal escrito (1,65·T → 1,5·T).
- [BLOCKING-proto] F3a/Open Questions: con 0 preguntas CU 0,100·T/UT contra TT 0,0825·T; preguntas sin beneficio → "no preguntar + CU" domina.
- [BLOCKING-proto] Open Questions: métrica de descarte unilateral y por UT; falta techo de la esperada y medición por jornada.
- [BLOCKING-proto] F3a/R8e: B/T sin distribución ni señales observables para el prototipo (requisito saliente a Arquetipos).
- [BLOCKING-proto] R8f: sin gate de estado (tras el reparto siempre se ofrece) y sin costo; no medible.
- [BLOCKING] AC: cero AC de transiciones ilegales del orden de atención.
- [BLOCKING] AC: R8b sin AC con posición libre; R8d sin AC.
- [BLOCKING] AC: R8e sin AC ("ningún código la calcula" es falso); R11a sin trazabilidad.
- [BLOCKING] States: revalidación de R6 inalcanzable (AC-29), truco sobre posición confirmada contra R8c, saltear posición, orden aclaratoria/palabra, Disponible vs Fama.
- [BLOCKING] R8: vela corta medida al sentarse el cliente (exploit de bajar la vela adrede).
- [BLOCKING] AC-30: falta 19 UT y roles deshabilitados.
- [BLOCKING] UI: orden y foco fijos del selector; reversibilidad de confirmar; palabra elegida al llegar la aclaratoria; estado "elegida" y rechazo de R6; motivo visible frente al Pilar 3; no disponibles visibles u ocultas.
- [RECOMMENDED] Tuning Knobs: barrer π_TT 1,8–2 en el prototipo; rangos de costos como dominio conjunto.
- [RECOMMENDED] Script de economía: cola de 10–19 UT.
- [RECOMMENDED] F4: asimetría de Match sí (4 temas) / no (9); validar ρ en (0,1); rotular la mezcla.
- [RECOMMENDED] F1/F3/F5: k = 0, s por familia y exacto, cota con rol repetido.
- [RECOMMENDED] AC: ajustes de qa-lead Q5–Q19 (AC-12, 13, 16, 17b, 17c, 18, 19, 22, 24, 26b, 29, 31, rótulos, fixture).
- [RECOMMENDED] Resonancia: varianza de R mayor con tiradas grandes.
- [RECOMMENDED] Open Questions: gate de spec y hardware para la Cruz Celta.
Disputas: (i) economy MAJOR contra NEEDS REVISION — NEEDS REVISION, arreglos locales. (ii) Hipótesis D-57 — se resuelve en el prototipo con condiciones, sin fijar π ni el valor final de las preguntas. (iii) Rangos contra validador (systems, bloqueante) — recomendado. (iv) Fantasía no entregada (game-designer, bloqueante) — no bloquea Tiradas; requisito saliente y verificación en el prototipo. (v) UX — reglas que tocan pilares al GDD, el resto a /ux-design. Rechazados: G7 ("contestar siempre no" da 50 %), AC-23/27 fuera de rango (son de borde), Monte Carlo previo al prototipo.
Receipt: sellado sobre la versión revisada, antes de las correcciones; systems-index.md con su hash previo al cambio de estado.
Reviewed-Content-Hash: design/gdd/tiradas.md fc3bc479643ba3dabdd755e1e513371049aa8020
Reviewed-Content-Hash: design/registry/entities.yaml 57baf5849122b8e7da5e197f10ee09b9b1f7b428
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 194338d159df1c729fbd990fbcb4a6f285e5485d
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md b37ffe1ed707d4760640a7e8f4326b8e22c51d47
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/gdd/systems-index.md 45bc092b57bb53392663a5347d5d152be52180df
Reviewed-Content-Hash: design/decision-log.md 3abc53b922cc653a1a7d13d37807e5961812142e
Reviewed-Content-Hash: design/balance/cifras-cartas.md a55d6717e2bd70757e764fc8aaaaf81b030401e6
Reviewed-Content-Hash: design/balance/economia-mvp.md 9d7032562c3c2d170b30213df756fdc90f791147
Reviewed-Content-Hash: tools/balance/economia_mvp.py 319c7d2b47321f84d97aabf8bbc8ddd39d588aef

## Review — 2026-10-26 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: L
Specialists: game-designer, systems-designer, economy-designer, qa-lead, ux-designer, creative-director (senior)
Blocking items: 11 (6 para prototipar, 5 para APPROVED) | Recommended: 9
Summary: Cuarta pasada. La estructura está estable y la aritmética es correcta, pero la economía provisoria de F3a no converge: el stub de preguntas no tenía tope, no dependía del Match ni de la intención y suponía cola ilimitada, así que la hipótesis podía aprobar o descartar por el motivo equivocado. La contradicción de States (preguntar entre elegir y confirmar) la encontraron por separado cuatro revisores. El CD pidió sacar la hipótesis al plan del prototipo y dejar en Tiradas solo invariantes (D-59).
Prior verdict resolved: Yes (los 12 bloqueantes anteriores figuran corregidos; las correcciones de F3a abrieron los bloqueantes 1–3 y 11)
Findings:
- [BLOCKING-proto] F3a: stub R_0(1+α·q) sin tope, sin Match ni intención; aclaratoria con retorno 0; con α < 0,30 el resultado se conoce antes de jugar.
- [BLOCKING-proto] F3a/Open Questions: clientes por jornada (N) sin definir; según N domina TT o CU, no el cliente.
- [BLOCKING-proto] Open Questions: métrica 80/95 % sin potencia con 3–5 clientes; barrido de π_TT del lado conocido.
- [BLOCKING-proto] States: paso 5 contra tabla de operaciones (preguntar y negociar con tirada elegida); AC-29c sin sentido.
- [BLOCKING-proto] R8f: condición en vivo (gastar vela la habilita); q del cliente que vuelve sin definir.
- [BLOCKING-proto] R10: polaridad del sí o no sin especificar.
- [BLOCKING] States: elegir tirada no ofrecida, reversibilidad de la afirmación, aclaratoria y trucos tras afirmar.
- [BLOCKING] AC: AC-23, 19 y 16 pasan con código incorrecto; AC-26b, 33, 17a/c, 10 incompletos; R11 sin AC positivo; fixture contra AC-01; sin AC de orden y foco.
- [BLOCKING] UI: negociar sin confirmación; "Repartir" sin especificar; ningún botón debe elegir y confirmar.
- [BLOCKING] UI/Pilar 3: motivo sin política de subtítulo, ritmo, interrupción ni repetición; accessibility-requirements.md no existe.
- [BLOCKING] F3a (si quedaba): "con B < T gana siempre la CU" es falso con R < 1; cruce general B > 1,5·T·R.
- [RECOMMENDED] E1/UI: vela corta silenciosa; vista previa pasiva de tiradas perdidas.
- [RECOMMENDED] R8e: al menos una señal de B independiente del estatus.
- [RECOMMENDED] Tuning Knobs: rangos como dominio conjunto; validar ρ en (0,1).
- [RECOMMENDED] AC fusionados (02, 06, 11b/c, 13, 14, 24, 25, 28, 30, 31, 35); borde 19/20 de AC-31; convención de provisorios con dueño.
- [RECOMMENDED] UI: estados del selector sin color; contador y ubicación de la aclaratoria; confirmar posición contra error de entrada.
- [RECOMMENDED] Resonancia: vender bien una carta muda tiene que pagar (Pilar 6).
- [RECOMMENDED] economia-mvp.md: dos fuentes de verdad; pasar a "en recalibración".
- [RECOMMENDED] economia_mvp.py: las UT de 10–19 valen una CU; el corte en 20 pierde 15–25 % del ingreso.
- [RECOMMENDED] Registro: faltan π, n_acl, B_tirada y α.
Disputas: (i) Preguntar con tirada elegida — ux pedía rechazarlo, el CD intercalar; el diseñador eligió intercalar. (ii) F3a contra la economía aprobada — bloqueante del plan y de la economía, no de Tiradas. (iii) Fila Base — el fondo del hallazgo de economy vale, pero la tabla es ambigua; queda para Fila y Mirilla. (iv) Cruce 1,5·T (systems, bloqueante) — recomendado, porque está rotulado con R = 1. (v) Stub sin Match — defecto del instrumento, no del contrato. Decisiones del diseñador (D-59): plan del prototipo, intención completa en el modelo (contra la recomendación del CD), N como parámetro en vela escasa, intercalar, R8f al sentarse sin q, subtítulo + repetir + accesibilidad, polaridad como campo (contra la recomendación de contrato de redacción), negociar en dos pasos.
Receipt: sellado sobre la versión revisada, antes de las correcciones; decision-log.md y systems-index.md con su hash previo al cambio.
Reviewed-Content-Hash: design/gdd/tiradas.md 552e0c33a51be762ad93e6e59c7d346ba82236fe
Reviewed-Content-Hash: design/registry/entities.yaml 57baf5849122b8e7da5e197f10ee09b9b1f7b428
Reviewed-Content-Hash: .claude/skills/design-review/SKILL.md a63d8fba9b7142eeb43791f061e2e1533c429b43
Reviewed-Content-Hash: design/gdd/taxonomia-de-temas-y-roles.md 194338d159df1c729fbd990fbcb4a6f285e5485d
Reviewed-Content-Hash: design/gdd/base-de-datos-de-cartas.md b37ffe1ed707d4760640a7e8f4326b8e22c51d47
Reviewed-Content-Hash: design/gdd/game-concept.md 4405d37092a5eb83ecbd4495a41b5db928dc4617
Reviewed-Content-Hash: design/gdd/systems-index.md 4303f55de6f7826bbc2bd9ee0cb08053a162e515
Reviewed-Content-Hash: design/decision-log.md 2c986e77c6433423a3cf0e6a22f7378938d33ee1
Reviewed-Content-Hash: design/balance/cifras-cartas.md a55d6717e2bd70757e764fc8aaaaf81b030401e6
Reviewed-Content-Hash: design/balance/economia-mvp.md 9d7032562c3c2d170b30213df756fdc90f791147
Reviewed-Content-Hash: design/ARCANUM_VULGARIS_GDD.md c5059d53f17055a59c460c9d4f734b3264c606f4
Reviewed-Content-Hash: tools/balance/economia_mvp.py 319c7d2b47321f84d97aabf8bbc8ddd39d588aef
