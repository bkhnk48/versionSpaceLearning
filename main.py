# Import thư viện NumPy và đặt tên viết tắt là np
import numpy as np
# Import thư viện Pandas và đặt tên viết tắt là pd
import pandas as pd

# Đọc dữ liệu từ tệp CSV '2.csv' và lưu vào biến data
data = pd.read_csv('2.csv')
# Lấy các cột từ 0 đến cột cuối cùng trừ cột cuối cùng (target) và lưu vào biến concepts
concepts = np.array(data.iloc[:, 0:-1])
# Lấy cột cuối cùng (target) và lưu vào biến target
target = np.array(data.iloc[:, -1])

# Định nghĩa hàm learn với tham số concepts và target
def learn(concepts, target):
    # Sao chép giá trị của hàng đầu tiên trong concepts và lưu vào biến specific_h
    specific_h = concepts[0].copy()
    print("Khởi tạo specific_h \n", specific_h)
    
    # Khởi tạo ma trận general_h với kích thước bằng specific_h và tất cả phần tử đều là "?"
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("Khởi tạo general_h \n", general_h)

    # Duyệt qua từng hàng trong concepts
    for i, h in enumerate(concepts):
        # Nếu target là "yes"
        if target[i] == "yes":
            print("Nếu instance là Positive")
            # So sánh từng phần tử của h với specific_h
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        # Nếu target là "no"
        if target[i] == "no":
            print("Nếu instance là Negative")
            # So sánh từng phần tử của h với specific_h
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

        print("Bước {}".format(i + 1))
        print(specific_h)
        print(general_h)
        print("\n")
        print("\n")

    # Xác định các chỉ số của các hàng trong general_h có giá trị là ['?', '?', '?', '?', '?', '?']
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    # Loại bỏ các hàng có giá trị là ['?', '?', '?', '?', '?', '?'] khỏi general_h
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    # Trả về specific_h và general_h sau khi học
    return specific_h, general_h

# Gọi hàm learn với concepts và target
s_final, g_final = learn(concepts, target)

# In ra kết quả specific_h và general_h sau khi học
print("Specific_h cuối cùng:", s_final, sep="\n")
print("General_h cuối cùng:", g_final, sep="\n")
