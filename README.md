# Big Data Analytics with Google Cloud Dataproc

This project demonstrates end-to-end execution of MapReduce, Spark, and Dataproc Web UI tasks using Google Cloud Platform. It includes hands-on experiments, error handling, and working code samples—all structured for learning and reproducibility.

---

## 📁 Project Structure
bigdata-dataproc-challenge/
├── Challenge-4.docx # Combined documentation/report for all tasks

├── Task1-MapReduce/
│ ├── data/
│ │ ├── Table_A.xlsm
│ │ ├── Table_B.xlsm
│ │ └── .gitkeep
│ ├── src/
│ │ ├── mapper.py
│ │ ├── reducer.py
│ │ └── .gitkeep
│ └── README.md # Instructions and output summary for Task 1

├── Task2-Spark/
│ ├── data/
│ │ ├── Sample.xlsx # Output sample of 1000 rows
│ │ └── .gitkeep
│ ├── src/
│ │ ├── random_sample_task2.py # PySpark sampling code
│ │ └── .gitkeep
│ └── README.md # Step-by-step Task 2 explanation

├── Task3-WebUI/
|
│ └── README.md # Task 3 explanation (Web UI)


### ✅ Task 1: MapReduce Join on Dataproc

- Wrote `mapper.py` and `reducer.py` to simulate SQL JOIN of `Table_A` (students) and `Table_B` (courses) using Hadoop Streaming.
- Applied filter: **DOB >= 1995-01-01**
- Ran job both locally and on Dataproc using:
  - `gsutil` to move files
  - `hadoop fs` to stage input
  - `hadoop-streaming.jar` to execute
- Output: Successfully joined and filtered records, with 3 reducers, but only 1 producing the final result.

📂 More details in `Task1-MapReduce/README.md`

---

### ✅ Task 2: Spark with Gen AI (UAE Amazon Reviews)

- Generated a **4.5 GB synthetic dataset** using a Python script.
- Tested random sampling in RStudio using `data.table::fread()` + `sample(.N, 100)`
- Created `random_sample_task2.py` using Gen AI
- Ran Spark jobs using:
  - ✅ **Persistent Dataproc cluster**
  - ✅ **Ephemeral (serverless) cluster**
  - ✅ **SSH into cluster → Jupyter → Spark + HDFS**
- Output: 100 sampled records saved and shared as `Sample.xlsx`

📂 See `Task2-Spark/README.md` for scripts and terminal outputs.

---

### ✅ Task 3: Run Hadoop Job via Dataproc UI

- Reused Task 1 Mapper/Reducer scripts
- Initially faced issues with JAR paths and GCS output permissions
- Debugged via `gcloud` CLI before succeeding in Dataproc UI
- Compared CLI vs Web UI runtimes (1.23s vs 1.17s)
- Learned:
  - PySpark jobs are easier to manage due to better integration
  - Hadoop JARs require more setup (permissions, bucket prep, GCS paths)

📂 Explained in `Task3-WebUI/README.md`

---

## 🚀 How to Run

Each task folder contains a `README.md` with commands, screenshots, and helpful notes. Start from any of the following:

```bash
# Task 1: Hadoop MapReduce
cd Task1-MapReduce/
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files src/mapper.py,src/reducer.py ...

# Task 2: PySpark
cd Task2-Spark/
gcloud dataproc jobs submit pyspark src/random_sample_task2.py ...

# Task 3: Use Dataproc Web UI
1. Go to https://console.cloud.google.com/dataproc
2. Choose "Submit Job"
3. Upload mapper, reducer, and dataset

📄 Documentation
All steps, screenshots, and results are consolidated in Challenge-4.docx.
