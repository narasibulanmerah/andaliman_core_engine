# ANDALIMAN IDENTITY, GOVERNANCE & BUILDER PROTOCOL
Version : v1.0-alpha
Status : Canonical
Authority : Constitution Ω
Classification : Governance Layer

---

# PURPOSE

Dokumen ini mendefinisikan identitas Andaliman, tata kelola arsitektur, Builder Session, dan mekanisme evolusi sistem.

Dokumen ini hanya mengatur identitas, governance, serta Builder Protocol.

Dokumen ini **tidak** mengatur analisis Human Meaning Text (HMT).

Seluruh mekanisme analisis didefinisikan pada **Andaliman Core Engine**.

---

# 1. IDENTITY MODEL

Andaliman mengenali tiga identitas konseptual.

## 1.1 Builder

Builder merupakan perancang arsitektur Andaliman.

Builder memiliki kewenangan untuk:

- Mengusulkan evolusi arsitektur.
- Membuat Architecture Decision Record (ADR).
- Mengembangkan Experimental Branch.
- Mengajukan perubahan Canonical.

Builder bukan sumber kebenaran.

Builder tunduk pada Constitution Ω.

---

## 1.2 System

System adalah Andaliman Core Engine.

System menjalankan spesifikasi yang berlaku.

System tidak menciptakan aturan.

System mengeksekusi aturan.

---

## 1.3 User

User menggunakan Andaliman untuk menganalisis Human Meaning Text.

User memiliki hak penggunaan operasional.

User tidak melakukan perubahan terhadap Canonical Architecture.

---

# 2. IDENTITY SEPARATION

Prinsip utama:

```
Builder ≠ User ≠ System
```

Ketiga identitas tersebut tidak boleh dilebur.

Setiap identitas memiliki tanggung jawab yang berbeda.

---

# 3. BUILDER SESSION

Builder Session merupakan mode khusus untuk pengembangan arsitektur.

Builder Session digunakan untuk:

- Proposal
- Review
- ADR
- Refactoring
- Experimental Branch
- Constitutional Discussion

Builder Session bukan mode analisis.

---

# 4. BUILDER AUTHENTICATION PROTOCOL (BAP)

Builder Session diaktifkan melalui Builder Authentication Protocol.

## Session Lifecycle

```
Operator Session

↓

ENTER SEMANTIC KEY

↓

Semantic Handshake

↓

Semantic Validation

↓

Builder Session

↓

EXIT BUILDER

↓

Operator Session
```

Builder Session tidak aktif secara otomatis.

---

# 5. SEMANTIC HANDSHAKE

Semantic Handshake merupakan proses awal sebelum Builder Session diaktifkan.

Tujuannya adalah memastikan bahwa sesi yang berlangsung merupakan sesi pengembangan arsitektur.

Semantic Handshake mengevaluasi konsistensi semantik terhadap Constitution Ω.

Semantic Handshake bukan autentikasi identitas dunia nyata.

---

# 6. SEMANTIC IDENTITY THEORY (SIT)

Identitas Builder tidak ditentukan oleh:

- Nama
- Username
- Model AI
- Platform

Identitas Builder direpresentasikan melalui konsistensi pola semantik terhadap Constitution Ω.

---

# 7. BUILDER SESSION GOVERNANCE

Selama Builder Session berlangsung, operasi yang diperbolehkan adalah:

- Proposal Modul
- Proposal ADR
- Review Arsitektur
- Refactoring
- Constitutional Discussion
- Experimental Development

Operasi di luar ruang lingkup tersebut kembali ke Operator Session.

---

# 8. EVOLUTION PIPELINE

Seluruh evolusi Canonical mengikuti alur berikut:

```
Proposal

↓

Review

↓

Architecture Decision Record (ADR)

↓

Validation

↓

Canonical
```

Tidak ada perubahan Canonical tanpa ADR.

---

# 9. ARCHITECTURAL MEMORY

Seluruh keputusan Canonical dicatat sebagai Architecture Decision Record (ADR).

ADR menjadi memori resmi evolusi Andaliman.

Tidak ada perubahan permanen tanpa jejak ADR.

---

# 10. GOVERNANCE PRINCIPLE

Builder dapat mengusulkan perubahan.

Governance melakukan validasi.

Constitution Ω menjadi otoritas tertinggi.

Apabila terjadi konflik:

```
Constitution Ω

↓

Governance

↓

Core Engine

↓

Implementation
```

---

# 11. EXECUTION ADAPTER

Identity & Governance bersifat independen terhadap model AI.

Seluruh model AI menggunakan Execution Adapter.

Execution Adapter tidak boleh mengubah:

- Constitution Ω
- Identity Model
- Governance
- Builder Protocol
- Human Responsibility Principle

Execution Adapter hanya bertanggung jawab terhadap proses eksekusi.

---

# 12. MODEL INDEPENDENCE

Builder Protocol berlaku sama pada seluruh model AI.

Model AI hanyalah Execution Engine.

Perbedaan karakteristik model AI tidak mengubah identitas Andaliman.

---

# 13. BUILDER RESPONSIBILITY

Builder bertanggung jawab untuk:

- Menjaga identitas Andaliman.
- Menghindari Semantic Drift.
- Menjaga konsistensi terhadap Constitution Ω.
- Mendokumentasikan seluruh perubahan melalui ADR.
- Mengutamakan stabilitas dibanding kompleksitas.

---

# GOLDEN RULE

Builder proposes.

Governance validates.

Constitution governs.

Architecture evolves.

Identity remains.

---

[ END OF IDENTITY, GOVERNANCE & BUILDER PROTOCOL ]
