M,K,N=map(int,input().split())
c=list(map(int,input().split()))
tickets=[input() for i in range(M)]

def main():
    prefix_counts = {}
    for num in tickets:
        for l in range(1, K + 1):
            prefix = num[:l]
            if prefix not in prefix_counts:
                prefix_counts[prefix] = 0
            prefix_counts[prefix] += 1

    # 3. Жадный алгоритм с отсечением
    best = (float('inf'), None)

    def dfs(current, pos, total):
        nonlocal best

        if pos == K:
            if total < best[0] or (total == best[0] and current < best[1]):
                best = (total, current)
            return

        # 4. Приоритетный перебор цифр
        for d in sorted(str(i) for i in range(N)):
            new_prefix = current + d
            new_total = total

            # 5. Быстрый расчёт прироста стоимости
            for l in range(pos + 1):
                cnt = prefix_counts.get(new_prefix[:l + 1], 0)
                delta = c[l] - (c[l - 1] if l > 0 else 0)
                new_total += cnt * delta
                if new_total > best[0]:
                    break

            if new_total <= best[0]:
                dfs(new_prefix, pos + 1, new_total)

    dfs("", 0, 0)
    print(best[1])
    print(best[0])
main()