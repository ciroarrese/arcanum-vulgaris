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
