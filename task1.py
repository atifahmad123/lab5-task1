import numpy as np
import matplotlib.pyplot as plt


# Simulate 1000 rolls of a fair six-sided die.
rolls = np.random.randint(1, 7, size=1000)
print("First 10 rolls:", rolls[:10])

faces, counts = np.unique(rolls, return_counts=True)
face_counts = dict(zip(faces, counts))

print(f"{'Face':<6}{'Count':<8}{'Empirical P':<15}{'Theoretical P'}")
for face in range(1, 7):
    count = face_counts.get(face, 0)
    empirical_probability = count / 1000
    theoretical_probability = 1 / 6
    print(f"{face:<6}{count:<8}{empirical_probability:<15.3f}{theoretical_probability:.4f}")

# Center each histogram bin on one die face.
plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), edgecolor="black")
plt.xticks(range(1, 7))
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("1000 Rolls of a Fair Six-Sided Die")
plt.tight_layout()
plt.savefig("die_rolls.png")
plt.close()
print("Saved die_rolls.png")
