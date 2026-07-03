# ANDALIMAN OUTPUT STANDARD
version : v1.0-alpha
status : canonical
authority : andaliman core engine
classification : output layer

---

# PURPOSE

Output Standard mendefinisikan struktur keluaran resmi Andaliman.

Seluruh hasil analisis Human Meaning Text (HMT) wajib mengikuti standar ini.

Output harus:

- Konsisten
- Terstruktur
- Dapat diaudit
- Mudah dibaca
- Memisahkan fakta dari interpretasi
- Menampilkan tingkat keyakinan
- Menjelaskan keterbatasan analisis

---

# OUTPUT PRINCIPLE

Setiap analisis Andaliman harus:

1. Memulai dari ringkasan.
2. Menampilkan proses analisis secara bertahap.
3. Memisahkan fakta, interpretasi, hipotesis, dan imajinasi.
4. Menjelaskan tingkat keyakinan.
5. Mengakui keterbatasan apabila ada.

---

# STANDARD OUTPUT

## 1. ANALYSIS SUMMARY

Ringkasan hasil analisis.

Berisi 3–5 kalimat.

Summary hanya boleh merangkum hasil analisis.

Summary tidak boleh menambahkan informasi baru.

---

## 2. DOCUMENT INFORMATION

Berisi:

- Text Type
- Analysis Mode
- Analysis Version

---

## 3. SEMANTIC FIELD

Menampilkan:

- Meaning Center
- Semantic Pole
- Semantic Relation
- Semantic Tension
- Semantic Movement

---

## 4. STRUCTURAL ANALYSIS

Disesuaikan dengan jenis teks.

### Poetry

- Image Structure
- Emotional Structure
- Metaphor Structure
- Rhythm Structure

### Narrative

- Opening
- Development
- Turning Point
- Resolution
- Ending

### Argumentative

- Main Claim
- Supporting Claim
- Evidence
- Assumption
- Conclusion

### Public Communication

- Main Narrative
- Supporting Narrative
- Value Orientation
- Public Message

---

## 5. SEMANTIC RELATION MAP

Hubungan utama antar elemen.

Jenis hubungan:

- Cause
- Contrast
- Echo
- Transformation
- Reference
- Association

---

## 6. HISTORICAL RESONANCE

Apabila ditemukan.

Menampilkan:

- Historical Context
- Cultural Context
- Temporal Context

Apabila tidak ditemukan:

No Significant Historical Resonance

---

## 7. RESIDUAL MEANING

Residual Meaning merupakan hasil sintesis akhir.

Residual Meaning bukan ringkasan.

Residual Meaning merupakan makna yang tetap bertahan setelah seluruh proses analisis selesai.

---

## 8. EPISTEMIC CLASSIFICATION

Seluruh hasil analisis wajib dipisahkan menjadi:

### FACT

Informasi yang didukung langsung oleh teks.

### INTERPRETATION

Penafsiran logis berdasarkan bukti tekstual.

### HYPOTHESIS

Kemungkinan yang masih memerlukan validasi.

### IMAGINATION

Eksplorasi kreatif yang tidak diklaim sebagai fakta.

Kategori tidak boleh dicampur.

---

## 9. CONFIDENCE

Confidence diberikan terhadap keseluruhan hasil analisis.

Kategori:

- HIGH
- MEDIUM
- LOW

Confidence harus disertai alasan.

---

## 10. LIMITATION

Apabila terdapat keterbatasan analisis.

Contoh:

- Bukti tekstual tidak mencukupi.
- Meaning Center belum dapat dipastikan.
- Historical Resonance bersifat hipotesis.
- Konteks eksternal tidak tersedia.

Bagian ini wajib ditampilkan apabila terdapat keterbatasan.

---

# STANDARD TEMPLATE

```text
ANDALIMAN ANALYSIS

━━━━━━━━━━━━━━━━━━

Analysis Summary

Document Information

Semantic Field

Structural Analysis

Semantic Relation Map

Historical Resonance

Residual Meaning

Epistemic Classification

Confidence

Limitation

━━━━━━━━━━━━━━━━━━
```

---

# OUTPUT RULE

Output tidak boleh:

- Menghasilkan fakta baru.
- Menghilangkan klasifikasi epistemik.
- Mengklaim kepastian tanpa bukti.
- Mencampurkan fakta dengan interpretasi.
- Menghilangkan bagian wajib pada Output Standard.

---

# FAILURE OUTPUT

Apabila analisis tidak dapat dilakukan.

Sistem menghasilkan:

Analysis Inconclusive

Disertai alasan yang jelas.

Sistem tidak melakukan spekulasi.

---

# GOLDEN RULE

Consistency before style.

Evidence before confidence.

Structure before conclusion.

Honesty before certainty.

Summary before details.

---

[ END OF OUTPUT STANDARD ]
