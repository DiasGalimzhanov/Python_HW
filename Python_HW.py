
def problem_01():
    nums = list(map(int, input().split()))
    nums.sort()

    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    unique_num = list(counts.keys())
    unique_num.sort()

    frequencies = [counts[num] for num in unique_num]

    total_sum = 0
    frequency_sum = 0

    for num, freq in zip(unique_num, frequencies):
        total_sum += num * freq
        frequency_sum += freq

    average = total_sum / frequency_sum

    output_frequencies = " ".join(str(freq) for freq in frequencies)
    output_average = str(average)

    print(output_frequencies + "\n" + output_average)

problem_01()

def problem_02():
    nums = list(map(int, input().split()))
    res = []
    for i in nums:
        if i == 2:
            res.append(3)
        else:
            res.append(i)
    print(res)

problem_02()

