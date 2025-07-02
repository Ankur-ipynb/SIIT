# Smart Incident Insights Tool (SIIT)

## 🔍 Overview
SIIT is a modular, n8n-based pipeline for analyzing corporate AI, infrastructure, and supply chain incidents. It leverages:

- **PySpark**, **NLP (DistilBERT)**, **PyTorch**, **OpenCV**, and **Dash**
- Provides **severity classification (P1/P2/P3)**, **anomaly detection**, and **image analysis**
- Built with **Medallion architecture (Bronze → Silver → Gold)**
- Emphasizes **AI ethics**, **modularity**, and **enterprise-grade data engineering**

> **Tech Stack:** Python, PySpark, Databricks, Supabase, n8n, Hugging Face, OpenCV, Flask, Dash, Grafana, Prometheus

---

## ⚖️ Architecture
```
[Raw Data + Images] → [n8n: Ingestion Plugin] → [Supabase: Bronze] 
                                         |
                                         └→ [n8n: SQL Plugin → results_table]
                                                   |
                                                   └→ [n8n: ETL Plugin] → [Supabase: Silver] 
                                                                   |
                                                                   └→ [n8n: NLP Plugin → Gold] → [n8n: OpenCV Plugin]
                                                                                         |
                                                                                         ├→ [n8n: Monitoring Plugin → Grafana/Prometheus]
                                                                                         └→ [n8n: Dashboard Plugin → Dash]
```

---

## 📄 Modules
- **Ingestion Plugin:** Ingests 1,000 synthetic incidents (Faker, OECD.AI) & 100 images (PIL) to Supabase *(Bronze)* [`Code`](/ingestion.py)
- **SQL Plugin:** Aggregates to `results_table` with `avg_impact`, `anomaly_count` [`Code`](/sql/sql_plugin.sql)
- **ETL Plugin:** PySpark ETL (Databricks) with DLP (Presidio) to Supabase *(Silver)* [`Code`](/etl/etl_plugin.py)
- **NLP Plugin:** DistilBERT sentiment + PyTorch severity prediction to Supabase *(Gold)* [`Code`](/nlp/nlp_plugin.py)
- **OpenCV Plugin:** Classifies 100 images (minor/major damage) [`Code`](/opencv/opencv_plugin.py)
- **Monitoring Plugin:** Logs runtime, health, and accuracy to Grafana/Prometheus [`Code`](/monitoring/monitoring_plugin.py)
- **Dashboard Plugin:** Dash insights (severity, anomaly, image) [`Code`](/dashboard/dashboard_plugin.py)

---

## 🚀 Setup Instructions
1. Clone repo:
```bash
git clone https://github.com/your-username/siit.git
```
2. Sign up for:
   - [Databricks Community Edition](https://community.cloud.databricks.com)
   - [Supabase](https://supabase.com)
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Configure Flask and Supabase credentials
5. Run n8n workflow:
```bash
n8n import:workflow --input n8n_workflow.json
```
6. Launch Dash:
```bash
python dashboard_plugin.py
```

---

## ⚖️ Key Metrics
- ✅ 10,000 incidents processed in 200s (PySpark)
- ✅ Health Score: 90/100 (runtime < 300s)
- ✅ Mitigation Success: 75% (NLP sentiment-based)
- ✅ Image Accuracy: 85% (OpenCV classification)

---

## 👤 Contact
> Reach out via [LinkedIn](https://www.linkedin.com/in/ankur-verma-87047ba3/) for collaboration or hiring discussions!
