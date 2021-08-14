#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021/8/14 16:51
# @File     : tanabata.py
# @Project  : main.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.font_manager import FontProperties

fig = plt.figure(figsize=(8, 8))
ax = fig.gca(projection='3d')
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 580, 0.5) / 575 * 30 * np.pi - 10*np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
change = np.sin(20*t)/50
u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2 + change
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p)) * 1.5
h = u * (x * np.cos(p) - y * np.sin(p))
c = plt.get_cmap('magma')
surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1,
                       cmap=c, linewidth=0, antialiased=True)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

plt.axis('off')

font_set = FontProperties(fname=r"ArchitectsDaughter-Regular.ttf", size=30)
# Font Download：https://fonts.wr0926.ml/share?selection.family=Sigmar%20One
plt.title('While (Life < End) {\n OrangeCH3 @ SunLin;\n Love++;\n }', fontproperties=font_set, y=-0.1)
plt.show()
