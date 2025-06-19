
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Визуализация геометрических фигур")

fig_type = st.selectbox(
    "Выберите фигуру для отображения:",
    ("Круг", "Квадрат", "Треугольник")
)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

if fig_type == "Круг":
    circle = plt.Circle((0.5, 0.5), 0.4, color='skyblue')
    ax.add_patch(circle)
elif fig_type == "Квадрат":
    square = plt.Rectangle((0.1, 0.1), 0.8, 0.8, color='lightgreen')
    ax.add_patch(square)
elif fig_type == "Треугольник":
    triangle = plt.Polygon([[0.5, 0.9], [0.1, 0.1], [0.9, 0.1]], color='salmon')
    ax.add_patch(triangle)

st.pyplot(fig)

