get_customers_info = {
    "key": "",
    "query": """
            select 
                customer_id,
                age,
                gender
            public.customer_info;
            """,
}

get_customers_with_active_products = {
    "key": "",
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
