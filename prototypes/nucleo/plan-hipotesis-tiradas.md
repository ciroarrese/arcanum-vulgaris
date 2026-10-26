> PROTOTYPE - NOT FOR PRODUCTION

# Plan del prototipo del núcleo — Hipótesis de Tiradas

> **Estado:** borrador (D-59, 2026-10-26). Prototipo descartable: estos valores no son diseño final.
> **Origen:** sale de `design/gdd/tiradas.md` F3a y Open Questions. El GDD conserva solo los invariantes del pago (F3a) y los requisitos a Resonancia y Arquetipos (R8e); todo lo que es modelo, barrido y métrica vive acá.
> **Por qué:** la cuarta revisión de Tiradas (2026-10-26) encontró que cada número provisorio puesto en el GDD para sostener la hipótesis abría huecos nuevos. La hipótesis se mide en el prototipo, como pide D-54.

## 1. Hipótesis

Con precio por tirada (`π`), pago limitado por lo que tiene el cliente (`B_cliente`) y preguntas que mejoran el pago, elegir la tirada en un motivo de **situación general** deja de ser solo reconocer la forma: depende del cliente (lo que tiene y cuánto se lo investigó), y ninguna estrategia fija domina el pago por jornada en el régimen de vela escasa.

En **sí o no** la Carta Única es la esperada y la más barata. Que domine ahí es diseño aceptado (cuarta revisión): la decisión de tirada del MVP vive en los clientes de situación general.

## 2. Modelo de pago (intención completa, D-59)

Se usa la fórmula de ingreso de `design/balance/economia-mvp.md` §4, con el precio de la tirada y el tope:

`Pago = min( T · π · b · (M_intención + Credulidad/100 · K_propina) · Q , B_cliente )`

| Variable | Valor del prototipo | Fuente |
|---|---|---|
| `T` | Tarifa de sede × estatus del arquetipo | `economia-mvp.md` §1 |
| `π` | Carta Única ×1; Tres Tiempos barrido en {1,5; 1,8; 2; 2,2} | Tiradas R1 |
| `b` | 1,1 si se usó la esperada; 1 si no | Tiradas R8 (`B_tirada`) |
| `M_intención` | Consolar 1, Acusar 3, Paranoia 2, Extorsionar 5 | `economia-mvp.md` §4 |
| `Credulidad`, `K_propina` | Credulidad final de la lectura; `K` por arquetipo | `economia-mvp.md` §3 |
| `Q` | 0,9 floja, 1,0 correcta, 1,3 excelente; fallo paga `0,2 · T` sin tope adicional | `economia-mvp.md` §4 |
| Baja de Credulidad por no usar la esperada | 10 puntos (pesa a través de la propina) | Tiradas R8 |
| `B_cliente` | Fixture de la §5 | Tiradas R8e |

- **Doble Fondo:** fuera del tope. Es otra fuente de dinero (Pilar 4); se suma después del `min`. *Decisión provisoria del prototipo*: la definitiva es de la economía (Open Questions de Tiradas).
- **Riesgo conocido:** con `M_intención` hasta ×5, el tope `B_cliente` va a estar activo casi siempre con Acusar y Extorsionar. Si eso hace que la Carta Única gane por barata en esos casos, se registra por intención (§6).
- **Jugadores humanos:** el pago sale de lo que hacen en la mesa; no hay stub de preguntas. Las preguntas valen lo que valga la deducción que provocan.

## 3. Bots de línea base

Para separar preferencia de dominancia, cada celda se corre también con bots de estrategia fija, sobre los mismos clientes (misma semilla):

| Bot | Tirada | Preguntas |
|---|---|---|
| `siempre_cu` | Carta Única | 0 |
| `siempre_esperada` | La esperada de la forma | 2 |
| `q_max` | La esperada de la forma | 3 |
| `adaptativo` | Tres Tiempos si `B_cliente / T` ≥ umbral leído; si no, Carta Única | 0 a 3 según `B_cliente / T` |

Modelo de acierto de los bots (solo para ellos): probabilidad de éxito por perfil de `tools/balance/economia_mvp.py` (`p_exito`), +0,15 con Tres Tiempos (`BONO_TRES`) y +0,05 por pregunta **hasta 3 preguntas** (`q_max` = 3; retornos decrecientes, para que preguntar no sea un multiplicador sin techo). La aclaratoria suma lo que da F5 de Tiradas sobre esa probabilidad.

## 4. Clientes por jornada (`N`)

`N` es un parámetro, no un supuesto. Se barre en {3, 5, 7, 9}.

- **Régimen principal: vela escasa** (Pilar 5: atender a fondo a un pez gordo tiene que costar). Es el `N` más chico en que la vela de 100 UT no alcanza para leer a todos con Tres Tiempos y 2 preguntas (30 UT por cliente): hoy `N` ≥ 4.
- Con `N` = 3 sobra vela y Tres Tiempos con preguntas al máximo debería ganar siempre: se corre como control, no cuenta para la métrica.
- Qué significa "Fila Base" del GDD maestro §7.5 (total de la jornada o largo de la fila con reposición) lo decide Fila y Mirilla; este plan no depende de esa respuesta.

## 5. Datos de los clientes

**Distribución de `B_cliente / T`** (lognormal, `σ` = 0,4), por arquetipo:

| Arquetipo | Mediana de `B_cliente / T` |
|---|---|
| Vagabundo | 1,2 |
| Estibador | 2,0 |
| Apostador | 2,0 |
| Viuda | 3,0 |
| Detective | 3,0 |

Condición: en cada sede, al menos el 25 % de los clientes de situación general cae de cada lado del cruce en que Tres Tiempos empieza a pagar más que la Carta Única. Si no, se ajustan las medianas antes de medir.

**Señales de lo que tiene el cliente** (Tiradas R8e): al menos 2 por cliente, y al menos una independiente del estatus del arquetipo, para que `B_cliente / T` varíe dentro de un mismo estatus. Propuesta: el estado de la ropa (sale de `B_cliente / T`, no del arquetipo) y un tell de billetera o de joyas.

## 6. Métricas y descarte

Se mide **por celda** (`N` × `π` de Tres Tiempos × sede), con **al menos 20 jornadas por celda**, y se reporta con intervalo de confianza del 95 %.

1. **Valor de la elección adaptativa:** `VOI = pago medio del bot adaptativo / pago medio del mejor bot fijo − 1`. Si `VOI` < 10 % en el régimen de vela escasa, la elección de tirada no importa: la hipótesis cae.
2. **Dominancia en los dos sentidos** (humanos, clientes de situación general con vela suficiente al sentarse): la hipótesis cae si más del 80 % se leen con la Carta Única (domina la barata) o más del 95 % con la tirada esperada (domina la forma).
3. **Preguntas al techo:** si más del 70 % de los clientes reciben 3 preguntas, preguntar se volvió automático y no responde al cliente.
4. **Por intención:** pago medio por intención retórica y tirada, para ver si con intenciones caras la Carta Única gana por el tope.

Se registra por cliente: tirada, preguntas (`q`), `B_cliente / T`, intención, si el tope estuvo activo, pago, y si se usó la aclaratoria.

## 7. Negociar la vuelta (R8f)

- Condición: la vela **al sentarse** no alcanzaba para alguna tirada ofrecible (Tiradas R8f, D-59).
- Stub de costo: Paciencia −1 y probabilidad de que vuelva `p_vuelve` barrida en {0,3; 0,5; 0,7}.
- El cliente que vuelve es una atención nueva: llega sin las preguntas hechas.
- **Descarte:** si más del 30 % de las negociaciones se hacen con `B_cliente / T` ≥ 2 y la tasa de vuelta efectiva supera el punto de indiferencia, R8f se usa para diferir a los clientes ricos y hay que rediseñarla.

## 8. Otras mediciones del núcleo (vienen de Open Questions de Tiradas)

- Proporción de Cartas Únicas de sí o no resueltas con una palabra ambigua; si pasa del 50 %, Resonancia no cumple R11a (E8).
- Con 10 a 14 UT, la Carta Única sin aclaratoria posible justo cuando la carta puede salir muda (umbral de impuesto de la aclaratoria, D-53).
- Si Carta Única + invertir (12 UT) o Carta Única + aclaratoria (15 UT) desplazan a Tres Tiempos (20 UT).
- Si la aclaratoria ciega rescata lo suficiente o el Pilar 6 necesita otra palanca.
- Qué porcentaje de jugadores elige la Carta Única sin mover el foco inicial (sesgo del selector).
