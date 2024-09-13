def trial_division(n):
  """
  与えられた整数の素因数分解を試し割り法で行う。

  Args:
    n: 素因数分解したい整数

  Returns:
    nの素因数分解結果をリストで返す。
  """
  if n <= 1:
    return []
  result = []
  i = 2
  while i * i <= n:
    while n % i == 0:
      result.append(i)
      n //= i
    i += 1
  result.append(n)
  return result

# 例

n = 60
factors = trial_division(n)
print(f"{n}の素因数分解: {factors}")


