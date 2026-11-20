from atcoder.lazysegtree import LazySegTree


def _query_nodes(lst: "LazySegTree", ql: int, qr: int) -> list[int]:
    """prod(ql, qr) が採用するノードを左から右の順で返す"""
    l, r = ql + lst._size, qr + lst._size
    left, right = [], []

    while l < r:
        if l & 1:
            left.append(l)
            l += 1

        if r & 1:
            r -= 1
            right.append(r)

        l >>= 1
        r >>= 1

    return left + right[::-1]

def _print_panel(length: int = 40) -> None:
    print("-" * length)

def dump_raw(lst):
    """内部配列 _d / _lz をそのまま表示"""

    size = lst._size

    _print_panel()
    print("LazySegTree Raw")
    print(f"_n={lst._n}  _size={size}  _log={lst._log}")
    print()

    d_w = max(len(str(x)) for x in lst._d)
    lz_w = max(len(str(x)) for x in lst._lz)

    print(
        f"{'k':>3} "
        f"{'range':>12} "
        f"{'d':>{d_w}} "
        f"{'lz':>{lz_w}}"
    )

    for k in range(1, 2 * size):

        dep = k.bit_length() - 1
        seg = size >> dep

        l = (k - (1 << dep)) * seg
        r = l + seg

        if k < size:
            mark = " *" if lst._lz[k] != lst._id else ""

            print(
                f"{k:>3} "
                f"[{l:>3},{r:<3}) "
                f"{str(lst._d[k]):>{d_w}} "
                f"{str(lst._lz[k]):>{lz_w}}{mark}"
            )

        else:

            pad = " (pad)" if l >= lst._n else ""

            print(
                f"{k:>3} "
                f"[{l:>3},{r:<3}) "
                f"{str(lst._d[k]):>{d_w}}{pad}"
            )

    _print_panel()

def dump_values(lst):
    """実際の値"""

    vals = [lst.get(i) for i in range(lst._n)]

    _print_panel()
    print("Values")

    print(
        "idx :",
        *[f"{i:>4}" for i in range(lst._n)]
    )

    print(
        "val :",
        *[f"{x:>4}" for x in vals]
    )

    _print_panel()

def dump(
    lst: "LazySegTree",
    ql: int | None = None,
    qr: int | None = None,
    max_depth: int | None = None,
) -> None:
    """木構造表示"""

    size = lst._size
    n = lst._n

    has_query = ql is not None and qr is not None

    if has_query:
        selected = set(_query_nodes(lst, ql, qr))
    else:
        selected = set()

    d_w = max(len(str(x)) for x in lst._d)

    def dfs(k, l, r, prefix="", last=True):
        depth = k.bit_length() - 1

        head = ""
        if k != 1:
            head = prefix + ("└─ " if last else "├─ ")

        mark = []

        if k in selected:
            mark.append("@")

        if k < size:
            if lst._lz[k] != lst._id:
                mark.append("L")
            lazy = f" lz={lst._lz[k]}"
        else:
            lazy = ""

        if k >= size:
            if has_query and ql <= l < qr:
                mark.append("*")

            if l >= n:
                mark.append("(pad)")

        marks = ""
        if mark:
            marks = " " + "".join(mark)

        print(
            f"{head}"
            f"#{k} [{l},{r}) "
            f"= {str(lst._d[k]):>{d_w}}"
            f"{lazy}"
            f"{marks}"
        )

        if k >= size:
            return

        if max_depth is not None and depth >= max_depth:
            print(prefix + "   └─ ...")
            return

        child = prefix if k == 1 else prefix + ("   " if last else "│  ")

        m = (l + r) // 2

        dfs(k * 2, l, m, child, False)
        dfs(k * 2 + 1, m, r, child, True)

    _print_panel()

    if has_query:
        print(
            f"query=[{ql},{qr}) "
            f"@:prod node "
            f"*:leaf "
            f"L:lazy exists"
        )

    dfs(1, 0, size)

    _print_panel()

def dump_max_right(lst, l, f):

    r = lst.max_right(l, f)

    _print_panel()
    print(f"max_right({l}) = {r}")

    start = l
    end = min(lst._n, r + 1)

    for i in range(start, end + 1):

        x = lst.prod(l, i)

        print(
            f"prod([{l},{i})) = {x} -> {f(x)}"
            + (" <==" if i == r else "")
        )

    _print_panel()

def dump_min_left(lst, r, f):

    l = lst.min_left(r, f)

    _print_panel()
    print(f"min_left({r}) = {l}")

    begin = max(0, l - 1)

    for i in range(begin, r + 1):

        x = lst.prod(i, r)

        print(
            f"prod([{i},{r})) = {x} -> {f(x)}"
            + (" <==" if i == l else "")
        )

    _print_panel()
