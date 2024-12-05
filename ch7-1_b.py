# 匯入所需的模組
from skimage import io
import numpy as np
from numpy import arange
from numpy.fft import fft2,fftshift , ifft2
from skimage import exposure as ex
from matplotlib import pyplot as plt
# 讀取影像
cm = io.imread("engineer.png")    
 # 對影像進行2D傅里葉變換，並使用fftshift將零頻率成分移動到頻譜中心
cf = fftshift(fft2(cm))          
# 創建一個範圍從 -128 到 127 的數字陣列（對應影像的頻率坐標）
ar = arange(-128,128)
# 創建一個頻率網格，用來計算每個像素點的頻率
x , y = np.meshgrid(ar,ar)
# 設定 Butterworth 濾波器的截止頻率 D = 15
D = 15
# 計算低通濾波器的頻率響應（Butterworth低通濾波器）
bL = 1.0 /(1.0+((x*x+y*y)/D**2)**2)
# 高通濾波器的頻率響應是低通濾波器的補數
bH = 1 - bL
cfbL = cf*bL
cfbH = cf*bH
# 反傅里葉變換，將頻域影像轉換回空間域
lowpass_image = ex.rescale_intensity(abs(ifft2(cfbL)), out_range=(0.0, 1.0))
highpass_image = ex.rescale_intensity(abs(ifft2(cfbH)), out_range=(0.0, 1.0))
#顯示
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