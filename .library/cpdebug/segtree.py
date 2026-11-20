from atcoder.segtree import SegTree


def _interval(size: int, k: int) -> tuple[int, int]:
    h = k.bit_length() - 1
    w = size >> h
    l = (k - (1 << h)) * w
    return l, l + w


def _query_nodes(sgt: "SegTree", ql: int, qr: int) -> list[int]:
    """prod(ql, qr) が採用するノードを左から右の順で返す"""
    l, r = ql + sgt._size, qr + sgt._size
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


def dump(
    sgt: "SegTree",
    ql: int | None = None,
    qr: int | None = None,
    max_depth: int | None = None,
) -> None:
    """
    SegTree の内部木を表示する。

    Parameters
    ----------
    sgt : SegTree
        ACL SegTree

    ql, qr : int | None
        指定時は prod(ql, qr) の情報を重ねて表示する。

    max_depth : int | None
        表示する最大深さ。
        指定した深さ以降は省略表示する。

    Marks
    -----
    @
        prod(ql, qr) が採用するノード

    *
        クエリ区間に含まれる葉

    (pad)
        ACL が内部的に追加したダミー葉

    Example
    -------
    >>> A = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> sgt = SegTree(lambda a, b: a + b, 0, A)
    >>> dump(sgt, 2, 7)

    ----------------------------------------
    query = [2,7)   @: used by prod   *: leaf in range
    #1 [0,8) = 36
    ├─ #2 [0,4) = 10
    │  ├─ #4 [0,2) =  3
    │  │  ├─ #8 [0,1) =  1
    │  │  └─ #9 [1,2) =  2
    │  └─ #5 [2,4) =  7 @
    │     ├─ #10 [2,3) =  3 *
    │     └─ #11 [3,4) =  4 *
    └─ #3 [4,8) = 26
       ├─ #6 [4,6) = 11 @
       │  ├─ #12 [4,5) =  5 *
       │  └─ #13 [5,6) =  6 *
       └─ #7 [6,8) = 15
          ├─ #14 [6,7) =  7 @*
          └─ #15 [7,8) =  8
    ----------------------------------------
    """
    size, n = sgt._size, sgt._n

    has_query = ql is not None and qr is not None

    if has_query:
        assert 0 <= ql <= qr <= n
        selected = set(_query_nodes(sgt, ql, qr))
    else:
        selected = set()

    val_w = max(
        (len(str(x)) for x in sgt._d[1:]),
        default=1,
    )

    def dfs(
        k: int,
        l: int,
        r: int,
        prefix: str,
        is_last: bool,
    ) -> None:
        depth = k.bit_length() - 1

        is_root = k == 1

        head = (
            ""
            if is_root
            else prefix + ("└─ " if is_last else "├─ ")
        )

        child_prefix = (
            prefix
            if is_root
            else prefix + ("   " if is_last else "│  ")
        )

        marks = []

        if k in selected:
            marks.append("@")

        if k >= size:
            if has_query and ql <= l < qr:
                marks.append("*")

            if l >= n:
                marks.append("(pad)")

        tail = (" " + "".join(marks)) if marks else ""

        print(
            f"{head}#{k} [{l},{r}) = "
            f"{str(sgt._d[k]):>{val_w}}{tail}"
        )

        if k >= size:
            return

        if max_depth is not None and depth >= max_depth:
            print(f"{child_prefix}└─ ...")
            return

        m = (l + r) // 2

        dfs(k * 2, l, m, child_prefix, False)
        dfs(k * 2 + 1, m, r, child_prefix, True)

    _print_panel()

    if has_query:
        print(
            f"query = [{ql},{qr})   "
            f"@: used by prod   "
            f"*: leaf in range"
        )

    dfs(1, 0, size, "", True)

    _print_panel()


def dump_max_right(
    sgt: "SegTree",
    left: int,
    f,
    op_name: str = "op",
) -> int:
    """
    max_right() の探索過程を表示する。

    Parameters
    ----------
    left : int
        探索開始位置

    f
        max_right に与える判定関数

    op_name : str
        ログ出力用の演算名

    Returns
    -------
    int
        max_right(left, f)

    Notes
    -----
    ログ中の

        op(*prev, node)

    は

        prev = 確定済み累積値
        node = 今回試すノード値

    を表す。

    max_right では

        op(prev, node)

    の順で評価される。

    Example
    -------
    >>> A = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> sgt = SegTree(lambda a, b: a + b, 0, A)
    >>> dump_max_right(sgt, 2, lambda x: x < 12)

    ----------------------------------------
    [2,4) (#5  )  op(*0, 7) = 7  -> True
    [2,8) (#3  )  op(*7, 26) = 33  -> False
    [2,6) (#6  )  op(*7, 11) = 18  -> False
    [2,5) (#12 )  op(*7, 5) = 12  -> False

    max_right(2) = 4
    ----------------------------------------
    """
    assert 0 <= left <= sgt._n
    assert f(sgt._e)

    logs = []

    if left == sgt._n:
        _print_panel()
        print(f"max_right({left}) = {sgt._n}")
        _print_panel()
        return sgt._n

    l = left + sgt._size
    sm = sgt._e

    while True:
        while l % 2 == 0:
            l >>= 1

        _, R = _interval(sgt._size, l)

        prod = sgt._op(sm, sgt._d[l])
        ok = f(prod)

        logs.append(
            (left, R, l, sm, sgt._d[l], prod, ok)
        )

        if not ok:
            while l < sgt._size:
                l <<= 1

                _, R = _interval(sgt._size, l)

                prod = sgt._op(sm, sgt._d[l])
                ok = f(prod)

                logs.append(
                    (left, R, l, sm, sgt._d[l], prod, ok)
                )

                if ok:
                    sm = prod
                    l += 1

            ans = l - sgt._size
            break

        sm = prod
        l += 1

        if (l & -l) == l:
            ans = sgt._n
            break

    _print_panel()
    print(f"max_right({left}) = {ans}")
    print()

    for L, R, k, prev, node, prod, ok in logs:
        print(
            f"[{L},{R}) "
            f"(#{k:<3})  "
            f"{op_name}(*{prev}, {node}) = {prod}  "
            f"-> {ok}"
        )

    _print_panel()

    return ans


def dump_min_left(
    sgt: "SegTree",
    right: int,
    f,
    op_name: str = "op",
) -> int:
    """
    min_left() の探索過程を表示する。

    Parameters
    ----------
    right : int
        探索終了位置

    f
        min_left に与える判定関数

    op_name : str
        ログ出力用の演算名

    Returns
    -------
    int
        min_left(right, f)

    Notes
    -----
    ログ中の

        op(node, *prev)

    は

        prev = 確定済み累積値
        node = 今回試すノード値

    を表す。

    min_left では

        op(node, prev)

    の順で評価される。

    非可換モノイドでも評価順を確認できる。

    Example
    -------
    >>> A = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> sgt = SegTree(lambda a, b: a + b, 0, A)
    >>> dump_min_left(sgt, 7, lambda x: x < 12)

    ----------------------------------------
    [6,7) (#14 )  op(7, *0) = 7  -> True
    [4,7) (#6  )  op(11, *7) = 18  -> False
    [5,7) (#13 )  op(6, *7) = 13  -> False

    min_left(7) = 6
    ----------------------------------------
    """
    assert 0 <= right <= sgt._n
    assert f(sgt._e)

    logs = []

    if right == 0:
        _print_panel()
        print("min_left(0) = 0")
        _print_panel()
        return 0

    r = right + sgt._size
    sm = sgt._e

    while True:
        r -= 1

        while r > 1 and (r & 1):
            r >>= 1

        L, _ = _interval(sgt._size, r)

        prod = sgt._op(sgt._d[r], sm)
        ok = f(prod)

        logs.append(
            (L, right, r, sgt._d[r], sm, prod, ok)
        )

        if not ok:
            while r < sgt._size:
                r = 2 * r + 1

                L, _ = _interval(sgt._size, r)

                prod = sgt._op(sgt._d[r], sm)
                ok = f(prod)

                logs.append(
                    (L, right, r, sgt._d[r], sm, prod, ok)
                )

                if ok:
                    sm = prod
                    r -= 1

            ans = r + 1 - sgt._size
            break

        sm = prod

        if (r & -r) == r:
            ans = 0
            break

    _print_panel()
    print(f"min_left({right}) = {ans}")
    print()

    for L, R, k, node, prev, prod, ok in logs:
        print(
            f"[{L},{R}) "
            f"(#{k:<3})  "
            f"{op_name}({node}, *{prev}) = {prod}  "
            f"-> {ok}"
        )
    _print_panel()

    return ans
