from pathlib import Path

import duckdb
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

DB_PATH = "sales_analytics.duckdb"
OUTPUT_DIR = Path("outputs")
CHART_DIR = OUTPUT_DIR / "charts"
TABLE_DIR = OUTPUT_DIR / "tables"


def read_table(table_name: str) -> pd.DataFrame:
    with duckdb.connect(DB_PATH) as connection:
        return connection.execute(f"SELECT * FROM {table_name}").fetchdf()


def export_tables() -> dict[str, pd.DataFrame]:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    tables = {
        "mart_monthly_sales": read_table("mart_monthly_sales"),
        "mart_product_performance": read_table("mart_product_performance"),
        "mart_customer_metrics": read_table("mart_customer_metrics"),
    }
    for name, df in tables.items():
        df.to_csv(TABLE_DIR / f"{name}.csv", index=False)
    return tables


def create_monthly_revenue_chart(monthly_sales: pd.DataFrame) -> None:
    monthly_sales = monthly_sales.sort_values("order_month")
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_sales["order_month"], monthly_sales["total_revenue"], marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue (£)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "monthly_revenue.png", dpi=160)
    plt.close()


def create_top_products_chart(product_performance: pd.DataFrame) -> None:
    top_products = product_performance.sort_values("total_revenue", ascending=True).tail(8)
    plt.figure(figsize=(10, 6))
    plt.barh(top_products["product_name"], top_products["total_revenue"])
    plt.title("Top Products by Revenue")
    plt.xlabel("Revenue (£)")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "top_products_by_revenue.png", dpi=160)
    plt.close()


def create_customer_spend_chart(customer_metrics: pd.DataFrame) -> None:
    top_customers = customer_metrics.sort_values("total_spend", ascending=True).tail(8)
    plt.figure(figsize=(10, 6))
    plt.barh(top_customers["customer_name"], top_customers["total_spend"])
    plt.title("Top Customers by Total Spend")
    plt.xlabel("Total spend (£)")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "top_customers_by_spend.png", dpi=160)
    plt.close()


def main() -> None:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    tables = export_tables()
    create_monthly_revenue_chart(tables["mart_monthly_sales"])
    create_top_products_chart(tables["mart_product_performance"])
    create_customer_spend_chart(tables["mart_customer_metrics"])
    print(f"Exported tables to {TABLE_DIR}")
    print(f"Saved charts to {CHART_DIR}")


if __name__ == "__main__":
    main()
