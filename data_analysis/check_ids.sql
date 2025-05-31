SELECT COUNT(*) = (SELECT COUNT(*) FROM mock_data_raw) as check from mock_data_raw
WHERE id = sale_seller_id and sale_seller_id = sale_customer_id and sale_customer_id = sale_product_id;