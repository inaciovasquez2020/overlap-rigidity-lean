import Lake
open Lake DSL

package overlapRigidityLean where
  version := { major := 0, minor := 1, patch := 0 }

lean_lib OverlapRigidityLean where
  roots := #[`OverlapRigidityLean]

