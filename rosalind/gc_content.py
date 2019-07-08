def gc_con():
    tot = {}
    with open('/Users/ioneliabuzatu/Downloads/rosalind_gc.txt', 'r') as file:  # /Users/ioneliabuzatu/Downloads/rosalind_gc.txt
        f = file.read()
        fasta = 0
        l = len(f.split('>'))
        gc = [0 for i in range(l)]
        for seq in f.split('>'):
            for g in seq.split(' '):
                g = g.split(' ')
                g = [i.strip() for i in g]
                g = g[0].split('\n')
                id = g[0]
                tot[id] = 0
                g = g[1:]
                # print(g)
                for k in g:
                    for j in k:
                        if j == 'C' or j == 'G':
                            tot[id] += 1
                        gc[fasta] += 1
            fasta += 1

    return tot, gc


def max_content_gc(tot, gc):
    max_content = ['', 0]
    for t, gc in zip(tot.items(), gc):
        id = t[0]
        len_seq = t[1]
        # print(id, len_seq, gc)
        try:
            gc_content = (len_seq / gc) * 100
            print(gc_content)
            if (len_seq / gc) * 100 > max_content[1]:
                max_content[0], max_content[1] = id, gc_content
        except:
            continue
    return max_content


total_len, gc = gc_con()
print(max_content_gc(total_len, gc))
