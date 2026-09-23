# Pyae Sone 6705140004


# Assignment 03 — CHANGES

**Name:** Pyae Sone **Student ID:** 6705140004

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|1|Products were stored as bare tuples such as ("Laptop", 1200.0, "electronics").|Created a Product class with name, price, and category attributes.|Classes / Encapsulation|Ran python Assignment_03.py → PASS|
| 2 | *e.g. repeated `if tier == ...` for discount and points* | *`Gold`/`Silver`/… subclasses with `discount_rate()` and `points_mult`* | Polymorphism | PASS |
| 3 |The original code represented order data with raw tuples and handled customer/order information procedurally.  |Created OrderItem with a Product and quantity, and created Order with a Customer and a list of OrderItem objects. |Composition / Object-Oriented Design  | Ran python Assignment_03.py → PASS |
| 4 |The original calc() function calculated values and printed the receipt at the same time.  |Created separate subtotal(), discount(), tax(), total(), and points() methods, with receipt() handling the printing.  |Separation of calculation and I/O  |Ran python Assignment_03.py → PASS  |
| 5 |The original code used magic numbers and a global TAXRATE.  |Replaced magic numbers with named constants such as TAX_RATE, DISCOUNT_THRESHOLD, BULK_QTY_THRESHOLD, BULK_DISCOUNT_RATE, and POINTS_DIVISOR, and removed the global variable from the refactored code.  |Clean Code / Encapsulation  |Ran python Assignment_03.py → PASS  |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> _your reflection..._

The change that improved the code the most was replacing the membership tier if/elif chains with customer subclasses and polymorphism. Each customer type now knows its own discount rate and points multiplier, which makes the Order class simpler and easier to understand. Separating calculation methods from receipt printing also made the program easier to follow and verify. Keeping the behaviour identical required me to be careful not to change any discount rules, tax rules, quantities, products, or receipt formatting. I checked the result by running the built-in self-test after the refactoring steps. The final result was PASS - behaviour is unchanged. My refactor is safe.

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"Refactor this tier discount if/elif into subclasses"* | *Base `Customer` + 4 subclasses* | Edited (renamed methods) | Self-test PASS; read every line |
| 2 | "now this [FAIL output]" — Charlie was missing | Suggested adding PlatinumCustomer("Charlie") and Charlie's order  | Accepted | Ran python Assignment_03.py and checked the self-test |
| 3 | "now this [FAIL output]" — Dana/grand total was missing | Suggested adding Dana's order and then the grand total | Accepted  | Ran python Assignment_03.py → PASS |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [ ] `python Assignment_03.py` prints **PASS**.
- [ ] No tuples / parallel lists left — products, orders, and items are objects.
- [ ] No `if tier == ...` chains — tiers are a class family.
- [ ] Calculation methods **return** values and do not `print`; printing is separate.
- [ ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ ] The change table and reflection above are filled in.
- [ ] The prompt log is complete and the ownership statement is signed.
