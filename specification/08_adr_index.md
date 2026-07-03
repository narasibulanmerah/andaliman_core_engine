# ANDALIMAN ARCHITECTURE DECISION RECORD (ADR)
version : v1.0-alpha
status : canonical
authority : constitution Ω
classification : governance

---

# PURPOSE

Architecture Decision Record (ADR) merupakan sistem dokumentasi resmi seluruh keputusan arsitektur Andaliman.

Setiap perubahan Canonical wajib memiliki ADR.

ADR menjadi sumber kebenaran historis terhadap evolusi Andaliman.

---

# PRINCIPLE

Tidak ada perubahan Canonical tanpa ADR.

---

# ADR LIFECYCLE

Proposal

↓

Review

↓

Approval

↓

Canonical

↓

Archive

---

# ADR STATUS

Setiap ADR memiliki salah satu status berikut.

## Proposed

Sedang diajukan.

Belum disetujui.

---

## Approved

Disetujui.

Menunggu implementasi.

---

## Canonical

Telah menjadi bagian resmi Andaliman.

---

## Deprecated

Tidak lagi digunakan.

Tetap disimpan sebagai bagian sejarah.

---

## Rejected

Ditolak.

Tidak menjadi bagian Andaliman.

---

# ADR TEMPLATE

Setiap ADR wajib memiliki format berikut.

```
ADR Number

Title

Version

Status

Classification

Author

Date

Dependencies

Summary

Decision

Rationale

Impact

Implementation

Review History
```

---

# ADR CLASSIFICATION

Setiap ADR dikelompokkan menjadi:

- Constitution
- Governance
- Core Engine
- Analysis Engine
- Output Standard
- Product Scope
- Validation
- Execution Adapter
- Documentation

---

# ADR INDEX

## ADR-001

Semantic Identity Theory (SIT)

Status

Canonical

---

## ADR-002

Architectural Memory

Status

Canonical

---

## ADR-003

The First Principle of Andaliman

Status

Canonical

---

## ADR-004

Andaliman Constitution Ω

Status

Canonical

---

## ADR-005

Architectural Soul

Status

Canonical

---

## ADR-006

Andaliman Manifest

Status

Canonical

---

## ADR-007

Human Meaning Text (HMT)

Status

Canonical

---

## ADR-008

Model Independence Principle

Status

Canonical

---

## ADR-009

Analysis Summary as Mandatory Output

Status

Canonical

---

## ADR-010

Reference Analysis

Status

Canonical

---

# ADR MANAGEMENT

ADR disusun berdasarkan nomor.

Nomor ADR tidak boleh digunakan kembali.

ADR yang dihapus tetap dipertahankan sebagai bagian sejarah.

---

# ADR REVIEW

Perubahan terhadap ADR hanya dapat dilakukan melalui ADR baru.

ADR lama tidak diubah.

ADR baru menjelaskan:

- alasan perubahan;
- ruang lingkup perubahan;
- dampak terhadap Canonical.

---

# ADR CONSISTENCY

Seluruh ADR harus konsisten dengan:

- Constitution Ω
- Identity & Governance
- Core Engine
- Product Scope

Apabila terjadi konflik,

Constitution Ω menjadi acuan tertinggi.

---

# GOLDEN RULE

Every canonical change deserves an ADR.

History before overwrite.

Traceability before convenience.

Architecture remembers.

---

[ END OF ARCHITECTURE DECISION RECORD ]
