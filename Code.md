# IBM DSA Practice List: 200 Problems

**Tags:** ⭐ = reported by candidates as an IBM-style question. 🔥 = classic must-do pattern that comes up across companies. Level: E = Easy, M = Medium, H = Hard.

**If you're short on time:** do all ⭐ (20) and 🔥 (46) problems first, then the rest. The list has 63 easy, 124 medium and 13 hard problems, matching IBM's easy-to-medium difficulty.

---

## 1. What IBM's coding round looks like (from research)

- **Platform and format:** HackerRank. Reported formats differ by drive: 2 coding questions in 55 min (with a 10 min English test), or up to 75 min with 3 problems plus a business-style SQL question. Confirm with your placement cell.
- **Difficulty:** Mostly easy to medium. Reports describe the first questions as warm-ups and the last as harder. Basic to intermediate DP does appear.
- **Languages:** C, C++, Java, Python are allowed.
- **No official question bank.** IBM doesn't publish past questions, and questions aren't repeated verbatim, but patterns repeat. Everything here comes from candidate-reported experiences, so treat it as a guide and not a guarantee.

## 2. Topics that show up most

| Priority | Topics |
|---|---|
| Very high | Arrays and hashing, strings, sliding window, sorting and searching |
| High | Recursion, stacks and queues, basic graphs (BFS/DFS, shortest path), prefix sums |
| Medium | Basic DP, linked lists, trees, math (GCD, primes), pattern printing |
| Some drives | SQL (joins, aggregation, window functions), string/log parsing |

Reported IBM-style questions (⭐ below) include:
- Find indices where a server load exceeds twice the average
- Convert a phone number spoken in words (with "double" / "triple") to digits
- Shortest subarray with exactly K distinct integers
- GCD of an array (return -1 if the GCD is 1)
- Count subarrays with sum divisible by K
- Stock buy/sell, largest palindromic substring, pangram check, word break, second largest element, print all duplicates
- Palindrome formed from substrings of two strings, pattern printing, simple if-else logic, and a shortest-path graph problem

## 3. Strategy for the test

1. **Read for 2 minutes first.** Note constraints (n up to 2×10⁵ means O(n log n) or better) and ask about edge cases: empty input, k = 0, all equal values.
2. **Solve the easy problem fast (about 10-15 min)** so you bank the marks, then give the rest of the time to the harder one.
3. **Brute force first, then optimise.** A passing brute force earns partial test cases, so submit it if you run out of time.
4. **Use `long long`** for sums and products, since overflow is a common cause of failed hidden test cases.
5. **Fast I/O:** `ios::sync_with_stdio(false); cin.tie(nullptr);`
6. **Test your own edge cases** before the final submit. Hidden test cases are where most marks are lost.
7. **Keep code readable.** Use clear variable names and short functions.
8. **Match the input format exactly.** HackerRank reads the format you're given, so parse carefully.

## 4. C++ STL cheat sheet

- `unordered_map` / `unordered_set` for hashing; `map` / `set` when you need order
- `priority_queue<int, vector<int>, greater<int>>` for a min-heap
- `sort` with a lambda comparator; `lower_bound` / `upper_bound`
- `accumulate`, `reverse`, `next_permutation`, `std::gcd`
- `deque` for sliding window maximum; `stack` / `queue` for the basics

## 5. Suggested schedule (fits your 8-week plan)

You've solved about 400 problems already, so easy ones should take only a few minutes. Aim for 4-6 problems a day, and write down the pattern for each one (for example "sliding window + frequency map"), since that is what transfers to unseen questions.

| Week | Sections | Problems |
|---|---|---|
| 1 | A. Arrays & Hashing | 37 |
| 2 | B. Strings | 28 |
| 3 | C. Sliding Window, D. Binary Search | 26 |
| 4 | E. Linked List, F. Stack & Queue, L. Math & Patterns | 38 |
| 5 | G. Trees, H. Graphs, I. Heap | 39 |
| 6 | J. Backtracking, K. DP | 32 |
| 7 | SQL bonus, timed re-solve of all ⭐ and 🔥 | mocks |
| 8 | Full timed mocks (2 problems in 55 min) and weak-spot revision | mocks |

---

## 6. The 200 problems

### A. Arrays & Hashing (37)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 1 | [ ] | Two Sum | E | 🔥 |
| 2 | [ ] | Best Time to Buy and Sell Stock | E | ⭐🔥 |
| 3 | [ ] | Contains Duplicate | E |  |
| 4 | [ ] | Maximum Subarray (Kadane) | M | ⭐🔥 |
| 5 | [ ] | Product of Array Except Self | M | 🔥 |
| 6 | [ ] | Move Zeroes | E |  |
| 7 | [ ] | Rotate Array | M |  |
| 8 | [ ] | Majority Element | E |  |
| 9 | [ ] | Find All Duplicates in an Array (print all duplicates) | M | ⭐ |
| 10 | [ ] | Missing Number | E |  |
| 11 | [ ] | Second Largest Element in an Array | E | ⭐ |
| 12 | [ ] | Subarray Sum Equals K | M | 🔥 |
| 13 | [ ] | Count Subarrays With Sum Divisible by K | M | ⭐ |
| 14 | [ ] | Merge Intervals | M | 🔥 |
| 15 | [ ] | Merge Sorted Array | E |  |
| 16 | [ ] | Container With Most Water | M |  |
| 17 | [ ] | 3Sum | M | 🔥 |
| 18 | [ ] | Top K Frequent Elements | M | 🔥 |
| 19 | [ ] | Group Anagrams | M | 🔥 |
| 20 | [ ] | Longest Consecutive Sequence | M | 🔥 |
| 21 | [ ] | Indices Where Server Load > 2x Average (use long long for the sum) | E | ⭐ |
| 22 | [ ] | GCD of an Array (return -1 if GCD is 1) | E | ⭐ |
| 23 | [ ] | Next Permutation | M |  |
| 24 | [ ] | Set Matrix Zeroes | M |  |
| 25 | [ ] | Trapping Rain Water | H |  |
| 26 | [ ] | Find Pivot Index | E |  |
| 27 | [ ] | Range Sum Query (prefix sums) | E |  |
| 28 | [ ] | Contiguous Array | M |  |
| 29 | [ ] | Longest Subarray With Sum K | M |  |
| 30 | [ ] | Majority Element II | M |  |
| 31 | [ ] | Intersection of Two Arrays II | E |  |
| 32 | [ ] | First Missing Positive | H |  |
| 33 | [ ] | Find the Duplicate Number | M |  |
| 34 | [ ] | K-diff Pairs in an Array | M |  |
| 35 | [ ] | Largest Number | M |  |
| 36 | [ ] | Insert Interval | M |  |
| 37 | [ ] | Non-overlapping Intervals (greedy) | M |  |

### B. Strings (28)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 38 | [ ] | Valid Palindrome | E |  |
| 39 | [ ] | Valid Anagram | E | 🔥 |
| 40 | [ ] | Longest Substring Without Repeating Characters | M | 🔥 |
| 41 | [ ] | Longest Palindromic Substring | M | ⭐🔥 |
| 42 | [ ] | Reverse Words in a String | M |  |
| 43 | [ ] | Check if a Sentence Is a Pangram | E | ⭐ |
| 44 | [ ] | Phone Number in Words to Digits (handle double / triple) | M | ⭐ |
| 45 | [ ] | Word Break (can string be built from a word list) | M | ⭐🔥 |
| 46 | [ ] | String Compression | M |  |
| 47 | [ ] | Longest Common Prefix | E |  |
| 48 | [ ] | Find First Occurrence of a Substring (KMP) | M |  |
| 49 | [ ] | Count and Say | M |  |
| 50 | [ ] | Caesar Cipher | E |  |
| 51 | [ ] | Roman to Integer | E |  |
| 52 | [ ] | Integer to Roman | M |  |
| 53 | [ ] | String to Integer (atoi) | M |  |
| 54 | [ ] | Isomorphic Strings | E |  |
| 55 | [ ] | Remove All Adjacent Duplicates in String | E |  |
| 56 | [ ] | Decode String | M |  |
| 57 | [ ] | Sort Characters by Frequency | M |  |
| 58 | [ ] | Palindrome Formed by Concatenating Substrings of Two Strings | M | ⭐ |
| 59 | [ ] | Rotate String (check rotation) | E |  |
| 60 | [ ] | Add Binary | E |  |
| 61 | [ ] | Multiply Strings | M |  |
| 62 | [ ] | Count Palindromic Substrings | M |  |
| 63 | [ ] | Find All Anagrams in a String | M |  |
| 64 | [ ] | Minimum Add to Make Parentheses Valid | M |  |
| 65 | [ ] | Length of Last Word | E |  |

### C. Sliding Window & Two Pointers (15)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 66 | [ ] | Minimum Size Subarray Sum | M | 🔥 |
| 67 | [ ] | Longest Repeating Character Replacement | M | 🔥 |
| 68 | [ ] | Minimum Window Substring | H | 🔥 |
| 69 | [ ] | Max Consecutive Ones III | M |  |
| 70 | [ ] | Fruit Into Baskets | M |  |
| 71 | [ ] | Shortest Subarray With Exactly K Distinct Integers (return -1 if none) | M | ⭐ |
| 72 | [ ] | Sliding Window Maximum | H |  |
| 73 | [ ] | Permutation in String | M |  |
| 74 | [ ] | Two Sum II (sorted input) | E |  |
| 75 | [ ] | Remove Duplicates from Sorted Array | E |  |
| 76 | [ ] | Sort Colors (Dutch flag) | M | 🔥 |
| 77 | [ ] | Longest Substring With At Most K Distinct Characters | M |  |
| 78 | [ ] | Longest Subarray of 1s After Deleting One Element | M |  |
| 79 | [ ] | Subarrays With K Different Integers | H |  |
| 80 | [ ] | Boats to Save People | M |  |

### D. Binary Search (11)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 81 | [ ] | Binary Search | E | 🔥 |
| 82 | [ ] | Search in Rotated Sorted Array | M | 🔥 |
| 83 | [ ] | Find Minimum in Rotated Sorted Array | M |  |
| 84 | [ ] | Find Peak Element | M |  |
| 85 | [ ] | First and Last Position of Element in Sorted Array | M |  |
| 86 | [ ] | Koko Eating Bananas | M |  |
| 87 | [ ] | Capacity to Ship Packages Within D Days | M |  |
| 88 | [ ] | Median of Two Sorted Arrays | H |  |
| 89 | [ ] | Sqrt(x) | E |  |
| 90 | [ ] | Search a 2D Matrix | M |  |
| 91 | [ ] | Split Array Largest Sum | H |  |

### E. Linked List (12)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 92 | [ ] | Reverse Linked List | E | 🔥 |
| 93 | [ ] | Merge Two Sorted Lists | E | 🔥 |
| 94 | [ ] | Linked List Cycle | E | 🔥 |
| 95 | [ ] | Remove Nth Node From End | M |  |
| 96 | [ ] | Middle of the Linked List | E |  |
| 97 | [ ] | Palindrome Linked List | E |  |
| 98 | [ ] | Add Two Numbers | M |  |
| 99 | [ ] | Reorder List | M |  |
| 100 | [ ] | Remove Duplicates from Sorted List | E |  |
| 101 | [ ] | Rotate List | M |  |
| 102 | [ ] | Intersection of Two Linked Lists | E |  |
| 103 | [ ] | Swap Nodes in Pairs | M |  |

### F. Stack & Queue (13)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 104 | [ ] | Valid Parentheses | E | 🔥 |
| 105 | [ ] | Min Stack | M | 🔥 |
| 106 | [ ] | Daily Temperatures | M | 🔥 |
| 107 | [ ] | Next Greater Element | E |  |
| 108 | [ ] | Evaluate Reverse Polish Notation | M |  |
| 109 | [ ] | Implement Queue Using Stacks | E |  |
| 110 | [ ] | Reverse a Queue (using a stack) | E | ⭐ |
| 111 | [ ] | Baseball Game | E |  |
| 112 | [ ] | Largest Rectangle in Histogram | H |  |
| 113 | [ ] | Asteroid Collision | M |  |
| 114 | [ ] | Online Stock Span | M |  |
| 115 | [ ] | Remove K Digits | M |  |
| 116 | [ ] | Implement Stack Using Queues | E |  |

### G. Trees (16)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 117 | [ ] | Binary Tree Traversals (in / pre / post order) | E | ⭐ |
| 118 | [ ] | Maximum Depth of Binary Tree | E |  |
| 119 | [ ] | Level Order Traversal | M | 🔥 |
| 120 | [ ] | Validate BST | M | 🔥 |
| 121 | [ ] | Lowest Common Ancestor | M | 🔥 |
| 122 | [ ] | Invert Binary Tree | E |  |
| 123 | [ ] | Diameter of Binary Tree | E |  |
| 124 | [ ] | Symmetric Tree | E |  |
| 125 | [ ] | Path Sum | E |  |
| 126 | [ ] | Kth Smallest Element in a BST | M |  |
| 127 | [ ] | Binary Tree Right Side View | M |  |
| 128 | [ ] | Construct Tree from Preorder and Inorder | M |  |
| 129 | [ ] | Zigzag Level Order Traversal | M |  |
| 130 | [ ] | Same Tree | E |  |
| 131 | [ ] | Subtree of Another Tree | E |  |
| 132 | [ ] | Balanced Binary Tree | E |  |

### H. Graphs (15)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 133 | [ ] | Number of Islands | M | 🔥 |
| 134 | [ ] | Flood Fill | E |  |
| 135 | [ ] | Rotting Oranges | M |  |
| 136 | [ ] | Clone Graph | M |  |
| 137 | [ ] | Course Schedule | M | 🔥 |
| 138 | [ ] | Shortest Path in Binary Matrix (BFS) | M |  |
| 139 | [ ] | Network Delay Time (Dijkstra shortest path) | M | ⭐🔥 |
| 140 | [ ] | Word Ladder | H |  |
| 141 | [ ] | Number of Provinces (connected components) | M |  |
| 142 | [ ] | Pacific Atlantic Water Flow | M |  |
| 143 | [ ] | Cheapest Flights Within K Stops | M |  |
| 144 | [ ] | Course Schedule II (topological sort) | M |  |
| 145 | [ ] | Surrounded Regions | M |  |
| 146 | [ ] | Is Graph Bipartite? | M |  |
| 147 | [ ] | Redundant Connection (Union-Find) | M |  |

### I. Heap / Priority Queue (8)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 148 | [ ] | Kth Largest Element in an Array | M | 🔥 |
| 149 | [ ] | K Closest Points to Origin | M |  |
| 150 | [ ] | Merge K Sorted Lists | H |  |
| 151 | [ ] | Find Median from Data Stream | H |  |
| 152 | [ ] | Task Scheduler | M |  |
| 153 | [ ] | Kth Smallest Element in a Sorted Matrix | M |  |
| 154 | [ ] | Top K Frequent Words | M |  |
| 155 | [ ] | Reorganize String | M |  |

### J. Recursion & Backtracking (12)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 156 | [ ] | Subsets | M | 🔥 |
| 157 | [ ] | Permutations | M | 🔥 |
| 158 | [ ] | Combination Sum | M | 🔥 |
| 159 | [ ] | Generate Parentheses | M |  |
| 160 | [ ] | Letter Combinations of a Phone Number | M |  |
| 161 | [ ] | N-Queens | H |  |
| 162 | [ ] | Palindrome Partitioning | M |  |
| 163 | [ ] | Pow(x, n) | M |  |
| 164 | [ ] | Tower of Hanoi | E |  |
| 165 | [ ] | Word Search | M |  |
| 166 | [ ] | Combination Sum II | M |  |
| 167 | [ ] | Restore IP Addresses | M |  |

### K. Dynamic Programming (20)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 168 | [ ] | Climbing Stairs | E | 🔥 |
| 169 | [ ] | House Robber | M | 🔥 |
| 170 | [ ] | Coin Change | M | 🔥 |
| 171 | [ ] | Longest Increasing Subsequence | M | 🔥 |
| 172 | [ ] | Longest Common Subsequence | M | 🔥 |
| 173 | [ ] | Edit Distance | H |  |
| 174 | [ ] | 0/1 Knapsack | M | 🔥 |
| 175 | [ ] | Partition Equal Subset Sum | M |  |
| 176 | [ ] | Unique Paths | M | 🔥 |
| 177 | [ ] | Minimum Path Sum | M |  |
| 178 | [ ] | Decode Ways | M |  |
| 179 | [ ] | Maximum Product Subarray | M |  |
| 180 | [ ] | Longest Palindromic Subsequence | M |  |
| 181 | [ ] | Best Time to Buy and Sell Stock II | M |  |
| 182 | [ ] | Jump Game | M |  |
| 183 | [ ] | Min Cost Climbing Stairs | E |  |
| 184 | [ ] | Triangle (minimum path sum) | M |  |
| 185 | [ ] | Perfect Squares | M |  |
| 186 | [ ] | Target Sum | M |  |
| 187 | [ ] | Maximal Square | M |  |

### L. Math, Bits, Matrix & Patterns (13)

| # | Done | Problem | Level | Tag |
|---|---|---|---|---|
| 188 | [ ] | Count Primes (Sieve) | M | 🔥 |
| 189 | [ ] | Reverse Integer | E |  |
| 190 | [ ] | Palindrome Number | E |  |
| 191 | [ ] | Armstrong Number / Sum of Digits | E | ⭐ |
| 192 | [ ] | Single Number (XOR) | E |  |
| 193 | [ ] | Number of 1 Bits | E |  |
| 194 | [ ] | Spiral Matrix | M | 🔥 |
| 195 | [ ] | Rotate Image | M | 🔥 |
| 196 | [ ] | Print Patterns (triangle, pyramid, hollow square) | E | ⭐ |
| 197 | [ ] | Queries on a Permutation (move-to-front) | M | ⭐ |
| 198 | [ ] | Largest of Three Numbers / Grade Categorization (if-else logic) | E | ⭐ |
| 199 | [ ] | Matrix Multiplication | E |  |
| 200 | [ ] | Happy Number | E |  |

---

## 7. Bonus: SQL practice (some IBM drives include it)

Reports mention business-style SQL with joins, aggregation, and window functions. Practise these on LeetCode SQL or HackerRank SQL:

- [ ] Second Highest Salary
- [ ] Nth Highest Salary
- [ ] Employees Earning More Than Their Managers (self join)
- [ ] Department Top 3 Salaries (`DENSE_RANK`)
- [ ] Duplicate Emails (`GROUP BY` + `HAVING`)
- [ ] Customers Who Never Ordered (`LEFT JOIN` + `IS NULL`)
- [ ] Rank Scores (`RANK` / `DENSE_RANK`)
- [ ] Consecutive Numbers / Running Total (`LAG`, `SUM() OVER`)
- [ ] Monthly Sales per Category (`GROUP BY` with dates)
- [ ] Delete Duplicate Rows (keep lowest id)

---

## 8. Progress tracker

| Week | Target | Solved | Timed 2-problem sessions passed |
|---|---|---|---|
| 1 | 37 | | |
| 2 | 28 | | |
| 3 | 26 | | |
| 4 | 38 | | |
| 5 | 39 | | |
| 6 | 32 | | |
| 7 | Mocks + SQL | | |
| 8 | Mocks + revision | | |
