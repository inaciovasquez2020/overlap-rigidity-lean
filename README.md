# overlap‑rigidity‑lean

Canonical **Lean formalization dependency** for **Overlap Rigidity** (the *Final Wall* in the locality / rigidity program).

This repository is **frozen**. It exists to provide a stable, auditable Lean foundation that downstream projects may import without risk of semantic drift.

---

## Role in the program

This project formalizes the **core definitions, invariants, and local lemmas** required for Overlap Rigidity arguments. It is intentionally minimal and structural.

It sits **below** proof‑carrying manuscripts and **above** raw mathlib:

```
mathlib
   ↓
overlap‑rigidity‑lean   (this repo)
   ↓
cycle‑local‑rigidity / chronos / URF‑core
```

No claims are asserted here. This repository only establishes *formal objects* that other proofs depend on.

---

## What is (and is not) here

### Included

* Lean definitions for:

  * bounded‑degree graphs / local neighborhoods
  * local overlap and cycle‑interaction predicates
  * FOᵏ / locality‑compatible invariants (as abstract structures)
* Lemmas that are:

  * purely local
  * non‑asymptotic
  * reusable across multiple rigidity arguments

### Explicitly excluded

* Global rigidity theorems
* Asymptotic bounds or threshold constants
* Probabilistic arguments
* Any claim equivalent to “Overlap Rigidity is proven”

Those live **outside** this repository.

---

## Repository structure

```
.
├── src/
│   ├── Overlap/
│   │   ├── Basic.lean        # core definitions
│   │   ├── LocalTypes.lean   # locality / type abstractions
│   │   └── Support.lean      # overlap / support relations
│   └── Main.lean
├── tests/
│   └── sanity.lean           # minimal build checks
├── lake.toml
├── lake-manifest.json
├── STATUS.md
└── README.md
```

File names may evolve slightly, but **semantic scope will not**.

---

## Build requirements

* Lean version pinned in `lake.toml`
* mathlib as resolved by `lake-manifest.json`

No external tooling is required.

---

## Build and verification

To build and verify locally:

```bash
lake build
```

Optional sanity check:

```bash
lake test
```

Successful compilation is the **only acceptance criterion**.

---

## Stability and freezing policy

* This repository is **API‑frozen**
* Any future changes require:

  * a new tag
  * an explicit downstream migration note

The default branch is intended to remain permanently usable as a dependency.

---

## Downstream usage

Typical `lakefile.lean` dependency:

```lean
require overlapRigidity from git
  "https://github.com/inaciovasquez2020/overlap-rigidity-lean" @ "<tag>"
```

Downstream projects are expected to:

* state their own theorems
* import these definitions without modification

---

## Status

* Formal layer: **complete for intended scope**
* CI: **green**
* Claims: **none** (by design)

See `STATUS.md` for a precise scope statement.

---

## License

MIT (or compatible permissive license).

---

## Provenance note

This repository is part of a broader rigidity and locality research program. It is intentionally separated to ensure that **formal correctness, dependency hygiene, and auditability** are preserved independent of higher‑level claims.
\
