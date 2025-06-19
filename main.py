
coin_denomination_list = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(change: int) -> dict[int, int] :
  coins = coin_denomination_list[:]
  coins.sort(reverse=True)
  result = {}
  for coin in coins:
    count = change // coin
    if count > 0:
      result[coin] = count
      change -= coin * count
  return result

def find_min_coins(amount: int) -> dict[int, int]:
  coins = coin_denomination_list[:]
  coins.sort()
  dp = [float('inf')] * (amount + 1)
  dp[0] = 0
  coin_used = [0] * (amount + 1)

  for coin in coins:
    for x in range(coin, amount + 1):
      if dp[x - coin] + 1 < dp[x]:
        dp[x] = dp[x - coin] + 1
        coin_used[x] = coin

  result = {}
  while amount > 0:
    coin = coin_used[amount]
    result[coin] = result.get(coin, 0) + 1
    amount -= coin

  return result


if __name__ == '__main__':
    print('find_coins_greedy ',find_coins_greedy(113))
    print('find_min_coins', find_min_coins(115))