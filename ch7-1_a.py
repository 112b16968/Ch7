# 匯入所需的模組
from matplotlib import pyplot as plt
from skimage import io
import numpy as np
from numpy.fft import fft2,fftshift , ifft2
# 讀取影像
cm = io.imread("engineer.png")
 # 對影像進行2D傅里葉變換，並使用fftshift將零頻率成分移動到頻譜中心
cf = fftshift(fft2(cm))
# 設定低通濾波器的截止頻率 d = 10
d = 10
# 創建一個範圍從 -128 到 127 的數字陣列（對應影像的頻率坐標）
ar = range(-128,128)
# 創建一個頻率網格，用來計算每個像素點的頻率
x , y = np.meshgrid(ar,ar)
# 計算每個頻率點到中心的距離，並根據距離生成濾波器
c = (x**2 + y**2 > d**2)*1

# 應用濾波器，將頻譜中小於截止頻率的部分保留，其它部分去除
cf1 = cf * (1-c)
# 對濾波後的頻譜進行反傅里葉變換，轉回空間域並取絕對值
cf1c = abs(ifft2(cf1))

# 顯示圖片
a = plt.figure()
plt.subplot(1, 1, 1)
plt.imshow( cf1c , cmap='gray')
plt.title('LOW')
plt.axis('off')

plt.show()
