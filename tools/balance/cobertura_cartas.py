"""Cifras de cobertura de la Base de Datos de Cartas (F2 a F4) por mazo alcanzable.

Uso: python3 tools/balance/cobertura_cartas.py [--out RUTA]

Calcula, para los 15 mazos alcanzables (22 Mayores más 1 a 4 palos), las cifras
que el GDD de Cartas cita en vez de escribir la aritmética en prosa: piso F2,
P_pos, P_cero(k), P_cero_corr(k), P_cero_f(k), la carta aclaratoria, la cota de
Carta Única, el efecto de sacar sin reposición y la marca de progresión.

Los conteos salen de design/balance/cobertura-cartas-waite.md (recuento con los
4 palos): solo palabras clave claras, solo Waite III §2 y §3, una sola lectura.
Si cambian allí, cambian aquí. Como el conteo no tiene n_t por tema, p_f se
aproxima por la parte de cada familia en la suma de c_f (Cartas F3), y las
cifras son de P_pos (solo claras), no de P_pos⁺. Sin valencia.

Por defecto escribe design/balance/cifras-cartas.md. No editar ese archivo a mano.
"""

import argparse
from itertools import combinations
from math import comb

FAMILIAS = ("Emoción", "Bienes", "Conflicto", "Ambición", "Destino")
PALOS = ("copas", "oros", "espadas", "bastos")  # orden canónico de R13

# c_f por bloque: orientaciones con al menos una palabra clave clara de la familia.
C_BLOQUE = {
    "mayores": (9, 11, 16, 14, 6),
    "copas": (13, 8, 6, 6, 6),
    "bastos": (5, 11, 4, 9, 7),
    "espadas": (6, 2, 10, 10, 7),
    "oros": (4, 16, 2, 7, 3),
}
CARTAS_BLOQUE = {"mayores": 22, "copas": 14, "oros": 14, "espadas": 14, "bastos": 14}

Q_MIL = 100          # piso de F2, en milésimos (Tuning Knobs)
EPS_PROG = 0.005     # margen de la marca de progresión (Tuning Knobs)
K_TIRADAS = (1, 3)   # Carta Única y Tres Tiempos
K_LARGO = 10         # para mostrar cómo crece el efecto de la reposición
DEST = FAMILIAS.index("Destino")


def mazos():
    """Los 15 mazos alcanzables, como tuplas de palos en orden canónico."""
    return [p for r in range(1, 5) for p in combinations(PALOS, r)]


def nombre(mazo):
    return "+".join(mazo)


def conteos(mazo):
    """(N, O, c_f) del mazo: cartas, orientaciones y c_f por familia."""
    bloques = ("mayores",) + tuple(mazo)
    n = sum(CARTAS_BLOQUE[b] for b in bloques)
    c = tuple(sum(C_BLOQUE[b][i] for b in bloques) for i in range(len(FAMILIAS)))
    return n, 2 * n, c


def p_aprox(c):
    """p_f aproximado: parte de cada familia en la suma de c_f (F3)."""
    s = sum(c)
    return tuple(x / s for x in c)


def pasa_f2(c_f, o, q_mil=Q_MIL):
    """F2 en enteros: c_f · 1000 ≥ q_mil · O."""
    return c_f * 1000 >= q_mil * o


def p_pos(p, q):
    return sum(a * b for a, b in zip(p, q))


def potencia(x, k):
    """x^k por multiplicación repetida, igual en toda plataforma."""
    r = 1.0
    for _ in range(k):
        r *= x
    return r


def p_cero(pp, k):
    return potencia(1 - pp, k)


def p_cero_corr(p, q, k):
    return sum(a * potencia(1 - b, k) for a, b in zip(p, q))


def sin_reposicion_extremos(n, c_f, k):
    """P de que ninguna de k cartas distintas tenga la familia, en los dos extremos.

    Todo o nada: c_f/2 cartas tienen la familia en las dos orientaciones (u_f = q_f).
    Mitad: c_f cartas la tienen en una sola orientación (u_f = 2·q_f).
    """
    m = c_f // 2
    todo_o_nada = comb(n - m, k) / comb(n, k)
    mitad = sum(comb(c_f, j) * comb(n - c_f, k - j) * potencia(0.5, j)
                for j in range(k + 1)) / comb(n, k)
    return todo_o_nada, mitad


def cota_carta_unica(mazo):
    """Cota superior de P_pos si cada orientación de los palos cubriera las 3
    familias de mayor p_f (R4: como mucho 3 palabras clave), con p_f fijo."""
    _, o, c = conteos(mazo)
    p = p_aprox(c)
    aporte_mayores = sum(p[i] * C_BLOQUE["mayores"][i] for i in range(len(FAMILIAS))) / o
    o_palos = o - 2 * CARTAS_BLOQUE["mayores"]
    techo_palos = o_palos / o * sum(sorted(p, reverse=True)[:3])
    return aporte_mayores, techo_palos


def marcas_progresion(eps=EPS_PROG):
    """Pares (mazo, Aprendiz de 1 palo que contiene) con P_pos del mazo menor
    que P_pos del Aprendiz − eps (Cartas F4)."""
    pos = {}
    for m in mazos():
        _, o, c = conteos(m)
        pos[m] = p_pos(p_aprox(c), tuple(x / o for x in c))
    return [(m, (a,), pos[m], pos[(a,)]) for m in mazos() if len(m) >= 2
            for a in m if pos[m] < pos[(a,)] - eps - 1e-9]


def f(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


def informe():
    lineas = [
        "# Cifras de cobertura de Cartas",
        "",
        "> **Generado por `tools/balance/cobertura_cartas.py`. No editar a mano.**",
        "> Fuente: `design/balance/cobertura-cartas-waite.md` (recuento con los 4 palos).",
        "> Solo claras, solo Waite III §2 y §3, una sola lectura: cifras **pesimistas**",
        "> y **sin valencia**, con `p_f` aproximado por la parte de cada familia en",
        "> `Σ c_f` (Cartas F3). Se rehacen con el reconteo (Cartas, Open Questions).",
        "",
        "## Por mazo (F2 a F4)",
        "",
        "| Mazo | N | O | c_f (Emo/Bie/Con/Amb/Des) | Familias por orientación | P_pos | P_cero(1) | P_cero(3) | P_cero_corr(3) | Con aclaratoria `(1 − P_pos)²` | P_cero_corr(2) |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for m in mazos():
        n, o, c = conteos(m)
        p, q = p_aprox(c), tuple(x / o for x in c)
        pp = p_pos(p, q)
        lineas.append(
            f"| {nombre(m)} | {n} | {o} | {'/'.join(map(str, c))} | {f(sum(c) / o, 2)} | {f(pp)} "
            f"| {f(p_cero(pp, 1))} | {f(p_cero(pp, 3))} | {f(p_cero_corr(p, q, 3))} "
            f"| {f(p_cero(pp, 2))} | {f(p_cero_corr(p, q, 2))} |")

    lineas += ["", "## Por familia: `P_fallo_f` = `P_cero_f(1)` y `P_cero_f(3)`", "",
               "| Mazo | " + " | ".join(FAMILIAS) + " |",
               "|---|" + "---|" * len(FAMILIAS)]
    for m in mazos():
        _, o, c = conteos(m)
        celdas = [f"{f(1 - x / o)} / {f(p_cero(x / o, 3))}" for x in c]
        lineas.append(f"| {nombre(m)} | " + " | ".join(celdas) + " |")

    margenes = [(c[i] * 1000 // o, m, FAMILIAS[i]) for m in mazos()
                for _, o, c in [conteos(m)] for i in range(len(FAMILIAS))]
    peor = min(margenes)
    fallan = [(nombre(m), fam) for _, m, fam in margenes
              if not pasa_f2(conteos(m)[2][FAMILIAS.index(fam)], conteos(m)[1])]
    lineas += ["", "## Piso F2", "",
               f"- Con `q_mil` = {Q_MIL}: {'ningún mazo falla' if not fallan else 'fallan ' + str(fallan)}.",
               f"- El mínimo es {peor[2]} en {nombre(peor[1])}: `c_f · 1000 / O` = {peor[0]} milésimos. "
               f"Todos los mazos pasan con `q_mil` ≤ {peor[0]} y alguno falla desde {peor[0] + 1}."]

    lineas += ["", "## Cota de Carta Única", "",
               "Si cada orientación de los palos cubriera las 3 familias de mayor `p_f` (R4), con `p_f` fijo "
               "y los Mayores como están (solo Waite: no cuenta *Book T* ni Mathers):", "",
               "| Mazo | Aporte de los Mayores a P_pos | Techo de los palos | P_pos ≤ | P_cero(1) ≥ | Con aclaratoria ≥ |",
               "|---|---|---|---|---|---|"]
    for m in mazos():
        am, tp = cota_carta_unica(m)
        lineas.append(f"| {nombre(m)} | {f(am)} | {f(tp)} | {f(am + tp)} "
                      f"| {f(1 - am - tp)} | {f(p_cero(am + tp, 2))} |")

    lineas += ["", "## Sin reposición (F4, supuestos)", "",
               "Probabilidad de que ninguna de `k` cartas tenga la familia, con reposición y en los dos "
               "extremos sin reposición (todo o nada: `u_f` = `q_f`; mitad: `u_f` = 2·`q_f`). "
               "Mayor diferencia entre familias de cada mazo Aprendiz.", "",
               "| Mazo | k | Familia | Con reposición | Todo o nada | Mitad | Diferencia máxima |",
               "|---|---|---|---|---|---|---|"]
    for m in [x for x in mazos() if len(x) == 1]:
        n, o, c = conteos(m)
        for k in (3, K_LARGO):
            filas = []
            for i, cf in enumerate(c):
                con = p_cero(cf / o, k)
                ton, mit = sin_reposicion_extremos(n, cf, k)
                filas.append((con - ton, FAMILIAS[i], con, ton, mit))
            d, fam, con, ton, mit = max(filas)
            lineas.append(f"| {nombre(m)} | {k} | {fam} | {f(con)} | {f(ton)} | {f(mit)} | {f(d)} |")

    marcas = marcas_progresion()
    lineas += ["", "## Marca de progresión (producción)", "",
               f"Pares (mazo, Aprendiz de 1 palo que contiene) con `P_pos` del mazo menor que el del "
               f"Aprendiz − `ε_prog` ({f(EPS_PROG)}). No concluyente: la diferencia es del tamaño del "
               "error de la aproximación de `p_f`.", "",
               "| Mazo | Aprendiz | P_pos mazo | P_pos Aprendiz |", "|---|---|---|---|"]
    lineas += [f"| {nombre(m)} | {nombre(a)} | {f(pm)} | {f(pa)} |" for m, a, pm, pa in marcas]
    return "\n".join(lineas) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default="design/balance/cifras-cartas.md")
    args = ap.parse_args()
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(informe())
    print(f"Escrito {args.out}")


if __name__ == "__main__":
    main()
