# 🛒 E-Commerce Customer Segmentation: Unsupervised Machine Learning Pipeline
## 📌 Project Overview
This project delivers an end-to-end unsupervised machine learning pipeline using Python to segment **~50,000 e-commerce customers** into actionable behavioral personas. By analyzing **18 distinct behavioral, financial, and engagement metrics**, the model transforms raw customer data into strategic business segments to optimize marketing, retention, and personalized experiences.
## ⚙️ Technical Architecture & Methodology
The data science pipeline follows a rigorous, step-by-step workflow:
 * 🧹 **Data Preprocessing:** Handled missing values, checked for duplicates, and prepared customer-level records.
 * 📐 **Feature Scaling:** Applied StandardScaler to align variance across all 18 variables (including spending, frequency, and engagement metrics).
 * 📉 **Dimensionality Reduction:** Used Principal Component Analysis (PCA) to project high-dimensional data into a 2D space for spatial cluster separation and visualization.
 * 🤖 **Model Training & Optimization:** Implemented **K-Means Clustering** alongside the **Elbow Method** to map the inertia curve and determine the optimal number of clusters (K = 4).
## 👥 The 4 Customer Personas Unlocked
 1. **👑 VIP Champions**
   * **Profile:** High spenders with maximum lifetime value and frequent engagement.
   * **Strategy:** Exclusive loyalty programs, early access, and VIP rewards.
 2. **💎 Loyal Spenders**
   * **Profile:** Steady basket sizes, consistent order history, and reliable retention.
   * **Strategy:** Targeted cross-selling and strategic bundle recommendations.
 3. **🛒 Regular Shoppers**
   * **Profile:** Moderate purchasers with steady, predictable engagement metrics.
   * **Strategy:** Nurture campaigns designed to increase order frequency.
 4. **⚠️ At-Risk / Churned Customers**
   * **Profile:** High days since last purchase, increasing return counts, and dropping interaction rates.
   * **Strategy:** Automated re-engagement workflows and targeted churn-risk triggers.
## 🛠️ Tech Stack & Deliverables
 * 💻 **Languages & Libraries:** Python, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn.
 * 📊 **Key Outputs:** A clean dataset tagged with cluster labels, behavioral summary tables, 2D PCA cluster visualizations, and a reusable production-ready pipeline.
 * 🚀 **Future Roadmap:** Compare K-Means with Hierarchical Clustering or DBSCAN, integrate a predictive churn model, and build a real-time segmentation dashboard.
> 💡 **Business Impact:** This segmentation framework empowers e-commerce teams to move away from generic marketing and deliver hyper-targeted campaigns that maximize customer lifetime value, prevent churn, and optimize acquisition costs.
> 
