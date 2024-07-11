while True:
    try:
        N = int(input())
        custoPorDia = int(input())
        receitas = [int(input()) for _ in range(N)]

        dp = [0] * (N + 1)

        for i in range(1, N + 1):
            max_lucro = 0
            for j in range(i):
                lucro_atual = sum(receitas[j:i]) - custoPorDia * (i - j)
                max_lucro = max(max_lucro, lucro_atual)
            dp[i] = max(dp[i - 1], max_lucro)

        print(dp[N])

    except EOFError:
        break
