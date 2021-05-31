def init_dp(m:int,n:int):
    t = [[0 for j in range(0,n+1)]for i in range(0,m+1)]
    return t

def get_minimun_coin(t,coin_arr,s):
    for i in range(1,len(coin_arr)+1):
        for j in range(1,s+1):
            if i == 1:
                if coin_arr[i-1] <= j:
                    t[i][j] = j//coin_arr[i-1] + t[i][j%coin_arr[i-1]]
                else:
                    t[i][j] = t[i-1][j]
            if i != 1:
                if coin_arr[i-1] <=j:
                    t[i][j] = min((j//coin_arr[i-1] + t[i][j%coin_arr[i-1]]),t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
    return t[len(coin_arr)][s]


if __name__ == "__main__":
    coin_arr = [1,8,3,6,5]
    s = 7
    t = init_dp(len(coin_arr),s)
    min_coin_no = get_minimun_coin(t,coin_arr,s)
    print(min_coin_no)