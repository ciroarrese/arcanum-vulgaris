# Cross-GDD Review Report

Date: 2026-10-25
GDDs Reviewed: 3 of 3 present
Not read: ninguno
Focus: full
Systems Covered: Taxonomía de Temas y Roles, Base de Datos de Cartas, Tiradas
Agentes: game-designer (consistencia, Fase 2), game-designer (holismo, Fase 3); Fase 4 en la sesión principal.
Insumos: secciones recortadas de los 3 GDDs (Fase 2: Detailed Design, Formulas, Dependencies, Tuning Knobs, Acceptance Criteria, Cross-References; Fase 3: Summary, Overview, Game Feel, Open Questions), `design/registry/entities.yaml` (40 entradas), `systems-index.md`, `game-concept.md`, `economia-mvp.md`, D-50 a D-55. Ningún GDD tiene Player Fantasy (advisory en `standard`); la fantasía se dedujo del Summary, el Overview y el Game Feel. Motor sin elegir: nada engine-specific.

---

## Consistency Issues

### Blocking

🔴 **B1. "Sistema de desbloqueo" sin dueño.** Tiradas lo nombra como dependencia blanda (Dependencies, l.228), y de él dependen States, Tuning Knobs y AC-10. `systems-index.md` no tiene ningún sistema de desbloqueo de tiradas: las candidatas que nombra Tiradas (Open Questions: "Fama o Trastienda"), #21 y #24, están en el índice pero no listan a Tiradas. Decidir el dueño y anotarlo en los dos documentos. No afecta al MVP: Carta Única y Tres Tiempos están disponibles desde el inicio.

### Warnings

⚠️ **W7. Tiradas AC-17 contra Cartas F1.** AC-17 pide como candidatos al desenlace de un sí o no "exactamente los 4 temas favorables para sí y los 9 desfavorables para no". Cartas F1 prohíbe sortear un tema con `p_t` = 0, que es el caso de un tema que el mazo solo tiene como forzada (Cartas F1, E9, "tema trampa"). Con un mazo real, el AC falla o rompe el contrato. Decidir si los candidatos son "valencia ∩ temas sorteables del mazo activo". **Afecta al prototipo.**

⚠️ **W5. Cifras con valencia.** D-54 corrigió a D-53: `P_pos_v`, `P_pos⁺_v` y `P_cero_v` se quedan en Cartas porque el prototipo las necesita (son las de la Carta Única) y salen del reconteo (D-50). La revisión de Tiradas del mismo día las había atribuido por error a producción (D-53) en `tiradas.md`, D-55 y el review log; quedó corregido en esta sesión. Pendiente: el reconteo, que es condición previa al prototipo.

⚠️ **W6. `P_pos` contra `P_pos⁺`.** Tiradas F2, F3 y F5 definen `P_pos` como "acierto de familia posible" y usan `(1 − P_pos)^(k+1)`. Cartas F3 llama cifra principal a `P_pos⁺` (claras y forzadas; `P_pos` es cota inferior) y calcula la aclaratoria con `(1 − P_pos⁺)²`; Tiradas F4 ya usa `P_pos⁺_v`. Hoy coinciden solo porque el conteo no tiene forzadas. Decidir qué base usa Tiradas.

⚠️ **W1. Cartas cita a Tiradas con números viejos.** "Tiradas R8" para la carta aclaratoria (Cartas l.123, 227 y 251, E7): hoy es R8a–R8d (R8 es la tirada esperada). "(Tiradas E3)" en l.222 para "su motivo esperado es el sí o no": hoy está en Tiradas R1; E3 trata formas sin tirada disponible.

⚠️ **W3. Marcas provisorias vencidas en la Taxonomía.** R8 (l.105) dice "provisorios hasta el GDD de Tiradas", igual que `TIRADA_SIN_COMPARABLES` (R9) y el bloque de AC "Roles y posiciones"; AC-01c (l.346) dice "provisorio hasta Cartas y Tiradas"; las l.219 y 288 dicen "ninguno de estos sistemas tiene GDD todavía". Las filas de Tiradas y del Generador, en Dependencies e Interactions, no mencionan la valencia, que los dos consumen, y Cross-References no cita D-51.

⚠️ **W4. Tiradas no trata a Cartas como sistema con GDD.** La tabla Interactions no tiene fila de Cartas, aunque Dependencies (l.226) la declara dependencia dura; la l.131 dice "ninguno tiene GDD salvo la Taxonomía"; Cross-References cita "Cartas F1, F3, R11", pero el texto usa también R12 y F4.

⚠️ **W8. Dueño de `ρ`.** Tiradas F4 y Tuning Knobs: "data file (Generador)… está acá como referencia". Cartas (F3, mezcla): "ρ (Tiradas F4)" y "dato del Generador" en la misma frase. El registro: `proporcion_si_rho`, `source: tiradas.md`. Decidir el dueño (el Generador no tiene GDD).

⚠️ **W9. Las perillas de Tiradas no llegan al validador.** La regla de costos de Tiradas R12 usa `C_acl` y `n_acl`. La firma de la Taxonomía R13 recibe solo `tiradas`, y Cartas amplía las entradas con su propio `config`. Nadie define cómo entra la configuración de Tiradas ni sus errores de dominio, ni si "con un error de configuración no valida los datos" (Cartas, Tuning Knobs) alcanza a las reglas de Tiradas.

⚠️ **W10. Sujeto de error sin formato.** Cartas usa el sujeto `copas+oros/valencia.favorable` (l.103, AC-18n). La Taxonomía R13 no tiene un formato "mazo/valencia", y R4 no tiene prefijo `valencia.` (la valencia es un valor de campo, no un identificador). Decidir si se amplía R13 o se cambia el sujeto.

⚠️ **W2. "(R9)" ambiguo para la valencia.** Tiradas l.121, 224 y 243 citan "(R9)" para la valencia. En la Taxonomía la valencia está en R1 (su R9 son las posiciones libres); en Tiradas, R9 es la tabla de valencia. Aclarar el documento.

### Info

- **I1.** Cartas acepta `k` de 1 a 10 (l.161, dominio de `k_tiradas`) y discute `k` = 10 en F4; el máximo de Tiradas F1 es 6. Cubre de más, no rompe nada.
- **I2.** Tiradas AC-22 usa una "situación sin el rol origen" con Tres Tiempos (`k` = 2). Según la Taxonomía R10 y E3, el Generador asigna tema a todo rol habilitado; solo falta un rol deshabilitado (o una partida guardada, E9). Decidir si el Generador puede omitir roles habilitados.
- **I3.** La tabla de valencia está copiada en Tiradas R9 y Taxonomía R1 (hoy idénticas: 4/9/10); el registro no tiene la valencia. La misma perilla se llama `n_acl` en Tiradas y `a` en Cartas.
- **I4.** Los AC delegados existen y prueban lo que dicen: AC-31, AC-33, AC-37a/b, AC-38, AC-35d y AC-35e de la Taxonomía. SIN_COMPARACION lo prueban sus AC-13a/b (Tiradas cita "su E3").
- **I5.** A Cross-References de Tiradas le faltan D-53 y D-55.

**Revisado sin hallazgos:** listas de valencia iguales en Taxonomía y Tiradas; roles del MVP; regla de posición libre; los cuatro códigos de Tiradas en la tabla de R13; mezcla con `ρ` igual en Tiradas F4 y Cartas F3/F4; dominio de `k_tiradas`; costos de tiradas y aclaratoria contra el registro.

---

## Game Design Issues

### Blocking

Ninguno.

### Warnings

⚠️ **H2. En la Carta Única, la carta es decorado.** Tiradas F4: "La carta no informa… Toda la información del sí o no sale del cliente", y la palabra ambigua da Match 0 seguro (10 temas ambiguos de 23). En la forma esperada de la Carta Única el valor sale del sí o no, y la palabra clave pasa a ser un bono opcional. Agrava D-55 (elegir tirada se reduce a reconocer la forma): además del menú, se vacía la lectura de esa tirada. Choca con el Hook del concepto. ¿La carta tiene que pesar en el pago del sí o no? Lo miden Resonancia y el prototipo.

⚠️ **H4. Fantasía de acierto, no de venta.** La Taxonomía define "cuándo una lectura acierta exacto… a medias", y el jugador ve tema y familia de cada carta: la decisión por posición es emparejar una de 23 etiquetas contra una oculta, con 2/1/0. Roza el anti-pilar "tarot como combate numérico". El Pilar 6 ("hacer que cualquier tirada juegue a favor") y la reinterpretación del concepto no tienen mecánica en estos tres GDDs. ¿Viven en Interpretación y Sentencia? No evaluable del todo hasta esos GDDs.

⚠️ **H3. Carga de atención en la mesa.** En la interpretación quedan al menos 7 sistemas activos a la vez entre diseñados y planificados (Tells y memoria, tooltip de tema y familia, valencia, Gramática, Prestidigitación, Doble Fondo, Sentencia), contra un límite cómodo de 4. D-28 separa en el tiempo la vela de la lectura, pero no alivia la memoria. Ningún GDD dice si la valencia es pública en el tooltip. Carga real no evaluable hasta Interpretación, Gramática y Prestidigitación.

⚠️ **H1. "Éxito" sin definición común.** `tools/balance/economia_mvp.py` calibró las sedes con `p_exito` de 0,45 a 0,75 más `BONO_TRES` (+0,15) y no modela la aclaratoria. Esa tasa no está definida en términos de Match ni de Resonancia. (El agente la comparó con `P_alguno` de Tiradas F2, que mide otra cosa: la existencia de un acierto posible.) ¿Se vuelve a correr la simulación con el reconteo antes de fijar PROCEED/KILL?

⚠️ **H7. La Credulidad tiene sumideros y no fuentes.** Baja con la tirada no esperada (Tiradas R8, D-55) y quizá con la aclaratoria (Open Questions); alimenta la propina (`economia-mvp.md` §4). Ningún documento le da fuente ni dice si persiste entre clientes. No evaluable hasta Métricas del Cliente y Resonancia.

### Info

- **H5.** Ninguno de los tres pretende ser "el punto" del juego (son infraestructura), pero el esfuerzo se concentró en la capa que F4 declara sin información. Inspección y Tells no tiene GDD ni está en el prototipo; sin tells, la separación de habilidad de D-53 no tiene de dónde salir.
- **H6.** Sin estrategias dominantes nuevas: la aclaratoria ya está bajo el umbral de impuesto (D-53); las posiciones libres no existen en el MVP.
- **H8.** El escalado tiende a castigar la lectura grande: un mazo más grande empeora `P_cero`, las tiradas grandes rinden menos Match por UT y la vela es fija. Si la Sede 3 cambia el mazo, coincide con la subida de costos fijos y nuevos arquetipos.
- **H9.** Regla Cero bien servida (F4, aclaratoria ciega); Pilar 5 respetado (cobro al confirmar el reparto); Pilar 6 en el procedimiento, no en la cifra.

**No evaluable todavía:** Pilar 4 (Generador, Resonancia); Pilar 2 (Interpretación y Sentencia, Resonancia); carga real (H3); fuentes de Credulidad (Métricas del Cliente); peso de `B_tirada` y del sí o no (Resonancia); separación de temas por tells (Inspección y Tells); trucos por sede (Prestidigitación); recompensas, Fama y Usurero; posiciones libres (post-MVP); Sedes 4 a 8 (fuera del MVP).

---

## Cross-System Scenario Issues

Scenarios walked: 4
1. Sí o no con Carta Única y aclaratoria (Generador → Cartas F1 → Mazo y Robo → Tiradas → Interpretación → Resonancia)
2. Arranque y validación del catálogo (Taxonomía R13 → Cartas → Tiradas R12)
3. Tres Tiempos usada en un sí o no (Generador → Tiradas → Taxonomía R11 → Resonancia)
4. Vela baja (Reloj de Vela → Tiradas R6 y E1 → Fila y Mirilla)

### Blockers

Ninguno nuevo: el comportamiento indefinido aparece solo donde ya está declarado provisorio y el sistema dueño está en el índice.

### Warnings

⚠️ **Escenario 1 — Generador, Cartas, Tiradas, Resonancia.** Al sortear el desenlace, el candidato puede ser un tema con `p_t` = 0 (W7). Después, el pago del sí o no contra la palabra elegida queda sin definir hasta Resonancia (H2).

⚠️ **Escenario 2 — Taxonomía, Cartas, Tiradas.** Una perilla de costo inválida (`C_acl`, `n_acl`) no tiene vía definida hacia el validador (W9), y no queda claro si el error de configuración de Cartas detiene también las reglas de Tiradas.

⚠️ **Escenario 4 — Reloj de Vela, Tiradas, Fila y Mirilla.** Con 10 a 14 UT, la Carta Única se cobra al confirmar el reparto y la aclaratoria queda fuera de alcance justo cuando la carta puede salir muda (ya en Open Questions de Tiradas). Con menos de 10 UT el cliente queda "no se puede leer" y su destino es de Fila y Mirilla, sin GDD (en el índice).

### Info

ℹ️ **Escenario 3 — Generador, Tiradas, Taxonomía.** No está definido qué pasa con origen y conflicto en un sí o no (Tiradas R10). El AC-22 de Tiradas supone una situación sin origen que la Taxonomía R10 no produce (I2).

---

## GDDs Flagged for Revision

| GDD | Reason | Type | Priority |
|-----|--------|------|----------|
| tiradas.md | B1: desbloqueo sin dueño; W7: AC-17 contra Cartas F1; W2, W4, W6, W8 | Consistency | Blocking |
| base-de-datos-de-cartas.md | W1: referencias viejas a Tiradas; W10: sujeto de valencia | Consistency | Warning |
| taxonomia-de-temas-y-roles.md | W3: marcas provisorias vencidas; W9: firma del validador | Consistency | Warning |

---

## Verdict: FAIL

Un solo bloqueante (B1), por la regla de dependencia sin dueño; no afecta al MVP ni al prototipo. Lo que sí afecta al prototipo son W7, W5 (reconteo pendiente) y H2.

### If FAIL — required actions before re-running

1. **B1:** asignar el desbloqueo de Dos Caminos, El Vínculo y Cruz Celta a un sistema del índice (Fama o Trastienda), y que ese sistema liste a Tiradas en el índice.
2. **W7** (para el prototipo): decidir si los candidatos al desenlace de un sí o no son "valencia ∩ temas sorteables" y ajustar Tiradas AC-17.

---

**Aplicado el mismo día (quick fix):** W1 (Cartas cita Tiradas R8a y R1), W2 (Tiradas cita la valencia como R1 de la Taxonomía) e I5 (Cross-References de Tiradas con D-53 a D-55). Sigue abierto todo lo demás.

**Resuelto el mismo día (D-56):** B1 (el desbloqueo de tiradas es de Fama, Reputación y Ascenso de Sede) y W7 (el desenlace del sí o no se sortea entre los temas de la valencia sorteables en el mazo activo; AC-17 reescrito).
