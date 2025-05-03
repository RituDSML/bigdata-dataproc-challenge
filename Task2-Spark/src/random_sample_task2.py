from pyspark.sql import SparkSession
from pyspark.sql.functions import rand

spark = SparkSession.builder.appName("RandomSampleUAE").getOrCreate()

df = spark.read.csv("gs://ritu-dataproc-bucket/uae_amazon_reviews.csv", header=True, inferSchema=True)
sample_df = df.orderBy(rand()).limit(100)
sample_df.write.csv("gs://ritu-dataproc-bucket/output/sample_100_rows", header=True)

spark.stop()
