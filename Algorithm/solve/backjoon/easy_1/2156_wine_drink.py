import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    wine_list = [int(sys.stdin.readline()) for _ in range(n)]
    wine_dp = [wine_list[0]]
    if len(wine_list) > 1:
        wine_dp.append(wine_list[0] + wine_list[1])

    if len(wine_list) > 2:
        wine_dp.append(max(wine_list[0] + wine_list[2], wine_list[1] + wine_list[2], wine_dp[1]))

    for i in range(3, n):
        first_case = wine_list[i] + wine_dp[i-2]
        second_case = wine_list[i] + wine_list[i-1] + wine_dp[i-3]
        third_case = wine_dp[i-1]
        wine_dp.append(max(first_case, second_case, third_case))

    print(max(wine_dp))
