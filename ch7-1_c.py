# 匯入所需的模組
from skimage import io
import numpy as np
from numpy import arange , exp
from numpy.fft import fft2,fftshift , ifft2
from skimage import exposure as ex
from matplotlib import pyplot as plt
# 讀取影像
cm = io.imread("engineer.png")
# 對影像進行 2D 傅里葉變換，並將零頻率成分移動到頻譜的中心
cf = fftshift(fft2(cm))
# 創建一個範圍從 -128 到 127 的數字陣列（對應影像的頻率坐標）
ar = arange(-128,128)
# 創建一個頻率網格，用來計算每個像素點的頻率
x , y = np.meshgrid(ar,ar)
# 設定高斯濾波器的標準差 sigma = 20
sigma = 20
# 定義高斯濾波器函數
g = exp(-(x**2+y**2)/sigma**2)
# 將低通濾波器的值縮放到最大值為 1
gL = g / g.max()
# 高通濾波器為 1 減去低通濾波器
gH = 1 - g /g.max()
# 將高斯低通濾波器應用到頻域圖像
cgL = cf * gL
# 將高斯高通濾波器應用到頻域圖像
cgH = cf * gH
#反傅里葉變換
lowpass_image = ex.rescale_intensity(abs(ifft2(cgL)), out_range=(0.0, 1.0))
highpass_image = ex.rescale_intensity(abs(ifft2(cgH)), out_range=(0.0, 1.0))
# 顯示影像
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(lowpass_image , cmap='gray')
plt.title('LOW')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(highpass_image , cmap='gray')
plt.title('HIGH')
plt.axis('off')
plt.show()