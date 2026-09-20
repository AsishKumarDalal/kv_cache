# IBM Campus Prep: 8-Week Roadmap (AI Engineer)

## 1. IBM Campus Process (typical for freshers)

| Round | Details |
|---|---|
| Coding test (HackerRank) | 2 coding questions, 55 min |
| English assessment | 10 questions, 10 min. Negative marking. Some drives add a spoken English test and a short essay |
| Group discussion | 12-14 candidates, 5-7 min, general or tech topics (campus drives only) |
| Technical + HR interview | Usually one combined round, 25-30 min: DSA, DBMS, OS, networking, OOP, projects, HR questions |

**Eligibility:** generally 60% / 6.0 CGPA and no active backlogs. Confirm with your placement cell.

**Note:** Most published details are for the Associate System Engineer role. Ask your placement cell for the exact JD of the AI Engineer role, since it may add ML/GenAI questions.

---

## 2. Weekly Plan

### Weeks 1-2: Foundation
- [ ] DSA: arrays, strings, hashing, two pointers, sorting, basic recursion (2-3 easy/medium problems daily)
- [ ] DBMS + SQL: joins, normalization, indexing, transactions
- [ ] English: 15 min daily (grammar, reading comprehension)
- [ ] Set up HackerRank account and get comfortable with its editor and I/O style

### Weeks 3-4: Core Coding + CS
- [ ] DSA: stacks, queues, linked lists, binary search, trees, basic DP (medium level)
- [ ] Timed practice: 2 problems in 55 min, once or twice a week
- [ ] OS: processes, threads, deadlocks, scheduling
- [ ] OOP concepts and networking basics (TCP/IP, HTTP, DNS)

### Weeks 5-6: AI Depth + Communication
- [ ] Transformers and attention, embeddings, RAG
- [ ] Fine-tuning vs prompting, evaluation metrics, overfitting, bias-variance
- [ ] IBM specifics: watsonx, Granite models, recent IBM AI work
- [ ] Prepare a 2-minute explanation for each project (problem, design choices, trade-offs, improvements)
- [ ] Prepare a spoken self-introduction
- [ ] 2 mock GDs per week (tech and current-affairs topics)

### Week 7: Mocks
- [ ] 3 full timed coding tests (55 min coding + 10 min English)
- [ ] 2 mock technical interviews (DSA, DBMS, OS, OOP, projects)
- [ ] Revise weak topics found in mocks

### Week 8: Polish
- [ ] 1-2 problems daily plus revision of notes
- [ ] HR answers: why IBM, strengths/weaknesses, a challenge you solved, 5-year goals
- [ ] Resume review: every line must be defensible in detail
- [ ] Rest well before the drive

---

## 3. Daily Split (about 3-4 hours)

| Time | Activity |
|---|---|
| 1.5 hr | DSA |
| 1 hr | CS fundamentals or AI topics |
| 30 min | English or GD practice |
| 30 min | Revision |

---

## 4. C++ Tips for the Coding Round

**STL to know cold**
- `vector`, `string`, `pair`, `sort` with custom comparators, `lower_bound` / `upper_bound`
- `unordered_map`, `unordered_set` (hashing); `map`, `set` (ordering)
- `stack`, `queue`, `deque`, `priority_queue` (min-heap: `priority_queue<int, vector<int>, greater<int>>`)
- `bitset`, `accumulate`, `reverse`, `next_permutation`

**Test habits**
- Add `ios::sync_with_stdio(false); cin.tie(nullptr);` for large inputs
- Use `long long` where sums or products can overflow
- Follow the exact input/output format (you write `main` yourself on HackerRank)
- Check edge cases: empty input, single element, all elements equal

**C++ interview topics**
- Virtual functions and vtables
- Constructors and destructors
- Copy vs move semantics
- Smart pointers
- `struct` vs `class`

Keep Python comfortable too, for ML/GenAI questions.

---

## 5. Checkpoints

- [ ] End of week 2: solving easy problems comfortably in C++
- [ ] End of week 4: 1 medium problem in about 25 min
- [ ] End of week 6: can explain every project and core GenAI concept out loud
- [ ] End of week 7: consistently solving 2 medium problems in 55 min

The coding round is the main filter, so give it the most time.
