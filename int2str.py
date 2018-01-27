def encrypt(strs):
    spool = [
        'm047gl2foj',
        'wg3h0c32nl',
        'j6o3w8kclh',
        'tode62c4fi',
        'c9f5aeb62v',
        'kimtpltyaw',
        'pkn4clgasz',
        '3kf16cxi2h',
        'qo82ezx524',
        'ivb6ndxc47',
        's8p943ukhf',
        '09xzm5ru63',
        'wbyn60ai3d',
        'q7v9264mjl',
        'gh6jxkdabt',
        'kpo0ct1f6a'
    ]
    len_mask = '46a78fe94c352b2'
    strs = str(strs)

    if strs == '':
        return ''
    total_len = 16
    lens = len(strs)
    if (lens + 1) > total_len:
        return ''
    tmp = ''
    i = 0
    for i in range(0, lens):
        ss = spool[i]
        tmp = tmp+ss[int(strs[i])]

    last_char = strs[lens-1]

    for i in range(lens, (total_len-1)):
        sss = spool[int(last_char)]
        
        tmp = tmp+sss[i % 10]

    
    return tmp + len_mask[lens - 1]
