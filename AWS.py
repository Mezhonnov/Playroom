from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .appName("S3Example")
         .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
         .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
         .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.406")
         .getOrCreate())

# Попробуем просто открыть S3 CSV
df = spark.read.csv("s3a://my-datasets-playroom/airlines_flights_data.csv", header=True, inferSchema=True)

df.show(5)
#spark.stop()