import matplotlib.pyplot as plt


strain = [0, 0.0001, 0.0002, 0.0004, 0.0008, 0.0013, 0.0015, 0.0018, 0.0020, 0.0023, 0.0026, 0.0032, 0.0036, 0.0040, 0.0044, 0.0048]
stress = [0.00, 2.26, 4.43, 6.58, 8.45, 11.82, 13.79, 15.83, 17.09, 19.23, 21.62, 24.36, 25.42, 27.68, 28.64, 28.41]
normalized_strain=[0, 0.018, 0.050, 0.101, 0.181, 0.295, 0.350, 0.407, 0.462, 0.522, 0.602, 0.741, 0.819, 0.920, 1.000, 1.103]
normalized_stress=[0.00,0.079,0.155, 0.230, 0.295, 0.413, 0.481, 0.553, 0.597, 0.671, 0.755, 0.851, 0.888, 0.966, 1.000, 0.992]


plt.subplot(1,2,1)
plt.plot(strain,stress ,color='red',label='stress vs strain curve',marker='o')
plt.grid(color='gray',linestyle=':',linewidth='1')
plt.legend(loc='upper left',fontsize=7)
plt.xlabel('strain')
plt.ylabel('stress')
plt.title(' stess vs  strain curve')

plt.subplot(1,2,2)
plt.plot(normalized_strain,normalized_stress, color='green',label='normalized_stress vs normalized_strain curve', marker='o')
plt.grid(color='gray',linestyle=':',linewidth='1')
plt.legend(loc='upper left',fontsize=7)
plt.xlabel('normalized_strain')
plt.ylabel('normalized_stress')
plt.title('Normalized stress vs normalized strain curve')
plt.tight_layout()
#plt.savefig("stress vs strain.jpg",dpi=300, bbox_inches='tight')
plt.show()