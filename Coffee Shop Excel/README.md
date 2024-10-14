# Coffee Shop Sales Excel Project
This project involves analyzing sales data from a coffee shop using Excel. We used various Excel functions to clean and explore the data, and we created a simple dashboard to visualize sales performance.

## Introduction
In this project, we looked at coffee shop sales to understand which products are selling well and how much revenue is being generated. The data includes product names, dates of sales, quantities sold, and prices. We cleaned the data and then used Excel functions to find trends and create a basic dashboard.

## Data Source
The data for this project comes from three sheets: **Orders**, **Customers**, and **Products**.

### Orders
The Orders sheet contains sales transaction data, and its columns are as follows:

* **Order ID**: Unique identifier for each order.
* **Order Date**: Date when the order was placed.
* **Customer ID**: Identifier for the customer (to be linked with the Customers sheet).
* **Product ID**: Identifier for the product (to be linked with the Products sheet).
* **Quantity**: Number of items sold in the order.
* **Customer Name**: (Empty, to be filled using the Customer ID from the Customers sheet).
* **Email**: (Empty, to be filled using the Customer ID from the Customers sheet).
* **Country**: (Empty, to be filled using the Customer ID from the Customers sheet).
* **Coffee Type**: (Empty, to be filled using the Product ID from the Products sheet).
* **Roast Type**: (Empty, to be filled using the Product ID from the Products sheet).
* **Size**: (Empty, to be filled using the Product ID from the Products sheet).
* **Unit Price**: (Empty, to be filled using the Product ID from the Products sheet).

### Customers
The Customers sheet holds information about the customers and has the following columns:

* **Customer ID**: Unique identifier for each customer.
* **Customer Name**: Name of the customer.
* **Email**: Customer's email address.
* **Phone Number**: Contact number of the customer.
* **Address Line 1**: Address of the customer.
* **City**: City of residence.
* **Country**: Country of residence.
* **Postcode**: Postal code of the customer's location.
* **Loyalty Card**: Indicates whether the customer has a loyalty card (Yes/No).

### Products
The Products sheet lists the available products, including the type of coffee and pricing details. Its columns are:

* **Product ID**: Unique identifier for each product.
* **Coffee Type**: The type of coffee.
* **Roast Type**: The roast level.
* **Size**: The size of the coffee.
* **Unit Price**: Price per unit of the product.
* **Price per 100g**: The price for 100 grams of the product.
* **Profit**: The profit margin for each product.

## Excel Functions Used

* **XLOOKUP**: To search for values across the dataset.
* **INDEX MATCH**: For advanced lookup of data based on multiple criteria.
* **SUM**: To calculate totals, like total revenue.
* **IF**: To perform conditional checks and calculations.
* **Pivot Tables**: To summarize and group data for easy analysis.
* **Charts**: To visually represent trends and key metrics.

## Dashboard
