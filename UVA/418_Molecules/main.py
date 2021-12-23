from sys import stdin
from itertools import permutations

def iter_word_groups():
    lines = [line.strip()[1:-1] for line in stdin.readlines()]
    for i in range(0, len(lines), 4):
        if not lines[i] or lines[i][0] == 'Q':
            break
        yield lines[i:i + 4]

def _find_max_area_arrangement(words):
    vl, vr, ht, hb = words
    max_area = 0

    for vl_p, vl_c in enumerate(vl):
        for ht_p, ht_c in enumerate(ht):
            if vl_c != ht_c:
                continue

            for vr_p, vr_c in enumerate(vr):
                for ht_p_vr in range(ht_p + 2, len(ht)):
                    if vr_c != ht[ht_p_vr]:
                        continue

                    horizontal_size = ht_p_vr - ht_p - 1
                    vl_p_s, vr_p_s = vl_p + 2, vr_p + 2
                    vl_rem_len = len(vl) - vl_p_s
                    vr_rem_len = len(vr) - vr_p_s
                    n_hb_iters = min(vl_rem_len, vr_rem_len)

                    step = horizontal_size + 1
                    for vl_vr_rel_p in range(n_hb_iters):
                        vl_c_hb = vl[vl_p_s + vl_vr_rel_p]
                        vr_c_hb = vr[vr_p_s + vl_vr_rel_p]

                        for hb_p_l in range(len(hb) - step):
                            hb_p_r = hb_p_l + step
                            if hb[hb_p_l] == vl_c_hb and hb[hb_p_r] == vr_c_hb:
                                vertical_size = vl_vr_rel_p + 1
                                area = horizontal_size * vertical_size
                                max_area = max(max_area, area)

    return max_area

def find_max_area_arrangement(words):
    return max(map(_find_max_area_arrangement, permutations(words)))

print("\n".join(map(str, map(find_max_area_arrangement, iter_word_groups()))))
