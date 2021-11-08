def rod_cut(prices, v, cuts, n):
    for i in range(1, n):
        print("arr: " + str(v))
        m_v = -1000
        temp = 0
        for j in range(1, i):
            print("prices: " + str(prices[j]))
            print("val: " + str(v[i - j]))
            temp = prices[j] + v[i - j]
            if temp > m_v:
                cuts[i] = j
            print("m: " + str(m_v) + " t: " + str(temp))
            m_v = max(m_v, temp)
        v[i] = m_v

    return v

prices = [0,1,5,8,9,10,17,17,20,24]
n = len(prices)
cuts = [0 for x in range(n)]
v = [0 for x in range(n+1)]
v[0] = 0

rod_cut(prices, v, cuts, n)
print("Prices: " + str(prices))
print("Values: " + str(v))
print("Max value: " + str(v[n]))