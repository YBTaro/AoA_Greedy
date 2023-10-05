# AOA Greedy Algorithm
## Team Members
We are team34 with two members:
* Yu-Bo Chen (ID: )
    * Contributions:
        * yours
* Ting-Yi Li (ID: )
    * Contributions:
        * mine

## Greedy Strategies
### STRAT1
**i)** Algorithm design
- Sort bags by $numWorking$ in ascending order.
- For each iteration, add an extra device to the first bag, then sort it in the right place according to its new $numWorking$ value.

**ii)** Example: $b_1 = (3, 5), b_2 = (1, 3), k = 1$
- Following the strategy:
    - The original average percentage is around **46.7%**
    - According to the strategy, add an extra device to $b_2$
    - $b_2 = (2, 4)$, average percentage becomes around **55%**
- If the strategy is not followed, add this new device to $b1$ instead
    - $b_1 = (4, 6)$, average percentage becomes around **50%**
    - Since **55%** > **50%**, the strategy yields the optimal solution

**iii)** Counter Example: $b_1 = (2, 3), b_2 = (1, 100), k = 1$
- Following the strategy:
    - The original average percentage is around **33.8%**
    - According to the strategy, add an extra device to $b_2$
    - $b_2 = (2, 101)$, average percentage becomes around **34.3%**
- If the strategy is not followed, add this new device to $b_1$ instead
    - $b_1 = (3, 4)$, average percentage becomes around **70.8%**
    - Since **34.3%** < **70.8%**, the strategy does not yield the optimal solution

### STRAT2
**i)** Algorithm design
- Calculate $\dfrac{numWorking}{total}$ for every bag.
- Sort bags by $numWorking/total$ in ascending order.
- For each iteration, add an extra device to the first bag, then sort it in the right place according to its new $numWorking/total$ value.

**ii)** Example: $b_1 = (3, 5), b_2 = (2, 5), k = 1$
- Following the strategy:
    - The original average percentage is around **50%**
    - According to the strategy, add an extra device to $b_2$
    - $b_2 = (3, 6)$, average percentage becomes around **55%**
- If the strategy is not followed, add this new device to $b_1$ instead
    - $b_1 = (4, 6)$, average percentage becomes around **53.3%**
    - Since **55%** > **53.3%**, the strategy yields the optimal solution

**iii)** Counter Example: $b_1 = (2, 3), b_2 = (50, 100), k = 1$
- Following the strategy:
    - The original average percentage is around **58.3%**
    - According to the strategy, add an extra device to $b_2$
    - $b_2 = (51, 101)$, average percentage becomes around **58.6%**
- If the strategy is not followed, add this new device to $b_1$ instead
    - $b_1 = (3, 4)$, average percentage becomes around **62.5%**
    - Since **58.6%** < **62.5%**, the strategy does not yield the optimal solution

### STRAT3
**i)** Algorithm design
- Sort bags by $total$ in ascending order.
- For each iteration, add an extra device to the first bag, then sort it in the right place according to its new $total$ value.

**ii)** Example: $b_1 = (1, 5), b_2 = (1, 6), k = 1$
- Following the strategy:
    - The original average percentage is around **18.3%**
    - According to the strategy, add an extra device to $b_1$
    - $b_1 = (2, 6)$, average percentage becomes around **25%**
- If the strategy is not followed, add this new device to $b_2$ instead
    - $b_2 = (2, 7)$, average percentage becomes around **24.3%**
    - Since **25%** > **24.3%**, the strategy yields the optimal solution

**iii)** Counter Example: $b_1 = (4, 5), b_2 = (1, 10), k = 1$
- Following the strategy:
    - The original average percentage is around **45%**
    - According to the strategy, add an extra device to $b_1$
    - $b_2 = (5, 6)$, average percentage becomes around **46.7%**
- If the strategy is not followed, add this new device to $b_2$ instead
    - $b_1 = (2, 11)$, average percentage becomes around **49.1%**
    - Since **46.7%** < **49.1%**, the strategy does not yield the optimal solution

### STRAT4
**i)** Algorithm design
- Calculate $\dfrac{numWorking+1}{total+1}-\dfrac{numWorking}{total}$ for every bag.
- Sort bags by $\dfrac{numWorking+1}{total+1}-\dfrac{numWorking}{total}$ in ascending order.
- For each iteration, add an extra device to the first bag, then sort it in the right place according to its new $\dfrac{numWorking+1}{total+1}-\dfrac{numWorking}{total}$ value.

**ii)** Example: $b_1 = (3, 5), b_2 = (2, 5), k = 1$
- Following the strategy:
    - The original average percentage is around **50%**
    - According to the strategy, add an extra device to $b_2$
    - $b_2 = (3, 6)$, average percentage becomes around **55%**
- If the strategy is not followed, add this new device to $b_1$ instead
    - $b_1 = (4, 6)$, average percentage becomes around **53.3%**
    - Since **55%** > **53.3%**, the strategy yields the optimal solution

**iii)** Prove it's optimal
* Everytime when a new device is added to one of the bags, the change in average percentage, namely $\Delta avg$, is as followed:
    * Suppose the chosen bag is $b_j$
    * $\Delta avg = \dfrac{1}{n}(\sum\limits_{i = 1, i \ne j}^n{\dfrac{numWorking_i}{total_i}} + \dfrac{numWorking_j+1}{total_j+1})-\dfrac{1}{n}\sum\limits_{i = 1}^n{\dfrac{numWorking_i}{total_i}} \\ = \dfrac{1}{n}(\dfrac{numWorking_j+1}{total_j+1}-\dfrac{numWorking_j}{total_j})$
    * Therefore, maximize $\dfrac{numWorking_j+1}{total_j+1}-\dfrac{numWorking_j}{total_j}$ in order to get the optimal solution.