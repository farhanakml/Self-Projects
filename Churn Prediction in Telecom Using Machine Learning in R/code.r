R.home("bin")

# Install Packages
install.packages(c("tidyverse", "caret", "randomForest", "e1071", "ROCR", "pROC"))

# Load required libraries
library(tidyverse)

# Load the dataset
data <- read.csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# View the first few rows
head(data)

# Check for missing values
print(paste("Missing data values before removed:", sum(is.na(data))))

# Remove rows with missing values
data <- na.omit(data)
print(paste("Missing data values after:", sum(is.na(data))))

# Convert categorical variables to factors
data$gender <- as.factor(data$gender)
data$Partner <- as.factor(data$Partner)
data$Dependents <- as.factor(data$Dependents)
data$PhoneService <- as.factor(data$PhoneService)
data$MultipleLines <- as.factor(data$MultipleLines)
data$InternetService <- as.factor(data$InternetService)
data$OnlineSecurity <- as.factor(data$OnlineSecurity)
data$OnlineBackup <- as.factor(data$OnlineBackup)
data$DeviceProtection <- as.factor(data$DeviceProtection)
data$TechSupport <- as.factor(data$TechSupport)
data$StreamingTV <- as.factor(data$StreamingTV)
data$StreamingMovies <- as.factor(data$StreamingMovies)
data$Contract <- as.factor(data$Contract)
data$PaperlessBilling <- as.factor(data$PaperlessBilling)
data$PaymentMethod <- as.factor(data$PaymentMethod)
data$Churn <- as.factor(data$Churn)

# Normalize tenure and TotalCharges
data$tenure <- scale(data$tenure)
data$MonthlyCharges <- scale(data$MonthlyCharges)
data$TotalCharges <- as.numeric(data$TotalCharges)  # Convert TotalCharges to numeric
data$TotalCharges <- scale(data$TotalCharges)

# Split the data
set.seed(42)
library(caret)
trainIndex <- createDataPartition(data$Churn, p = 0.8, list = FALSE)
trainData <- data[trainIndex, ]
testData <- data[-trainIndex, ]

