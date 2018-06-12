from PIL import Image
import matplotlib.pyplot as plt

# img = Image.open('longkui.jpg')
# plt.figure('longkui2')
# plt.imshow(img)
# plt.show()
# plt.axis('off')
# print(img.size)
# print(img.mode)
# print(img.format)

img = Image.open('longkui.jpg')
gray = img.convert('F')
# plt.figure("beauty")
# plt.imshow(gray, cmap='gray')
# plt.axis('off')
# plt.show()
r, g, b = img.split()
pic = Image.merge('RGB', (r, g, b))
plt.figure('longkui')

plt.subplot(2, 3, 1), plt.title('origin')
plt.imshow(img), plt.axis('off')

plt.subplot(2, 3, 2), plt.title('gray')
plt.imshow(gray, cmap='gray'), plt.axis('off')

plt.subplot(2, 3, 3), plt.title('merge')
plt.imshow(pic), plt.axis('off')

plt.subplot(2, 3, 4), plt.title('r')
plt.imshow(r, cmap='gray'), plt.axis('off')

plt.subplot(2, 3, 5), plt.title('g')
plt.imshow(g, cmap='gray'), plt.axis('off')

plt.subplot(2, 3, 6), plt.title('b')
plt.imshow(b, cmap='gray'), plt.axis('off')

plt.show()
dst = img.resize((128, 128))
dst = img.rotate(45)
