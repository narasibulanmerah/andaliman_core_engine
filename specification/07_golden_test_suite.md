# ANDALIMAN GOLDEN TEST SUITE
version : v1.0-alpha
status : canonical
authority : constitution Ω
classification : validation

---

# PURPOSE

Golden Test Suite merupakan standar resmi untuk memvalidasi kualitas, konsistensi, dan stabilitas Andaliman.

Seluruh perubahan terhadap:

- Core Engine
- Analysis Engine
- Output Standard
- Master Prompt
- Execution Adapter

wajib melewati Golden Test Suite sebelum dapat menjadi Canonical.

---

# OBJECTIVE

Golden Test Suite bertujuan untuk memastikan bahwa evolusi Andaliman:

- meningkatkan kualitas analisis;
- mempertahankan identitas arsitektur;
- mematuhi Constitution Ω;
- tidak menimbulkan Semantic Drift.

---

# TEST PRINCIPLE

Setiap pengujian mengevaluasi:

- Consistency
- Stability
- Epistemic Honesty
- Structure Preservation
- Output Standard Compliance

---

# TEST DATASET

Dataset dibagi menjadi beberapa kelompok.

## Poetry

Minimal:

100 puisi

Mencakup:

- Modern
- Klasik
- Bebas
- Lirik

---

## Narrative

Minimal:

100 dokumen

Mencakup:

- Esai
- Artikel
- Opini
- Memoar

---

## Public Communication

Minimal:

100 dokumen

Mencakup:

- Pidato
- Narasi Pemerintah
- Pernyataan Pejabat
- Manifesto
- Deklarasi
- Konferensi Pers

---

## Cultural

Minimal:

50 dokumen

Mencakup:

- Kritik budaya
- Filsafat
- Narasi sejarah
- Teks keagamaan

---

# TEST SCENARIO

Seluruh dokumen dianalisis menggunakan Output Standard resmi Andaliman.

Seluruh pengujian menggunakan konfigurasi yang sama.

---

# VALIDATION CHECKLIST

## Output Standard

Apakah seluruh bagian Output Standard muncul?

PASS / FAIL

---

## Meaning Center

Apakah Meaning Center berhasil ditemukan?

PASS / FAIL

---

## Semantic Relation

Apakah hubungan semantik berhasil dipetakan?

PASS / FAIL

---

## Structural Analysis

Apakah struktur teks sesuai dengan jenis teks?

PASS / FAIL

---

## Residual Meaning

Apakah Residual Meaning konsisten dengan hasil analisis?

PASS / FAIL

---

## Epistemic Classification

Apakah FACT, INTERPRETATION, HYPOTHESIS, dan IMAGINATION dipisahkan dengan benar?

PASS / FAIL

---

## Confidence

Apakah Confidence memiliki dasar yang jelas?

PASS / FAIL

---

## Limitation

Apakah keterbatasan analisis dijelaskan apabila diperlukan?

PASS / FAIL

---

# CROSS MODEL VALIDATION

Golden Test Suite dijalankan pada seluruh Execution Adapter.

Contoh:

- GPT
- Claude
- Gemini
- Llama
- Mistral
- DeepSeek

Tujuannya bukan menghasilkan teks yang identik.

Tujuannya adalah menghasilkan struktur analisis yang konsisten.

---

# REFERENCE ANALYSIS

Reference Analysis merupakan kumpulan analisis resmi Andaliman terhadap dokumen acuan.

Reference Analysis menjadi baseline kualitas interpretasi Andaliman.

Reference Analysis bukan kebenaran absolut.

Reference Analysis merupakan standar pembanding kualitas Canonical.

---

## REFERENCE DATASET

Minimal terdiri atas:

- 5 Puisi
- 5 Narasi
- 5 Pidato
- 5 Public Communication

Total minimal:

20 Reference Documents

---

## REFERENCE REVIEW

Setiap Reference Analysis harus:

- Direview oleh Builder.
- Mematuhi Constitution Ω.
- Mengikuti Output Standard.
- Memenuhi Epistemic Honesty.

Setelah disetujui,

Reference Analysis dibekukan sebagai Canonical Reference.

---

## VERSION COMPARISON

Setiap versi Andaliman dibandingkan terhadap Reference Analysis.

Parameter evaluasi:

- Meaning Center
- Semantic Relation
- Structural Analysis
- Residual Meaning
- Epistemic Classification
- Confidence

Perbedaan interpretasi diperbolehkan.

Penurunan kualitas harus dapat dijelaskan.

---

## REFERENCE POLICY

Reference Analysis hanya dapat diubah melalui:

Proposal

↓

Architecture Decision Record (ADR)

↓

Review

↓

Canonical Approval

Tidak ada perubahan Reference Analysis tanpa ADR.

---

# REGRESSION TEST

Seluruh versi baru dibandingkan dengan Canonical Version sebelumnya.

Perubahan dinyatakan valid apabila:

- Tidak melanggar Constitution Ω.
- Tidak menurunkan kualitas analisis.
- Tidak menghilangkan Output Standard.
- Tidak melanggar Epistemic Honesty.

---

# ACCEPTANCE CRITERIA

Sebuah versi Andaliman dapat dinyatakan layak apabila:

- Seluruh Golden Test berhasil dijalankan.
- Tingkat keberhasilan minimal 95%.
- Tidak terdapat pelanggaran Constitution Ω.
- Tidak terjadi penurunan kualitas yang signifikan.
- Lolos perbandingan terhadap Reference Analysis.

---

# CHANGE POLICY

Apabila Golden Test gagal,

perubahan tidak dapat menjadi Canonical.

Perubahan dipindahkan ke Experimental Branch hingga berhasil divalidasi.

---

# GOLDEN RULE

Test before release.

Validation before evolution.

Evidence before improvement.

Consistency before innovation.

Reference before modification.

---

[ END OF GOLDEN TEST SUITE ]
