# Formal Scope Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository is frozen and claim-free.
It contains:
1. core Lean definitions;
2. local overlap and support predicates;
3. locality-compatible invariant structures;
4. reusable local lemmas.

It does not contain:
1. global rigidity theorems;
2. asymptotic threshold bounds;
3. probabilistic arguments;
4. any proof of Overlap Rigidity.

## Weakest admissible extension
Let
\[
T_{\mathrm{loc}}
\]
denote the current local Lean theory formalized in this repository.

Let
\[
\mathcal I_{\mathrm{loc}}
\]
denote the class of locality-compatible invariant structures defined over bounded-degree neighborhoods.

The weakest next structural artifact is an interface certificate:
\[
\forall I \in \mathcal I_{\mathrm{loc}},
\quad
I \text{ is definable in } T_{\mathrm{loc}}
\Longrightarrow
I \text{ is stable under the repository's local support morphisms.}
\]

## Minimal next artifact
The weakest next artifact is an executable audit emitting:
1. exported local definitions;
2. exported local lemmas;
3. invariant structures depending only on local data;
4. declarations intentionally excluded from repository scope.

## Label
This note is CONDITIONAL.
It preserves the repository's frozen, claim-free dependency role.
