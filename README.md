# MapReduce Join Operation on Google Cloud Dataproc

## 📌 Project Overview
This project performs a MapReduce-based **SQL-style join** of two CSV files using Hadoop Streaming on **Google Cloud Dataproc**.

### Goals:
- Join student records (`Table_A`) with course records (`Table_B`)
- Filter students born on or after **1995-01-01**
- Run both **locally** and on **Dataproc**

---

## 📁 Project Structure

| Folder        | Description                                |
|---------------|--------------------------------------------|
| `data/`       | Input CSV files                            |
| `src/`        | Mapper and Reducer Python scripts          |
| `docs/`       | Report and screenshots                     |
| `scripts/`    | Bash script to submit the Dataproc job     |

---

## 🧪 How to Run

### 🖥️ Local Test
```bash
cat data/Table_*.csv | python3 src/mapper.py | sort | python3 src/reducer.py

☁️ On Google Cloud Dataproc

bash scripts/run_dataproc.sh

Sample Output:
M989898,John,1995-05-20,CSD5050,merit
M989898,John,1995-05-20,CSD5566,distinction

📝 Documentation
Found in docs/Challenge-4.pdf:

Problem Statement

Pandas testing approach

Mapper & Reducer logic

GCP cluster setup

Hadoop Streaming execution

Final results and screenshots

📸 Screenshots
Located in docs/screenshots/:

Local output

Dataproc job execution

Final results

🔧 run_dataproc.sh (sample)
#!/bin/bash
BUCKET="your-bucket-name"
CLUSTER="your-cluster-name"
REGION="your-region"

# Upload input and code files to GCS
gsutil cp data/*.csv gs://$BUCKET/input/
gsutil cp src/*.py gs://$BUCKET/code/

# Submit Hadoop job on Dataproc
gcloud dataproc jobs submit hadoop \
  --cluster=$CLUSTER \
  --region=$REGION \
  --jar=file:///usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  --files=gs://$BUCKET/code/mapper.py,gs://$BUCKET/code/reducer.py \
  --input=gs://$BUCKET/input/Table_*.csv \
  --output=gs://$BUCKET/output/ \
  --mapper="python3 mapper.py" \
  --reducer="python3 reducer.py"



