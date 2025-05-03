# Task 3: Run a Job via Dataproc UI (Hadoop Streaming)

## 🎯 Objective
Submit a Hadoop Streaming job using the **Google Cloud Dataproc web UI**, after verifying and fixing errors through `gcloud` CLI.

---

## 🧪 What Was Done

1. **Job Type**: Hadoop Streaming  
   (Not PySpark – this was an extension beyond Tasks 1 & 2)

2. **Initial Errors**
   - I attempted to directly submit via the Dataproc UI, but kept getting errors.
   - Switched to CLI (`gcloud dataproc jobs submit hadoop`) to debug issues more clearly.
   - Fixed file path problems, permissions, and JAR access issues.

3. **Fixes Applied**
   - Ensured proper permissions on GCS bucket
   - Manually uploaded `hadoop-streaming.jar` to GCS since public example JARs are often **no longer available**
   - Specified mapper/reducer correctly via `--files`
   - Verified input/output paths and ensured no overwrite issues

4. **Job Results**
   - **Dataproc UI run time**: `1.17 sec`
   - **gCLI run time**: `1.23 sec`

---

## 📚 Key Learnings

### ✅ Why PySpark Jobs Work Easily
- Managed through Dataproc’s internal configuration
- Uses default Service Accounts with IAM roles
- Automatically handles staging, Spark job submission

### ❌ Why Hadoop Jobs Can Fail
- Requires correct path to `hadoop-streaming.jar`
- Bucket access and file overwrite issues
- No pre-installed example JARs in some Dataproc clusters
- Must manage output path (`gs://bucket/output/`) manually
- `Service Account` permissions for HDFS, GCS, and staging matter

---

## 📁 Files Used

- `mapper.py` and `reducer.py` from Task 1
- Input files: `Table_A.csv` and `Table_B.csv` in GCS
- Hadoop JAR: Manually uploaded to `gs://ritu-dataproc-g4/jars/hadoop-streaming.jar`

---

## 📸 Screenshots
- Cluster UI status
- Job submission form
- Output from both UI and CLI runs
- All stored in `docs/screenshots/` (optional)

---

## ✅ Final Outcome

Despite a rocky start, I was able to:
- Fix all job errors
- Successfully submit and monitor the job via **Dataproc UI**
- Observe small time difference between CLI and UI executions
- Completed all 3 tasks using different types of jobs (MapReduce, PySpark, Hadoop)

---

📦 *This concludes Task 3 of my Big Data Challenge.*
