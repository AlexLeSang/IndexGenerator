
__author__ = 'varg'


def generate_index_list(n_req, dl_ccs):
    if n_req and dl_ccs:
        if dl_ccs > 1:
            l = [0] + range(1, dl_ccs)
            return _fit_to_len(l, n_req)

        return [0] * n_req


def _fit_to_len(l, n):
    if n < len(l):
        return l[0:n]

    else:
        old_l = l[1:len(l)]
        idx = 0
        while len(l) < n:
            l = l + [old_l[idx]]
            idx = (idx + 1) % len(old_l)

    return l


def test_given_none_none_returns_none():
    assert None == generate_index_list(None, None)


def test_given_n_req_1_dl_ccs_1_returns_zero_pcell():
    n_req = 1
    dl_ccs = 1
    assert [0] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_1_dl_ccs_2_returns_zero_pcell():
    n_req = 1
    dl_ccs = 2
    assert [0] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_2_dl_ccs_1_returns_zero_pcell_scell():
    n_req = 2
    dl_ccs = 1
    assert [0, 0] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_2_dl_ccs_2_returns_zero_pcell_scell():
    n_req = 2
    dl_ccs = 2
    assert [0, 1] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_3_dl_ccs_2_returns_zero_pcell_scell():
    n_req = 3
    dl_ccs = 2
    assert [0, 1, 1] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_3_dl_ccs_3_returns_zero_pcell_scell():
    n_req = 3
    dl_ccs = 3
    assert [0, 1, 2] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_4_dl_ccs_3_returns_zero_pcell_scell():
    n_req = 4
    dl_ccs = 3
    assert [0, 1, 2, 1] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_5_dl_ccs_3_returns_zero_pcell_scell():
    n_req = 5
    dl_ccs = 3
    assert [0, 1, 2, 1, 2] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_5_dl_ccs_4_returns_zero_pcell_scell():
    n_req = 5
    dl_ccs = 4
    assert [0, 1, 2, 3, 1] == generate_index_list(n_req, dl_ccs)


def test_given_n_req_2_dl_ccs_4_returns_zero_pcell_scell():
    n_req = 2
    dl_ccs = 4
    assert [0, 1] == generate_index_list(n_req, dl_ccs)
