import matplotlib.pyplot as plt 

input_values = range(1, 1001)
squares = [x**3 for x in input_values]

plt.style.use('seaborn-v0_8')
print(plt.style.available)
fig, ax = plt.subplots()
ax.scatter(input_values, squares, s=1, c=squares, cmap=plt.cm.Reds)

# ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)
# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style='plain')
plt.show()