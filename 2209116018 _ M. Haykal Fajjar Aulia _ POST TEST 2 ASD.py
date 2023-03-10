listnya = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def jump_search(arr, x):
    # data list di flatten menjadi satu dimensi
    flaten_arr = [element for sublist in arr for element in (sublist if isinstance(sublist, list) else [sublist])]
    n = len(flaten_arr)
    step = int(n**0.5)
    prev = 0
    while flaten_arr[min(step, n)-1] < x:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    while flaten_arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if flaten_arr[prev] == x:
        # memetakan index kembali ke list bercabang yang original
        def map_index(index):
            for i, sublist in enumerate(arr):
                if isinstance(sublist, list):
                    if index < len(sublist):
                        return [i, index]
                    else:
                        index -= len(sublist)
                else:
                    if index == 0:
                        return i
                    else:
                        index -= 1
        return map_index(prev)
    return -1

# 1. Cari Arsel, Avivah, Daiva
print("1. {} di Index {}, {} di Index {}, {} di Index {}".format(
    listnya[0], jump_search(listnya, listnya[0]), 
    listnya[1], jump_search(listnya, listnya[1]), 
    listnya[2], jump_search(listnya, listnya[2])))

# 2. Cari Wahyu pada Index 3 di kolom 0
wahyu_idx = jump_search(listnya[3], "Wahyu")
print("2. Wahyu pada Index 3 di kolom 0" if wahyu_idx == 0 else "Tidak menemukan Wahyu pada Index 3 di kolom 0")

# 3. Cari Wibi pada Index 3 di kolom 1
wibi_idx = jump_search(listnya[3], "Wibi")
print("3. Wibi pada Index 3 di kolom 1" if wibi_idx == 1 else "Tidak menemukan Wibi pada Index 3 di kolom 1")