
import math

def generate_ulam_sequence(a_start, b_start, n):
    """
    Generates an Ulam-like sequence of length n using the specialized 
    packed-bit/residue-based approach, starting with a_start and b_start.
    
    Returns:
        List[int]: A list of the n generated Ulam numbers.
    """
    # ---------------------------
    # 1) Configuration & globals
    # ---------------------------
    # We will store everything as local variables so the function is self-contained.
    # Adjust MAXN if needed. It must be at least 'n' and big enough to hold bit-packing.
    MAXN = max(2*n, 1000)  # a safety margin
    lamda = 2.44344296778474
    step  = 13.517831473

    # Arrays for the bit-packed approach
    arr_a = [0]*(MAXN + 1)    # stores offsets of Ulam numbers
    nx    = [0]*(MAXN + 1)    # next pointer (residue order)
    pv    = [0]*(MAXN + 1)    # previous pointer (residue order)
    
    # For storing whether a number is Ulam (bit-packed):
    k_size = (MAXN // 2) + 2
    arr_k  = [0]*k_size

    # We also maintain a small index array for residue ordering.
    nindex    = max(1, MAXN // 50)  # small index to help insertion
    index_arr = [0]*nindex

    # ---------------
    # 2) Subroutines
    # ---------------
    def mod_float(x, m):
        return x - m * math.floor(x / m)

    def set_ulam(x, idx):
        """
        Mark integer x as an Ulam number at index idx 
        and store offset into arr_a[idx].
        """
        m30 = x % 30
        d30 = x // 30
        arr_k[d30] |= (1 << m30)  # mark x as Ulam

        ground = int(idx * step)
        arr_a[idx] = x - ground   # store offset

    def get_ulam(idx):
        """
        Retrieve the integer value of the Ulam number at index idx,
        given the offset-based storage.
        """
        ground = int(idx * step)
        return ground + arr_a[idx]

    def is_ulam(x):
        """
        Check if x is marked as an Ulam number in the bit-packed array.
        """
        m30 = x % 30
        d30 = x // 30
        if d30 < 0 or d30 >= len(arr_k):
            return False
        return (arr_k[d30] & (1 << m30)) != 0

    def init_arrays():
        """Reset all arrays before generating a new sequence."""
        for i in range(len(arr_k)):
            arr_k[i] = 0
        for i in range(len(nx)):
            nx[i] = 0
            pv[i] = 0
            if i < len(arr_a):
                arr_a[i] = 0
        for i in range(len(index_arr)):
            index_arr[i] = 0

    def set_links(idx):
        """
        Insert Ulam number at index idx into the linked list 
        ordered by residue mod lamda.
        """
        rdn = mod_float(get_ulam(idx), lamda) / lamda
        j = int(nindex * rdn)
        pvi = index_arr[j]
        while True:
            i = nx[pvi]
            ai = get_ulam(i)
            rdi = mod_float(ai, lamda) / lamda
            if i == 0 or rdi >= rdn:
                break
            pvi = i

        nxi = nx[pvi]
        pv[idx] = pvi
        nx[pvi] = idx
        nx[idx] = nxi
        pv[nxi] = idx

        j += 1
        while j < nindex:
            ai_j = get_ulam(index_arr[j])
            if mod_float(ai_j, lamda) / lamda >= rdn:
                break
            index_arr[j] = idx
            j += 1

    # ---------------------------------------------------
    # 3) Main generation logic, adapted from your script
    # ---------------------------------------------------
    if n <= 0:
        return []
    if n == 1 and a_start <= b_start:
        return [a_start]
    if n == 1:
        return [b_start]

    # 3.1) Initialize
    init_arrays()
    # The index array helps to locate where new items go in the residue chain.
    # We'll set index_arr[...] = 0 to start, which is a dummy node with no next or previous.
    # Then we set dummy Ulam(0) at index 0:
    set_ulam(0, 0)

    # 3.2) The first two real Ulam numbers: a_start at index=1, b_start at index=2
    set_ulam(a_start, 1)
    set_links(1)
    set_ulam(b_start, 2)
    set_links(2)

    # current_idx is how many actual Ulam numbers we have so far
    current_idx = 2

    # We'll choose the next candidate integer to be at least bigger 
    # than the largest of a_start, b_start.
    a0 = max(a_start, b_start) + 1

    # 3.3) Generate until we have n Ulam numbers (indexes 1..n).
    while current_idx < n:
        rd0 = mod_float(a0, lamda) / lamda
        # We'll see if a0 can be uniquely written as sum of two distinct existing Ulam #s

        # The code has two ways to check: a brute force if rd0 in extreme range,
        # plus scanning from smallest/largest residue. We'll do the same.

        more = True
        ulam_flag = False
        a1x = 0  # remember one addend from the first successful sum

        # If residue is in extreme range, do the "brute force" from the top.
        if rd0 < 0.24 or rd0 > 0.80:
            j = current_idx
            aj = get_ulam(j)
            while more and 2*aj > a0:
                if is_ulam(a0 - aj):
                    # Found a representation
                    if ulam_flag:  
                        # Found more than one representation: not unique
                        ulam_flag = False
                        more = False
                    else:
                        ulam_flag = True
                        a1x = a0 - aj
                j -= 1
                if j == 0:
                    break
                aj = get_ulam(j)
            # Either found a second representation or finished
            more = False

        # If not proven multiple or none yet, do the scanning from both ends:
        if more:
            # Scan from smallest residue upward
            i = nx[0]
            while i != 0 and more:
                ai = get_ulam(i)
                rdi = mod_float(ai, lamda) / lamda
                # If 2*rdi > rd0 + small_epsilon, break
                if 2*rdi > rd0 + 1e-4:
                    break
                a2 = a0 - ai
                if is_ulam(a2) and a2 != ai and a2 != a1x:
                    if ulam_flag:
                        # Found more than one representation
                        ulam_flag = False
                        more = False
                    else:
                        ulam_flag = True
                        a1x = ai
                i = nx[i]

            # Then scan from largest residue downward
            if more:
                i = pv[0]
                while i != 0 and more:
                    ai = get_ulam(i)
                    rdi = mod_float(ai, lamda) / lamda
                    if 2*(1.0 - rdi) > (1.0 - rd0) + 1e-4:
                        break
                    a2 = a0 - ai
                    if is_ulam(a2) and a2 != ai and a2 != a1x:
                        if ulam_flag:
                            ulam_flag = False
                            more = False
                        else:
                            ulam_flag = True
                            a1x = ai
                    i = pv[i]

        # If we found exactly one representation, add a0 as the next Ulam
        if ulam_flag:
            current_idx += 1
            set_ulam(a0, current_idx)
            set_links(current_idx)
        a0 += 1

        # Safety check in case we exceed array capacities
        if current_idx >= MAXN:
            break

    # -------------------------------------------------------------
    # 4) Gather the final sequence (indexes 1..n) and return
    # -------------------------------------------------------------
    # We only return as many as we actually got. 
    # If the method fails to find n distinct Ulam numbers, we'll return fewer.
    length = min(current_idx, n)
    result = [get_ulam(i) for i in range(1, length+1)]
    return result

def diff(s):
    return [s[i + 1] - s[i] for i in range(len(s) - 1)]

def ulam(a, b, n):
  upper = n
  upper *= 2
  V = [0]*upper
  W = [1]*upper
  V[a - 1] = 1
  V[b - 1] = 1
  W[a - 1] = 0
  W[b - 1] = 0
  k=2

  while True and k < upper/2:
    V[k:2*k-1] = [((not a) and b and c) or (a and (not b) and (not c)) or (a and (not b) and c) for a,b,c in zip(V[k:2*k-1], V[0:k-1], W[k:2*k-1])]
    W[k:2*k-1] = [(not a) and b for a,b in zip(V[0:k-1], W[k:2*k-1])]
    # print(V)
    L = [j for j in range(k+1,upper) if V[j-1] == 1]
    if L == []:
      break
    else:
      k = min(L)
  ls = [i+1 for i in range(0, len(V)) if V[i]==1]
  ls = ls[0:len(ls)//2]
  return ls
def solve(a, b, k):
    # For Ulam(2, 2k + 1) {k >= 2}, there is periodicity.
    assert(a == 2 and b & 1 and b >= 5)

    to_try, times_to_check, max_p_len = 500, 5, 240
    seq = generate_ulam_sequence(a, b, to_try) 
    d = diff(seq)
    rdiff = list(reversed(d))
    # Try different period lengths until we find 5 in a row. From this extrapolate to k = 10^11
    # print(d)
    p_len, inc = None, None
    while True:
        last_p_len = 10
        for p_len in range(last_p_len, max_p_len + 1):
            w = True
            for q in range(times_to_check):
                # print(rdiff[q * p_len:(q+1) * p_len], rdiff[(q+1) * p_len:(q+2) * p_len])
                if rdiff[q * p_len:(q+1) * p_len] != rdiff[(q+1) * p_len:(q+2) * p_len]:
                    w = False
                    break
            if w:
                inc = sum(rdiff[q * p_len:(q+1) * p_len])
                break
        if inc == None:
            # If didnt find anything mult all params and retry
            print("Period not found under to_try: {} and max_p_len: {}".format(to_try, max_p_len))
            last_p_len = max_p_len
            to_try *= 2
            max_p_len *= 2
            seq = generate_ulam_sequence(a, b, to_try) 
            d = diff(seq)
            rdiff = list(reversed(d))
        else:
            print("Found p_len: {} and inc: {}".format(p_len, inc))
            break
    final_el = seq[-1]
    curr_pos = len(seq)
    times = (k - curr_pos) // p_len
    final_el, curr_pos = final_el + inc * times, curr_pos + times * p_len
    i = len(d) - p_len
    while curr_pos != k:
        final_el += d[i]
        curr_pos += 1
        i += 1
    return final_el

tot = 0
for n in range(2, 10 + 1):
    print("Solving U(2, {})".format(2 * n + 1))
    tot += solve(2, 2 * n + 1, 10**11)
print(tot)
