# Cifras de cobertura de Cartas

> **Generado por `tools/balance/cobertura_cartas.py`. No editar a mano.**
> Fuente: `design/balance/cobertura-cartas-waite.md` (recuento con los 4 palos).
> Solo claras, solo Waite III §2 y §3, una sola lectura: cifras **pesimistas**
> y **sin valencia**, con `p_f` aproximado por la parte de cada familia en
> `Σ c_f` (Cartas F3). Se rehacen con el reconteo (Cartas, Open Questions).

## Por mazo (F2 a F4)

| Mazo | N | O | c_f (Emo/Bie/Con/Amb/Des) | Familias por orientación | P_pos | P_cero(1) | P_cero(3) | P_cero_corr(3) | Con aclaratoria `(1 − P_pos)²` | P_cero_corr(2) |
|---|---|---|---|---|---|---|---|---|---|---|
| copas | 36 | 72 | 22/19/22/20/12 | 1,32 | 0,274 | 0,726 | 0,383 | 0,387 | 0,527 | 0,529 |
| oros | 36 | 72 | 13/27/18/21/9 | 1,22 | 0,275 | 0,725 | 0,381 | 0,396 | 0,525 | 0,532 |
| espadas | 36 | 72 | 15/13/26/24/13 | 1,26 | 0,277 | 0,723 | 0,378 | 0,392 | 0,523 | 0,529 |
| bastos | 36 | 72 | 14/22/20/23/13 | 1,28 | 0,268 | 0,732 | 0,392 | 0,398 | 0,535 | 0,538 |
| copas+oros | 50 | 100 | 26/35/24/27/15 | 1,27 | 0,270 | 0,730 | 0,389 | 0,397 | 0,533 | 0,536 |
| copas+espadas | 50 | 100 | 28/21/32/30/19 | 1,30 | 0,270 | 0,730 | 0,389 | 0,394 | 0,533 | 0,535 |
| copas+bastos | 50 | 100 | 27/30/26/29/19 | 1,31 | 0,268 | 0,732 | 0,393 | 0,395 | 0,536 | 0,537 |
| oros+espadas | 50 | 100 | 19/29/28/31/16 | 1,23 | 0,260 | 0,740 | 0,405 | 0,411 | 0,547 | 0,550 |
| oros+bastos | 50 | 100 | 18/38/22/30/16 | 1,24 | 0,275 | 0,725 | 0,381 | 0,397 | 0,526 | 0,533 |
| espadas+bastos | 50 | 100 | 20/24/30/33/20 | 1,27 | 0,265 | 0,735 | 0,397 | 0,403 | 0,540 | 0,543 |
| copas+oros+espadas | 64 | 128 | 32/37/34/37/22 | 1,27 | 0,261 | 0,739 | 0,404 | 0,408 | 0,547 | 0,548 |
| copas+oros+bastos | 64 | 128 | 31/46/28/36/22 | 1,27 | 0,270 | 0,730 | 0,388 | 0,398 | 0,532 | 0,537 |
| copas+espadas+bastos | 64 | 128 | 33/32/36/39/26 | 1,30 | 0,264 | 0,736 | 0,399 | 0,401 | 0,542 | 0,543 |
| oros+espadas+bastos | 64 | 128 | 24/40/32/40/23 | 1,24 | 0,262 | 0,738 | 0,402 | 0,409 | 0,545 | 0,548 |
| copas+oros+espadas+bastos | 78 | 156 | 37/48/38/46/29 | 1,27 | 0,261 | 0,739 | 0,403 | 0,407 | 0,546 | 0,547 |

## Por familia: `P_fallo_f` = `P_cero_f(1)` y `P_cero_f(3)`

| Mazo | Emoción | Bienes | Conflicto | Ambición | Destino |
|---|---|---|---|---|---|
| copas | 0,694 / 0,335 | 0,736 / 0,399 | 0,694 / 0,335 | 0,722 / 0,377 | 0,833 / 0,579 |
| oros | 0,819 / 0,550 | 0,625 / 0,244 | 0,750 / 0,422 | 0,708 / 0,355 | 0,875 / 0,670 |
| espadas | 0,792 / 0,496 | 0,819 / 0,550 | 0,639 / 0,261 | 0,667 / 0,296 | 0,819 / 0,550 |
| bastos | 0,806 / 0,523 | 0,694 / 0,335 | 0,722 / 0,377 | 0,681 / 0,315 | 0,819 / 0,550 |
| copas+oros | 0,740 / 0,405 | 0,650 / 0,275 | 0,760 / 0,439 | 0,730 / 0,389 | 0,850 / 0,614 |
| copas+espadas | 0,720 / 0,373 | 0,790 / 0,493 | 0,680 / 0,314 | 0,700 / 0,343 | 0,810 / 0,531 |
| copas+bastos | 0,730 / 0,389 | 0,700 / 0,343 | 0,740 / 0,405 | 0,710 / 0,358 | 0,810 / 0,531 |
| oros+espadas | 0,810 / 0,531 | 0,710 / 0,358 | 0,720 / 0,373 | 0,690 / 0,329 | 0,840 / 0,593 |
| oros+bastos | 0,820 / 0,551 | 0,620 / 0,238 | 0,780 / 0,475 | 0,700 / 0,343 | 0,840 / 0,593 |
| espadas+bastos | 0,800 / 0,512 | 0,760 / 0,439 | 0,700 / 0,343 | 0,670 / 0,301 | 0,800 / 0,512 |
| copas+oros+espadas | 0,750 / 0,422 | 0,711 / 0,359 | 0,734 / 0,396 | 0,711 / 0,359 | 0,828 / 0,568 |
| copas+oros+bastos | 0,758 / 0,435 | 0,641 / 0,263 | 0,781 / 0,477 | 0,719 / 0,371 | 0,828 / 0,568 |
| copas+espadas+bastos | 0,742 / 0,409 | 0,750 / 0,422 | 0,719 / 0,371 | 0,695 / 0,336 | 0,797 / 0,506 |
| oros+espadas+bastos | 0,812 / 0,536 | 0,688 / 0,325 | 0,750 / 0,422 | 0,688 / 0,325 | 0,820 / 0,552 |
| copas+oros+espadas+bastos | 0,763 / 0,444 | 0,692 / 0,332 | 0,756 / 0,433 | 0,705 / 0,351 | 0,814 / 0,540 |

## Piso F2

- Con `q_mil` = 100: ningún mazo falla.
- El mínimo es Destino en oros: `c_f · 1000 / O` = 125 milésimos. Todos los mazos pasan con `q_mil` ≤ 125 y alguno falla desde 126.

## Cota de Carta Única

Si cada orientación de los palos cubriera las 3 familias de mayor `p_f` (R4), con `p_f` fijo y los Mayores como están (solo Waite: no cuenta *Book T* ni Mathers):

| Mazo | Aporte de los Mayores a P_pos | Techo de los palos | P_pos ≤ | P_cero(1) ≥ | Con aclaratoria ≥ |
|---|---|---|---|---|---|
| copas | 0,162 | 0,262 | 0,424 | 0,576 | 0,331 |
| oros | 0,166 | 0,292 | 0,457 | 0,543 | 0,294 |
| espadas | 0,169 | 0,278 | 0,447 | 0,553 | 0,306 |
| bastos | 0,164 | 0,275 | 0,439 | 0,561 | 0,315 |
| copas+oros | 0,116 | 0,388 | 0,504 | 0,496 | 0,246 |
| copas+espadas | 0,118 | 0,388 | 0,505 | 0,495 | 0,245 |
| copas+bastos | 0,115 | 0,368 | 0,483 | 0,517 | 0,267 |
| oros+espadas | 0,119 | 0,401 | 0,520 | 0,480 | 0,230 |
| oros+bastos | 0,117 | 0,406 | 0,523 | 0,477 | 0,227 |
| espadas+bastos | 0,119 | 0,384 | 0,502 | 0,498 | 0,248 |
| copas+oros+espadas | 0,091 | 0,438 | 0,529 | 0,471 | 0,222 |
| copas+oros+bastos | 0,090 | 0,455 | 0,545 | 0,455 | 0,207 |
| copas+espadas+bastos | 0,091 | 0,427 | 0,518 | 0,482 | 0,233 |
| oros+espadas+bastos | 0,092 | 0,462 | 0,554 | 0,446 | 0,199 |
| copas+oros+espadas+bastos | 0,074 | 0,479 | 0,553 | 0,447 | 0,200 |

## Sin reposición (F4, supuestos)

Probabilidad de que ninguna de `k` cartas tenga la familia, con reposición y en los dos extremos sin reposición (todo o nada: `u_f` = `q_f`; mitad: `u_f` = 2·`q_f`). Mayor diferencia entre familias de cada mazo Aprendiz.

| Mazo | k | Familia | Con reposición | Todo o nada | Mitad | Diferencia máxima |
|---|---|---|---|---|---|---|
| copas | 3 | Emoción | 0,335 | 0,322 | 0,331 | 0,013 |
| copas | 10 | Destino | 0,162 | 0,118 | 0,145 | 0,043 |
| oros | 3 | Conflicto | 0,422 | 0,410 | 0,418 | 0,012 |
| oros | 10 | Conflicto | 0,056 | 0,033 | 0,049 | 0,023 |
| espadas | 3 | Ambición | 0,296 | 0,283 | 0,293 | 0,013 |
| espadas | 10 | Destino | 0,137 | 0,118 | 0,122 | 0,018 |
| bastos | 3 | Bienes | 0,335 | 0,322 | 0,331 | 0,013 |
| bastos | 10 | Emoción | 0,115 | 0,079 | 0,102 | 0,036 |

## Marca de progresión (producción)

Pares (mazo, Aprendiz de 1 palo que contiene) con `P_pos` del mazo menor que el del Aprendiz − `ε_prog` (0,005). No concluyente: la diferencia es del tamaño del error de la aproximación de `p_f`.

| Mazo | Aprendiz | P_pos mazo | P_pos Aprendiz |
|---|---|---|---|
| copas+oros | oros | 0,270 | 0,275 |
| copas+espadas | espadas | 0,270 | 0,277 |
| copas+bastos | copas | 0,268 | 0,274 |
| oros+espadas | oros | 0,260 | 0,275 |
| oros+espadas | espadas | 0,260 | 0,277 |
| espadas+bastos | espadas | 0,265 | 0,277 |
| copas+oros+espadas | copas | 0,261 | 0,274 |
| copas+oros+espadas | oros | 0,261 | 0,275 |
| copas+oros+espadas | espadas | 0,261 | 0,277 |
| copas+espadas+bastos | copas | 0,264 | 0,274 |
| copas+espadas+bastos | espadas | 0,264 | 0,277 |
| oros+espadas+bastos | oros | 0,262 | 0,275 |
| oros+espadas+bastos | espadas | 0,262 | 0,277 |
| oros+espadas+bastos | bastos | 0,262 | 0,268 |
| copas+oros+espadas+bastos | copas | 0,261 | 0,274 |
| copas+oros+espadas+bastos | oros | 0,261 | 0,275 |
| copas+oros+espadas+bastos | espadas | 0,261 | 0,277 |
| copas+oros+espadas+bastos | bastos | 0,261 | 0,268 |
