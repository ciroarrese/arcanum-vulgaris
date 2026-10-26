# Systems Index: Arcanum Vulgaris

> **Status**: Approved
> **Created**: 2026-10-20
> **Last Updated**: 2026-10-22
> **Source Concept**: design/ARCANUM_VULGARIS_GDD.md (GDD maestro v1.9; síntesis en `design/gdd/game-concept.md`)

---

## Overview

Arcanum Vulgaris es un roguelite de deducción donde el jugador es un tarotista estafador que lee cartas de tarot reales a clientes generados por combinación. El bucle central es **observar → leer → sentenciar → cobrar → sobrevivir**: inspeccionar al cliente y provocar sus tells, robar cartas al azar en una tirada, interpretarlas con una gramática de combinación real, elegir una intención retórica y cobrar según la Resonancia de la lectura, mientras la economía diaria y las Deudas de Sangre empujan hacia la ruina. Los sistemas se organizan alrededor de tres piezas que todo lo demás consume: un **vocabulario común de temas y roles** (Taxonomía), un **generador de situaciones** que crea la verdad oculta de cada cliente y una **regla de resolución** (Resonancia) que compara la lectura con esa verdad. Los pilares que más condicionan el diseño son el Pilar 6 (no hay carta mala, hay lector malo), el Pilar 3 (memoria pura sobre el cliente) y la regla de que la ruina nunca es sorpresiva.

**Base.** *Taxonomía de Temas y Roles* define los temas (traición, deuda, culpa…) y los roles narrativos (origen, conflicto, desenlace, el otro, caminos) que hablan cartas, situaciones, tiradas, preguntas y textos; desacopla al Generador de las Tiradas. *Modificadores* es el bus por el que artilugios, deudas, insumos, ediciones, la regla de mapa y los Grados de Infamia publican efectos que otros sistemas leen. *Base de Datos de Cartas* guarda las 78 cartas con elemento, palabras clave y temas. *RNG con Semilla* centraliza todo el azar para reproducir partidas, testear y sostener la Lectura Diaria. *Arquetipos y Pieles de Mapa* define los 10 arquetipos del sistema y su piel por mapa. *Flujo de Jornada* es la máquina de estados del día (mañana → mirilla → mesa → cierre).

**Núcleo.** *Mazo y Robo* baraja, roba y orienta las cartas según el Nivel de Mazo. *Reloj de Vela* descuenta UT por acción y abre ventanas de tiempo real solo para los tells. *Tiradas* define las 5 tiradas y traduce posiciones a roles. *Generador de Situaciones* combina arquetipo × secreto × motivo × urgencia y produce temas por rol. *Métricas del Cliente* sostiene Paciencia, Credulidad y Tensión. *Gramática de Combinación* aplica dignidades elementales, palo dominante, peso de Mayores y números según la forma de la tirada. *Textos por Plantillas* arma preguntas, respuestas y sentencias a partir de la situación, preparado para traducción. *Guardado de Partida y Perfil* persiste la partida al cierre de cada jornada y el perfil de desbloqueos.

**Funcionalidades.** Los sistemas de mesa (*Inspección y Tells*, *Preguntas Capciosas*, *Interpretación y Sentencia*, *Prestidigitación*, *Resonancia y Resolución*) forman la lectura. Los de supervivencia (*Economía de Sesión y Cierre*, *Fama, Reputación y Ascenso*, *Fila y Mirilla*, *Deudas de Sangre*, *Trastienda*, *Informantes*) forman la presión diaria. *Regla de Mapa*, *Meta-progresión*, *Lectura Diaria* y *Escenas de Derrota y Victoria* dan forma a la partida completa y a la vida útil.

**Presentación y Pulido.** *HUD de Mesa*, *Tapete y Tooltips*, *Pantallas de Gestión*, *Menú e Inicio de Partida*, *Voces en Balbuceo* y *Música, Efectos de Sonido y Feedback* envuelven a los sistemas de juego. *Tutorial, Accesibilidad y Localización* y *Servicios de Plataforma* cierran el producto.

**Equipo:** 1 persona (diseño, código y arte con ayuda de IA). **Recomendación registrada:** diseñar primero los 5 GDDs del núcleo de lectura (Taxonomía, Cartas, Tiradas, Generador, Resonancia) y validarlos con un prototipo descartable antes de diseñar el resto del MVP.

---

## Systems Enumeration

| # | System Name | Category | Priority | Status | Design Doc | Depends On |
|---|-------------|----------|----------|--------|------------|------------|
| 1 | Taxonomía de Temas y Roles (inferred) | Core | MVP | Needs Revision | [taxonomia-de-temas-y-roles.md](taxonomia-de-temas-y-roles.md) | — |
| 2 | Modificadores (inferred) | Core | MVP | Not Started | — | — |
| 3 | Base de Datos de Cartas | Core | MVP | Needs Revision | [base-de-datos-de-cartas.md](base-de-datos-de-cartas.md) | Taxonomía de Temas y Roles |
| 4 | RNG con Semilla (inferred) | Core | MVP | Not Started | — | — |
| 5 | Arquetipos y Pieles de Mapa | Core | MVP | Not Started | — | Taxonomía de Temas y Roles |
| 6 | Flujo de Jornada (inferred) | Core | MVP | Not Started | — | — |
| 7 | Mazo y Robo | Gameplay | MVP | Not Started | — | Base de Datos de Cartas, RNG con Semilla |
| 8 | Reloj de Vela | Gameplay | MVP | Not Started | — | Flujo de Jornada, Modificadores |
| 9 | Tiradas | Gameplay | MVP | Needs Revision | [tiradas.md](tiradas.md) | Taxonomía de Temas y Roles, Mazo y Robo, Base de Datos de Cartas, Reloj de Vela |
| 10 | Generador de Situaciones | Gameplay | MVP | Not Started | — | Taxonomía de Temas y Roles, Base de Datos de Cartas, Tiradas, Arquetipos y Pieles de Mapa, RNG con Semilla |
| 11 | Métricas del Cliente | Gameplay | MVP | Not Started | — | Arquetipos y Pieles de Mapa, Modificadores |
| 12 | Gramática de Combinación | Gameplay | MVP | Not Started | — | Taxonomía de Temas y Roles, Base de Datos de Cartas, Tiradas |
| 13 | Textos por Plantillas (inferred) | Narrative | MVP | Not Started | — | Taxonomía de Temas y Roles, Arquetipos y Pieles de Mapa |
| 14 | Guardado de Partida y Perfil (inferred) | Persistence | MVP | Not Started | — | Flujo de Jornada |
| 15 | Inspección y Tells | Gameplay | MVP | Not Started | — | Generador de Situaciones, Métricas del Cliente, Reloj de Vela, Textos por Plantillas |
| 16 | Preguntas Capciosas | Gameplay | MVP | Not Started | — | Generador de Situaciones, Métricas del Cliente, Inspección y Tells, Reloj de Vela, Textos por Plantillas |
| 17 | Interpretación y Sentencia | Gameplay | MVP | Not Started | — | Taxonomía de Temas y Roles, Tiradas, Base de Datos de Cartas, Textos por Plantillas |
| 18 | Resonancia y Resolución | Gameplay | MVP | Not Started | — | Taxonomía de Temas y Roles, Base de Datos de Cartas, Generador de Situaciones, Tiradas, Gramática de Combinación, Interpretación y Sentencia, Métricas del Cliente |
| 19 | Prestidigitación | Gameplay | MVP | Not Started | — | Mazo y Robo, Tiradas, Métricas del Cliente, Reloj de Vela |
| 20 | Economía de Sesión y Cierre de Caja | Economy | MVP | Not Started | — | Resonancia y Resolución, Arquetipos y Pieles de Mapa, Modificadores |
| 21 | Fama, Reputación y Ascenso de Sede | Progression | MVP | Not Started | — | Resonancia y Resolución, Economía de Sesión y Cierre de Caja, Tiradas |
| 22 | Fila y Mirilla | Gameplay | MVP | Not Started | — | Generador de Situaciones, Métricas del Cliente, Reloj de Vela, Fama, Reputación y Ascenso de Sede |
| 23 | Deudas de Sangre | Gameplay | MVP | Not Started | — | Arquetipos y Pieles de Mapa, Resonancia y Resolución, Economía de Sesión y Cierre de Caja, Modificadores |
| 24 | Trastienda | Economy | MVP | Not Started | — | Economía de Sesión y Cierre de Caja, Prestidigitación, Modificadores |
| 25 | Tapete y Tooltips de Cartas (inferred) | UI | MVP | Not Started | — | Taxonomía de Temas y Roles, Base de Datos de Cartas, Tiradas, Interpretación y Sentencia |
| 26 | HUD de Mesa (inferred) | UI | MVP | Not Started | — | Reloj de Vela, Métricas del Cliente, Deudas de Sangre, Prestidigitación, Fama, Reputación y Ascenso de Sede |
| 27 | Pantallas de Gestión (inferred) | UI | MVP | Not Started | — | Economía de Sesión y Cierre de Caja, Trastienda, Deudas de Sangre, Fama, Reputación y Ascenso de Sede |
| 28 | Informantes y Dossiers | Economy | Vertical Slice | Not Started | — | Economía de Sesión y Cierre de Caja, Generador de Situaciones |
| 29 | Escenas de Derrota y Victoria | Narrative | Vertical Slice | Not Started | — | Deudas de Sangre, Fama, Reputación y Ascenso de Sede |
| 30 | Menú e Inicio de Partida (inferred) | UI | Vertical Slice | Not Started | — | Mazo y Robo, Guardado de Partida y Perfil |
| 31 | Voces en Balbuceo | Audio | Vertical Slice | Not Started | — | Arquetipos y Pieles de Mapa, Métricas del Cliente, Textos por Plantillas |
| 32 | Música, Efectos de Sonido y Feedback Sensorial | Audio | Vertical Slice | Not Started | — | Resonancia y Resolución, Inspección y Tells, Prestidigitación |
| 33 | Tutorial, Accesibilidad y Localización (inferred) | Meta | Vertical Slice | Not Started | — | Textos por Plantillas, todas las pantallas de UI |
| 34 | Regla de Mapa (El Ticker en el Mapa B) | Gameplay | Alpha | Not Started | — | Generador de Situaciones, Modificadores |
| 35 | Meta-progresión | Progression | Alpha | Not Started | — | Guardado de Partida y Perfil, Fama, Reputación y Ascenso de Sede |
| 36 | Lectura Diaria | Meta | Full Vision | Not Started | — | RNG con Semilla, Guardado de Partida y Perfil, núcleo completo, Servicios de Plataforma |
| 37 | Servicios de Plataforma (inferred) | Meta | Full Vision | Not Started | — | Guardado de Partida y Perfil |

---

## Categories

| Category | Description | Typical Systems |
|----------|-------------|-----------------|
| **Core** | Foundation systems everything depends on | Taxonomía, Modificadores, Cartas, RNG, Arquetipos, Flujo de Jornada |
| **Gameplay** | The systems that make the game fun | Tiradas, Generador, Tells, Preguntas, Resonancia, Prestidigitación, Deudas de Sangre |
| **Progression** | How the player grows over time | Fama, Reputación y Ascenso; Meta-progresión |
| **Economy** | Resource creation and consumption | Economía de Sesión, Trastienda, Informantes |
| **Persistence** | Save state and continuity | Guardado de Partida y Perfil |
| **UI** | Player-facing information displays | HUD, Tapete y Tooltips, Pantallas de Gestión, Menú |
| **Audio** | Sound and music systems | Voces en Balbuceo, Música/SFX/Feedback |
| **Narrative** | Story and dialogue delivery | Textos por Plantillas, Escenas de Derrota y Victoria |
| **Meta** | Systems outside the core game loop | Tutorial/Accesibilidad/Localización, Lectura Diaria, Servicios de Plataforma |

---

## Priority Tiers

| Tier | Definition | Target Milestone | Design Urgency |
|------|------------|------------------|----------------|
| **MVP** | Required for the core loop to function. Without these, you can't test "is this fun?" | First playable prototype (Mapa B, Sedes 1–3) | Design FIRST |
| **Vertical Slice** | Required for one complete, polished area. Demonstrates the full experience. | Demo pulida de las Sedes 1–3 | Design SECOND |
| **Alpha** | All features present in rough form. Complete mechanical scope, placeholder content OK. | Mapa B completo (Sedes 1–8, 5 tiradas, 78 cartas, 10 arquetipos) | Design THIRD |
| **Full Vision** | Polish, edge cases, nice-to-haves, and content-complete features. | Release (Mapas A y C, Lectura Diaria, plataformas) | Design as needed |

> **Review gates** (MVP, todas las capas): TD-SYSTEM-BOUNDARY, PR-SCOPE y CD-SYSTEMS omitidos — modo de revisión "lean". PR-SCOPE se reemplaza por la evaluación de alcance registrada abajo.
>
> **Scope note** (MVP): 27 sistemas para un equipo de 1 persona ≈ 60 sesiones de diseño solo en GDDs (9 S, 12 M, 6 L). Mitigación aprobada: diseñar y prototipar primero el núcleo de lectura (órdenes 1, 2, 8, 10 y 18 del orden de diseño de abajo, marcados con ★) antes de diseñar el resto del MVP.

---

## Dependency Map

### Foundation Layer (no dependencies)

1. Taxonomía de Temas y Roles — vocabulario común (temas y roles narrativos) de cartas, situaciones, tiradas, preguntas y textos; desacopla Generador y Tiradas.
2. Modificadores — bus de efectos: las fuentes publican, los sistemas afectados leen; evita que cada fuente conozca a cada destino.
3. Base de Datos de Cartas — depends on: Taxonomía. Datos de las 78 cartas.
4. RNG con Semilla — todo el azar reproducible (tests deterministas, Lectura Diaria, reproducción de bugs).
5. Arquetipos y Pieles de Mapa — depends on: Taxonomía. Los 10 arquetipos y su piel por mapa.
6. Flujo de Jornada — máquina de estados del día donde se enganchan los demás sistemas.

### Core Layer (depends on foundation)

1. Mazo y Robo — depends on: Cartas, RNG
2. Reloj de Vela — depends on: Flujo de Jornada, Modificadores
3. Tiradas — depends on: Taxonomía (roles), Mazo y Robo, Cartas (`acierto_posible`, solo para diseño; D-50). Traduce posiciones a roles. La palanca del Pilar 6 ante una carta muda es la carta aclaratoria **ciega** (D-52), que se ofrece sin consultar la verdad ni `acierto_posible` de Cartas. Pasa a Cartas los `k` de sus tiradas como argumento del informe (`k_tiradas`, D-53); Cartas no lee Tiradas.
4. Generador de Situaciones — depends on: Taxonomía, Cartas (pesos `p_t` del mazo activo, D-48), Arquetipos, RNG. Produce temas por **rol**, no por posición, porque la tirada se elige después.
5. Métricas del Cliente — depends on: Arquetipos, Modificadores
6. Gramática de Combinación — depends on: Taxonomía (familias por palo), Cartas, Tiradas (la forma de la tirada define qué cartas son vecinas)
7. Textos por Plantillas — depends on: Taxonomía, Arquetipos. Sube a Núcleo porque preguntas y sentencias son texto.
8. Guardado de Partida y Perfil — depends on: Flujo de Jornada. Cada sistema registra su estado con una interfaz común.

### Feature Layer (depends on core)

1. Inspección y Tells — depends on: Generador, Métricas, Reloj, Textos
2. Preguntas Capciosas — depends on: Generador, Métricas, Tells, Reloj, Textos
3. Interpretación y Sentencia — depends on: Taxonomía (tema de cada palabra clave), Tiradas, Cartas, Textos
4. Prestidigitación — depends on: Mazo, Tiradas, Métricas, Reloj
5. Resonancia y Resolución — depends on: Taxonomía (regla de comparación), Cartas (`acierto_posible`, solo para diseño; D-50), Generador, Tiradas, Gramática, Interpretación, Métricas **Pendiente (D-50):** la palanca del Pilar 6 ante una carta muda, ciega (ver Tiradas).
6. Economía de Sesión y Cierre de Caja — depends on: Resonancia, Arquetipos, Modificadores
7. Fama, Reputación y Ascenso de Sede — depends on: Resonancia, Economía. Se calcula **en el cierre nocturno**.
8. Fila y Mirilla — depends on: Generador, Métricas, Reloj, Fama. Lee la Fama **al empezar el día**.
9. Deudas de Sangre — depends on: Arquetipos, Resonancia, Economía (cobra por la interfaz de pago), Modificadores
10. Trastienda — depends on: Economía, Prestidigitación, Modificadores
11. Informantes y Dossiers — depends on: Economía, Generador
12. Regla de Mapa — depends on: Generador, Modificadores
13. Meta-progresión — depends on: Guardado, Ascenso
14. Lectura Diaria — depends on: RNG, Guardado, núcleo completo, Servicios de Plataforma
15. Escenas de Derrota y Victoria — depends on: Deudas, Ascenso

### Presentation Layer (depends on features)

1. HUD de Mesa — depends on: Reloj, Métricas, Deudas, Prestidigitación, Fama/Reputación
2. Tapete y Tooltips de Cartas — depends on: Taxonomía (tema, familia y marca), Cartas, Tiradas, Interpretación
3. Pantallas de Gestión — depends on: Economía, Trastienda, Informantes, Deudas, Ascenso
4. Menú e Inicio de Partida — depends on: Meta-progresión, Mazo, Guardado
5. Voces en Balbuceo — depends on: Arquetipos, Métricas, Textos
6. Música, Efectos de Sonido y Feedback Sensorial — depends on: Resonancia, Tells, Prestidigitación

### Polish Layer (depends on everything)

1. Tutorial, Accesibilidad y Localización — depends on: Textos y todas las pantallas
2. Servicios de Plataforma — depends on: Guardado (logros, rankings y nube de Steam y Switch)

---

## Recommended Design Order

★ = núcleo de lectura: diseñar y validar con prototipo antes de seguir.

| Order | System | Priority | Layer | Agent(s) | Est. Effort |
|-------|--------|----------|-------|----------|-------------|
| 1 ★ | Taxonomía de Temas y Roles | MVP | Foundation | game-designer, narrative-director | L |
| 2 ★ | Base de Datos de Cartas | MVP | Foundation | game-designer, writer | L |
| 3 | Arquetipos y Pieles de Mapa | MVP | Foundation | game-designer, narrative-director | M |
| 4 | Modificadores | MVP | Foundation | systems-designer | S |
| 5 | RNG con Semilla | MVP | Foundation | technical-director | S |
| 6 | Flujo de Jornada | MVP | Foundation | game-designer | S |
| 7 | Mazo y Robo | MVP | Core | systems-designer | S |
| 8 ★ | Tiradas | MVP | Core | game-designer | M |
| 9 | Gramática de Combinación | MVP | Core | systems-designer | M |
| 10 ★ | Generador de Situaciones | MVP | Core | game-designer, systems-designer | L |
| 11 | Métricas del Cliente | MVP | Core | systems-designer | S |
| 12 | Reloj de Vela | MVP | Core | systems-designer | S |
| 13 | Textos por Plantillas | MVP | Core | writer, localization-lead | L |
| 14 | Guardado de Partida y Perfil | MVP | Core | technical-director | S |
| 15 | Inspección y Tells | MVP | Feature | game-designer, ux-designer | M |
| 16 | Preguntas Capciosas | MVP | Feature | game-designer, writer | M |
| 17 | Interpretación y Sentencia | MVP | Feature | game-designer | M |
| 18 ★ | Resonancia y Resolución | MVP | Feature | systems-designer, game-designer | L |
| 19 | Prestidigitación | MVP | Feature | game-designer | M |
| 20 | Economía de Sesión y Cierre de Caja | MVP | Feature | economy-designer | M |
| 21 | Fama, Reputación y Ascenso de Sede | MVP | Feature | economy-designer | S |
| 22 | Fila y Mirilla | MVP | Feature | game-designer | M |
| 23 | Deudas de Sangre | MVP | Feature | game-designer, systems-designer | L |
| 24 | Trastienda | MVP | Feature | economy-designer | S |
| 25 | Tapete y Tooltips de Cartas | MVP | Presentation | ux-designer | M |
| 26 | HUD de Mesa | MVP | Presentation | ux-designer | S |
| 27 | Pantallas de Gestión | MVP | Presentation | ux-designer | M |
| 28 | Informantes y Dossiers | Vertical Slice | Feature | economy-designer | S |
| 29 | Escenas de Derrota y Victoria | Vertical Slice | Feature | narrative-director, writer | M |
| 30 | Menú e Inicio de Partida | Vertical Slice | Presentation | ux-designer | S |
| 31 | Voces en Balbuceo | Vertical Slice | Presentation | audio-director, sound-designer | M |
| 32 | Música, Efectos de Sonido y Feedback Sensorial | Vertical Slice | Presentation | audio-director, technical-artist | M |
| 33 | Tutorial, Accesibilidad y Localización | Vertical Slice | Polish | ux-designer, accessibility-specialist, localization-lead | L |
| 34 | Regla de Mapa | Alpha | Feature | game-designer, economy-designer | M |
| 35 | Meta-progresión | Alpha | Feature | game-designer | M |
| 36 | Servicios de Plataforma | Full Vision | Polish | technical-director, release-manager | M |
| 37 | Lectura Diaria | Full Vision | Feature | game-designer, live-ops-designer | M |

Effort estimates: S = 1 session, M = 2-3 sessions, L = 4+ sessions.

---

## Circular Dependencies

- **Fila y Mirilla ↔ Fama, Reputación y Ascenso:** resuelto por tiempo. La Fama se escribe solo en el cierre nocturno; la Fila la lee solo al empezar el día.
- **Deudas de Sangre ↔ Economía de Sesión:** resuelto con una interfaz. La Economía emite "balance negativo"; las Deudas cobran a través de una función de pago de la Economía. Se diseña la interfaz primero.
- **Deudas de Sangre ↔ Fila / Reloj:** resuelto con Modificadores. Las Deudas publican efectos (−30% Paciencia, −10 UT) y la Fila y el Reloj los leen sin conocer a las Deudas.

---

## High-Risk Systems

| System | Risk Type | Risk Description | Mitigation |
|--------|-----------|-----------------|------------|
| Generador de Situaciones | Design | Producir de forma automática situaciones coherentes y deducibles (pistas → secreto → tells → temas por rol). Si falla, la deducción se siente arbitraria. | Prototipo descartable del núcleo antes de diseñar el resto; empezar con pools chicos (5 arquetipos, ~15 temas). |
| Resonancia y Resolución | Design | Que el resultado se sienta justo y explicable; que el pago por calidad recompense la investigación sin volver la lectura un cálculo. | Prototipo con el Generador; mostrar al jugador por qué resonó o no la lectura. |
| Taxonomía de Temas y Roles | Scope / Design | Cuello de botella: 7 sistemas dependen directamente de ella (Cartas, Arquetipos, Tiradas, Generador, Textos, Gramática, Resonancia) y casi todo el resto a través de ellos. Un vocabulario mal cortado contamina cartas, situaciones y textos. | Diseñarla primero; crecer por mapa sin renombrar temas existentes. |
| Textos por Plantillas | Technical | Plantillas que se rompen al traducir (género, número, concordancia). | Diseñar el sistema de plantillas con la localización desde el inicio (localization-lead). |
| Base de Datos de Cartas | Scope | 78 cartas × palabras clave derechas e invertidas × temas: mucho contenido a escribir y validar. | El MVP usa 36 cartas (nivel Aprendiz). |
| Deudas de Sangre | Design | Espiral de muerte si se acumulan hilos sin salida. | Tope de 3 hilos, al menos dos salidas por hilo, visibles en el HUD. |

---

## Progress Tracker

| Metric | Count |
|--------|-------|
| Total systems identified | 37 |
| Design docs started | 3 |
| Design docs reviewed | 1 |
| Design docs approved | 0 |
| MVP systems designed | 3/27 |
| Vertical Slice systems designed | 0/6 |

---

## Next Steps

- [x] Review and approve this systems enumeration
- [ ] Design the reading core first (★): Taxonomía → Cartas → Tiradas → Generador → Resonancia (`/design-system [system-name]`)
- [ ] Prototype the reading core (`/prototype`) before designing the rest of the MVP
- [x] Generate `design/gdd/game-concept.md` from the GDD maestro (pillars included; `game-pillars.md` optional at `standard`)
- [ ] Design the remaining MVP-tier systems
- [ ] Run `/design-review` on each completed GDD
- [ ] Run `/gate-check technical-setup` when MVP systems are designed
