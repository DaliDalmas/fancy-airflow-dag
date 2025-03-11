from airflow.models import Variable
bucket_name = Variable.get('bucket_name')

get_customers_info = {
    "key": f"s3://{bucket_name}/extract/active_customers/get_customers_info.parquet",
    "query": """
            select 
                customer_id,
                age,
                gender
            from
            public.customer_info;
            """,
}

get_customers_with_active_products = {
    "key": f"s3://{bucket_name}/extract/active_customers/get_customers_with_active_products.parquet",
    "query": """
            select 
                cp.customer_id,
                cp.signup_date_time,
                pi.name as product_name,
                pi.price as product_price,
                pi.billing_cycle as product_billing_cycle
            from public.customer_product cp
            join public.product_info pi on pi.product_id=cp.product
            where cp.cancel_date_time is not null
            ;
            """,
}
