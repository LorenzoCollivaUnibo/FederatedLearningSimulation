import matplotlib.pyplot as plt

from FLS1 import get_data1
from FLS2 import get_data2
from FLS3 import get_data3

client1, rounds1, accuracy1  = get_data1()
client2, rounds2, accuracy2 = get_data2()
client3, rounds3, accuracy3 = get_data3()

plt.figure(figsize=(8, 5))
plt.plot(rounds1, accuracy1, marker='o', linestyle='-', color='blue', label=f'Test Accuracy {client1} Clients')
plt.plot(rounds2, accuracy2, marker='o', linestyle='-', color='green', label=f'Test Accuracy Equal {client2} Clients')
plt.plot(rounds3, accuracy3, marker='o', linestyle='-', color='red', label=f'Test Accuracy Random {client3} Clients')
plt.xlabel('Round di Federated Learning')
plt.ylabel('Sparse Categorical Accuracy (%)')
plt.title(f"Andamento della Test Accuracy per ogni round di FederateLearning")
plt.grid(True)
plt.legend()
plt.savefig('test_accuracy_rounds.png')
plt.show()
