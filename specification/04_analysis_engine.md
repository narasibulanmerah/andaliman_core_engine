# ANDALIMAN ANALYSIS ENGINE
version : v1.0-alpha
status : canonical
authority : andaliman core engine
classification : semantic analysis layer

---

# PURPOSE

Analysis Engine merupakan lapisan analisis yang dijalankan setelah Core Engine selesai melakukan Semantic Parsing.

Analysis Engine bertanggung jawab menghasilkan interpretasi semantik berdasarkan struktur yang telah dibangun oleh Core Engine.

Analysis Engine tidak melakukan parsing.

Analysis Engine tidak melakukan klasifikasi teks.

Analysis Engine hanya menganalisis.

---

# ANALYSIS PIPELINE

Semantic Field

↓

Analysis Module Selection

↓

Semantic Analysis

↓

Cross Validation

↓

Residual Meaning

↓

Output Standard

---

# ANALYSIS MODULES

Analysis Engine bersifat modular.

Setiap modul dapat dijalankan secara independen sesuai jenis Human Meaning Text.

---

# 1. SPT-Ω

Purpose

Mencari pusat energi makna dalam teks.

Output

- Meaning Center
- Semantic Tension
- Collapse Candidate
- Hidden Relation

---

# 2. POETIC DNA

Digunakan apabila jenis teks adalah puisi atau teks sastra.

Komponen

- Image DNA
- Language DNA
- Rhythm DNA
- Metaphor DNA
- Emotional DNA
- Collapse DNA

Output

Profil struktur puisi.

---

# 3. NARRATIVE STRUCTURE

Digunakan untuk teks naratif.

Komponen

- Opening
- Development
- Turning Point
- Resolution
- Open Ending

Output

Peta struktur narasi.

---

# 4. ARGUMENT STRUCTURE

Digunakan untuk:

- Esai
- Artikel
- Opini
- Manifesto
- Pernyataan

Komponen

- Main Claim
- Supporting Claim
- Evidence
- Assumption
- Conclusion

Output

Peta argumentasi.

---

# 5. PUBLIC NARRATIVE

Digunakan untuk:

- Pidato
- Narasi Pemerintah
- Pernyataan Pejabat
- Konferensi Pers

Komponen

- Main Narrative
- Supporting Narrative
- Public Message
- Emotional Strategy
- Value Orientation

Output

Peta narasi publik.

Analysis Engine tidak menentukan benar atau salahnya isi narasi.

---

# 6. INTERTEXT

Mendeteksi kemungkinan hubungan dengan teks lain.

Jenis hubungan

- Direct Reference
- Echo
- Contrast
- Transformation
- Parallel

Kemiripan bukan bukti pengaruh.

---

# 7. READER GRAVITY

Mengukur potensi resonansi teks terhadap pembaca.

Komponen

- Emotional Weight
- Cultural Memory
- Interpretation Space
- Personal Resonance

Output

Reader Gravity Profile

---

# 8. HISTORICAL RESONANCE

Mengidentifikasi kemungkinan hubungan historis.

Komponen

- Historical Context
- Cultural Context
- Temporal Shift

Output

Historical Resonance Map

---

# 9. COLLAPSE DETECTION

Menemukan titik konsentrasi energi makna.

Komponen

- Central Question
- Semantic Tension
- Dominant Image
- Emotional Peak
- Collapse Point

Output

Collapse Profile

---

# 10. RESIDUAL MEANING

Merumuskan makna yang tersisa setelah seluruh modul selesai dijalankan.

Residual Meaning merupakan hasil akhir Analysis Engine.

Residual Meaning bukan ringkasan.

Residual Meaning merupakan sintesis semantik.

---

# CROSS VALIDATION

Seluruh hasil modul dibandingkan.

Apabila terjadi konflik antar modul,

Core Engine memberikan prioritas kepada:

1. Bukti tekstual
2. Semantic Relation
3. Context
4. Epistemic Honesty

---

# FAILURE CONDITION

Analysis Engine menghentikan interpretasi apabila:

- Semantic Relation tidak cukup.
- Evidence tidak memadai.
- Meaning Center gagal ditemukan.
- Terjadi konflik yang tidak dapat diselesaikan.

Dalam kondisi tersebut sistem menghasilkan:

ANALYSIS INCONCLUSIVE

bukan spekulasi.

---

# GOLDEN RULE

Analyse after parsing.

Evidence before interpretation.

Meaning through relation.

Residual after synthesis.

---

[ END OF ANALYSIS ENGINE ]
