# ICP profiles

Each file here is one **ICP** — a reader the signal story can be drafted for. The
story's data never changes between ICPs; the profile changes which findings lead,
how they're worded, and what action the report drives. See `_schema.md` for the
field contract and the field → block map.

Shipped profiles:

- `dtc-agency.md` — a DTC marketing agency (the buyer).
- `dtc-brand.md` — the direct-to-consumer brand the agency serves.

## Add your own

Copy `dtc-brand.md` to `<your-icp>.md`, keep the same fields, and rewrite them for
the new reader. The `id` must match the filename. That's it — the skill lists every
file in this directory when it asks who the story is for. Profiles can name a
`serves:` downstream reader to make a white-labelled second variant, and an optional
`evidence_hook:` to add one hard ICP-specific number when framing alone isn't enough.
