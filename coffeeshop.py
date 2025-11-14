h_list = []
d_list = []

with open("coffeeShopSales.txt", encoding="utf-8") as f:
    h_list = (f.readline().split())
    h_list.append("평균")
    h_list.append("합계")
    sum_list = []
    avg_list = []
    for line in f:
        temp_list = [int(data) for data in line.split() if data.isdigit()]
        temp_sum = sum(temp_list)
        temp_avg = round(temp_sum / len(temp_list), 2)
        temp_list.append(temp_avg)
        temp_list.append(temp_sum)
        for i in range(len(temp_list)):
            if len(sum_list) == i:
                sum_list.append(0)
            sum_list[i] += temp_list[i]
        d_list.append([line.split()[0], *temp_list])
    avg_list = [round(sum_data / len(d_list), 2) for sum_data in sum_list]
    d_list.append(["평균", *avg_list])
    d_list.append(["합계", *[round(sum_data, 2) for sum_data in sum_list]])
d_list.insert(0, h_list)
for row in d_list:
    print("\t".join([f"{str(data):<8}" for data in row]))

with open("coffeeShopSalesResult.txt", "w", encoding="utf-8") as f:
    for row in d_list:
        f.write("\t".join([f"{str(data):<8}" for data in row]) + "\n")
