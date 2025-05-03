# Task 2: Spark Program with Gen AI – UAE Amazon Reviews Dataset

## 📌 Objective
Use Spark (PySpark) on Google Cloud Dataproc to randomly sample records from a **4.5GB synthetic UAE Amazon Reviews dataset**.

---

## 📁 Folder Structure
ask2-Spark/
├── data/
│ ├── Sample.xlsx # Sample of 1000 rows extracted for sharing
│ └── .gitkeep
├── src/
│ ├── random_sample_task2.py # Spark script to sample 100 records
│ └── .gitkeep
├── README.md # This file

---

## 🛠️ How This Was Done

### ✅ Step-by-Step Summary

1. **Generated** a 4.5GB UAE Amazon Reviews dataset using a Python script.
2. **Tested sampling locally** in RStudio using:
   ```r
   df <- fread("uae_amazon_reviews.csv")
   sample_100 <- df[sample(.N, 100)]

3.Created random_sample_task2.py using Gen AI and tested PySpark locally (failed due to missing Spark/Hadoop).

4.Uploaded files to GCS and ran the PySpark job using both:

           ----Dataproc persistent cluster

           ----Ephemeral cluster via gcloud dataproc batches
5. SSH-ed into Dataproc and tested PySpark directly:
   df = spark.read.csv("gs://your-bucket/uae_amazon_reviews.csv", header=True, inferSchema=True)
sample_df = df.sample(withReplacement=False, fraction=0.001).limit(100)
sample_df.show(5)

6.☁️ Run on Dataproc Cluster
# Submit with persistent cluster
gcloud dataproc jobs submit pyspark src/random_sample_task2.py \
  --cluster=your-cluster-name \
  --region=your-region
🔁 Run with Ephemeral Cluster
gcloud dataproc batches submit pyspark gs://your-bucket/random_sample_task2.py \
  --region=your-region \
  --deps-bucket=gs://your-bucket \
  --batch=batch-$(date +%s)
  
  
  📝 Notes
Ephemeral clusters are cost-efficient for one-time jobs.
Sample output (Sample.xlsx) is shared in the data/ folder.
Screenshots and detailed logs are embedded in Challenge-4.docx.

✅ Outcome
Successfully:

Sampled 100 rows using Spark
Ran PySpark via 3 methods:
Persistent cluster
Ephemeral cluster
Jupyter Notebook + HDFS
